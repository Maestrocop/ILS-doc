# Beheerdersgids

Deze gids beschrijft de beheer- en curriculumwerkwijzen die beschikbaar zijn in ILS.

## Verantwoordelijkheden van beheerders

Beheerders beheren de volledige levenscyclus van het curriculum, van de eerste inrichting tot en met rapportages.

## Belangrijkste beheerpagina's

De belangrijkste beheerpagina's zijn:

- **Instellingen** — beheer gegevens op instellingsniveau
- **Campussen** — beheer campussen en rapportageregels
- **Cursussen** — maak cursussen aan en beheer het cursusaanbod
- **Modules** — stel curriculumonderdelen vast en koppel leeruitkomsten, thema's en onderwijsmethoden
- **Opdrachten** — maak opdrachten binnen modules aan en beheer ze
- **Curriculum Composer** — bekijk en beheer curriculuminhoud op cursusniveau
- **Curriculum Composer V2** — maak cursusblauwdrukken van de volgende generatie met terugkerende periodestructuren
- **Mijn werk** — bekijk en beheer werkwijzen voor inzendingen
- **Course Builder** — bekijk cursusinhoud en -structuur zoals studenten die zien
- **Module Composer** — stel curriculuminhoud op moduleniveau samen en verfijn deze
- **Quizzen** — maak quizbeoordelingen aan en beheer ze
- **Klassen** — beheer klassen en context voor studenteninschrijvingen
- **Periodes** — beheer onderwijsperiodes
- **Thema's** — beheer thema's die op meerdere vakgebieden betrekking hebben
- **Leeruitkomsten** — beheer leeruitkomsten en categorieën
- **Categorieën** — beheer categorielabels die in leeruitkomsten en rapporten worden gebruikt
- **Rubrics** — maak beoordelingsrubrics aan en beheer ze
- **Criteriaoverzicht** — bekijk rubriccriteria van alle rubrics
- **Koppelingsmatrix** — bekijk welke leeruitkomsten in het curriculum door opdrachten worden beoordeeld
- **Projecten** — maak projectbeoordelingen en bijbehorende bestanden aan en beheer ze
- **Controlelogboeken** — bekijk systeemgebeurtenissen en wijzigingen
- **Controle installatie** — controleer of het systeem klaar is en of de configuratie in orde is
- **Docentendashboard** — bekijk kengetallen van docenten en overzichten van klassen en studenten
- **Gebruikers** — beheer gebruikers van de applicatie en hun rollen
- **Academische kalender** — beheer feestdagen, examenperiodes en semestergrenzen op instellingsniveau

## Curriculum beheren

In het curriculummodel van ILS zijn de structurele inhoud en de leerinformatie van elkaar gescheiden.
Beheerders bouwen het curriculum op in deze lagen:

- **Structurele hiërarchie** — instellingen, campussen, cursussen, modules, opdrachten en klassen
- **Leer- en beoordelingslaag** — thema's, leeruitkomsten, rubrics, rubriccriteria en scores

Door deze scheiding blijft de curriculumstructuur stabiel en kun je evaluatie- en rapportageonderdelen hergebruiken.

### Cursussen en modules beheren

- **Cursussen** zijn de benoemde onderdelen op het hoogste niveau.
- **Modules** horen bij cursussen en vormen de onderdelen waarin het curriculum wordt aangeboden.
- **Opdrachten** horen bij modules en zijn de taken die studenten inleveren.
- **Klassen** koppelen studenten aan een module en bieden de context voor beoordeling.

### Module-editor

Met de module-editor kun je:

- modulegegevens bewerken
- leeruitkomsten aan een module koppelen
- onderwijsmethoden toevoegen
- de structuur van een module bepalen
- beoordelingsregels en wegingen instellen

### Opdracht-editor

Met de opdracht-editor kun je:

- opdrachtgegevens en deadlines beheren
- instellingen voor de beoordeling van opdrachten aanpassen
- gekoppelde rubrics selecteren
- een opdracht voor een module aanmaken

## Rubrics en leeruitkomsten beheren

Rubrics zijn de belangrijkste instrumenten voor beoordeling in het systeem.
Als beheerder kun je:

- een rubric aanmaken met een titel, beschrijving en categorie
- criteria aan de rubric toevoegen
- scoringsniveaus voor elk criterium instellen
- afzonderlijke criteria aan leeruitkomsten koppelen
- overbodige rubrics verwijderen

De pagina Criteriaoverzicht is alleen-lezen en toont alle criteria van alle rubrics.
Je kunt deze pagina gebruiken om:

- te controleren welke criteria door rubrics worden gedekt
- criteria te vinden die al aan leeruitkomsten zijn gekoppeld
- de consistentie tussen rubrics te controleren

### Leeruitkomsten beheren

Leeruitkomsten zijn de leerdoelen waarop rapportages over beheersing zijn gebaseerd.
Beheerders kunnen:

- gegevens van leeruitkomsten aanmaken en bewerken
- leeruitkomsten aan categorieën toewijzen
- berekeningsmethoden en parameters voor scores op leeruitkomsten instellen

De koppeling `module_learning_outcomes` verbindt leeruitkomsten aan modules.
Het veld `rubric_criteria.linked_outcome_id` koppelt rubriccriteria aan leeruitkomsten voor rapportages.

## Rapportages en leerinformatie beheren

Beheerpagina's geven ook inzicht in de rapportagegegevens die docenten gebruiken:

- **Koppelingsmatrix** toont welke leeruitkomsten door welke opdrachten worden beoordeeld.
- **Heatmap** en **Classroom Intelligence** zijn rapporten voor docenten die afhankelijk zijn van koppelingen tussen rubrics en leeruitkomsten.

De matrix is vooral handig om te controleren of opdrachten en rubrics de gewenste leeruitkomsten dekken.

## Kalender beheren en roosters maken

De kalender bevat nu weergaven per rol en functies voor de onderwijsplanning.

- `/admin/calendar` — docentenagenda (deadlines en eigen activiteiten voor meerdere klassen)
- `/admin/classes/:classId/calendar` — agenda voor één klas
- `/admin/academic-calendar` — beheer van onderwijsactiviteiten voor de hele instelling, zoals feestdagen, examenperiodes en begin- en einddatums van semesters

Gegevens in de academische kalender worden apart beheerd van opdrachten en quizzen. Datums van opdrachten en quizzen verschijnen via berekende gebeurtenissen wel in de agendaweergaven.

## Aandachtspunten voor API en backend

Beheertaken worden uitgevoerd via backend-routes in `ILS-dev/backend/routes`.
Belangrijke backend-eindpunten zijn:

- `/api/courses`
- `/api/modules`
- `/api/assignments`
- `/api/themes`
- `/api/outcomes`
- `/api/rubrics`
- `/api/matrix`

Sommige beheertaken zijn ook beschikbaar onder `/api/admin/*` voor migraties en hulpprogramma's voor metadata.

## Praktische werkwijze voor beheerders

1. Maak cursus- en modulegegevens aan of controleer ze.
2. Definieer leeruitkomsten en onderwijsmethoden voor modules.
3. Stel rubrics samen en koppel criteria aan leeruitkomsten.
4. Maak opdrachten aan en koppel rubrics eraan.
5. Maak klassen aan voor het onderwijs en schrijf studenten in.
6. Controleer de dekking in de Koppelingsmatrix.
7. Gebruik rapportagepagina's voor docenten om te controleren of gegevens over beheersing van leeruitkomsten goed worden verwerkt.

## Wat deze gids niet behandelt

Deze gids is geen complete handleiding voor systeembeheer.
De inhoud is gericht op de huidige beheerfuncties in `ILS-dev` en het productiedatamodel.


**Laatst bijgewerkt:** 2026-07-08
