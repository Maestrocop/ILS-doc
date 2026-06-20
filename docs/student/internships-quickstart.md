# Student Quickstart — Internship Search & Applications

This quickstart guides students through uploading documents, applying to companies (log or send), and updating application outcomes.

## Access the Internship Page

Open the **Internship Page** from your main dashboard.
It has two primary panels: **Your Documents** and **My Applications**.

## Upload your CV

1. In **Your Documents** select **CV** from the document type dropdown.
2. Click **Choose file**, pick your CV (PDF or DOCX), then click **Upload**.
3. After upload the UI shows: **CV submitted — awaiting review**.

Notes:
- The file is stored as a versioned `internship_document` and awaits coach review before it can be used for applications.
- Only the Documents panel shows the upload status.

## Check coach feedback and approval

- Refresh `/student/internship` after coach review.
- Approved: `✓ CV approved` (green) appears in the Documents panel.
- Needs revision: `⚠ CV needs revision` (amber) plus coach feedback appears.

If your CV needs revision, update your file and upload a new version.

## Apply to a company (Log or Send)

1. Click **+ Apply to a company** in **My Applications**.
2. Fill fields: Company name, Contact name, Company email.
3. Select an approved CV from the attachments dropdown.
4. Optionally attach or adapt a motivation letter.
5. Choose action:
   - **Log application** — saves the application in the system (no email sent).
   - **Send application** — attempts to send the application email from the app.

Behavior when sending:
- If the system mail relay (SendGrid/Mailgun) or SMTP is configured, the backend will send an email with the CV + letter attached.
- The application record is saved with `sent_at = now()` and `sent_via_app = true` when the send succeeds (or is recorded). If relay is not configured the app will record the request as "Send recorded (relay not configured)".

After sending or logging, the application appears in **My Applications** with company, date, and status.

## Update application outcome (e.g., interview)

1. In **My Applications** locate the application row and click **Update outcome**.
2. Select the new outcome (for example: **Interview scheduled**) and set the date.
3. Click **Save**.

Result: The application status and the student timeline update; coaches receive alerts such as: **"[Student] — Interview @ Company X — [date]"**.

## Troubleshooting & FAQs

- CV not in attachments dropdown: the CV is not yet **Approved**. Wait for coach review or re-upload a corrected version.
- I clicked Send but company didn't get the email: check the application record — if the system shows "Send recorded (relay not configured)", ask your coordinator to enable SMTP/relay in the backend `.env`.
- I can't see my application: verify class/campaign enrollment and page filters on `/student/internship`.

## Privacy & Coach visibility

- Applications sent via the app are timestamped and visible to your coach. This helps coaches support your search progress.
- Replies from companies go to the school's mailbox (Reply-To is set so replies route appropriately).

---

If you want a printable one-page checklist or a short in-app help panel text for this flow, tell me and I'll create it.
