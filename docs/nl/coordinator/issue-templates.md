# Issuetemplates voor coördinatoren

Kopieer deze issuetemplates naar je issue tracker wanneer je implementatiewerk aanmaakt voor roadmaptaken van coördinatoren.

## Gegeven tegenover gepland aantal sessies — issuetemplate

**Titel:** Meetwaarde voor gegeven tegenover gepland aantal sessies implementeren

**Beschrijving:**

Doel: `planned_sessions`, `delivered_sessions` en `percent_delivered` per module berekenen en tonen op de pagina Status van het programma voor coördinatoren.

**Acceptatiecriteria:**
- De backend berekent de velden en slaat ze op of maakt ze beschikbaar via de API.
- De UI voor coördinatoren toont percent_delivered per module en markeert modules met minder dan 80%.
- Een voorbeeld van de API-respons is opgenomen in de specificatie.

**Opmerkingen:** databronnen: roostergebeurtenissen (gepland), gebeurtenissen voor gegeven sessies (geleverd) en annuleringen.

## Interventienotitie — issuetemplate

**Titel:** Model en UI voor interventie- / contactnotities toevoegen

**Beschrijving:**

Doel: coördinatoren en begeleiders in staat stellen interventienotities aan te maken, te bekijken en te doorzoeken, gekoppeld aan studenten, docenten en modules.

**Acceptatiecriteria:**
- De velden van het gegevensmodel zijn geïmplementeerd zoals beschreven in de specificatie.
- De UI-processen voor aanmaken, weergeven en bekijken zijn geïmplementeerd.
- Rechten worden afgedwongen en auditlogging is aanwezig.

## Rapportage van moduleprestaties op klasniveau — issuetemplate

**Titel:** Rapportage van moduleprestaties op klasniveau toevoegen

**Beschrijving:**

Doel: het gemiddelde cijfer per module en cohort tonen, filterbaar op datumbereik en exporteerbaar als CSV.

**Acceptatiecriteria:**
- Rapportagekolommen: module_id, cohort, average_grade, median_grade, submission_rate, sample_size.
- Toegankelijk via Status van het programma voor coördinatoren, met doorklik naar de studentenlijst.

---

Gebruik deze templates als uitgangspunt; pas eigenaren en schattingen aan je werkwijze aan.

**Laatst bijgewerkt:** 2026-07-06
