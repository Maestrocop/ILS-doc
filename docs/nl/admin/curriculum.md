# Curriculum Composer

Curriculum Composer is een beheerpagina voor het samenstellen van curriculuminhoud op cursusniveau.
De pagina is geïmplementeerd in `ILS-dev/frontend/src/pages/CurriculumComposerPage.jsx` en staat op `/admin/curriculum`.
Een nieuwere versie van dezelfde werkwijze is beschikbaar op `/admin/curriculum-v2` voor de editor voor cursusblauwdrukken van de volgende generatie.

<!-- TODO: Voeg een reeks screenshots toe van het bewerken van de periodestructuur, de volgorde aanpassen door slepen en neerzetten en moduleslots plaatsen. -->

## Beheerinterface

- Oudere curriculumroute: `/admin/curriculum`
- Nieuwste curriculumroute: `/admin/curriculum-v2`
- Cursusgebonden curriculumroute: `/admin/curriculum/:courseId`

## Doel

Deze pagina is een werkruimte om curriculuminhoud samen te stellen en de cursusstructuur te bekijken.
De pagina is bedoeld voor beheerders die curriculuminhoud op cursusniveau beheren buiten de basiseditors voor cursussen en modules.

## Blauwdruk tegenover bevestiging voor een klas

Curriculum Composer is vooral bedoeld als hulpmiddel om een cursusblauwdruk te maken. Je legt erin vast wat er in een cursus moet worden onderwezen: de geplande modules, periodes en geneste lesstructuur.

Deze periodes zijn specifiek voor een cursus en bevatten bewust geen echte datums. Ze leggen de structuur van het curriculum vast, bijvoorbeeld drie blokken of weken in semester 1, maar niet de officiële academische kalender van de instelling.

Er is ook een werkwijze voor docenten op klasniveau. Zodra een cursusblauwdruk klaar is, kan een docent deze voor een specifieke klas bevestigen door echte docenten aan modules toe te wijzen en de modules vast te leggen in het klasplan. Dit is geen dubbel werk: op dit moment wordt de blauwdruk omgezet in een concreet lesplan voor de klas.

Bij het instellen van een klas zien docenten doorgaans een paneel met een blauwdruk. Daarin staan modules die door Curriculum Composer worden voorgesteld. Een handmatige keuzelijst met modules is een terugvaloptie voor oudere klassen zonder blauwdruk of wanneer een docent een extra module nodig heeft die niet in het cursusplan stond.

Bestaat er een complete blauwdruk? Dan is de verwachte werkwijze:

1. Gebruik `+ Add all` om de cursusblauwdruk aan de klas toe te voegen.
2. Wijs aan elke module een docent toe.
3. Controleer het klasplan en het rooster.

De handmatige keuzelijst met modules is alleen nodig als de blauwdruk ontbreekt, onvolledig is of bewust wordt uitgebreid.

## Werking van de pagina

Je kunt op de pagina:

- een cursus selecteren of een werkruimte voor een specifieke cursus openen
- curriculuminhoud in de context van een cursus bekijken
- tussen curriculumonderdelen van de cursus navigeren
- de indeling van semesters en periodes voor de cursus beheren

## Hiërarchie van periodes

De composer ondersteunt nu een recursieve boomstructuur voor academische periodes, met onbeperkte nesting.
Elke periode kan een container worden door subperiodes toe te voegen. Elke geneste laag krijgt automatisch een eigen visuele stijl.

- Containerperiodes worden op elk niveau weergegeven als `SemesterSection`.
- Periodes zonder subperiodes worden weergegeven als `PeriodSection`.
- Containers kunnen ook rechtstreeks moduleslots bevatten. Deze worden bovenaan het onderdeel getoond.

De frontend-hulpfuncties ondersteunen nu recursieve nesting:

- `flattenPeriodSlots(periods)` maakt op elk niveau recursief een platte lijst van slots.
- `slotsByPeriod` doorzoekt geneste periodestructuren recursief.
- `findSlotById` zoekt recursief een slot op basis van ID.
- `collapseAllPeriods` verzamelt recursief de ID's van alle ingeklapte periodes.
- `renamePeriod` werkt geneste periodes direct bij.

In de gebruikersinterface:

- `SemesterSection` kan worden ingeklapt en versleept.
- De stijl verandert per nestingsniveau (lichtere achtergronden en randen op diepere niveaus).
- Je kunt aan elke periode zonder subperiodes met `+ Add Sub-period` subperiodes toevoegen.
- Je kunt modules rechtstreeks naar een containerperiode slepen.

De werkwijze is:

1. Maak eerst een gewone periode aan (bijvoorbeeld `Semester 1`).
2. Gebruik in die periode `+ Add Sub-period` om deze bij de volgende keer laden om te zetten in een containerperiode.
3. Sleep geneste periodekaarten binnen hun bovenliggende periode naar de gewenste plek.
- Gebruik de bedieningselementen voor inspringen en uitspringen om de bovenliggende periode te wijzigen zonder de subperiodes te verliezen.
- Zet modules neer op een containerperiode of op kaarten van subperiodes.

In deze interface zijn containerperiodes groepskoppen. Geneste periodes zijn versleepbare kaarten die zelf weer subperiodes of directe modules kunnen bevatten.

### Periodetemplates

Het systeem ondersteunt herbruikbare periodetemplates waarmee je snel de periodestructuur van een cursus kunt invullen.

- Beheer templates via het tabblad `Period Templates` op `/admin/periods`.
- Elke template bevat een geneste periodestructuur met namen, relaties tussen bovenliggende en onderliggende periodes en de weergavevolgorde.
- Je kunt templates aanmaken, hernoemen, opnieuw ordenen, dupliceren en verwijderen in de template-editor.
- In stap 2 van Curriculum Composer V2 staat een keuzelijst `Apply template`. Hiermee kopieer je de template direct naar de academische periodes van de cursus.
- `Apply template` behoudt bestaande cursusperiodes en is daardoor geschikt om de structuur geleidelijk aan te passen.
- De implementatie ondersteunt ook de modus `Replace`, maar alleen als er geen actieve cursusperiodes zijn waaraan modules zijn toegewezen. Bij gebruik van Replace worden de huidige cursusperiodes soft deleted voordat de template opnieuw wordt toegepast.
- Toegepaste templates zijn eenmalige kopieën. Wijzigingen aan een template worden niet automatisch overgenomen in cursusstructuren die al zijn aangepast.

Deze functie is bedoeld om structuren op programmaniveau te hergebruiken:

- sla standaardstructuren voor jaren, semesters, kwartalen of blokken één keer op
- pas dezelfde structuur toe op meerdere cursussen
- pas de structuur per cursus aan zonder de hele boom opnieuw op te bouwen

De templatewerkwijze is vooral handig voor meerjarige programma's en cursussen met hetzelfde academische ritme, maar met verschillende moduletoewijzingen.

## Backendcontract

De pagina gebruikt waarschijnlijk API's voor cursussen en curriculum, zoals:

- `GET /api/courses`
- `GET /api/courses/:id`
- `GET /api/curriculum/:courseId`

## Werkwijze voor beheerders

1. Open `/admin/curriculum`.
2. Selecteer een cursus om de curriculuminhoud te bekijken of bewerken.
3. Gebruik indien beschikbaar de cursusgebonden route om de werkruimte voor een specifieke cursus te openen.

## Opmerkingen

- Deze route staat in de huidige configuratie van live beheerroutes.
- De route staat los van de basiseditors voor cursussen en modules en is bedoeld om curriculum op cursusniveau samen te stellen.


**Laatst bijgewerkt:** 2026-07-08
