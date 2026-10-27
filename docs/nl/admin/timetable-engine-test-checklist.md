# Timetable Engine — testchecklist (Ticket #163)

Deze checklist beschrijft handmatige teststappen voor Timetable Engine en de werkwijze voor bijeenkomsten. Gebruik de checklist om wijzigingen aan het rooster te controleren.

## 1. Een rooster aanmaken

- Klik op **+ Nieuw rooster**.
- Selecteer een klas.
- Selecteer een onderwijsperiode → de datums worden automatisch ingevuld op basis van de periode.
- Pas de datums zo nodig aan (geldig vanaf / geldig tot en met).
- Voeg een wekelijks tijdslot toe: kies een dag (bijvoorbeeld ma) en stel `09:00 → 11:00` in.
- Klik op **+ Tijdslot toevoegen** om een tweede tijdslot op een andere dag toe te voegen.
- Klik op **Rooster aanmaken** → het rooster verschijnt links in de lijst met de status `draft`.

## 2. Bijeenkomsten genereren

- Selecteer het rooster en klik op **⚡ Bijeenkomsten genereren**.
- Er verschijnt een melding "N bijeenkomsten gegenereerd". Controleer of N een logisch aantal is voor het datumbereik.
- De lijst met bijeenkomsten wordt gevuld. Elke bijeenkomst heeft de badge `scheduled` (hemelsblauw).

## 3. Een les markeren als gehouden (nieuw in deze commit)

- Beweeg de muis over een bijeenkomst met de status `scheduled` → rechts verschijnt de knop **Gehouden**.
- Klik erop → de statusbadge verandert direct in `held` (groen). Er verschijnt geen dialoogvenster; één klik is voldoende.

## 4. Een bijeenkomst handmatig bewerken

- Beweeg de muis over een bijeenkomst en klik op **Bewerken**.
- Wijzig de status in `cancelled` → er verschijnt een veld **Reden**.
- Vul een reden in (bijvoorbeeld "docent afwezig").
- Sla op → de bijeenkomst krijgt de status `cancelled`, wordt doorgestreept weergegeven en toont de reden.

## 5. Een inhaalbijeenkomst toevoegen (nieuw in deze commit)

- Klik op **+ Inhaalbijeenkomst** (oranje knop rechtsboven in het paneel met bijeenkomsten).
- Er verschijnt een oranje formulier. Vul een datum, `09:00`, `11:00` en eventueel opmerkingen in.
- Klik op **Inhaalbijeenkomst toevoegen** → de nieuwe bijeenkomst verschijnt met een oranje badge `makeup`.
- Open de filterlijst en selecteer "Inhaalbijeenkomst" → alleen die bijeenkomst wordt getoond.

## 6. Een bestaand tijdslot bewerken

- Klik in het onderdeel **Wekelijks patroon** op het potloodpictogram **✎** van een tijdslot.
- Wijzig de tijd direct, bijvoorbeeld `10:00 → 12:00`.
- Klik op ✓ → de melding *"Tijdslot bewerkt — klik op ↻ Bijeenkomsten opnieuw synchroniseren om de wijzigingen toe te passen"* verschijnt.
- Klik op **↻ Bijeenkomsten opnieuw synchroniseren** → de tijden van de bijeenkomsten worden bijgewerkt.

## 7. Na het aanmaken een tijdslot toevoegen

- Klik op **+ Tijdslot toevoegen** in de kop van Wekelijks patroon.
- Kies een nieuwe dag en tijd en klik op Toevoegen → het nieuwe tijdslot verschijnt.

## 8. Een rooster dupliceren

- Selecteer een rooster en klik op **Dupliceren**.
- Er verschijnt een dialoogvenster. Tijdsloten en datums zijn vooraf ingevuld; de klas is leeg.
- Selecteer een **andere** klas en klik op Rooster aanmaken → het tweede rooster verschijnt in de lijst.


---

Opmerkingen:
- Deze checklist is bedoeld voor het QA-team en release-engineers die wijzigingen aan het rooster controleren. De checklist gaat ervan uit dat de standaard rapportageregels van de campus en actieve onderwijsperiodes aanwezig zijn.
- Voor automatisering kun je deze stappen omzetten in Playwright-workflows met selectors van de roosterinterface.


**Laatst bijgewerkt:** 2026-07-08
