# Outcomes Importer — API-contract

Doel: de HTTP-API definiëren voor serverintegratie van importtaken met de ImportShell-gebruikersinterface.

Basiseindpunt
- `POST /api/admin/imports/outcomes` — start een importtaak

Aanvraag (multipart/form-data)
- `file` — upload van een CSV- of XLSX-bestand (verplicht)
- `mapping` — JSON-object dat de geüploade kolommen aan doelvelden koppelt (optioneel)
- `mode` — een van `create_only`, `create_or_update`, `replace` (standaard: `create_or_update`)
- `notify` — boolean die aangeeft of er na afloop een asynchrone melding wordt verstuurd (standaard: false)

Antwoord (201 Created)
- Inhoud: `{ "job_id": "<uuid>", "status": "queued" }`

Status opvragen
- `GET /api/admin/imports/outcomes/{job_id}` — geeft de voortgang van de taak en een voorbeeldweergave terug
- Voorbeeldantwoord:
```
{
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "running", // queued | running | finished | failed
  "progress": 42, // percent
  "preview": [{ "row": 1, "status": "OK", "message": null }],
  "summary": { "total": 100, "ok": 88, "warnings": 8, "errors": 4 }
}
```

Rapport ophalen
- `GET /api/admin/imports/outcomes/{job_id}/report` — geeft een CSV- of JSON-rapport met statussen per rij terug

Mislukte rijen opnieuw uitvoeren
- `POST /api/admin/imports/outcomes/{job_id}/replay` met inhoud `{ rows: [1,5,7] }` om alleen mislukte rijen opnieuw te proberen.

Webhooks en meldingen
- Verstuur na afloop van een taak een minimale melding naar de geconfigureerde webhook: `{ job_id, status, summary }`.

Fouten
- Gebruik standaardreacties volgens problem+json met de velden `type`, `title`, `status` en `detail`.

Beveiliging
- Vereis de rol `Admin` of `Designer`, bescherming tegen CSRF en limieten voor bestandsgrootte; scan geüploade bestanden op virussen.

Snelheidslimieten en quota
- Stel configureerbare limieten in voor het aantal gelijktijdige importtaken per organisatie.

Zie ook: `admin/outcomes-importer-spec.md`, `admin/import-report.md`, `admin/import-shell.md`.

**Laatst bijgewerkt:** 2026-07-07
