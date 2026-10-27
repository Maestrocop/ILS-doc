# De functie BSA-beoordeling voor andere instellingen gebruiken

De werkwijze voor BSA (Bindend Studieadvies) is ontwikkeld voor het Nederlandse mbo. De architectuur is generiek: BSA is een ingestelde variant van de review-engine. Dit document legt uit hoe andere instellingen dezelfde functie met andere instellingen kunnen gebruiken.

## Kernidee

BSA is geen vast ingebouwde werkwijze, maar een configuratie met een lokale naam, een instelling voor bindend advies, een tijdschema en beleidsregels. De review-engine voert de werkwijze uit; de definitie bepaalt het gedrag en de labels.

## Voorbeelden van configuraties
- Nederlands mbo
  - Lokale naam: "BSA"
  - Bindend: ja
  - Tijdschema: 9 maanden
  - Beleid: waarschuwing, interventie en bevestiging verplicht
- Britse universiteit
  - Lokale naam: "Beoordeling studievoortgang"
  - Bindend: nee
  - Tijdschema: einde van het studiejaar
  - Beleid: alleen gesprek
- Amerikaanse hogeschool
  - Lokale naam: "Studie op proef"
  - Bindend: ja
  - Tijdschema: per semester
  - Beleid: advies van de faculteit

Alle instellingen gebruiken dezelfde vier uitkomsttypen (doorgaan / doorgaan onder voorwaarden / overstappen / stoppen), maar de labels kunnen verschillen.

## Een nieuwe school aansluiten (praktische stappen)
1. Beheerder: ga naar Instellingen → Typen voortgangsbeoordeling → Maak een nieuw type aan.
   - Stel de lokale naam, bindendheid, timing en verplichte beleidsstappen in.
2. SLB'er / coördinator: blijf het SLB-dashboard en Student Cockpit gebruiken zoals gewoonlijk. Dezelfde werkwijze is van toepassing.
3. Optioneel: voeg waar nodig instellingsspecifieke labels toe aan de tekst in de gebruikersinterface.

## Opmerking over de implementatie (huidige beperking)
- Definities zijn nu algemeen en zichtbaar voor alle instellingen. De database heeft al een veld `institution_id`; de ontbrekende stap is een filter in de query, zodat typen per instelling worden afgeschermd.
- Kleine wijziging: voeg `WHERE institution_id = ?` toe aan de queries voor typen beoordelingen en toon alleen typen voor de huidige instelling. Dit is een kleine wijziging in de backend; voor de gebruikersinterface zijn geen andere wijzigingen nodig dan gefilterde lijsten.

**Instellingen → Typen voortgangsbeoordeling**

Op dit tabblad staat de BSA-definitie die je hebt aangemaakt. Elke beheerder kan hier een nieuw beoordelingstype voor de eigen instelling aanmaken, een lokale naam instellen, aangeven of het bindend is en de beleidsvereisten configureren.

Het enige ontbrekende onderdeel is het filter op `institution_id`, zodat elke school alleen de eigen definities ziet. Op dit moment zouden instellingen elkaars typen kunnen zien. Dit is een kleine aanpassing wanneer je dit nodig hebt.

## Aanbeveling
- Maak voor een directe start een nieuw beoordelingstype aan dat past bij het beleid van de instelling en gebruik de bestaande werkwijze.
- Plan voor een correcte werking met meerdere instellingen de kleine backendwijziging om definities vóór het aansluiten van meerdere instellingen op `institution_id` te filteren.

## Opmerkingen
- Wijzig `ILS-dev` niet tijdens deze documentatie-update. Dit document beschrijft het waargenomen gedrag en aanbevolen aanpassingen.


**Laatst bijgewerkt:** 2026-07-08
