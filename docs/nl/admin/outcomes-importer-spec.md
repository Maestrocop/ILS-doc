# Outcomes Importer — specificatie

Doel: het schema, de validatie, de voorbeeldweergave en de regels voor samenvoegen vastleggen voor het importeren van leeruitkomsten.

Toegestane bestandsformaten: CSV (UTF-8), XLSX (eerste werkblad)

Verplichte kolommen:
- `code` (string) — unieke korte code, verplicht
- `title` (string) — verplicht
- `description` (string) — optioneel
- `framework` (string) — optioneel (wordt gekoppeld aan een bestaande naam van een raamwerk)
- `level` (string) — optioneel (bijvoorbeeld "Introductory", "Advanced")

Validatieregels:
- `code` moet uniek zijn binnen het bestand en bij bestaande leeruitkomsten (behalve in de modus Samenvoegen).
- `title` mag niet leeg zijn.
- Is `framework` ingevuld? Dan moet de waarde overeenkomen met een bestaand raamwerk; anders wordt een waarschuwing getoond.

Gedrag van de voorbeeldweergave:
- Toon de eerste 100 rijen met statusbadges: `OK`, `Warning`, `Error`.
- Sta toe om `code` en `title` direct in de voorbeeldweergave te bewerken.
- Geef bij veelvoorkomende problemen suggesties voor automatisch herstellen (spaties verwijderen en hoofdlettergebruik normaliseren).

Regels voor samenvoegen:
- Modi: `Create only`, `Create or Update (by code)`, `Replace` (gevaarlijk)
- Standaard: `Create or Update` met veilige regels; de beschrijving en titel worden alleen overschreven als `--force` is ingesteld.

Voorbeeld van een CSV-kopregel:
```
code,title,description,framework,level
OUT001,Define variables,Students can define variables,Core,Introductory
```

Rapportage:
- Maak na de import een importrapport met statussen en meldingen per rij (zie `admin/import-report.md`).

Rechten: voor importeren is de rol `Admin` of `Designer` vereist, volgens `admin/permissions.md`.

**Laatst bijgewerkt:** 2026-07-07
