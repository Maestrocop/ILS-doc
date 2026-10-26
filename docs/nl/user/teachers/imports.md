# Gegevens importeren (docenten)

Gebruik `Data Exchange` → `Import` om CSV-bestanden met cijfers of leeruitkomsten te uploaden. Volg de stappen van ImportShell:
- Upload: kies een CSV-bestand en een sjabloon.
- Map: koppel de CSV-kolommen aan systeemvelden.
- Validate: los fouten per rij op.
- Preview: bekijk voorbeeldrijen.
- Confirm: voer de import uit en bekijk het rapport.

Laatst bijgewerkt: 2026-07-08

Sjablonen:
- Cijferlijstsjabloon: `docs/admin/templates/gradebook_template_v1.csv`
- Sjabloon voor leeruitkomsten: `docs/admin/templates/outcomes_template_v1.csv`

Tips voor validatie:
- Controleer of `student_id` of `student_email` overeenkomt met bestaande gebruikers.
- Scores moeten numeriek zijn en binnen de grenzen van de rubric vallen.

Gedetailleerde stappen voor ImportShell

1) Uploaden
- Klik op `Data Exchange` → `Import` → kies het sjabloon `Gradebook` of `Outcomes`.
- Selecteer het CSV-bestand en klik op `Upload`.

2) Kolommen koppelen
- Kies voor elke CSV-kolom het bijbehorende systeemveld. Verplichte velden: `student_id` of `student_email`, `assignment_code` en de kolom met de score of het cijfer.

3) Valideren
- Het systeem toont validatieresultaten per rij. Veelvoorkomende fouten:
	- `Unknown student_id`: de student bestaat niet — corrigeer `student_id` of gebruik `student_email`.
	- `Invalid score`: de waarde is niet numeriek of valt buiten het toegestane bereik.

4) Voorbeeld bekijken
- Bekijk een voorbeeld van de rijen die correct zijn verwerkt en eventuele gemarkeerde rijen.

5) Bevestigen
- Bevestig om de wijzigingen op te slaan. Je vindt het taakrapport onder `Data Exchange` → `Reports`.

Plaatsaanduidingen voor screenshots
- [screenshot: import-upload]
- [screenshot: import-map]
- [screenshot: import-validate]
