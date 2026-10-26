# Cijferlijst

Overzicht: beheer cijfers en uitsplitsingen van rubricscores, publiceer cijfers en exporteer cijferlijsten.

Stappen:
- Open `Course` → `Gradebook`.
- Pas cijfers rechtstreeks aan of download een CSV-bestand om meerdere cijfers tegelijk te wijzigen (`Data Exchange` → `Export` → `Gradebook Template`).
- Cijfers publiceren: selecteer `Publish` om cijfers zichtbaar te maken voor studenten.

Tips: gebruik filters om resultaten per module, opdracht of student te bekijken.

Laatst bijgewerkt: 2026-07-08

Voorbeeld van een CSV-sjabloon (zie `docs/admin/templates/gradebook_template_v1.csv`):

- Kolommen: `student_id`, `student_email`, `assignment_code`, `grade`, `comment`

Importeren om meerdere cijfers tegelijk te wijzigen:
- Exporteer de huidige cijferlijst via `Data Exchange` → `Export` → `Gradebook`.
- Bewerk het CSV-bestand en laat `student_id` en `assignment_code` ongewijzigd.
- Importeer het bestand opnieuw via `Data Exchange` → `Import` en kies `Gradebook Template`.

Beleid voor publiceren
- Concept- en gepubliceerde cijfers: alleen docenten kunnen cijfers zien die als concept zijn opgeslagen. Gebruik `Publish` om de cijfers zichtbaar te maken voor studenten.

Cijferaanpassingen en controles
- Elke wijziging van een cijfer wordt in een controlelogboek vastgelegd. Wil je een gepubliceerd cijfer aanpassen? Bewerk het dan en publiceer het opnieuw. Het controlelogboek registreert de gebruiker, het tijdstip en de vorige waarde.

Plaatsaanduidingen voor screenshots
- [screenshot: gradebook-inline-edit]
- [screenshot: gradebook-export]
