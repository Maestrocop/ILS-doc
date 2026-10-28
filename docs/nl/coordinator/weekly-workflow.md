# Wekelijkse werkwijze voor coördinatoren

**Missie:** ervoor zorgen dat onderwijs, leren en curriculumuitvoering binnen het programma op schema blijven.

## Rolbeschrijving

De coördinator is verantwoordelijk voor de gezondheid van het programma — niet om het werk zelf uit te voeren, maar om ervoor te zorgen dat het wordt gedaan. De coördinator grijpt in wanneer docenten, studenten of het curriculum achterop raken.

De coördinator werkt op programmaniveau, niet op klasniveau. De coördinator beoordeelt niet, registreert geen aanwezigheid en geeft geen les. De coördinator houdt toezicht, signaleert en handelt.

---

## Maandagochtend — wekelijkse controle

### 1. Onderwijsuitvoering
*Aanwezigheid • Beoordeling • Uitvoering van lessen*

| Signaal | Drempel | Actie |
|---|---:|---|
| Aanwezigheid niet geregistreerd voor een gegeven sessie | Elke keer | Neem contact op met de docent — "Registreer de aanwezigheid voor [Class] op [Date]" |
| Achterstand in het nakijken per docent | Meer dan 14 dagen oud | Neem contact op met de docent — escaleer als er binnen 48 uur geen reactie komt |
| Sessies zonder aankondiging geannuleerd | Elke keer | Neem contact op met de docent voor opvolging |

**Besluit:** neem voor elk achterstallig punt contact op met de docent of escaleer naar de programmamanager.

---

### 2. Controle van studievoortgang
*BSA-dossiers • Toewijzing van begeleiders • Aanwezigheidstrends*

| Signaal | Drempel | Actie |
|---|---:|---|
| Aanwezigheidspercentage van een student daalt | Minder dan 80% in deze periode | Start een gesprek met de begeleider |
| Student heeft 3 of meer opeenvolgende sessies gemist | Elke keer | Signaleer dit bij de SLB-begeleider en maak een interventienotitie aan |
| Student heeft opdrachten niet ingediend en de deadline is verstreken | Elke keer | Begeleider neemt contact op met de student |
| Studenten met risico in BSA | Iedereen in de rode zone | Plan een voortgangsbeoordeling in |

**Besluit:** wijs elke student die risico loopt toe aan een begeleider, plan een beoordeling in of registreer een interventie.

---

### 3. Controle van curriculumuitvoering
*Geplande dekking • Daadwerkelijke dekking • Moduletempo*

| Signaal | Drempel | Actie |
|---|---:|---|
| Gegeven tegenover geplande sessies voor een module | Minder dan 80% van het geplande aantal | Bespreek met de docent of de module op schema ligt |
| Module loopt achter op schema | Elke keer | Bespreek dit met de onderwijsverantwoordelijke — schema aanpassen of inkorten |
| Klasprestaties voor een module liggen aanzienlijk onder het gemiddelde | Gemiddelde cohort < 5.5 | Bespreek dit met de moduleverantwoordelijke — ligt het aan het curriculum of de uitvoering? |

**Besluit:** organiseer voor elke achterstand een gesprek met de docent of een curriculumbeoordeling.

---

## Einde van de week — status van het programma
**Vraag:** wat moet ik signaleren voordat de volgende week begint?

- Zijn er onopgeloste achterstanden in het nakijken?
- Zijn er studenten die de hele week afwezig waren?
- Zijn er BSA-dossiers waarvoor een formele beoordeling moet worden ingepland?
- Loopt een module aanzienlijk achter?

Zo ja → maak een taak aan, plan een gesprek of escaleer. Zo nee → het programma is gezond.

---

## Onderwijskwaliteit (vierde controle)

Deze controle gaat over continue verbetering, niet over de dagelijkse uitvoering.

Voorbeelden:
- Studenten geven herhaaldelijk aan dat opdracht X onduidelijk is.
- Module X heeft in drie cohorten een niet-slagingspercentage van 40%.
- Een leeruitkomst wordt nooit behaald.
- Exit- of reflectieformulieren laten zien dat hetzelfde onderwerp verwarring oplevert.

Actie: registreer aandachtspunten voor curriculumbeoordeling en plan een evaluatiegesprek over onderwijskwaliteit.

---

## Wat de coördinator NIET doet

- Beoordeelt geen inzendingen.
- Registreert geen aanwezigheid.
- Neemt niet rechtstreeks contact op met studenten over de lesinhoud (dat is de taak van de docent).
- Beheert geen individuele lesplannen.
- Wijst geen opdrachten toe.
- Maakt geen roosters (verantwoordelijkheid van de beheerder).

Dit zijn verantwoordelijkheden van docenten of beheerders. De coördinator grijpt alleen in wanneer de docent of het systeem niet handelt.

---

## Koppeling met ILS — wat bestaat en wat ontbreekt

Houd dit bij als een levend architectuurdocument: werk de status hier bij wanneer een functie is geïmplementeerd.

| Processtap | ILS-functie | Status |
|---|---|---:|
| Achterstand in het nakijken per docent bekijken | Dashboard → Teacher Grading Backlog | ✅ Beschikbaar |
| Aanwezigheid die niet per klas is geregistreerd bekijken | Monitoringpagina → Class Attendance | ✅ Beschikbaar (percentage = —) |
| Studenten zien die risico lopen | BSA-dashboard | ✅ Beschikbaar |
| Voortgangsbeoordeling inplannen | Voortgangsbeoordelingen | ✅ Beschikbaar |
| Aanwezigheidstrend van een student bekijken | Pagina Student Attendance | ✅ Beschikbaar |
| Gegeven tegenover geplande sessies bekijken | — | ❌ Ontbreekt |
| Interventie- of contactnotitie registreren | — | ❌ Ontbreekt |
| Klasprestaties per module bekijken | — | ❌ Ontbreekt |

---

## Conclusie voor de monitoringpagina

De monitoringpagina moet worden ingedeeld rond de drie bovenstaande controles — onderwijsuitvoering, studievoortgang en curriculumuitvoering — aangevuld met onderwijskwaliteit.

Elke sectie moet antwoord geven op de vraag: **"Wat moet ik doen als deze waarde rood is?"**

Als het antwoord duidelijk is en er binnen ILS actie op kan worden ondernomen, bouw de sectie dan. Is het antwoord "mail de docent buiten het systeem om", dan hoort de sectie als waarschuwing op het dashboard en niet op een afzonderlijke rapportagepagina.

---

## Voorgestelde taken (begin van de roadmap)

1. Implementeer de meetwaarde "Gegeven tegenover geplande sessies" voor modules (backend en UI-heatmap).
2. Voeg een model en UI voor "Interventie-/contactnotitie" toe om acties van coördinatoren vast te leggen en te koppelen aan studenten, docenten en modules.
3. Voeg rapportages met klasprestaties per module toe (gemiddeld cijfer per module en cohort).
4. Toon een widget voor achterstand in het nakijken per docent op het coördinatorendashboard (met doorklik naar de studentenlijst).
5. Voeg een tracker voor onderwijskwaliteit toe om kwalitatieve signalen vast te leggen (enquêtevragen voor studenten en exitreflecties).

---

**Laatst bijgewerkt:** 2026-07-06
