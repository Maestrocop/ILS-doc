# Admin Quick Start

Essential steps for administrators preparing ILS for school use.

## 1. Environment & Secrets
- Ensure production env variables are set (do NOT use `.env` in git)
- Rotate JWT secret, SMTP and DB passwords when provisioning

## 2. User & Institution Setup
- Create institutions, campuses, and courses under **Admin → Institutions**
- Set `Mastery Levels` in **Settings** before importing outcomes

## 3. Timetable & Class Setup
- Use **Class Setup** to create classes and assign `class_module_teachers`
- In **Timetable**, create schedule rules and **Publish** timetables (published timetables are visible to teachers/students)

## 4. Backups & Monitoring
- Verify automated backups and test a restore on a separate server
- Enable monitoring and error alerts (Sentry, uptime checks)

## 5. Security Checklist (Before Pilot)
- HTTPS + HSTS enabled
- Rate limiting on login and sensitive endpoints
- Audit logging enabled for grades and attendance
- File download/delete authorization enforced

## Troubleshooting & Support
- For data export/import issues, use the Admin Tools page
- For suspicious access, review Security Logs and revoke sessions

**Last updated:** 2026-07-03
