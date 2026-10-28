# Herinneringsregels en meldingsfilosofie

Doel: de aanbevolen documentatie-eerstaanpak voor herinneringen en escalaties binnen ILS beschrijven. Dit is een product- en UX-besluitdocument; er zijn geen codewijzigingen in opgenomen.

## Principes

- Dashboard als uitgangspunt: het docentendashboard is de primaire bron van informatie.
- E-mail is voor escalatie, niet voor routinemeldingen.
- Beperkt, zelden en respectvol: voorkom herhaalde aansporingen; geef de voorkeur aan één bruikbare herinnering.
- Taal waarin de student centraal staat: benoem de student en de context, niet de schuldige.

## Aanbevolen drempelwaarden (startconfiguratie)

### Nakijken
- 0–13 dagen: alleen dashboard (geen herinneringen)
- 14 dagen: melding in de app (eenmaal per onderdeel) — niet herhalen voor hetzelfde onderdeel
- 21 dagen: e-mail aan docent + markeer als geëscaleerd naar coördinator

### Aanwezigheid
- Eén gemiste sessie: alleen dashboard
- Meerdere gemiste sessies of een patroon (bijvoorbeeld meer dan 3 dagen of 3 opeenvolgende gemiste sessies): herinnering in de app
- Herhaald patroon nadat een herinnering is gestuurd: escaleer naar coördinator en overweeg e-mail

## Gedrag van herinneringen

- Eenmalig: één herinnering in de app per onderdeel op de ingestelde drempelwaarde.
- Escalatieteller: houd het aantal herinneringen per onderdeel bij om escalatieregels te ondersteunen (bijvoorbeeld één herinnering → escalatie naar de coördinator na X dagen).
- Handmatige trigger: laat beheerders de herinneringslogica handmatig uitvoeren voor tests (er is nog geen scheduler).

## Richtlijnen voor toon en inhoud

- Onderwerpregel (e-mail): "Een student wacht nog op feedback"
- Voorbeeld van de berichttekst:

  Hoi Peter,

  Lotte de Vries wacht al 27 dagen op feedback over "Praktijkopdracht — Onderzoekend Vermogen".

  Cijfer → [link]

  Bekijk het werk en geef feedback. Bedankt.

- Gebruik formuleringen waarin de student centraal staat; vermijd beschuldigende taal.

## Operationele opmerkingen

- Geef prioriteit aan een interventielogboek: herinneringen zonder opvolging zijn minder nuttig.
- Begin met een handmatig endpoint om toon en logica te valideren voordat geplande taken in productie worden ingeschakeld.

**Laatst bijgewerkt:** 2026-07-06
