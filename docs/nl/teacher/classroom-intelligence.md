# Classroom Intelligence

Classroom Intelligence is het interpretatierapport dat volgt op de Heatmap.
Het is geïmplementeerd in `ILS-dev/frontend/src/pages/ClassroomIntelligencePage.jsx` en beschikbaar op `/admin/classroom-intelligence`.

[Schermafbeelding van Classroom Intelligence: overzicht van de cohortstatus met patroondetectie en interventies]

## Wat Classroom Intelligence doet

De pagina zet de matrix met beheersingsscores van de klas om in een overzicht voor docenten.
Je ziet hierin:

- hoeveel studenten voldoende beoordeeld bewijs hebben
- hoeveel studenten onder de streefdrempel zitten
- of de klas klaar is voor aanbevelingen op cohortniveau
- of de klas technische of gepolariseerde prestatiepatronen vertoont

## Bronnen in de backend en gebruikersinterface

Classroom Intelligence gebruikt:
- `GET /grading/classes` — lijst met klassen
- `GET /modules` — lijst met modules voor de geselecteerde cursus
- `GET /classes/:classId` — gegevens over de klas
- `GET /campuses/:campusId/reporting-rules` — drempelwaarden van de campus
- `GET /heatmap/classes/:classId?moduleId=...` — de belangrijkste gegevens voor de klas

## Bedieningselementen op de pagina

- **Klas selecteren** — kies de klas die je wilt analyseren.
- **Module selecteren** — filter het rapport, indien beschikbaar, op een specifieke module.
- **Besluiten toelichten** — schakel deze optie in om het bewijs achter aanbevelingen te bekijken.

## Belangrijke onderdelen van het rapport

### Onderdeel 0 — Overzicht leeruitkomsten (aandacht voor zwakke onderdelen)

Wanneer er scores voor leeruitkomsten zijn, toont Classroom Intelligence nu een overzichtstabel met leeruitkomsten vóór Cohort Health.
De tabel staat in volgorde van slechtste naar beste resultaat (eerst het hoogste percentage studenten onder de drempel), zodat je snel zwakke onderdelen kunt herkennen.

Dit onderdeel bevat:

- code en naam van de leeruitkomst
- klasgemiddelde per leeruitkomst
- percentage studenten onder de drempel
- een statuslabel (`Critical`, `Attention`, `Watch`, `On track`)

Bij urgente situaties worden waarschuwingskaarten getoond voor de leeruitkomsten met de meeste studenten onder de drempel.

### Onderdeel 1 — Cohort Health

Dit onderdeel toont:

- het totale aantal studenten
- het aantal beoordeelde studenten
- het aantal studenten onder de succesdrempel
- of opnieuw lesgeven wordt aanbevolen
- een betrouwbaarheidsniveau op basis van het aandeel beoordeelde studenten

### Besluit om lesstof opnieuw te behandelen: Required (exacte betekenis)

`Re-teach decision: Required` betekent dat de klas de drempel uit het beleid van de campus voor het opnieuw behandelen van lesstof heeft overschreden. De docent moet de voortgang daarom pauzeren en de leeruitkomsten die zwak scoren opnieuw behandelen voordat de klas verdergaat.

Beslislogica in de praktijk:

- **succesdrempel:** minimale beheersingsscore (bijvoorbeeld `6.0`)
- **drempel voor opnieuw behandelen:** maximaal toegestaan aandeel studenten onder de doelscore (bijvoorbeeld `40%`)
- **werkelijk aandeel onder de drempel:** berekend op basis van alleen beoordeelde studenten

Formule:

Opnieuw behandelen als (aantal studenten onder de drempel / aantal beoordeelde studenten) * 100 >= drempel voor opnieuw behandelen

Algemeen voorbeeld:

- klas: `15` studenten in totaal
- beoordeelde studenten: `15` (iedereen is beoordeeld)
- onder de succesdrempel: `14`
- berekening: `(14/15)*100 = 93%` onder de drempel
- beleidsdrempel: `40%`
- resultaat: `93% >= 40%` → `Re-teach decision = Required`

Voorbeeld (WILISE1A — SM-BASIS):

- Cursus: `SM-BASIS - Service Management Basis`
- Succesdrempel: `6.0`
- Drempel voor opnieuw behandelen: `40%`
- Totaal aantal studenten: `15`
- Beoordeelde studenten: `4`
- Onder de drempel: `1`
- Berekend percentage onder de drempel: `(1/4)*100 = 25%`
- Resultaat: `25% < 40%` → `Re-teach decision = Not required`

Opmerkingen:

- Alleen **beoordeelde studenten** tellen mee in de noemer. Studenten die nog niet zijn beoordeeld, hebben geen invloed op het percentage onder de drempel.
- Het rapport toont ook overzichten per leeruitkomst (klasgemiddelden en percentages onder de drempel). Daarmee kun je bepalen welke leeruitkomsten je als eerste opnieuw behandelt, ook als de hele klas nog niet opnieuw les hoeft te krijgen.

Ernst van deze situatie interpreteren:

- dit is een signaal met hoge ernst, geen situatie die maar net aan de drempel voldoet
- kaarten voor zwakke onderdelen met zeer lage klasgemiddelden (bijvoorbeeld rond `1.0/10`) wijzen op grote leerachterstanden binnen het cohort

Aanbevolen vervolgstappen voor docenten:

1. Pauzeer de voortgang met nieuwe lesstof voor deze groep leeruitkomsten.
2. Controleer of alle beoordelingen compleet zijn (alle verwachte inzendingen beoordeeld, geen recente beoordelingen ontbreken).
3. Behandel eerst de leeruitkomsten die het laagst scoren (de bovenste rijen in het overzicht van leeruitkomsten).
4. Voer een korte formatieve herbeoordeling uit voor dezelfde leeruitkomsten.
5. Open na de herbeoordeling Classroom Intelligence en Heatmap opnieuw om te controleren of het aandeel onder de drempel onder de beleidsgrens is gedaald.

Mogelijke oorzaken om te controleren:

- de leerstof is vóór de beoordeling niet volledig behandeld
- studenten hebben het werk gemaakt, maar de beoogde leeruitkomsten niet begrepen
- beoordelingen of gegevens zijn niet compleet (minder waarschijnlijk als de meeste studenten al zijn beoordeeld)

Zie [Draaiboek besluit over lesstof opnieuw behandelen](reteach-decision-playbook.md) voor een operationele checklist met stappen.

### Onderdeel 2 — Patronen herkennen

De pagina zoekt naar patronen zoals:

- **Gepolariseerd cohort** — een groot verschil tussen studenten die sterker en zwakker presteren.
- **Cluster met technische zwakke punten** — technische leeruitkomsten blijven achter.
- **Actieve risicogroep** — studenten onder de drempel die nog werk inleveren.

Deze patronen helpen je de juiste aanpak te kiezen.

### Verschillen tussen leeruitkomsten (wat betekent dit?)

Verschillen tussen leeruitkomsten laten zien bij welke leeruitkomsten te veel studenten nog onder de streefdrempel van de klas zitten.
Zo zie je op welke punten het cohort de verwachte beheersing nog niet haalt.

Elke rij met een verschil tussen leeruitkomsten vertegenwoordigt één leeruitkomst en bevat doorgaans:

- het klasgemiddelde voor die leeruitkomst
- het percentage studenten onder de drempel
- het aantal studenten onder de drempel

Gebruik deze gegevens om te bepalen welke leerstof je opnieuw behandelt en welke interventies je plant.
Heeft een leeruitkomst zowel een laag klasgemiddelde als een hoog percentage studenten onder de drempel? Dan heeft dit leerpunt hoge prioriteit.

### Onderdeel 3 — Inzichten voor docenten

Het rapport kan observaties in tekstvorm geven, bijvoorbeeld:

- welke categorieën leeruitkomsten het sterkst of zwakst zijn
- of het cohort dicht bij de drempel zit
- of de klas onder druk staat doordat veel studenten net onder de drempel zitten

### Onderdeel 4 — Aanbevolen interventies

De pagina kan acties aanbevelen, zoals:

- gerichte workshops met voordoen en uitleg
- groepswerk waarbij studenten elkaar ondersteunen
- een formatieve herbeoordeling
- het huidige lestempo aanhouden wanneer er geen actief signaal is

Als Besluiten toelichten is ingeschakeld, toont het rapport ook de onderliggende bewijswaarden en uitkomsten van regels.

## Waarvoor je het rapport gebruikt

Gebruik Classroom Intelligence na de Heatmap.
Dit is de beste plek om op basis van patronen bij leeruitkomsten beslissingen over je onderwijs te nemen.

- Open het wanneer de Heatmap grote verschillen tussen leeruitkomsten laat zien.
- Open het wanneer de klas dicht bij een waarschuwing staat om de lesstof opnieuw te behandelen.
- Gebruik het om te controleren of een aanbevolen actie door voldoende bewijs wordt ondersteund.

## Samenhang met andere docentweergaven

- **Student Cockpit** toont welke acties direct nodig zijn voor individuele studenten.
- **Heatmap** toont de beheersing van leeruitkomsten in de klas.
- **Classroom Intelligence** interpreteert het klassignaal en doet aanbevelingen.
- **Grading** levert het bewijs voor het rapport.
- **Interventions** legt uit hoe je de aanbevelingen uitvoert.

## Richtlijnen voor de gebruikersinterface: samenvattingskaarten (compacte indeling en tooltips)

Aanbeveling: gebruik de compacte kaartindeling (Optie B), met korte labels op de kaarten en toelichtende tooltips bij bewijs en trends. Zo blijft het dashboard visueel consistent en kunnen docenten het bewijs snel bekijken.

- Regels voor kaarten:
	- Houd de inhoud kort (feiten op één regel). Voorbeeld: `Graded` → `8 / 12 outcomes`; `Avg Score` → `8.0 ↓ Declining`.
	- Toon bewijs en betrouwbaarheid via tooltips bij aanwijzen in plaats van met lange tekst op de kaart.
	- Voeg boven het overzicht van leeruitkomsten een korte regel met bewijs toe: `Scores based on 8 graded assignments`. Zo is de context zichtbaar zonder dat je er met de muis overheen hoeft te gaan.

- Voorbeelden van tooltips:
	- Tooltip bij Beoordeeld: "Scores zijn gebaseerd op 8 beoordeelde opdrachten · 4 leeruitkomsten zijn nog niet beoordeeld."
	- Tooltip bij Gemiddelde score: "1,0 punt lager dan bij de vorige beoordelingssnapshot." (Verduidelijk in de campusinstellingen wat "vorige" betekent.)

- Onderbouwing:
	- Kaarten met gelijke hoogte zijn makkelijker te scannen en uit te lijnen met kaarten als `Pending` en `Overdue`.
	- Tooltips geven extra informatie zonder het scherm druk te maken. De korte regel met bewijs boven de tabel met leeruitkomsten geeft daar de benodigde context.

Opmerking: dit zijn alleen richtlijnen voor documentatie. Wijzig geen code in `ILS-dev` vanuit de docs-repository.
