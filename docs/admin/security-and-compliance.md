# Security & Compliance

This guide helps institutional IT admins prepare ILS for deployment and operation.

## Before Going Live

### Essential Deployment Requirements

**Environment Setup**
- [ ] Secure hosting provisioned (EU data center if serving EU schools)
- [ ] HTTPS configured (no HTTP)
- [ ] Database not publicly accessible (firewall rules)
- [ ] Admin interfaces (pgAdmin, SSH) restricted to known IPs only
- [ ] SSH key-only authentication configured

**Secrets Management**
- [ ] All environment variables set in production (never from `.env` files)
- [ ] Database password generated (strong, random, 32+ characters)
- [ ] Email password configured in secure secret store
- [ ] JWT secret generated (256-bit random string, never reused)

**Database & Backups**
- [ ] Database migrations applied on first run
- [ ] Automated backups scheduled (minimum daily)
- [ ] Backups stored off-server (not on same machine as application)
- [ ] Backups encrypted at rest
- [ ] Restore test performed on a different server (critical!)
- [ ] Restore procedure documented

**Monitoring & Alerting**
- [ ] Uptime monitoring configured (e.g., UptimeRobot)
- [ ] Error tracking enabled (e.g., Sentry)
- [ ] Disk space alerts configured
- [ ] Backup status alerts configured
- [ ] Email delivery status monitored

**Email Delivery**
- [ ] SPF, DKIM, DMARC DNS records configured for sending domain
- [ ] Test email sent and received successfully
- [ ] Verify emails are not landing in spam folders

---

## System Health Dashboard (Admin Page)

After go-live, administrators should check the **System Health** page daily. This shows:

### Operational Status
- Attendance completion rate today
- Assignments awaiting grading (oldest first)
- Students at risk (requires intervention)
- Teachers with overdue grading (>7 days)

### System Status
- Notification queue health
- Last backup completion time
- Email service status
- Disk usage

### Security Status (Last 24 Hours)
- Failed login attempts
- Locked accounts
- Password resets
- Suspicious activity alerts

**Action:** If any indicator is red or amber, contact your system administrator immediately.

---

## Data Protection & GDPR Compliance

### Your Responsibilities as Data Controller

ILS is a **data processor**. Your school is the **data controller**. You are responsible for:

1. **Consent** — Ensure students and staff have consented to their data being in ILS
2. **Privacy Policy** — Publish how student data is used, stored, and protected
3. **Data Retention** — Define how long records are kept (typical: 7 years after graduation)
4. **Data Subject Rights** — Be prepared to handle requests to export or delete student data
5. **Incident Response** — Have a plan if data is breached or lost

### Data Minimization

ILS collects:
- ✅ Student name, ID, email, cohort (required for functionality)
- ✅ Grades and attendance (core educational data)
- ❓ Student photos (requires explicit consent)
- ❓ Attendance patterns/analytics (requires consent if used for purposes beyond grading)

**Before using behavioral analytics or optional features, ensure you have explicit consent from students/parents.**

### Data Retention

**Recommended retention schedule:**
- Grades & attendance: 7 years after graduation
- Personal data (names, emails): 7 years after graduation
- Temporary files (drafts, backups): 30 days

Contact your system administrator to configure retention policies.

### Data Export (Right to Portability)

Students and staff can request a complete export of their data from ILS. The export includes:
- Grades
- Attendance records
- Submissions and feedback
- Timeline events
- All personal data in the system

**To request an export:**
1. Go to **Settings** → **Data Export**
2. Click **Request Export**
3. The system emails you the exported data within 24 hours

### Data Deletion (Right to Erasure)

Students and staff can request deletion of their account and associated data.

**Important:** Some data may be legally required to retain (BSA decisions, final grades). Deletion requests are reviewed by your administration before processing.

---

## Audit Logs & Grade Integrity

All changes to student records are logged:

- **Grade changes** — who changed it, from what value to what value, when, and why
- **Attendance changes** — who marked attendance, edit history if modified
- **Role changes** — who was promoted/demoted, by whom, when
- **File access** — who downloaded which submission file, when

These logs are **immutable** — they cannot be edited or deleted. They exist to:
- Protect teachers from accusations of grade manipulation
- Give schools confidence in assessment integrity
- Comply with audits and investigations

**Accessing logs:** Contact your system administrator for audit log reports.

---

## Backup & Disaster Recovery

### Recovery Objectives

- **RPO (Recovery Point Objective):** Maximum 24 hours of data loss
- **RTO (Recovery Time Objective):** Maximum 4 hours to restore to normal operation

### Backup Schedule

- **Daily:** Full database backup (1:00 AM)
- **Hourly:** Incremental transaction log backups
- **Weekly:** Verification restore test on separate server

### Restore Procedure

If your database is lost or corrupted:

1. **Stop the application** (prevent further writes)
2. **Provision a clean server** with the same OS and PostgreSQL version
3. **Restore the latest backup** (IT admin procedure)
4. **Verify data** — check that students, classes, and grades are present
5. **Restart the application**
6. **Run a test** — log in and verify core workflows work

**Time required:** 1–4 hours depending on database size

Contact your system administrator for full restore procedures.

---

## Security Best Practices for Your School

### For All Users
- ✅ Use a strong, unique password (12+ characters, mixed case, numbers, symbols)
- ✅ Never share your login credentials
- ✅ Log out when leaving a computer
- ✅ Report suspicious activity to your IT admin

### For Teachers & Coordinators
- ✅ Verify student submissions are authentic (check timestamps, metadata)
- ✅ Review grade history if a student's score seems unusual
- ✅ Use the audit logs to demonstrate due diligence for high-stakes decisions

### For Administrators
- ✅ Monitor failed login attempts (System Health dashboard)
- ✅ Review access logs if sensitive data access is questioned
- ✅ Enforce password changes annually
- ✅ Archive or delete accounts when staff/students leave
- ✅ Test backups quarterly

---

## Incident Response

### If Something Goes Wrong

**Data Loss / Corruption**
1. Contact system administrator immediately
2. Do NOT attempt to restore without IT support
3. System will restore from latest backup (24-hour window)

**Security Breach / Unauthorized Access**
1. Contact system administrator
2. System will investigate audit logs to determine what was accessed and by whom
3. Affected individuals will be notified

**System Unavailable / Down**
1. Check System Health dashboard
2. Contact system administrator if status shows system is down
3. ETA for recovery will be provided

**Email Not Working**
1. Check that SPF/DKIM records are configured
2. Check email firewall/antivirus is not blocking
3. Send a test email from ILS (Settings → Send Test Email)

---

## Contact & Support

**System Administrator:** [Your contact here]  
**Email Support:** [support email]  
**Emergency Hotline:** [phone number]  

---

**Last Updated:** 2026-06-27  
**Version:** 1.0 (Pilot Readiness)
