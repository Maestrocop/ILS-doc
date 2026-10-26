# Studentdashboard (Mijn dashboard)

Je dashboard is je persoonlijke startpagina voor je leerproces. Je ziet hier in één oogopslag je voortgang, recente cijfers, aanwezigheid en voortgang per module.

## Wat je op het dashboard ziet

- **Gemiddelde score** — je gemiddelde beheersing op basis van leeruitkomsten (schaal 0–10), niet het gewone gemiddelde van je opdrachtscores. De score laat zien hoeveel leeruitkomsten je daadwerkelijk beheerst. Je opdrachtscores kunnen hiervan afwijken als je een leeruitkomst meerdere keren goed moet aantonen voordat deze als beheerst telt.
- **Snelle statistieken** — hoeveel opdrachten je hebt ingeleverd, hoeveel er nog openstaan en hoeveel er zijn beoordeeld
- **Volgende acties** — opdrachten die binnenkort ingeleverd moeten worden of waarvan de deadline is verstreken, gerangschikt op urgentie en met een directe link naar de opdracht
- **Aanwezigheid** — een overzicht van aanwezig, afwezig, te laat en met geldige reden afwezig, met een waarschuwing als je aanwezigheid onder de 80% komt
- **Modules** — hoeveel van je ingeschreven modules zijn afgerond, bezig zijn of nog niet zijn gestart, plus een voortgangsbalk voor het afronden van modules (zie "Voortgang per module" hieronder)
- **Recente cijfers** — je meest recent beoordeelde inzendingen, met cijfers en links naar feedback
- **Resultaten per leeruitkomst** — je niveau per leeruitkomst (Sterk / In ontwikkeling / Risico), als dagelijks of wekelijks overzicht van je beheersing van competenties
- **Aftellen tot examen** — staat er binnenkort een examen voor je klas gepland? Dan zie je bovenaan een kaart die live aftelt in dagen, uren, minuten en seconden. Deze verschijnt pas nadat een docent een examendatum voor je klas heeft ingepland. Is er nog geen examen ingepland, dan zie je de kaart niet.

## Voortgang per module

Elke module krijgt een status op basis van wat je hebt ingeleverd, niet op basis van of je de module hebt geopend:

- **Niet gestart** — je hebt in deze module nog geen opdrachten ingeleverd of laten beoordelen. Alleen een module openen of een concept starten verandert deze status niet; daarvoor moet je iets inleveren.
- **Bezig** — je hebt minimaal één opdracht ingeleverd, die al beoordeeld kan zijn of nog op beoordeling wacht, maar nog niet alle opdrachten in de module zijn beoordeeld.
- **Afgerond** — alle opdrachten in de module zijn beoordeeld.

Je voortgang wordt getoond als het aantal afgeronde modules, bijvoorbeeld "10/13 modules behaald, 77%". Dit is geen schatting van studiepunten.

### Opgelost op 2026-09-19: de EC-schatting paste niet bij het MBO

Eerder stond hier `~X / 45 EC estimated`. **EC (European Credits / ECTS)** is terminologie voor het hoger onderwijs (hbo en universiteit) uit het Europese studiepuntensysteem van Bologna. Het MBO gebruikt geen EC. Het is opgebouwd rond kwalificatiedossiers, kerntaken en werkprocessen, met studiebelasting in uren (SBU) in plaats van studiepunten. De widget en de achterliggende constante `BSA_NORM_EC` waren bedoeld voor het hoger onderwijs. "BSA" staat voor Bindend Studieadvies, een regeling uit het hbo en wo. De widget is nooit aangepast toen hetzelfde dashboard ook voor MBO-studenten van TCR werd gebruikt. Zie #386.

De gekozen oplossing ("Optie 3a") is opgeleverd: de verwijzing naar EC is verwijderd en de widget toont nu alleen het percentage afgeronde modules. Hiervoor waren geen nieuwe gegevens nodig. Tijdens deze wijziging is ook een fout opgelost waardoor resultaten te laag werden geteld. De aantallen Sterk / In ontwikkeling / Risico in Resultaten per leeruitkomst werden ongemerkt beperkt tot 10 door een backendlimiet `LIMIT 10` die bedoeld was voor een ander doel: de tien zwakste resultaten controleren. Daardoor werden werkelijk beheerste leeruitkomsten niet meegeteld als je onderbouwing had voor meer dan 10 leeruitkomsten.

### Opgeleverd: voortgang per kerntaak

De geplande voortgang per kerntaak is nu beschikbaar in de widget **Kerntaken Progress**. De leeruitkomsten worden gegroepeerd per kerntaak, bijvoorbeeld "Beheert de infrastructuur". Een kerntaak telt pas als beheerst wanneer *alle* bijbehorende leeruitkomsten de beheersingsdrempel halen, niet alleen de leeruitkomsten waarvoor je al een cijfer hebt. De bijbehorende widget **Exam / PvB readiness** gebruikt dezelfde groepering, maar kijkt naar het niveau van werkprocessen.

Let op: beide widgets tellen alleen leeruitkomsten mee waarvoor je minimaal één beoordeeld snapshot hebt. Staat de voortgang van een kerntaak op 0 terwijl je wel opdrachten hebt gemaakt die ermee te maken hebben? Controleer dan of de rubriccriteria van die opdrachten zijn gekoppeld aan leeruitkomsten onder die kerntaak. Meestal ontbreekt die koppeling, niet het werk.

## Je dashboard gebruiken

1. **Bekijk je Gemiddelde score** — krijg snel inzicht in je totale prestaties.
2. **Bekijk Recente cijfers** — klik op een cijfer om de volledige feedback en opdrachtgegevens te bekijken.
3. **Bekijk Resultaten per leeruitkomst** — ontdek welke leeruitkomsten je goed en minder goed beheerst.
4. **Plan je volgende stappen** — gebruik leeruitkomsten met een lage score om te bepalen wat je opnieuw gaat oefenen.

## Resultaten per leeruitkomst gebruiken

Zie je een leeruitkomst met een lage score?
- Klik erop om te zien welke opdrachten aan die score hebben bijgedragen.
- Bekijk de feedback bij die leeruitkomst.
- Bespreek met je docent of begeleider hoe je je resultaat kunt verbeteren.

## Korte werkwijze

1. Open na het inloggen **Mijn dashboard**.
2. Bekijk je statistieken en let op onderdelen die aandacht nodig hebben.
3. Heb je werk dat nog openstaat? Bekijk dan de opdrachtpagina voor meer informatie.
4. Is een opdracht beoordeeld? Bekijk dan meteen de feedback.
5. Gebruik de trends per leeruitkomst om te bepalen wat je opnieuw gaat oefenen.


**Laatst bijgewerkt:** 2026-10-03
