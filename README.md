# awesome_okapi_v2

<div align="center">

<img width="360" height="360" alt="okapi1" src="https://github.com/user-attachments/assets/79756a04-84ca-4e02-a6b3-516227e92ade" />

[![GitHub stars](https://img.shields.io/github/stars/Iankulani/awesome_okapi_v2?style=for-the-badge&logo=github)](https://github.com/Iankulani/awesome_okapi_v2/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Iankulani/awesome_okapi_v2?style=for-the-badge&logo=github)](https://github.com/Iankulani/awesome_okapi_v2/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Iankulani/awesome_okapi_v2?style=for-the-badge&logo=github)](https://github.com/Iankulani/awesome_okapi_v2/watchers)
[![GitHub contributors](https://img.shields.io/github/contributors/Iankulani/awesome_okapi_v2?style=for-the-badge&logo=github)](https://github.com/Iankulani/awesome_okapi_v2/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/Iankulani/awesome_okapi_v2?style=for-the-badge&logo=git)](https://github.com/Iankulani/awesome_okapi_v2/commits/main)
[![License](https://img.shields.io/github/license/Iankulani/awesome_okapi_v2?style=for-the-badge)](https://github.com/Iankulani/awesome_okapi_v2/blob/main/LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-blue?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/Iankulani/awesome_okapi_v2)
[![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-supported-blue?style=for-the-badge&logo=docker&logoColor=white)](https://github.com/Iankulani/awesome_okapi_v2)
[![Cybersecurity](https://img.shields.io/badge/cybersecurity-authorized%20testing-red?style=for-the-badge&logo=github)](https://github.com/Iankulani/awesome_okapi_v2)

</div>


Awesome Okapi_v2 is a cybersecurity penetration-testing and security-operations platform designed to help authorized security professionals, penetration testers, red teams, blue teams, security researchers, and organizations evaluate the security of their digital environments. The platform provides a centralized command-and-control interface through which authorized operators can interact with approved testing infrastructure using communication channels such as Discord, Telegram, Slack, Google Chat, WhatsApp, Signal, and a dedicated web application.

The primary objective of Awesome Okapi_v2 is to simplify authorized security testing while maintaining strong controls around authentication, authorization, auditing, scope management, and operational safety. Instead of requiring security teams to continuously switch between communication platforms, terminals, dashboards, and testing environments, the platform provides a unified interface for submitting approved security-testing commands and receiving structured results.

Awesome Okapi_v2 is intended exclusively for systems, applications, networks, accounts, devices, and infrastructure for which the operator has explicit authorization to perform security testing. Its design emphasizes controlled penetration testing, security validation, vulnerability assessment, incident-response exercises, security-awareness simulations, and laboratory environments.

The platform can integrate with isolated testing environments and approved security tools. Commands can be submitted through supported communication channels and routed to an authorized execution environment where policy checks are performed before an operation is executed. Results can then be returned to the appropriate channel or displayed through the web dashboard.

# Multi-Channel Command Interface

One of the major features of Awesome Okapi_v2 is its multi-channel command interface.

Security teams frequently operate across several communication platforms. A security engineer may use Slack for organizational communication, Discord for a security laboratory, Telegram for operational notifications, Google Chat for collaboration, WhatsApp for authorized team communication, or Signal for secure internal communications.

Awesome Okapi_v2 provides a common command architecture behind these interfaces.

Each integration acts as a controlled client of the platform rather than receiving unrestricted access to the underlying operating system. Incoming commands should first pass through authentication and authorization checks. The platform can then determine:

Who issued the command.
Which organization or workspace they belong to.
Which project they are assigned to.
Which testing environment they are authorized to access.
What operations they are permitted to perform.
Whether the target is inside the approved scope.
Whether additional approval is required.
Whether the requested operation should be blocked.
How the operation should be logged.

This architecture helps prevent a communication account from becoming an unrestricted remote shell.

# Discord Integration

The Discord integration can provide a controlled interface for authorized penetration-testing teams and cybersecurity laboratories.

A security team can create a dedicated Discord environment for a penetration-testing project. Authorized users can submit supported commands through a bot interface, request information about an assessment, retrieve scan results, inspect task status, or launch predefined testing workflows against approved laboratory targets.

Role-based permissions can determine which Discord users are allowed to perform specific actions.

For example, a trainee may only be allowed to run reconnaissance exercises against a deliberately vulnerable laboratory machine, while a senior tester may be allowed to initiate a broader approved assessment.

Every request should be associated with the user's Discord identity and recorded in the platform audit system.

# Telegram Integration

The Telegram integration provides another controlled interface for security teams.

Authorized users can communicate with the Awesome Okapi_v2 bot and request approved security-testing tasks. The bot can provide status notifications, assessment summaries, vulnerability findings, laboratory exercise results, and other authorized information.

Telegram commands should not automatically translate into unrestricted operating-system commands. Instead, the platform should use a command registry containing explicitly permitted operations.

This design allows administrators to disable dangerous operations, restrict commands to specific projects, and require additional approval for sensitive activities.

# Slack Integration

Slack integration allows Awesome Okapi_v2 to operate inside organizational security workflows.

Security teams can use dedicated Slack channels for penetration-testing activities, vulnerability-management operations, security-awareness exercises, and incident-response simulations.

The platform can provide structured responses rather than dumping raw terminal output into communication channels.

For example, a security assessment result could contain:

Assessment identifier.
Target environment.
Test status.
Findings.
Severity.
Evidence reference.
Recommended remediation.
Timestamp.
Tester identity.

This approach makes results easier to review and reduces accidental disclosure of sensitive information.

# Google Chat Integration

Google Chat can provide another collaboration interface for authorized security teams.

The integration can support controlled commands, task notifications, vulnerability summaries, assessment status updates, and security-awareness exercises.

Google Workspace administrators can restrict which spaces and users are permitted to interact with the system.

The integration should use secure authentication mechanisms and should never rely solely on a username or display name as proof of authorization.

# WhatsApp Integration

Awesome Okapi_v2 can support WhatsApp-based interaction where an organization has an approved business integration and appropriate authorization.

The WhatsApp interface can provide carefully restricted functionality such as assessment status, alerts, reports, security-training exercises, and predefined testing workflows.

Because messaging platforms can be compromised, the platform should treat every incoming request as untrusted until authentication and authorization are verified.

Sensitive results should preferably be returned through the secure web dashboard rather than directly exposing confidential information in a messaging conversation.

# Signal Integration

Signal can provide a communication interface for authorized security teams that require secure messaging.

Awesome Okapi_v2 can use the Signal integration for controlled operational notifications and approved testing workflows.

The platform should still enforce centralized authentication, authorization, audit logging, and scope validation because encrypted communications do not automatically make an operation authorized.

# Web Application

The web application serves as the central management interface for Awesome Okapi_v2.

Administrators and authorized security professionals can use the dashboard to create projects, define testing scopes, manage users, configure integrations, review assessments, inspect logs, manage security-awareness simulations, and generate reports.

The web application can contain sections such as:

# Dashboard

The dashboard provides a high-level overview of current security activities.

It may display:

Active assessments.
Completed assessments.
Vulnerability counts.
Critical findings.
Security-awareness campaign statistics.
Connected communication platforms.
Running laboratory jobs.
Recent security events.
Audit-log activity.
Project Management

Each penetration-testing project can have its own scope, users, permissions, credentials, testing environments, and reporting configuration.

A project can define authorized targets such as:

Internal laboratory networks.
Test web applications.
Approved domains.
Cloud test environments.
Virtual machines.
Containers.
Development systems.

The platform should prevent operations against targets that are outside the configured scope.

Controlled Command Execution

Awesome Okapi_v2 can provide command execution capabilities for authorized penetration-testing environments.

However, commands should be handled through a controlled execution architecture.

Instead of allowing arbitrary commands from a chat message to execute directly on a production server, the platform can use an allowlisted command registry.

Each command can contain:

Command name.
Description.
Required role.
Allowed project types.
Required approval level.
Target restrictions.
Execution timeout.
Logging requirements.
Output-handling rules.
Safety classification.

For example, a laboratory reconnaissance command could be permitted against a predefined test network, while a destructive operation could be disabled entirely.

The system should support dry-run functionality so operators can preview what a task would do before execution.

Scope Enforcement

Scope management is one of the most important security features of Awesome Okapi_v2.

Before a testing task is executed, the platform should determine whether the requested target belongs to the authorized assessment.

Scope can be represented using explicit assets such as:

IP addresses.
CIDR networks.
Hostnames.
Domains.
Applications.
Cloud resources.
Container environments.
Laboratory identifiers.

An operation against an unknown or unauthorized target should be rejected.

This prevents accidental testing of unrelated systems and provides an additional safety barrier when commands originate from chat platforms.

Approval Workflow

Sensitive operations can require approval from another authorized user.

For example:

Tester creates a task.
Awesome Okapi_v2 validates the requested target.
The platform determines that the operation requires approval.
An authorized reviewer receives an approval request.
The reviewer approves or rejects the task.
The platform executes the approved operation.
Results are stored in the assessment record.
An audit event records the complete process.

This workflow supports separation of duties and reduces the risk of accidental execution.

Phishing Simulation

Awesome Okapi_v2 can include a phishing-awareness simulation module for authorized security-awareness programs.

The purpose of this module is to help organizations evaluate whether employees recognize simulated phishing attempts and to measure security-awareness improvements.

The system should use controlled simulation infrastructure rather than real credential theft.

A campaign could contain:

Campaign name.
Authorized recipient group.
Simulation template.
Training objective.
Start date.
End date.
Tracking configuration.
Educational landing page.
Results dashboard.

The simulated message can direct participants to an organization-controlled training page that explains the warning signs of phishing.

The system should not collect real passwords, authentication tokens, private messages, or unnecessary personal information.

Instead, the simulation can record safe educational metrics such as:

Message delivered.
Message opened, where technically appropriate.
Training page visited.
Simulation recognized.
Reported as suspicious.
Training completed.
Safe Phishing Landing Pages

The phishing-simulation component should use clearly controlled landing pages owned or operated by the organization conducting the exercise.

A training page can explain that the participant encountered a simulated security-awareness exercise and provide educational information about common phishing indicators.

The page can teach users to recognize:

Suspicious domains.
Unexpected login requests.
Urgent language.
Unexpected attachments.
Requests for confidential information.
Spoofed identities.
Suspicious shortened links.
Social-engineering techniques.

The simulation should never be designed to secretly capture real credentials.

Security-Awareness Reporting

Campaign administrators can receive reports showing overall organizational performance.

For example, a report might show:

Total simulated messages.
Number delivered.
Number of participants who interacted with the simulation.
Number who reported the message.
Number who completed training.
Improvement between campaigns.

Reports can be anonymized or aggregated where appropriate to reduce unnecessary exposure of employee information.

Vulnerability Assessment

Awesome Okapi_v2 can integrate authorized vulnerability-assessment tools into a controlled workflow.

The platform can coordinate assessment tasks and normalize results into a common format.

Findings can include:

Vulnerability title.
Severity.
Affected asset.
Evidence.
Detection source.
Recommended remediation.
Status.
Assigned security team.
Verification state.

Security teams can track findings from discovery through remediation and verification.

Penetration-Testing Workflows

The platform can support structured penetration-testing phases.

Reconnaissance

Authorized testers can collect information about assets inside the defined scope.

Enumeration

Approved tools can identify exposed services and application components in laboratory or authorized environments.

Vulnerability Validation

Testers can validate suspected weaknesses using non-destructive techniques where possible.

Exploitation Validation

Where explicitly authorized, controlled proof-of-concept testing can demonstrate the security impact of a vulnerability.

Post-Assessment Analysis

Results can be analyzed and converted into remediation recommendations.

Reporting

The system can automatically produce assessment reports for technical teams and management.

Laboratory Mode

Awesome Okapi_v2 should include a dedicated laboratory mode.

Laboratory mode allows security professionals and students to experiment without affecting production systems.

The laboratory can contain deliberately vulnerable applications, virtual machines, containers, simulated networks, and security-training environments.

Commands submitted from Discord, Telegram, Slack, Google Chat, WhatsApp, Signal, or the web application can be restricted to these environments.

This makes the platform particularly useful for cybersecurity education and controlled penetration-testing exercises.

Audit Logging

Every significant action should be recorded.

Audit events can include:

Login attempts.
Authentication events.
Command submissions.
Approval decisions.
Task execution.
Target validation.
Blocked operations.
Integration changes.
User-management changes.
Phishing-campaign events.
Report generation.

Audit records should include timestamps, actor identity, project context, operation identifier, result status, and relevant security metadata.

Logs should be protected from unauthorized modification.

Role-Based Access Control

Awesome Okapi_v2 can support roles such as:

Administrator

Manages the platform, integrations, users, policies, and security settings.

Security Manager

Creates assessments, assigns testers, reviews findings, and approves selected operations.

Penetration Tester

Performs authorized security-testing activities within assigned projects.

Security Analyst

Reviews findings, evidence, logs, and remediation status.

Trainee

Uses restricted laboratory environments for cybersecurity education.

Auditor

Reviews activity and compliance records without being permitted to execute testing operations.

Authentication and Security

The platform should support strong authentication mechanisms such as multi-factor authentication, secure sessions, role-based authorization, API tokens with limited permissions, and integration-specific credentials.

Secrets should not be hard-coded into source code.

API keys, bot tokens, passwords, signing secrets, and encryption keys should be stored using secure secret-management mechanisms.

The platform should also support token rotation and immediate credential revocation.

Secure Architecture

A recommended architecture separates the communication layer from the execution layer.

The architecture can contain:

Communication adapters.
Authentication service.
Authorization service.
Command parser.
Policy engine.
Scope-validation engine.
Job queue.
Isolated execution workers.
Results processor.
Audit-log service.
Web dashboard.
Reporting engine.

Communication adapters receive requests but should not directly execute operating-system commands.

The policy engine determines whether a request is permitted.

The job system can then send approved tasks to isolated workers.

This separation reduces the impact of a compromised integration.

Containerized Execution

Security-testing jobs can be executed inside isolated containers or dedicated laboratory virtual machines.

Containers can have:

Limited filesystem access.
Restricted network access.
CPU limits.
Memory limits.
Execution timeouts.
Temporary workspaces.
Restricted privileges.

For higher-risk operations, dedicated virtual machines or disposable laboratory environments can provide stronger isolation.

Data Protection

Awesome Okapi_v2 may process security-sensitive information, so data protection should be considered throughout the architecture.

The platform should minimize stored information and retain only what is necessary for the security-testing purpose.

Sensitive data should be encrypted during transmission and protected at rest.

Access to assessment data should be governed by project permissions.

API

A secure API can allow authorized applications to interact with Awesome Okapi_v2.

Potential API resources include:

/projects
/targets
/assessments
/tasks
/findings
/campaigns
/reports
/audit
/users

API access should use authentication, authorization, rate limiting, input validation, and detailed logging.

Command Safety

Awesome Okapi_v2 should distinguish between informational commands, assessment commands, administrative commands, and high-risk operations.

High-risk operations should either be unavailable or require explicit authorization and approval.

The platform should reject malformed requests, unexpected parameters, unauthorized targets, suspicious command chaining, and attempts to bypass security policies.

Rate Limiting

Communication integrations should have rate limits to prevent abuse.

Rate limits can be applied by:

User.
Organization.
Channel.
Bot.
API token.
Project.
IP address.

The platform can temporarily block excessive requests and generate security alerts.

Monitoring

Administrators can monitor:

Authentication activity.
Command activity.
Failed authorization attempts.
Integration health.
Job execution.
Worker status.
Vulnerability findings.
Phishing simulations.
Suspicious behavior.

Security alerts can be routed to approved monitoring systems.

Incident-Response Support

Although Awesome Okapi_v2 is primarily designed for penetration testing and security validation, its controlled command architecture can also support incident-response exercises.

Security teams can use the platform to coordinate approved defensive actions in controlled environments.

For example, an incident-response exercise could simulate:

Malware detection.
Suspicious login activity.
Unauthorized access.
Compromised test endpoint.
Data-exposure scenario.
Phishing campaign.
Cloud-security incident.

The platform can track the actions taken by the response team and generate a timeline for after-action review.

Reporting

Awesome Okapi_v2 can generate professional penetration-testing reports.

A report can contain:

Executive summary.
Assessment scope.
Methodology.
Testing dates.
Assets assessed.
Findings.
Severity classifications.
Evidence references.
Business impact.
Remediation recommendations.
Retesting results.
Conclusion.

Technical reports can provide detailed information for security engineers, while executive reports can summarize business risk for management.

Security by Design

Awesome Okapi_v2 should follow a security-by-design philosophy.

Important principles include:

Least privilege.
Explicit authorization.
Default deny.
Strong authentication.
Separation of duties.
Scope validation.
Auditability.
Isolation.
Data minimization.
Secure secret management.
Continuous monitoring.

The fact that a user can access a communication channel should never automatically grant permission to execute a security-testing operation.

Educational Use

The platform can also serve cybersecurity students and training organizations.

Students can receive controlled laboratory assignments through supported messaging platforms and complete security exercises against intentionally vulnerable systems.

Instructors can monitor progress, review results, and generate training reports.

This provides an interactive environment for learning penetration-testing concepts while maintaining strict boundaries around real-world infrastructure.

Extensibility

Awesome Okapi_v2 can be designed with a plugin architecture.

Future integrations could include additional collaboration platforms, security scanners, SIEM systems, ticketing systems, cloud platforms, vulnerability-management platforms, and laboratory environments.

Each integration should follow the same security model.

A plugin should not automatically receive unrestricted access to the underlying system.

Deployment

Awesome Okapi_v2 can be deployed in several environments, including:

Private servers.
Security laboratories.
Cloud infrastructure.
Container platforms.
Virtualized environments.
Internal enterprise networks.

Production deployments should use secure network segmentation, HTTPS, centralized logging, backups, monitoring, and restricted administrative access.

Mission

The mission of Awesome Okapi_v2 is to make authorized penetration testing and cybersecurity training more accessible, organized, measurable, and secure.

By connecting communication platforms with controlled security-testing infrastructure, the platform can allow cybersecurity teams to coordinate assessments without requiring every operation to begin from a traditional terminal.

Its core philosophy is simple: centralized control, explicit authorization, controlled execution, comprehensive auditing, and safe security testing.

# Conclusion

Awesome Okapi_v2 is envisioned as a comprehensive cybersecurity platform for authorized penetration testing, security assessment, security-awareness training, and laboratory exercises.

Its multi-channel architecture enables authorized security professionals to interact with security-testing workflows through Discord, Telegram, Slack, Google Chat, WhatsApp, Signal, and a web application.

The platform can provide command orchestration, vulnerability-assessment workflows, laboratory execution, phishing-awareness simulations, reporting, role-based access control, scope enforcement, approval workflows, audit logging, and security monitoring.

The phishing component is designed specifically for authorized security-awareness exercises and should use controlled simulation pages rather than collecting real credentials. Likewise, the command-execution architecture should prioritize allowlists, isolated workers, scope validation, authentication, authorization, and comprehensive logging.

With these safeguards, Awesome Okapi_v2 can become a powerful platform for cybersecurity professionals, penetration testers, security teams, educators, and organizations seeking to evaluate and improve their defensive capabilities without turning communication integrations into unrestricted remote-access mechanisms.

Awesome Okapi_v2 — Authorized testing. Controlled execution. Measurable security. 


# How to Install 

```bash
git clone https://github.com/Iankulani/awesome_okapi_v2.git
cd awesome_okapi_v2
```

# How to run
```bash
python awesome_okapi_v2.py
```

# Documentation

# References:
```bash
```


# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Iankulani/awesome_okapi_v2&type=Date)](https://star-history.com/#Iankulani/awesome_okapi_v2&Date)
