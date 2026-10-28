# Outcomes Importer — README voor ontwikkelaars

Doel: notities over de implementatie en voorbeeldpatronen om de importtaak voor leeruitkomsten, rapportgeneratie en webhooks aan te sluiten.

Architectuuroverzicht
- De HTTP-API accepteert een upload en geeft een `job_id` terug.
- Een achtergrondworker verwerkt het bestand: parseren, valideren met `schemas/outcomes-import-schema.json`, een voorbeeldweergave maken en databasewijzigingen uitvoeren.
- De worker verstuurt voortgangsgebeurtenissen en het eindrapport. De taakstatus wordt opgeslagen in de tabel `imports_jobs` of in de metadatastore van de wachtrij.
- Na afloop kan optioneel een webhook of melding worden verstuurd.

Aanbevolen onderdelen
- Controller: verwerk de multipart-upload, sla het bestand op in objectopslag, plaats de taak in de wachtrij en geef `job_id` terug.
- Worker: haal een taak uit de wachtrij, parseer het bestand als stream, valideer elke rij, schrijf voorbeeldrijen naar de tabel `import_preview_rows` of een cache en voer wijzigingen per batch uit binnen een transactie.
- Rapportgenerator: maak het eindrapport als CSV of JSON, sla het op in objectopslag en bied het eindpunt `GET /report` aan.
- Eindpunt voor opnieuw uitvoeren: accepteer een lijst met rijen en plaats alleen mislukte rijen opnieuw in de wachtrij.

Voorbeeld van pseudocode voor een worker (vergelijkbaar met Node.js):

```
async function processJob(job) {
  const stream = openFileStream(job.filePath);
  const parser = csvParser(stream);
  let rowNum = 0;
  for await (const row of parser) {
    rowNum++;
    const valid = validateRow(row, outcomesSchema);
    if (!valid) {
      savePreviewRow(job.id, rowNum, 'Error', getErrors(valid));
      continue;
    }
    const result = await applyRowToDb(row, job.mode);
    savePreviewRow(job.id, rowNum, result.status, result.message);
    updateProgress(job.id, calculateProgress());
  }
  const report = await compileReport(job.id);
  saveReportToStore(job.id, report);
  notifyWebhook(job.webhookUrl, { job_id: job.id, status: 'finished', summary: report.summary });
}
```

Validatie en acceptatietests
- Gebruik `schemas/outcomes-import-schema.json` met een validator voor JSON Schema (Ajv voor Node, jsonschema voor Python).
- Voeg unittests toe met geldige CSV-rijen, waarschuwingen en fouten. Controleer daarin de statussen in de voorbeeldweergave en de aantallen in het eindrapport.

Transactiestrategie
- Schrijf gegevens in batches (bijvoorbeeld 100 rijen) binnen transacties om de gevolgen van een rollback te beperken.
- Gebruik in de modus `create_or_update` `UPSERT`-gedrag op basis van `code`.

Beveiliging en operationele opmerkingen
- Scan geüploade bestanden op virussen voordat je ze verwerkt.
- Stel configureerbare limieten in voor bestandsgrootte en aantal rijen.
- Leg een controlelogboek vast: wie het bestand heeft geüpload, tijdstip, job_id en uitgevoerde acties.
- Beperk het aantal gelijktijdige imports per organisatie.

Monitoring
- Verzamel statistieken: jobs_started, jobs_failed, rows_processed en avg_row_latency.
- Sla verwerkingslogboeken per taak op om problemen te onderzoeken.

Opnieuw proberen en idempotentie
- Zorg dat `applyRowToDb` idempotent is. Gebruik `code` als natuurlijke sleutel om duplicaten te herkennen.
- Het eindpunt voor opnieuw uitvoeren accepteert rijnummers en voert dezelfde validatie en verwerking uit.

Zie ook: `admin/outcomes-importer-api.md`, `admin/schemas/outcomes-import-schema.json`, `admin/outcomes-sample-responses.md`.

**Laatst bijgewerkt:** 2026-07-07
