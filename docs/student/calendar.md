# Student Calendar

Your calendar shows all your deadlines, class sessions, and important dates in one timeline.

## What you see on your calendar

- **Assignment due dates** — when each assignment is due
- **Quiz dates** — when quizzes are scheduled and when they are due
- **Class sessions** — when your classes meet
- **Calendar events** — special events, holidays, or announcements from your teachers or institution

## How to use the calendar

1. Open **My Calendar** in your dashboard
2. Look at today and the next 4 months of upcoming events
3. Click any event to see more details or jump to the assignment/quiz

## Event types explained

- **Assignment open** — the day an assignment becomes available for you to start
- **Assignment due** — the deadline for submitting your work
- **Quiz available** — the day a quiz opens for you to attempt
- **Quiz due** — the deadline to complete the quiz
- **Class session** — your regular class meeting time
- **Academic event** — holidays, exam periods, semester boundaries, or other campus-wide dates

## Planning tip

Check your calendar at least once a week to stay on top of deadlines. Mark high-priority assignments in your personal calendar so you don't miss them.

## Recurring events

Some events repeat each week (like regular classes or weekly check-ins). When you see a recurring event, the calendar shows each occurrence so you can see the full pattern.
3. Students view events and dates; color coding is used to indicate class context (client sets `useClassColor=true`).
4. Students cannot add events via the calendar UI (`canAddEvent=false`) — only teachers and admins can create calendar events.

Troubleshooting & Gate clarifications

- Ambiguity: precise route path/URL label for "My Calendar" in the student navigation (I can capture the literal label from the running UI if you want exact copy).
- Ambiguity: whether class sessions are stored in a dedicated table or derived — code suggests class module linkage and class_module relationships are used to map assignment/quiz items into class calendars.

References (read-only)

- `frontend/src/pages/StudentCalendarPage.jsx`
- `frontend/src/components/CalendarWidget.jsx`
- `backend/routes/events.js`

---

Next steps: I will wait on your confirmation whether to document `Student Cockpit` here or treat it as a teacher-facing page (code in `frontend/src/pages/StudentCockpitPage.jsx` shows Teacher/Manager scopes). If you prefer I proceed to draft `Student Cockpit` under Teacher Guide, I will do so and validate with `mkdocs build --strict`.