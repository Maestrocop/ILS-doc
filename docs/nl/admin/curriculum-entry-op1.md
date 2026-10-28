## Mijlpaal: inzicht in gebruik en archivering (kritieke waarborgen)

Voer deze waarborgen in voordat het systeem verder groeit en zich ontwikkelt van CRUD naar een echt curriculumplatform:

### Inzicht in gebruik ("Waar wordt dit gebruikt?")
Controleer altijd het volgende voordat je een verwijderactie uitvoert of andere onomkeerbare wijzigingen toestaat (opdracht verwijderen, blauwdruk bewerken, module-item archiveren):

- In hoeveel modules wordt dit onderdeel gebruikt?
- In hoeveel actieve klassen?
- Hoeveel inzendingen verwijzen ernaar?
- Staat het in een rooster?

Zo voorkom je dat het curriculum per ongeluk wordt beschadigd of dat er gegevens verloren gaan wanneer hergebruik toeneemt.

### Alleen soft deletes of archiveren
Voor opdrachten, quizzen, modules en andere onderdelen van het curriculum:

- Vermijd definitief verwijderen; archiveer onderdelen of gebruik soft deletes.
- Zo blijven analyses, inzendingen, snapshots en verwijzingen vanuit roosters behouden voor historische controle.

**Samenvatting:**
Onderdelen, plaatsingen, herkomst en gebruik moeten naast elkaar blijven bestaan. Inzicht in gebruik en archivering zijn essentieel voor een veilige ontwikkeling van het curriculum en een stabiel platform.
## QA van begin tot eind: sessieoverzicht en architectuurstappen

Alle 8 stappen zijn tijdens deze sessie afgerond:

### Stappen 1–3 — Architectuur van curriculumonderdelen
- **Migratie 0070:** `origin_module_id` toegevoegd aan opdrachten (legt vast uit welke module de opdracht afkomstig is)
- **Opdrachtformulier:** trapsgewijze keuzelijst Cursus → Module toegevoegd om de herkomst bij het opslaan vast te leggen
- **POST/PUT:** beide maken automatisch een plaatsing in `module_items` aan als `origin_module_id` is opgegeven
- **Migratie 0071:** `is_blueprint`, `blueprint_id` en `derived_from_id` toegevoegd aan opdrachten (schema is actief; de gebruikersinterface volgt na #64)

### Stappen 4–6 — DIS-BASIS-inhoud
- **SM-BASIS Quiz 1 (id=11):** 10 ITIL meerkeuzevragen, tijdslimiet van 30 minuten, gepubliceerd
- **DIS-A1–A5 (ids 23–27):** PowerShell Basics, Python Fundamentals, SQL Queries, Automation Script en Data Analysis — allemaal gekoppeld aan DIS-BASIS via `origin_module_id` en `module_items`
- **DIS Quiz 1 (id=12):** 12 vragen (4 PowerShell, 4 Python, 4 SQL), gepubliceerd

### Stappen 7–8 — Klassen en rooster
- **Modules toegewezen:** SM-BASIS en DIS-BASIS toegewezen aan zowel WILISE1A als WILISE1B via `class_modules`
- **Roosters aangemaakt:**
  - WILISE1A: ma 9–11 / wo 13–15 / vr 10–12 → 63 bijeenkomsten
  - WILISE1B: di 9–11 / do 13–15 / vr 13–15 → 63 bijeenkomsten
  - Semester 1: 7 sep 2026 – 29 jan 2027

**Opmerking:** de backend moet opnieuw worden gestart om de twee modelwijzigingen (`origin_module_id`, `is_blueprint`, `blueprint_id`, `derived_from_id`) te laden.

---
Dit overzicht beschrijft de volledige QA van begin tot eind en het proces voor curriculuminvoer voor zowel beheerders als docenten, inclusief model- en gebruikersinterfacewijzigingen, inhoud aanmaken en roosters plannen.
## Stap 3 — Opdrachten en quizzen aanmaken, modules aan klassen koppelen en roosters plannen

Volg deze stappen voor elke module in de aangegeven volgorde (herhaal voor SM-BASIS en DIS-BASIS):

### 1. Opdrachten
- Ga naar: zijbalk Beheer → Opdrachten → + Nieuwe opdracht
- Maak voor elke module 5 opdrachten aan:
  - SM-BASIS: A1–A4 plus Service Management Simulation
  - DIS-BASIS: A1–A4 plus Mini Information System
- Doe voor elke opdracht het volgende:
  - Vul de titel, deadline en punten/schaal in en koppel de juiste module en leeruitkomsten volgens de curriculumkaart.
  - Sla de opdracht op en controleer of deze in de opdrachtenlijst van de module staat.

### 2. Quizzen
- Ga naar: zijbalk Beheer → Quizzen → + Nieuwe quiz
- Maak voor elke module de quiz aan:
  - SM-BASIS: Service Management Quiz 1
  - DIS-BASIS: Digital Information Systems Quiz 1
- Vul de titel, deadline, punten/schaal en het type (meerkeuze) in en koppel de juiste module.
- Sla de quiz op en controleer of deze in de quizlijst van de module staat.

### 3. Modules aan klassen toewijzen
- Ga naar: zijbalk Beheer → Klassen → [Selecteer klas: WILISE1A of WILISE1B]
- Wijs op de pagina met klasdetails (weergave van het lesplan voor docenten) beide modules (SM-BASIS en DIS-BASIS) aan elke klas toe.
- Controleer of beide modules voor elke klas in de lijst staan.

### 4. Roosters plannen
- Ga naar: zijbalk Beheer → Rooster (of Klasdetails → tabblad Rooster).
- Plan bijeenkomsten voor beide klassen vanaf september, volgens de moduleschema's (bijvoorbeeld SM-BASIS: maandag 09:00–11:00, DIS-BASIS: dinsdag 09:00–11:00).
- Voeg week 9 toe als inhaal- of evaluatieweek.
- Controleer of alle bijeenkomsten in de agendaweergave van elke klas staan.

---
Plak hieronder elke voltooide stap in het QA-formaat, zodat deze kan worden bijgehouden.
## Stap 2 — Module 1: Service Management Basis (volledig invoervoorbeeld)

In dit onderdeel staat een volledig voorbeeld van het invoeren van Module 1 (Service Management Basis) in het moduleformulier, met alle velden en onderdelen zoals ze in de gebruikersinterface worden getoond.

### Identiteit
- Cursus: ICT System Engineer
- Duur: 9 weken (8 lessen + 1 inhaalweek)
- Modulecode: SM-BASIS
- Niveau: N4
- Modulenaam: Service Management Basis
- Beschrijving: Inleiding in ICT-servicemanagement, ITIL-processen en hulpmiddelen voor servicemanagement. Studenten behandelen incidenten, communiceren met gebruikers en werken volgens SLA's.

### Thema's (gekoppeld)
- Seed Theme B
- Smoke Theme - edited123
- Seed Theme A
- Smoke Theme API
- Seed Theme A (edited)
- Service Management
- Communication Skills
- ITIL

### Moduledoelen
1. ITIL-basis — Maak kennis met de belangrijkste ITIL-processen voor servicemanagement.
2. Vaardigheid met hulpmiddelen — Ontwikkel praktische vaardigheden met een servicemanagementtool (TopDesk).
3. Professioneel communiceren — Pas communicatietechnieken toe in situaties met ICT-ondersteuning.

### Moduleopbouw (per week)
| Week | Onderwerp | Activiteit | Opbrengst / in te leveren werk |
|------|------------------------------------|-------------------------|---------------------------|
| 1 | Inleiding in ITIL en servicemanagement | College | Lezen en aantekeningen |
| 2 | Communicatie met gebruikers | College en rollenspel | Opdracht 1 |
| 3 | SLA's — theorie | College | Verslag, oefeningen… |
| 4 | SLA's — praktijk en quiz | Workshop | Opdracht 2 + quiz |
| 5 | Incidentbeheer | College | Verslag, oefeningen… |
| 6 | Praktisch werken met TopDesk | Practicum | Opdracht 3 |
| 7 | Problemen oplossen en escaleren | Workshop | Opdracht 4 |
| 8 | Project voorbereiden | Zelfstudie | Verslag, oefeningen… |
| 9 | (Inhalen / evalueren) | College, workshop… | Opdracht 5 |

### Beoordeling
| Type | Beschrijving | Weging (%) |
|------------|---------------------------------------------|------------|
| Opdracht | 4 individuele opdrachten (A1–A4) | 40 |
| Quiz | Meerkeuze — Service Management Quiz 1 | 20 |
| Project | Service Management Simulation (A5 + presentatie) | 40 |
| **Totaal** | | **100** |

### Verdieping / didactiek
- workshop
- College
- Seminar
- Zelfstudie
- Practicum

---
Plak hieronder elke voltooide stap (opslaan, toewijzen enz.) in het QA-formaat, zodat deze kan worden bijgehouden.
# Curriculum invoeren — OP1 (end-to-end-checklist voor beheerder en docent)

Deze pagina is een werkchecklist en sjabloon voor het invoeren van de curriculumreferentiekaart "OP1 — ICT Support and Systems · Jaar 1 · September 2027" in de beheerinterface van ILS. Gebruik de checklist tijdens de end-to-endtest. Plak na elke stap in de interface het resultaat in het gesprek met de assistent, met het voorgeschreven QA-formaat. De assistent zet dit om in de uiteindelijke gebruikerstekst.

Curriculumreferentiekaart — OP1

- Cursus: ICT Support and Systems (code: 23405)
- Gedeelde leeruitkomsten:
  - SO-1: Behoeften van gebruikers in duidelijke taal verduidelijken en vastleggen
  - SO-2: Een technische oplossing presenteren aan iemand zonder technische achtergrond

Module 1 — Service Management Basis (SM-BASIS)
- Uren OP1: 16 uur (8 × lessen van 2 uur)
- Totaal aantal uren: 34 uur
- Rooster: maandag 09:00–11:00 · week 9 = inhaalweek
- Leeruitkomsten:
  - SM-O1: ITIL-concepten en processen voor servicemanagement toepassen in het dagelijkse ICT-werk
  - SM-O2: Incidenten registreren en behandelen met een servicemanagementtool (TopDesk)
  - Gedeeld: SO-1 ✓, SO-2 ✓
- Opdrachten:
  - A1 — Inleiding in ITIL en servicemanagement — deadline week 2 (2027-09-12) — 10 punten (/10) — gekoppeld: SM-O1
  - A2 — Communicatie met gebruikers — deadline week 4 (2027-09-26) — 20 punten (/20) — gekoppeld: SO-1
  - A3 — Werken met SLA's — deadline week 6 (2027-10-10) — 15 punten (/20) — gekoppeld: SM-O1, SM-O2
    - Opmerking: punten en schaal komen niet overeen (15 punten vermeld, schaal /20). Controleer of de bedoelde schaal `/15` is of dat het aantal punten `20` moet zijn.
  - A4 — Incidenten afhandelen in TopDesk — deadline week 8 (2027-10-24) — voldoende/onvoldoende — gekoppeld: SM-O2
  - A5 — Service Management Simulation — deadline week 9 (2027-11-01) — 100 punten (/100) — gekoppeld: alle leeruitkomsten

- Quiz (sluit A2 af): Service Management Quiz 1 — deadline week 4 (2027-09-26) — 10 punten (/10) — meerkeuze

Module 2 — Basis digitale informatiesystemen (DIS-BASIS)
- Uren OP1: 16 uur (8 × lessen van 2 uur)
- Totaal aantal uren: 34 uur
- Rooster: dinsdag 09:00–11:00 · week 9 = inhaalweek
- Leeruitkomsten:
  - DIS-O1: Eenvoudige scripts schrijven en uitvoeren met PowerShell of Python
  - DIS-O2: Gegevens uit een database opvragen en interpreteren met SQL
  - Gedeeld: SO-1 ✓, SO-2 ✓
- Opdrachten:
  - A1 — Wat is digitale informatie? — deadline week 2 (2027-09-12) — 10 punten (/10) — gekoppeld: DIS-O1
  - A2 — Eenvoudige scripts schrijven — deadline week 4 (2027-09-26) — 20 punten (/20) — gekoppeld: DIS-O1
  - A3 — Logica en beslissingen in scripts — deadline week 6 (2027-10-10) — 15 punten (/20) — gekoppeld: DIS-O1
  - A4 — Basis van databases en SQL-query's — deadline week 8 (2027-10-24) — voldoende/onvoldoende — gekoppeld: DIS-O2
  - A5 — Een klein informatiesysteem bouwen — deadline week 9 (2027-11-01) — 100 punten (/100) — gekoppeld: alle leeruitkomsten

- Quiz (sluit A3 af): Digital Information Systems Quiz 1 — deadline week 6 (2027-10-10) — 10 punten (/10) — meerkeuze

Controles vóór invoer (bevestig dit voordat je begint)

- Controleer of de `Course` bestaat ("ICT Support and Systems"). Zo niet, maak deze dan aan via Beheer → Cursussen met code `23405`.
- Bepaal hoe je het verschil tussen het aantal punten en de schaal van A3 hierboven afhandelt.
- Zorg voor een beheerdersaccount met rechten om cursussen en modules aan te maken en, als dit een ander account is, een docentaccount ter controle.

Stap 1 — Module aanmaken (Module 1: Service Management Basis)

- Pad in de gebruikersinterface: zijbalk Beheer → Modules → + Nieuwe module
- Vul de velden exact als volgt in:
  - Naam: Service Management Basis
  - Code: SM-BASIS
  - Cursus: ICT Support and Systems (selecteer deze in de lijst)
  - Uren OP1: 16
  - Totaal aantal uren: 34
  - Rooster: maandag 09:00–11:00 (voeg als weekopmerking toe: week 9 = inhaalweek)
  - Leeruitkomsten: voeg SM-O1 en SM-O2 toe en koppel SO-1 en SO-2 als gedeelde leeruitkomsten
  - Opdrachten: maak de basisgegevens van opdrachten A1–A5 aan met de deadlines per week en schalen die hierboven staan

Klik na het opslaan op Opslaan en rapporteer het resultaat in dit QA-formaat (één stap per item):

- Rol: Beheerder | Docent
- Pagina / gebruikersinterface: (bijvoorbeeld Modules → Service Management Basis)
- Actie: (aanmaken, opslaan, toewijzen, uploaden enz.)
- Invoer en gebruikte gegevens: (exacte waarden, geüploade bestanden)
- Verwacht resultaat: (wat er zou moeten gebeuren)
- Werkelijk resultaat: (wat er gebeurde; plak foutmeldingen als die er zijn)

Voorbeeldrapport (vul dit in nadat je Module 1 hebt opgeslagen):

- Rol: Beheerder
- Pagina / gebruikersinterface: Modules → + Nieuwe module → Service Management Basis
- Actie: klik op Opslaan
- Invoer en gebruikte gegevens: Naam=Service Management Basis, Code=SM-BASIS, Cursus=ICT Support and Systems, Uren OP1=16, Totaal aantal uren=34, Rooster=ma 09:00–11:00
- Verwacht resultaat: de module is opgeslagen en staat in de modulelijst; de module kan in de cursus-editor worden geselecteerd.
- Werkelijk resultaat: (laat leeg als alles goed ging; plak anders de foutmelding of screenshot)

Opmerkingen voor de assistent

- Ik zet elk rapport dat je plakt om in een beknopte stap voor de handleiding voor beheerders en docenten en voeg probleemoplossing toe wanneer het werkelijke resultaat afwijkt van het verwachte resultaat.
- Ik wijzig `ILS-dev` niet; dit is alleen documentatie en het vastleggen van QA-resultaten.

## Stap 1 — Resultaat (vastgelegd)

- Rol: Beheerder
- Pagina / gebruikersinterface: Beheer → Cursussen
- Actie: controleren of de cursus "ICT Support and Systems" bestaat (zo niet, deze aanmaken)
- Invoer / gebruikte gegevens: Naam = ICT Support and Systems, Code = 23405
- Verwacht resultaat: de cursus bestaat of is aangemaakt en staat in de cursuslijst. Je kunt deze selecteren bij het aanmaken van een module.
- Werkelijk resultaat: afgerond zonder problemen (door de gebruiker gemeld). Bevestig of de cursus al bestond of is aangemaakt en plak de exacte weergavenaam als deze afwijkt van "ICT Support and Systems".

## Cursus aanmaken — ICT System Engineer (vastgelegd)

- Rol: Beheerder
- Pagina / gebruikersinterface: Beheer → Cursussen → + Nieuwe cursus
- Actie: cursus aanmaken en opslaan
- Invoer / gebruikte gegevens:
  - Volledige naam: ICT System Engineer
  - Code: Crebonr. 27016
  - Korte code: ISE-N4
  - Niveau: MBO 4
  - Duur: 3 jaar
  - Beschrijving: korte beschrijving van deze cursus…
  - Instellingen: Status = Concept, Inschrijving = Vrije inschrijving, Studiepunten (ECTS) = bijvoorbeeld 240
  - Cursuskleur: #92a30f
  - Partnerinstellingen: BIM Institute of Technology
- Verwacht resultaat: de cursus is opgeslagen en staat in de cursuslijst. De cursus kan worden geselecteerd bij het aanmaken van modules.
- Werkelijk resultaat: cursus aangemaakt (door de gebruiker gemeld). Bevestig de exacte cursusnaam en code zoals deze in de cursuslijst staan en of de status na het opslaan `Draft` bleef.



**Laatst bijgewerkt:** 2026-07-08
