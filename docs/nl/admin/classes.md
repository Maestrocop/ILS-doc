# Klassen

Klassen zijn onderwijssecties waarin studenten voor een cursus worden ingedeeld. Gebruik de pagina Klassen om groepen te beheren, studenten in te schrijven en je lesgroepen te organiseren.

## Wat je kunt doen

Ga in het beheermenu naar **Klassen** om:

- alle klassen te bekijken
- een klas voor een cursus of module aan te maken
- klasgegevens te bewerken (naam, rooster en toewijzing van docenten)
- studenten afzonderlijk of in één keer via CSV in te schrijven
- klassen te verwijderen die niet meer nodig zijn

## Gegevens van een klas

Bij het aanmaken of bewerken van een klas stel je het volgende in:

- **Klasnaam** — de naam van de groep die studenten zien
- **Cursus of module** — het onderdeel dat deze klas volgt
- **Rooster** — dagen en tijden (optioneel)
- **Toewijzing van docenten** — wie lesgeeft aan deze klas

## Studenten inschrijven

**Student afzonderlijk inschrijven:**
1. Open een klas.
2. Klik op "Student toevoegen".
3. Selecteer de student uit de lijst.

**Studenten in één keer via CSV inschrijven:**
1. Open een klas.
2. Klik op "Importeren vanuit CSV".
3. Upload het bestand met de studentenlijst.
4. Bekijk het voorbeeld (hierin staat welke studenten worden aangemaakt of ingeschreven).
5. Bevestig om het inschrijven af te ronden.

Het systeem:
- maakt nieuwe studentenaccounts aan als deze nog niet bestaan
- slaat studenten over die al bij deze klas zijn ingeschreven
- toont na het importeren een overzicht (aangemaakt, ingeschreven, overgeslagen)

## Werkwijze voor beheerders

1. Ga naar `/admin/classes`.
2. Controleer actieve klassen en de koppeling met cursussen en modules.
3. Maak klasgegevens aan of werk ze zo nodig bij.
4. Verwijder klassen die niet meer nodig zijn.

## Opmerkingen

- Klassen zijn een centrale beheerentiteit die cursussen, docenten en studenten met elkaar verbindt.
- Klassen bepalen voor welke studenten opdrachten worden getoond en hoe voortgang wordt bijgehouden.

## Recente wijzigingen (juni 2026)

- Bij inschrijven in bulk via CSV kunnen nu nieuwe studentenaccounts tijdens het importeren worden aangemaakt. Ook zijn waarschuwingen per rij duidelijker voor studenten die al in een overlappende klas zijn ingeschreven. Staat een student in twee klassen voor dezelfde module? Dan waarschuwt de interface voordat je de import bevestigt.
- Er is een optie toegevoegd om met één klik een heel cohort bij een klas in te schrijven.


**Laatst bijgewerkt:** 2026-07-08
