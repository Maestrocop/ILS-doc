# Effectiviteit van het curriculum (CE01 / CE02 / CE03)

Deze pagina beschrijft de bestaande rapporten over curriculumeffectiviteit en de verschillende vragen die ze beantwoorden. Het is een feitelijke, alleen-lezen beschrijving van de drie rapporten: CE01, CE02 en CE03. Er worden geen wijzigingen aangebracht in `ILS-dev`.

## Doelgroep
Deze pagina is bedoeld voor:
- curriculumontwerpers
- programmamanagers
- onderwijsmanagers
- coördinatoren (in de curriculumweergave)

Niet bedoeld voor: docenten, mentoren/SLB'ers en studenten. Deze gebruikers hebben Cockpit, Heatmap, Student Success en BSA-dashboards.

---

## CE01 — slagingspercentages per module
Vraag: "Bij welke modules is het slagingspercentage laag?"

Wat er beschikbaar is:
- Een tabel per module met de modulenaam, het programma, het aantal ingeschreven studenten, het slagingspercentage en eenvoudige categorieën: geslaagd, risico of niet behaald. De standaard slagingsdrempel is 55%.
- Gebruik: curriculumteams bekijken modules met lage slagingspercentages om vragen over het curriculum te onderzoeken, zoals moeilijkheid, vereiste voorkennis, geldigheid van beoordelingen, lesmateriaal en invloed van de docent.

Voorbeeld (fragment):
- Marketing & Strategie — slagingspercentage 64.0%
- MOD - BIM Fundamentals & ISO 19650 — slagingspercentage 42.6%

CE01 is een alarmsignaal: het toont modules waarvoor studenten minder vaak slagen dan verwacht.

---

## CE02 — overzicht studenten die meerdere modules niet behalen (vervangt de eerdere weergave per student)
Vraag: "Hoe groot is het probleem van meerdere niet-behaalde modules binnen het cohort?"

Wat wordt getoond (de bestaande aanpak is hier in de documentatie beschreven):
- Een beknopt overzicht van het aantal studenten dat meerdere modules niet behaalt, bijvoorbeeld:
  - "9 studenten behalen momenteel 3 of meer modules niet."
  - "4 studenten behalen 5 of meer modules niet."
  - "2 studenten behalen 7 of meer modules niet."
- Een korte toelichting: dit totaalbeeld kan wijzen op te veel lesstof, ontbrekende vereiste voorkennis of leerproblemen in het hele cohort. Bekijk voor details per student het Student Success Dashboard.

Waarom deze weergave bestaat: deze is gericht op het curriculum en de gezondheid van het cohort, niet op individuele studenten. De weergave meet de omvang van het probleem zonder afzonderlijke studenten op te sommen.

---

## CE03 — analyse van faalketens
Vraag: "Welke modules komen het vaakst voor bij studenten die meerdere modules niet behalen?"

Wat er beschikbaar is of moet worden getoond:
- Een gerangschikte lijst of tabel met modules en hoe vaak ze voorkomen binnen de groep studenten die N of meer modules niet behaalt (de maatstaf "komt voor in gevallen"). Bijvoorbeeld:
  - Marketing & Strategie — komt voor in 8 van de 9 gevallen met meerdere niet-behaalde modules (88.9%)
  - BIM Fundamentals — komt voor in 7 van de 9 gevallen met meerdere niet-behaalde modules (77.8%)
  - Ondernemen — komt voor in 6 van de 9 gevallen (66.7%)
- Interpretatie: modules met hoge percentages zijn waarschijnlijk beginpunten in faalketens en daarom belangrijke aandachtspunten bij onderzoek naar het curriculum (vereiste voorkennis, volgorde en ontwerp van beoordelingen).

Waarom CE03 belangrijk is:
- CE01 vindt zwakke modules (signaleert symptomen).
- CE02 meet de impact (omvang van het probleem).
- CE03 helpt mogelijke oorzaken te vinden door modules aan te wijzen die vaak voorafgaan aan bredere problemen.

Voorbeelden van de meerwaarde:
- Twee modules met hetzelfde slagingspercentage kunnen een heel verschillend belang voor het curriculum hebben. Laat CE03 zien dat één module onevenredig vaak voorkomt bij studenten met meerdere niet-behaalde modules, dan is die module waarschijnlijk een knelpunt.
- Een module met een laag slagingspercentage maar een lage aanwezigheid in CE03 kan moeilijk zijn zonder het grotere systeem te beïnvloeden. Deze module is dan minder waarschijnlijk de oorzaak van het structurele probleem.

---

## Korte gebruiksinstructie
- Gebruik CE01 als alarmsignaal op moduleniveau.
- Vervang de eerdere studentenlijst in CE02 door de totalen uit het "Overzicht studenten die meerdere modules niet behalen".
- Gebruik CE03 als hulpmiddel voor curriculumleiders: met de "Analyse van faalketens" vind je mogelijke beginpunten voor onderzoek.
- Koppel CE02 en CE03 altijd aan het Student Success Dashboard voor opvolging per student, wanneer dat nodig is.

Dit document beschrijft de beoogde structuur van de rapporten en de bestaande signalen. Dit bestand wijzigt geen code of gegevens in `ILS-dev`.
