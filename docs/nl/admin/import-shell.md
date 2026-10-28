# ImportShell — gedeelde werkwijze voor importeren

Doel: de gebruikerservaring voor imports van verschillende soorten gegevens standaardiseren, zodat elke importer zich kan richten op het schema en de validatie.

Stappen (aanbevolen):
- Uploaden
- Kolommen koppelen (optioneel)
- Valideren
- Voorbeeld bekijken
- Bevestigen
- Rapport

Verantwoordelijkheden van de importer:
- toegestane bestandstypen en verplichte kolommen definiëren
- validatieregels en foutmeldingen leveren
- bepalen hoe gegevens worden opgeslagen of samengevoegd

Verantwoordelijkheden van de shell:
- interface voor bestandsupload en voortgang
- interface voor het koppelen van kolommen (tijdens de stap Kolommen koppelen)
- validatie uitvoeren en een overzicht van fouten tonen
- voorbeeldweergave en acties per rij
- downloadbaar importrapport aanmaken

Gegevens voor het koppelen van kolommen
- Sta toe dat gebruikers koppelingen per bron opslaan (bijvoorbeeld Canvas of Moodle).
- Bied voorbeeldkoppelingen aan om de werkwijze eenvoudiger te maken.

Voorbeeld: importer voor leeruitkomsten
1. De beheerder uploadt `outcomes.csv`.
2. (Sla het koppelen van kolommen over bij een standaardbestand.) Valideer de rijen op verplichte velden.
3. Bekijk de eerste 50 rijen met waarschuwingen bij de rijen.
4. Bevestig de import. Toon het eindrapport en een downloadbaar CSV-bestand met statussen.

**Laatst bijgewerkt:** 2026-07-07
