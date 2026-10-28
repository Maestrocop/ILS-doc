# Voortgangsbeoordeling — end-to-end-testgids

## Vereisten
Controleer voordat je begint of aan het volgende is voldaan:

- Er is minimaal één **Klas** met ingeschreven studenten.
- Er is minimaal één **Definitie van een voortgangsbeoordeling** ingesteld (Instellingen → Typen voortgangsbeoordeling). Bestaat er nog geen? Maak er dan een aan, bijvoorbeeld "BSA Review", type: BSA.
- Je bent aangemeld als **beheerder** of **coördinator**.

---

## Stap 1 — De pagina Voortgangsbeoordelingen openen
Ga naar **Beheer → Voortgangsbeoordelingen** (`/admin/progression-reviews`).

**Wat moet je controleren?**

- Bovenaan de pagina staan 5 KPI-kaarten: Totaal, In afwachting, Bezig, Besloten en **Achterstallig**.
- De kaart Achterstallig is grijs (0) totdat je een beoordeling met een verlopen deadline aanmaakt.

---

## Stap 2 — Een nieuwe beoordeling aanmaken
Klik rechtsboven op **+ Nieuwe beoordeling**.

Vul in het venster het volgende in:

Veld: wat selecteer je? Type beoordeling: de definitie die je hebt aangemaakt (bijvoorbeeld "BSA Review"). Klas: een klas met studenten. Student: een ingeschreven student. Deadline: **de datum van gisteren** — hiermee wordt de detectie van achterstallige beoordelingen geactiveerd.

Klik op **Beoordeling aanmaken**. Je wordt automatisch doorgestuurd naar de detailpagina van de beoordeling.

**Wat moet je controleren?**

- De beoordeling is aangemaakt en de detailpagina wordt geopend.
- De status is **In afwachting**.

---

## Stap 3 — De beoordeling uitvoeren
Op de detailpagina zie je panelen aan de rechterkant. Test elk paneel:

**a) Een notitie toevoegen**
Typ iets in het paneel Notities en sla op. Vernieuw de pagina en controleer of de notitie is bewaard.

**b) Een gebeurtenis vastleggen** (indien zichtbaar)
Selecteer een type gebeurtenis, voeg een notitie toe en sla op.

**c) Een aanbeveling instellen** (als de definitie een besluitbeleid heeft)
Werk eventuele vereiste controlelijst af voordat het besluit beschikbaar komt.

---

## Stap 4 — Een besluit vastleggen
In het **Beslispaneel**:

1. Stel **Status** in op `In Progress` en sla op. Controleer of de KPI-kaart op de overzichtspagina wordt bijgewerkt.
2. Stel **Besluit** in op `Continue` en sla op. Controleer of de besluitkaart groen wordt weergegeven.
3. Ga terug en wijzig het besluit in **`Exit`**.

Wanneer je Exit selecteert:

- Er moet een keuzelijst **Primaire reden** verschijnen (verplicht, gemarkeerd met een rood sterretje).
- Er moeten selectievakjes **Bijkomende factoren** verschijnen (optioneel).

Selecteer:

- Primaire reden: `Wrong Program Choice`
- Bijkomende factoren: selecteer `Academic Performance` en `Motivation`

Klik op **Besluit opslaan**.

**Wat moet je controleren?**

- Als je Exit kiest zonder een reden te selecteren, wordt opslaan geblokkeerd en verschijnt er een foutmelding.
- Na het opslaan toont de besluitkaart het label van het besluit, de primaire reden en de labels van de bijkomende factoren.
- De status op de overzichtspagina verandert in **Besloten**.

---

## Stap 5 — Detectie van achterstallige beoordelingen controleren
Ga terug naar de lijst met **Voortgangsbeoordelingen**.

**Wat moet je controleren?**

- De KPI-kaart **Achterstallig** toont **1** (rode achtergrond).
- Als je erop klikt, wordt de lijst gefilterd en zie je alleen de achterstallige beoordeling.
- De achterstallige rij heeft een rode achtergrondtint en een badge **Achterstallig** bij de deadline.
- In de filterbalk staat de filtertag "Alleen achterstallig", met een X om deze te wissen.

---

## Stap 6 — Controleren of de gegevens in de hub verschijnen
Ga naar **Intelligence Hub → tabblad Programs**.

**Wat moet je controleren?**

- De student voor wie je Exit hebt vastgelegd, staat nu in de tabel **Uitstroompercentage per programma**.
- Bij het programma van de student staat `total_exits: 1`.

---

## Wat je moet terugkoppelen
Geef bij elke stap aan:

1. Is het uitgevoerd zoals beschreven?
2. Zo niet, wat zag je dan?
3. Ontbreken er velden, werken knoppen niet of verschijnen er onverwachte fouten?

------------------------

## Opmerking over het afdwingen van beleid (waargenomen gedrag)

Probeer je een besluit Exit op te slaan en blokkeert het systeem dit? Dan legt de interface uit wat er ontbreekt. Voorbeeld van de controlelijst:

Vereiste | Status | Betekenis
Waarschuwing vastgelegd | ✓ Gereed — iemand heeft een waarschuwing geregistreerd
Interventie vastgelegd | ! Ontbreekt — er is nog geen interventie geregistreerd
Bevestiging student | ! Ontbreekt — de student heeft de waarschuwing nog niet bevestigd

Om het besluit Exit beschikbaar te maken, moet je beide acties vastleggen:

1. Ga naar het onderdeel **Acties** → voeg een actie van het type `Intervention` toe.
2. Ga naar het onderdeel **Controlelogboek** → leg een gebeurtenis van het type `Warning Acknowledged` vast.

Zijn beide acties vastgelegd? Ga dan terug naar het Beslispaneel, selecteer Exit en klik op Besluit opslaan. Dit hoort nu te werken.

Zo wordt het BSA-proces afgedwongen: een instelling kan een student niet formeel laten uitstromen zonder vastgelegd bewijs dat de student is gewaarschuwd en de waarschuwing heeft bevestigd.

---

## Geverifieerde resultaten (voorbeeld)

- De test is volledig geslaagd: definitief besluit Exit, besloten op 6-6-2026. Het besluit kon worden opgeslagen nadat aan alle vereisten was voldaan.

Opmerkingen tijdens de controle:

1. Het Beslispaneel blijft bewerkbaar nadat een besluit is opgeslagen. Het zou alleen-lezen moeten zijn of verborgen moeten worden zodra er een besluit is vastgelegd.
2. De bijkomende factoren op de besluitkaart worden gemengd weergegeven en moeten duidelijker worden gescheiden of gelabeld.

---

*Raak ILS-dev niet aan.*

---

## Slagingsstatus maar tekort op leeruitkomsten (opmerking)

Het zijpaneel van de Voortgangsbeoordeling zou waarschuwingen moeten tonen voor "Slagingsstatus maar tekort op leeruitkomsten" (wanneer een student gemiddeld voldoende staat, maar minstens één leeruitkomst onder de diagnostische drempel scoort). Voeg een directe actie toe waarmee je een plan voor extra ondersteuning bij de gemarkeerde leeruitkomst kunt vastleggen. Deze ingang in het zijpaneel ontbreekt nog in de implementatie en moet in een toekomstige update worden toegevoegd.


**Laatst bijgewerkt:** 2026-07-08
