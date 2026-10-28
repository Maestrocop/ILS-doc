# Herinneringsengine — specificatie voor handmatige trigger

Doel: een documentatie-eerstspecificatie opstellen voor de handmatige trigger voor herinneringen en het registratiemodel `reminder_log`. Dit is een product-/UI-specificatie; er worden geen codewijzigingen uitgevoerd.

## Overzicht

Begin met een handmatig admin-endpoint om de herinneringslogica voor tests en validatie uit te voeren. Het endpoint:

- voert alle ingestelde herinneringsregels uit (nakijken, aanwezigheid, BSA) op basis van de huidige gegevens
- maakt voor elke verzonden herinnering een registratie aan in `reminder_log`
- retourneert een samenvattende payload van de gegenereerde herinneringen (per docent / per onderdeel)

## Handmatig trigger-endpoint (documentatie)

- Methode: `GET`
- Pad: `/api/admin/jobs/run-reminders` (alleen documentatie)
- Rechten: alleen beheerders
- Gedrag: voert herinneringsregels één keer uit en retourneert een JSON-samenvatting. Er wordt geen scheduler gestart.

Voorbeeldrespons (alleen documentatie):

```json
{
  "run_at": "2026-07-07T10:00:00Z",
  "reminders": [
    {
      "teacher_id": "staff_123",
      "teacher_email": "peter@example.com",
      "items": [
        { "item_id": "sub_456", "type": "grading", "age_days": 27 }
      ]
    }
  ]
}
```

## `reminder_log` (documentatie)

Velden voor het registreren van herinneringen en het ondersteunen van escalatielogica.

- `id` (string)
- `item_id` (string) — id van het object waarover de herinnering is gestuurd (id van een inzending of aanwezigheidsregistratie)
- `item_type` (enum: `grading`, `attendance`, `bsa`)
- `recipient_id` (string) — gebruikers-id van degene die de herinnering ontving (docent / begeleider)
- `channel` (enum: `in_app`, `email`)
- `reminder_stage` (integer) — bijvoorbeeld 1 voor de eerste herinnering, 2 voor escalatie
- `sent_at` (timestamp)
- `status` (enum: `sent`, `failed`)
- `actor` (string) — systeem of beheerder die de trigger uitvoerde

## Te implementeren regels (documentatie)

- Nakijken: maak een herinnering in de app aan na 14 dagen; escaleer na 21 dagen via e-mail en naar de coördinator.
- Aanwezigheid: stuur een herinnering in de app bij patronen; escaleer volgens de escalatiematrix.
- BSA: volg de BSA-regels in `escalation-matrix.md`.

## Acceptatiecriteria (documentatie)

- De beheerder kan `/api/admin/jobs/run-reminders` uitvoeren en ontvangt een samenvatting van de herinneringen.
- `reminder_log` bevat één registratie per verzonden herinnering; registraties bevatten de fase en het kanaal.
- Een handmatige uitvoering plant geen herhaalde verzendingen in; elk onderdeel wordt beoordeeld op basis van de ouderdom en eerdere herinneringen.

## Testen en validatie (documentatie)

- Lever een testdataset voor QA aan (beschreven in de documentatie): voorbeeldinzendingen die gedurende verschillende aantallen dagen niet zijn beoordeeld.
- Documenteer de verwachte uitvoer voor de testdataset.

---

**Laatst bijgewerkt:** 2026-07-07
