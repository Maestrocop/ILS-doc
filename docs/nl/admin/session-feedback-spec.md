# Session Feedback — RFC / specificatie (alleen documentatie)

Doel: een minimaal, implementatieonafhankelijk ontwerp voor Session Feedback beschrijven voor productdocumentatie en technische besprekingen. Dit is uitsluitend documentatie; `ILS-dev` wordt niet aangepast.

## Doelen

- Korte feedback van studenten met een hoge respons vastleggen, gekoppeld aan een specifiek lesmoment.
- Directe signalen tonen aan docenten en coördinatoren (signalen bij kleine aantallen).
- Reacties bewaren voor analyses en rapportages over langere perioden.

## Belangrijkste UX-processen

1. Een docent vraagt feedback aan voor een lesmoment (knop `Request Feedback` op de lesmomentkaart).
2. Studenten ontvangen een korte vraag (in de app en eventueel via e-mail/sms) en sturen hun antwoorden in.
3. Geaggregeerde resultaten verschijnen in het overzicht van het lesmoment en in Intelligence Hub.

## Minimale enquête (aanbevolen)

1. Duidelijkheid: 1–5
2. Betrokkenheid: 1–5
3. Vrije tekst: "Wat is nog onduidelijk?" (optioneel)

Houd het totale aantal vragen op maximaal 3 om het responspercentage te verhogen.

---

## Gegevensmodel (alleen documentatie)

- session_feedback
  - id: bigint PK
  - session_id: bigint FK -> sessions
  - student_id: bigint FK -> users
  - clarity_score: smallint
  - engagement_score: smallint
  - comments: text
  - created_at: timestamptz

- session_feedback_summary (gematerialiseerde view / gedenormaliseerd)
  - session_id
  - avg_clarity
  - avg_engagement
  - response_count
  - latest_comments (voorbeeld)

Opmerkingen: sla scores op als gehele getallen; houd comments nullable.

---

## Minimale API-oppervlakte (alleen documentatie)

- POST `/api/feedback/session/:sessionId/request`
  - Auth: docent of beheerder
  - Actie: markeer session.feedback_requested = true; plan meldingen in; retourneer 202

- POST `/api/feedback/session/:sessionId/response`
  - Body: `{ student_id, clarity_score, engagement_score, comments? }`
  - Auth: student (of systeem via een beveiligd token)
  - Actie: voeg een rij toe aan `session_feedback`; werk het overzicht bij

- GET `/api/feedback/session/:sessionId/summary`
  - Retourneert geaggregeerde meetwaarden en voorbeeldopmerkingen

Beveiliging: zorg ervoor dat alleen studenten die voor het lesmoment zijn ingeschreven een reactie kunnen indienen.

---

## Analyse en Intelligence

- Realtime signalen bij kleine aantallen: als response_count < 10 maar avg_clarity <= 2, toon dan een waarschuwing voor de coördinator.
- Trends: aggregaties op moduleniveau over lesmomenten en onderwijsperioden.
- CSV-export voor handmatige beoordeling.

---

## Voorgestelde beheerpagina's (alleen documentatie)

- Dashboard Session Feedback: lijst met recente lesmomenten en gemiddelde scores, met filters voor klas, module en docent.
- Feedbackrapport per module: geaggregeerde feedback over lesmomenten per module en periode.

---

## Migratieopmerkingen (alleen documentatie)

- De nieuwe tabel `session_feedback` kan via migraties worden toegevoegd; een backfill is optioneel.
- Backfill: als historische feedback op lesmomentniveau niet bestaat, begin dan vanaf nu met verzamelen.

---

Als je wilt, voeg ik JSON-voorbeeldpayloads voor de API's en een voorbeeldsjabloon voor migratie-SQL toe aan de documentatie. Ik wijzig `ILS-dev` niet.


**Laatst bijgewerkt:** 2026-07-08
