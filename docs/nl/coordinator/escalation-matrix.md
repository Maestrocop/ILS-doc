# Escalatiematrix

Doel: één escalatiematrix vastleggen die consistent wordt toegepast op signalen over nakijken, aanwezigheid en BSA.

## Algemene escalatieregels (aanbevolen)

Kolommen: Signaal | Fase | Voorwaarde | Actie | Zichtbaarheid

- Nakijken | Fase 1 | 14 dagen niet beoordeeld | Herinnering in de app aan docent (eenmalig) | Alleen docent
- Nakijken | Fase 2 | 21 dagen niet beoordeeld | E-mail aan docent; markeer als geëscaleerd naar coördinator | Coördinator + docent
- Aanwezigheid | Fase 1 | 3 dagen aanwezigheid niet geregistreerd | Herinnering in de app aan docent | Alleen docent
- Aanwezigheid | Fase 2 | Patroon van gemiste sessies | Herinnering in de app + signaal voor coördinator | Coördinator + docent
- BSA | Fase 1 | Risico vastgesteld | Begeleider geïnformeerd | Begeleider + coördinator

## Registratie

- `reminder_log` (documentatie): elke registratie bevat item_id, reminder_stage, sent_at, channel en actor.
- Escalatiemarkering: berekend veld `escalation_status`, zichtbaar op Status van het programma.

## Gebruiksnotities

- Begin met handmatige triggers en controleer het aantal onnodige meldingen voordat je dagelijkse geautomatiseerde taken in productie inschakelt.
- Houd de regels terughoudend om te voorkomen dat docenten te veel meldingen ontvangen.

**Laatst bijgewerkt:** 2026-07-06
