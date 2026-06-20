# Internships — End-to-End Flow

This page describes the complete internship search and application workflow for Coordinators, Coaches, and Students.

## Overview

The platform supports a verified application workflow where student applications are timestamped, trackable by coaches, and replies return to the school's inbox.

## Step 1: Coordinator creates a Programme

Go to **Internships** in the admin menu and click **+ New programme**.

Set:
- Class
- Academic year
- Type
- Programme name
- Search start and end dates

Click **Create Campaign**.

Result: A campaign is created and you are taken to the campaign detail page.

## Step 2: Coordinator enrolls students

Open the programme you just created and click **+ Enroll students**.

Select one or more students using the checkboxes and click **Enroll N students**.

Result: Students are enrolled and appear in the campaign's Search phase list.

## Step 3: Student uploads CV

Student navigates to their internship page and scrolls to **Your Documents**.

They:
1. Choose **CV** from the document type dropdown
2. Click **Choose file** and select the CV (PDF/DOCX)
3. Click **Upload**

The CV appears as **CV submitted — awaiting review**.

## Step 4: Coach reviews CV

Go to the campaign and click the student's name to open their detail view.

In the **Documents** section:
1. Click the student's CV
2. Choose status: **Approved ✓** or **Needs revision**
3. Optionally add coach feedback
4. Click **Save review**

Result: Document status is updated and the student can see the new status.

## Step 5: Student sees updated CV status

In **Your Documents** the CV now shows:
- `✓ CV approved` (green)
- `⚠ CV needs revision` (amber) with coach feedback

## Step 6: Student applies to companies

Student clicks **+ Apply to a company** and fills in:
- Company name
- Contact person
- Company email
- Select an approved CV from attachments
- Optionally upload a motivation letter

Then choose:
- **Log application** (record only)
- **Send application** (send via the app)

Result: The application appears in **My Applications**. The coach sees updates like "Lars sent application to Company X — 10 min ago" on the campaign timeline.

## Company reply & outcome update

When the company replies to the school's inbox:
1. Student opens the application in the app
2. Clicks **Update outcome**
3. Selects **Interview scheduled** and sets the date
4. Clicks **Save**

Result: The campaign dashboard and student timeline show "Lars — Interview @ Company X — next Tuesday" and the student's record advances in the search workflow.

## Status strings & where they appear

- `CV submitted — awaiting review` — appears in the student **Documents** panel after upload
- `✓ CV approved` — appears in the student **Documents** panel after coach approval
- `⚠ CV needs revision` — appears with coach feedback in the **Documents** panel
- Application: `sent_at` timestamp and `sent_via_app = true` are logged on the application record

Note: These status strings are shown in the Documents and Applications panels; they are intentionally not replicated in the page header.

---

## Implementation notes (non-technical)

The internship flow includes admin campaign setup, student document upload and coach review, supervisor invitations, and an application timeline. Email sending may require a mail relay configured by the school; when relay is not configured the action is recorded but external delivery is not guaranteed.

If you want, I can split this into `admin` + `student` quickstart pages, add screenshots, or produce a QA checklist. Tell me which and I'll continue.

## Recent changes (June 2026)

- A full internship lifecycle was implemented, including campaign management, supervisor portals, activity logs, evaluation phases, and auto-invitations for supervisors.
- The student application flow now supports both `Log only` and `Send from app` modes; if a relay is unavailable the system records a send attempt and shows a descriptive message to the coordinator.
