# Roadmaptaken voor coördinatoren (doorlopende checklist)

Dit bestand is een doorlopende checklist van documentatieklare taken op basis van de wekelijkse werkwijze voor coördinatoren. Het gaat om documentatie- en producttaken — niet om codewijzigingen — en dient als gedeelde specificatie en acceptatiechecklist.

Elke taak bevat: eigenaar, prioriteit, inspanning, acceptatiecriteria, opmerkingen en status.

---

## 1. Meetwaarde gegeven tegenover gepland aantal sessies
- Eigenaar: Product / Analytics (documentatie)
- Prioriteit: Hoog
- Geschatte inspanning: Gemiddeld
- Acceptatiecriteria:
  - De documentatie beschrijft de vereiste databronnen: geplande sessies, gebeurtenissen voor sessies die 'held' zijn en annuleringen.
  - Definieert berekende velden: planned_sessions, delivered_sessions, percent_delivered.
  - Voorbeeldquery en verwachte uitvoer zijn opgenomen.
  - UI-acceptatie: het coördinatorendashboard toont percent_delivered; modules met minder dan 80% worden gemarkeerd.
- Opmerkingen: koppel dit aan bestaande rooster- en sessielogboeken.
- Status: Todo

---

## 2. Interventie- / contactnotitie (specificatie)
- Eigenaar: Product / UX (documentatie)
- Prioriteit: Hoog
- Geschatte inspanning: Gemiddeld
- Acceptatiecriteria:
  - Documenteer de velden van het gegevensmodel: author, linked_student_id, linked_teacher_id, module_id, note_text, timestamp, visibility, tags.
  - Documenteer rechten: wie kan aanmaken, bewerken, bekijken en verwijderen; bewaartermijnen volgens de AVG.
  - Voeg notities voor een UI-wireframe toe: notitie aanmaken, koppelen aan student/docent/module, notities weergeven en filteren.
  - Neem voorbeeld-API-payloads op voor aanmaken en lezen (alleen documentatie).
- Opmerkingen: auditlogging en bewaarbeleid moeten worden opgenomen.
- Status: Todo

---

## 6. Herinneringsengine en handmatige trigger (documentatie + specificatie)
- Eigenaar: Product / Operations (documentatie)
- Prioriteit: Hoog
- Geschatte inspanning: Klein → gemiddeld (eerst documentatie)
- Acceptatiecriteria:
  - Documenteer herinneringsdrempels en toon (`reminder-rules.md`).
  - Documenteer de escalatiematrix (`escalation-matrix.md`).
  - Beschrijf hoe beheerders de herinneringstaak handmatig kunnen uitvoeren voor tests.
  - Definieer de velden van `reminder_log` en acceptatiecriteria voor eenmalige herinneringen en escalatiemarkeringen.
- Opmerkingen: begin met een handmatig endpoint; voeg later een scheduler toe.
- Status: Todo

---

## 3. Rapportage van moduleprestaties op klasniveau
- Eigenaar: Product / Rapportage
- Prioriteit: Gemiddeld
- Geschatte inspanning: Gemiddeld
- Acceptatiecriteria:
  - Documenteer rapportagekolommen: module_id, cohort, average_grade, median_grade, submission_rate, sample_size.
  - Beschrijf filters en exportvereisten (datumbereik, cohort, module).
  - Voeg UI-wireframenotities toe voor de coördinatorweergave en doorklik naar de studentenlijst.
- Opmerkingen: verduidelijk de cijferschaal en hoe concepten worden behandeld.
- Status: Todo

---

## 4. Widget voor achterstand in het nakijken (coördinatorendashboard)
- Eigenaar: Product / UX
- Prioriteit: Hoog
- Geschatte inspanning: Klein
- Acceptatiecriteria:
  - Definieer wat als achterstand geldt (inzendingen die langer dan X dagen niet zijn beoordeeld).
  - Definieer de gegevenspunten voor de widget: docent, klas, aantal, oudste datum van een niet-beoordeelde inzending en link naar de achterstand bij de docent.
  - Documenteer verwachte interacties (filteren op docent en escalatieactie).
- Opmerkingen: hergebruik waar mogelijk bestaande gegevens over achterstand bij docenten.
- Status: Todo

---

## 5. Tracker voor onderwijskwaliteit
- Eigenaar: Product / Curriculum
- Prioriteit: Gemiddeld
- Geschatte inspanning: Gemiddeld
- Acceptatiecriteria:
  - Documenteer vastgelegde signalen (waarschuwingen uit studentenenquêtes, herhaaldelijk lage leeruitkomsten en niet-slagingspercentages per cohort).
  - Definieer de werkwijze voor het aanmaken van kwaliteitskwesties, toewijzen van beoordelaars en volgen van verbetermaatregelen.
  - Geef een voorbeeldindeling voor een dashboard met kwaliteitsmeetwaarden.
- Opmerkingen: dit is een langetermijnfunctie; neem alleen de eerste MVP-signalen op.
- Status: Todo

---

## Dit bestand gebruiken
- Werk `Status` bij naarmate je vordert.
- Werk taken uit in afzonderlijke specificatiebestanden (link naar de map `coordinator/`).
- Houd acceptatiecriteria beknopt en testbaar.

---

**Laatst bijgewerkt:** 2026-07-06
