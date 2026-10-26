# Centrum voor gegevensuitwisseling

Centraal onderdeel voor exporteren, importeren en sjablonen. Docenten en beheerders gebruiken dit om CSV-gegevens van en naar het systeem over te zetten.

De stappen in ImportShell zijn: Upload → Map → Validate → Preview → Confirm. Voorbeeldsjablonen staan in `docs/admin/templates/`.

Laatst bijgewerkt: 2026-07-08

Exporteren: stapsgewijs
1) Ga naar `Data Exchange` → `Export`.
2) Kies een entiteit (Students, Grades, Outcomes).
3) Selecteer een sjabloon en datumbereik en klik op `Export`.

Importeren: stapsgewijs (beheerder)
1) `Data Exchange` → `Import` → kies een sjabloon.
2) Volg de stappen in ImportShell. Imports door beheerders ondersteunen opnieuw afspelen en meldingen via webhooks.

Validatieregels
- Verplichte velden moeten zijn ingevuld; ID's moeten overeenkomen met bestaande databasegegevens; numerieke velden moeten binnen het verwachte bereik vallen.

Plaatsaanduidingen voor screenshots
- [screenshot: data-exchange-export]
- [screenshot: data-exchange-import]
