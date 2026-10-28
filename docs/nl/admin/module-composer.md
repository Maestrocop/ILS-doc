# Module Composer

Module Composer is een werkruimte voor het samenstellen en bewerken van afzonderlijke modules.

## Wat je kunt doen

Ga in het beheermenu naar **Module Composer** om:

- module-inhoud aan te maken en te bewerken
- leeruitkomsten en onderwijsmethoden voor een module te selecteren
- modulegegevens en roosterinstellingen te bekijken
- vergrendelingen en vereiste voorkennis voor onderdelen in te stellen
- wijzigingen aan de module op te slaan

## Werkwijze

1. Open Module Composer.
2. Maak een module aan of open een bestaande module.
3. Voeg modulebeschrijvingen, leeruitkomsten en instructies toe.
4. Stel zo nodig vergrendelingen en vereiste voorkennis voor onderdelen in.
5. Sla de gewijzigde module op.

## Verschil met andere editors

- Module Composer richt zich op curriculumontwerp op moduleniveau.
- De editor is anders dan de hoofdeditor voor cursussen.
- Module Composer vult Course Composer aan, dat de structuur op cursusniveau beheert.

## Onderdelen vergrendelen en vereiste voorkennis

In Module Composer kun je afzonderlijke opdrachten en quizzen vergrendelen en vereiste voorkennis instellen. Zo bepaal je op basis van een gekozen voorwaarde wanneer het volgende onderdeel beschikbaar wordt voor studenten.

### Betekenis van de voorwaarden

- **Ingediend** — het volgende onderdeel wordt beschikbaar zodra de student op *Indienen* klikt. Gebruik dit als je alleen wilt dat de student de opdracht probeert voordat die verdergaat.
- **Beoordeeld** — de docent moet de inzending beoordelen voordat het volgende onderdeel beschikbaar wordt. Gebruik dit wanneer feedback van de docent nodig is voordat de student verdergaat.
- **Behaald (≥55%)** — werkt hetzelfde als *Beoordeeld*, maar de student moet minimaal 55% halen. Scoort de student lager? Dan moet die de opdracht opnieuw inleveren (als er pogingen over zijn) en alsnog behalen voordat het volgende onderdeel beschikbaar wordt. De drempel van 55% ligt momenteel vast.

### Wanneer wordt een onderdeel beschikbaar? (snel overzicht)

| Voorwaarde | Wanneer wordt het onderdeel beschikbaar? |
|-----------|-----------------| 
| Ingediend | De student klikt op Indienen |
| Beoordeeld | De docent beoordeelt de inzending |
| Behaald | De docent beoordeelt de inzending en de score is ≥ 55% |

### Gedrag van de interface en voorbeeld

Elke rij wordt als één regel weergegeven. De schakelaar voor vergrendelen en de keuzelijst voor vereiste voorkennis staan bij het onderdeel. Het eerste onderdeel in een reeks heeft geen vergrendelingspictogram. Voorbeeld:

[1]  [A]  Opdracht één        concept                   ⋮    ← geen vergrendeling (eerste onderdeel)  
[2]  [Q]  Quiz twee           gepubliceerd   🔓         ⋮    ← beschikbaar; klik om te vergrendelen  
[3]  [A]  Opdracht drie       concept       🔒 submitted ⋮    ← vergrendeld, met keuzelijst  

Klik op 🔓 om te vergrendelen en op 🔒 om te ontgrendelen. Is het onderdeel vergrendeld, dan kun je via de keuzelijst wisselen tussen `submitted`, `graded` en `passed`. Het volgende onderdeel wordt beschikbaar op basis van de gekozen voorwaarde.

### Hulp bij aanwijzen voor docenten

HTML-elementen `<option>` ondersteunen niet op elk platform op dezelfde manier tooltips bij aanwijzen. Module Composer toont daarom een korte uitleg via een dynamisch `title`-attribuut op het element `<select>` zelf. De tooltip toont de geselecteerde optie en wordt bijgewerkt wanneer de docent een andere optie kiest. Beweeg de muis over de keuzelijst om de korte uitleg over de geselecteerde vereiste voorkennis te zien.


**Laatst bijgewerkt:** 2026-07-08
