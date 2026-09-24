## Admin User Guide — Setting Up a Mentor

### Step 1 — Assign the Mentor Role (Users page)

1. Go to **Settings → Users**
2. Find the staff member (e.g. Peter Groen)
3. Open the kebab menu → **Edit** (or the roles button)
4. Check **mentor** in the role list — they can keep `teacher` as well
5. Save

> The `mentor` role is the coarse gate. Without it, the person cannot access the review system at all.

---

### Step 2 — Assign Students (Student Advisors page)

1. Go to **Student Support → Student Advisors**
2. Click **Bulk Assign** and select the class
3. Choose advisor type: **mentor**
4. Select the staff member and the students they are responsible for
5. Save

> This is the fine gate. A mentor can only open a BSA review for students explicitly assigned to them here. If a student is not listed, the system will block the action with "You are not the assigned advisor for this student."

---

### The Rule

Both layers must be in place:

- `Settings → Users` → `users.roles` must include `mentor` (coarse gate).
- `Student Advisors` → `student_advisors` row must list the student(s) assigned to that mentor (fine gate).

Either alone is not sufficient: the person needs the `mentor` role and the student assignment to act on a given student's review.
