# Perioden draaiboek — stapsgewijze uitleg

Praktische stapsgewijze uitleg voor beheerders: een periodetemplate op een cursus toepassen en modules aan een klas koppelen.

## Vereisten

- Je bent aangemeld als beheerder of coördinator.
- Je weet welke cursus en klas je gaat instellen.

## Stap A — Een periodetemplate op de cursus toepassen

1. Open Curriculum Composer voor je cursus.
2. Ga naar **Stap 2 — Periodes**.
3. Klik op **Template toepassen** en kies de gewenste structuur (bijvoorbeeld `Year-1 Periods N-4` voor een indeling met 4 blokken).
4. Klik naast de gekozen template op **+ Toevoegen** en bevestig.
5. Controleer of de nieuwe periodes in Composer staan.

## Stap B — Modules aan de cursus toevoegen

1. Ga in Composer naar **Stap 3 — Modules**.
2. Zoek in de bibliotheek of gebruik de modulekiezer om de benodigde modules toe te voegen.
3. Controleer of de volgorde en duur van modules aansluiten bij de periodeblokken.

## Stap C — Modules aan je klas koppelen

1. Ga naar **Stap 4 — Klassen**.
2. Selecteer je klas in de lijst.
3. Wijs de moduleset aan de klas toe en sla op.
4. Controleer de volledige configuratie.
5. Sla de instellingen van Composer op.

## Alternatief: snel toevoegen via Klas instellen

1. Ga naar **Klassen** en selecteer je klas.
2. Klik op het tabblad **Curriculum** op **+ Module handmatig toevoegen**.
3. Voeg modules één voor één toe.
4. Klik op **Opslaan**.

## Controlelijst

- De modules staan in het curriculumtabblad van de klas.
- De periodes van de cursus zijn zichtbaar in Composer.
- De volgorde van modules komt overeen met de geplande volgorde.

## Programma's van meerdere jaren (studiejaren)

Eén programma (bijvoorbeeld "ICT system engineer BBL") kan een doorlopend curriculum voor meerdere jaren bevatten (jaar 1, jaar 2 en jaar 3), in plaats van voor elk studiejaar een apart programma aan te maken. Dit is belangrijk omdat meerdere cohorten van hetzelfde programma tegelijk onderwijs volgen, bijvoorbeeld een klas in jaar 1 en een klas in jaar 2 tijdens hetzelfde schooljaar.

**Zo werkt het:**
- Elke module in de stap Modules van Composer heeft een veld **Studiejaar** (1, 2, 3, enzovoort). Dit bepaalt welk onderwijs wordt aangeboden. Als je een klas aan het programma koppelt met een bepaald studiejaar, krijgt deze alleen de modules van dat jaar toegewezen, ongeacht hoeveel jaar aan inhoud het programma bevat.
- Periodes zijn alleen bedoeld voor planning en weergave, niet voor het toewijzen van onderwijs. Gebruik bijvoorbeeld doorlopende periodenummers voor het hele programma (Periode 1–4 = jaar 1, Periode 5–8 = jaar 2, Periode 9–12 = jaar 3). De tabbladen in de stap Modules worden automatisch gegroepeerd op basis van deze nummering.
- Ook klassen hebben een veld Studiejaar. Dit wordt ingesteld wanneer je ze aan het programma koppelt en kan later worden aangepast. Het bepaalt welke modules de klas krijgt.

**Overgang naar een nieuw schooljaar:** maak nieuwe perioderijen met de echte datums van het nieuwe schooljaar aan. **Wijzig nooit de begin- of einddatum van een bestaande periode.** Zo blijven historische rapportages betrouwbaar, bijvoorbeeld wanneer je jaren later de resultaten van een student per periode vergelijkt. Als je datums van een bestaande periode hergebruikt of overschrijft, geeft deze niet meer betrouwbaar weer wat een eerder cohort heeft meegemaakt. Zie [ILS-dev#399](https://github.com/Maestrocop/ILS-dev/issues/399) voor de volledige onderbouwing en de nog openstaande vervolgstap: afzonderlijke inzendingen aan een periode koppelen voor rapportages per kwartaal. Dit is nog niet gebouwd; vergelijking per studiejaar via Studiejaar is al mogelijk.

**Laatst bijgewerkt:** 2026-09-20
