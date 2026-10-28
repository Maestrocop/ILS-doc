# Periodes

Op de pagina Periodes beheer je de academische tijdsindeling die voor klassen en rapportages wordt gebruikt.

## Wat je kunt doen

Ga in het beheermenu naar **Periodes** om:

- alle actieve academische periodes te bekijken
- periodes met begin- en einddatums aan te maken en bij te werken
- verouderde of ongebruikte periodes te verwijderen
- een geneste hiërarchie van academische periodes te definiëren (semesters, blokken, onderdelen)
- herbruikbare periodetemplates voor cursussen en programma's te beheren
- gebeurtenissen in de academische kalender te beheren (feestdagen, examens, sluitingsdagen)

## Gebeurtenissen in de academische kalender

Gebeurtenissen in de Academische kalender staan los van Academische periodes. Ze leggen uitzonderingen en speciale datums vast, zoals:

- feestdag
- examen
- sluitingsdag
- gebeurtenis

Gebeurtenissen kunnen gelden voor een instelling, campus of klas. Ze bevatten opties zoals:
- Is dit een lesdag?
- Zichtbaar voor studenten?
- Zichtbaar voor docenten?

Deze gebeurtenissen zijn afzonderlijke agenda-aanduidingen die de zichtbaarheid en de status van het onderwijs per dag beïnvloeden.

## Officiële academische periodes tegenover periodes in een cursusblauwdruk

**Academische periodes** vormen de officiële kalenderstructuur van de instelling. Ze zijn:
- voorzien van datums en gelden voor de hele school
- niet bedoeld om weken, modules of specifieke details over het onderwijs binnen een cursus te beschrijven

Voorbeeldstructuur:
- Studiejaar 2025-2026 (sep 2025 → jun 2026, voor de hele instelling)
  - Semester 1 (sep 2025 → jan 2026)
    - Blok 1 (sep → okt 2025)
    - Blok 2 (nov → jan 2026)
  - Semester 2 (feb 2026 → jun 2026)
    - `Block 3 (Feb → Mar 2026)`
    - Blok 4 (apr → jun 2026)

**Belangrijke regel:** Academische periodes gelden voor de hele instelling en hebben datums. Ze vormen de officiële, gepubliceerde schoolkalender.

De **curriculumstructuur van een cursus** hoort in Curriculum Composer V2. Deze periodes beschrijven alleen de structuur van de cursusblauwdruk: de volgorde en nesting van lesblokken of weken. Ze hebben geen echte datums en gelden niet op instellingsniveau.

Door deze scheiding geldt:
- **Academische periodes** = officiële datums van de schoolkalender
- **Periodes in Curriculum Composer** = structuur van de cursusblauwdruk, zonder datums

## Tabblad Period Templates

Naast Academische periodes is er een tabblad **Period Templates**.

### Wat je met templates kunt doen

- Eenmalig herbruikbare periodestructuren maken en opslaan als benoemde templates.
- De geneste periomeboomstructuur in een template vastleggen.
- Templates bewerken met bedieningselementen om te slepen, in te springen en namen te wijzigen.
- Opgeslagen templates opnieuw gebruiken in cursussen en curriculumwerkwijzen.
- Een template op een cursus toepassen om de periodestructuur van die cursus direct in te vullen.
- Toegepaste templates zijn losse kopieën: latere wijzigingen in de template worden niet gesynchroniseerd met een cursus waarop deze al is toegepast.

### Wanneer gebruik je templates?

- Wanneer meerdere cursussen dezelfde periodestructuur gebruiken.
- Om nieuwe cursussen snel met standaardsemester- en blokindelingen in te richten.
- Om de structuur binnen programma's consistent te houden.

### Hoe templates werken

- Bij het toepassen van een template blijven bestaande periodes in de cursus behouden.
- De modus Volledig vervangen is beschikbaar, maar wordt geblokkeerd als er al modules zijn toegewezen aan actieve periodes in de cursus.
- Is de boomstructuur van periodes in een cursus na het toepassen aangepast? Bewerk deze dan rechtstreeks in Curriculum Composer V2 in plaats van de template opnieuw te synchroniseren.

## Hiërarchie van periodes

Het model voor academische periodes ondersteunt onbeperkte nesting. Je kunt elke periode omzetten in een container door subperiodes toe te voegen. Containers kunnen ook rechtstreeks modules bevatten.

Voorbeeld:
- Semester 1 (bovenliggende periode)
  - Periode 1 (onderdeel van Semester 1) — kan worden gekoppeld aan Module "Basics"
    - Unit 1 (onderdeel van Periode 1) — kan worden gekoppeld aan Module "Basics Week 1"

## Werkwijze voor beheerders

1. Open `/admin/periods`.
2. Voeg academische periodes toe voor het huidige semester of studiejaar.
3. Pas zo nodig de begin- en einddatums aan.
4. Archiveer oude periodes wanneer deze niet meer relevant zijn.

## Opmerkingen

- Periodes geven klassen, cursusonderdelen en rapportages over voortgang een tijdsdimensie.
- Ze worden vaak gebruikt om opdrachten en de evaluatie van cohorten af te bakenen.


**Laatst bijgewerkt:** 2026-07-08
