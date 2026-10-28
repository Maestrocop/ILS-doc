# Session Feedback — UI-mock-up

Deze mock-up toont een eenvoudige feedbackstroom voor docenten en studenten rond een lesmoment. Alleen-lezen: dit is uitsluitend documentatie; `ILS-dev` wordt niet aangepast.

## Docentenweergave (lesmomentkaart)

Lesmoment: BK-J1-2526 — ma 09:00–12:00 — Module: Inleiding Bedrijfskunde

- [Feedback aanvragen]

Wanneer de docent op `Request Feedback` klikt, doet het systeem het volgende:

1. Markeert het lesmoment als `feedback_requested`.
2. Stuurt ingeschreven studenten een korte vraag (in de app en eventueel via e-mail/sms).

## Studentenweergave (geschikt voor mobiel)

Kaart:

Lesmoment: ma 09:00–12:00 — Inleiding Bedrijfskunde

Hoe duidelijk was de les van vandaag?


Hoe betrokken voelde je je?


Wat is nog onduidelijk? (optioneel)

_Vrij tekstveld_

[Verzenden]

## Beknopte analyses (docent/coördinator)


## Visuele mock-ups

Docentenkaart voor een lesmoment (klik op `Request Feedback`):

![Docentenkaart voor een lesmoment](../../images/session-feedback-teacher-card.svg)

Dialoogvenster voor studenten (geschikt voor mobiel):

![Studentendialoogvenster](../../images/session-feedback-student-modal.svg)
## Minimale API-schets (alleen documentatie)

- POST `/api/feedback/session/:sessionId/request` — markeer dat feedback voor het lesmoment is aangevraagd en plan meldingen in
- POST `/api/feedback/session/:sessionId/response` — body: `{ student_id, clarity_score, engagement_score, comments }`
- GET `/api/feedback/session/:sessionId/summary` — retourneert geaggregeerde meetwaarden en voorbeeldopmerkingen


**Laatst bijgewerkt:** 2026-07-08
