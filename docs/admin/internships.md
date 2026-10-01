# Internships — End-to-End Flow

This page describes the verified, coach-visible internship search and application flow for Coordinators, Coaches, and Students.

---

## Overview

The platform supports a verified "send from app" workflow so student applications are timestamped, trackable by the coach, and replies land in the school's mailbox. The flow below describes the happy path for coordinator setup, student document handling, coach review, and application logging/sending.

---

## Four-phase internship lifecycle

The internship process also maps to four phases that match the role responsibilities already visible in the product:

### 1. Searching

- **Student**: uploads CV and motivation letter, sends applications to companies, and tracks outcomes such as pending, interview scheduled, rejected, or accepted.
- **School**: reviews and approves CV / motivation letter documents and monitors whether the student is actively applying. This is where the **at risk - no applications** signal belongs.
- **Company**: not involved yet; no supervisor exists at this stage.
- **Moves to Placed when**: an application's outcome becomes **accepted**.

### 2. Placed

- **Student**: confirms placement details.
- **School**: verifies company details and works through the placement checklist: supervisor assigned, dates defined, learning objectives set, agreements signed.
- **Company**: assigns the supervisor, receives the token-based portal link, confirms company details, and confirms the working schedule.
- **Moves to On-site when**: the placement checklist is sufficiently complete and / or the start date arrives.

### 3. On-site

- **Student**: submits regular activity logs. This is the primary evidence trail.
- **School**: monitors engagement using days since last log and hours logged, and intervenes if the student goes quiet. This is the execution monitoring / risk dashboard gap.
- **Company**: supervisor acknowledges or comments on logs via the portal link.
- **Moves to Evaluating when**: the end date arrives or the school explicitly opens evaluation.

### 4. Evaluating

- **Student**: optionally submits a self-reflection.
- **School**: submits assessment score and feedback.
- **Company**: supervisor submits an independent assessment. The gap between the two scores is itself a useful signal for calibration and reality-checking.
- **Marked complete when**: both assessments are in, or the school closes it out.

---

## Step 1: Coordinator creates a Programme (Admin)

- Go to: `/admin/internships`
- Click **+ New programme**
- Select: Class, Academic year, Type, Programme name, Search start / end dates
- Click **Create Campaign**

Result: A campaign record is created and you are taken to the campaign detail page.

---

## Step 2: Coordinator enrolls students (Admin)

- Open the programme you just created (`/admin/internships` → select campaign)
- Click **+ Enroll students**
- Select one or more students using the checkboxes
- Click **Enroll N students**

Result: An `internship` record is created for each enrolled student and they appear in the campaign's Search phase list.

---

## Step 3: Student uploads CV (Student)

- Student logs in and navigates to `/student/internship`
- Scroll to the **Your Documents** section
- Choose **CV** from the document type dropdown
- Click **Choose file** and select the CV (PDF/DOCX)
- Click **Upload**

App shows: **CV submitted — awaiting review** (status visible in the Documents panel)

Note: The uploaded file is stored as a versioned `internship_document` and waits coach review.

---

## Step 4: Coach reviews CV (Admin / Coach)

- Go to: `/admin/internships/campaigns/[id]`
- Click the student's name to open the student detail view
- Find the **Documents** section and click the student's CV
- Choose status: **Approved ✓** or **Needs revision**
- Optionally add coach feedback
- Click **Save review**

Result: Document status is updated. If approved, the CV becomes selectable for applications.

---

## Step 5: Student sees updated CV status (Student)

- Student refreshes `/student/internship`
- In **Your Documents** the CV now shows one of:
  - `✓ CV approved` (green)
  - `⚠ CV needs revision` (amber) — coach feedback is shown

Important: The document status updates in the Documents panel only (not in the page header).

---

## Step 6: Student applies to companies (Student)

- In `/student/internship` click **+ Apply to a company**
- Fill in company details: Name, Contact, Company email
- Select an approved CV from the attachments dropdown
- Optionally upload/adapt a motivation letter
- Choose action: **Log application** (record only) or **Send application** (send via app)

Behavior when sending:
- If **Send application** chosen the backend records `sent_at = now()` and `sent_via_app = true` and attaches the selected document IDs.
- If SMTP/relay not configured the action is logged and marked as "Send recorded (relay not configured)".

Student UI: The application appears in **My Applications** with company, date, and status.

Coach UI: Coach sees timeline/alerts such as: **"Lars sent application to Company X — 10 min ago"** on the campaign risk/updates panel.

---

## Company reply & outcome update

- Company replies to the school's mailbox (reply-to configured by send-from-app behaviour)
- Student opens the application in the app and clicks **Update outcome** on the application row
- Select: **Interview scheduled** and set date (e.g., next Tuesday)
- Click **Save**

Result: Campaign risk board and student timeline reflect: **"Lars — Interview @ Company X — next Tuesday"** and the student's record is advanced in the search workflow.

---

## Status strings & where they appear

- `CV submitted — awaiting review` — appears in the student **Documents** panel after upload
- `✓ CV approved` — appears in the student **Documents** panel after coach approval
- `⚠ CV needs revision` — appears with coach feedback in the **Documents** panel
- Application: `sent_at` timestamp and `sent_via_app = true` are logged on the application record

Note: These status strings are shown in the Documents and Applications panels; they are intentionally not replicated in the page header.

---

## Developer & QA notes (short)

- Route references:
  - Admin campaign list: `/admin/internships`
  - Campaign detail: `/admin/internships/campaigns/[id]`
  - Student dashboard: `/student/internship`
- Database entities involved: `internship_documents`, `internship_applications`, `internships` (enrollments)
- Email sending: prefer relay (SendGrid/Mailgun) initially; add SMTP_* env block for direct-from-school option later.

---

If you want, I can split this into two files (`admin` + `student` quickstart), add screenshots, or create a QA checklist. Tell me which and I'll continue.
