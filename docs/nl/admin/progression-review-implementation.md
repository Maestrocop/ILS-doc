# Voortgangsbeoordeling (BSA) — overzicht

Voortgangsbeoordelingen worden gebruikt om besluiten over de voortgang van studenten vast te leggen en te volgen. Het systeem ondersteunt meerdere beoordelingstypen en besluitprocessen.

## Wat je kunt doen

Met voortgangsbeoordelingen kun je:

- beoordelingstypen voor je instelling aanmaken en configureren
- ondersteuningsmaatregelen, waarschuwingen en formele besluiten vastleggen
- de status en resultaten van beoordelingen per student volgen
- coördinatorendashboards met voortgangsstatistieken genereren
- beleidsvereisten afdwingen voordat bindende besluiten worden genomen

## Onderdelen van een beoordeling

**Tijdlijn en bewijs** — registraties van ondersteuning en meldingen
- ontwikkelgesprekken
- waarschuwingen en formele meldingen
- vervolggesprekken
- besluitvormingsgesprekken
- bevestigingen van studenten
- doorverwijzingen naar counselors
- uitstel en bijzondere gevallen

**Verbeterplan en acties** — geplande activiteiten voor studenten
- geplande gesprekken
- inzendingen van opdrachten
- doelen voor scoreverbetering
- afspraken met counselors
- interne notities van coördinatoren

## Besluitfasen

Het beoordelingsproces verloopt doorgaans als volgt:

1. **Advies van de mentor** — de mentor adviseert over de uitkomst.
2. **Beoordeling door de commissie** — de commissie beoordeelt het bewijs.
3. **Definitief besluit** — er wordt een bindend besluit genomen.

## Beleidsafdwinging

Het systeem dwingt beleidsvereisten af voordat negatieve of bindende besluiten kunnen worden genomen, bijvoorbeeld:

- de waarschuwing moet zijn gegeven
- het ontwikkelgesprek moet hebben plaatsgevonden
- de student moet zijn geïnformeerd
- het besluitvormingsgesprek moet zijn vastgelegd
- het recht op uitstel moet zijn gecontroleerd

## Instellingen configureren

Elke instelling kan het volgende configureren:

- namen en beschrijvingen van beoordelingstypen
- besluitdrempels en -fasen
- vereist bewijs en besluitbeleid
- typen gebeurtenissen en acties
- UI-labels en beleidsdocumenten
- toepasselijke academische jaren
- `ILS-dev/backend/scripts/backfill_outcome_snapshots.cjs`
- `ILS-dev/frontend/src/pages/ProgressionReviewsPage.jsx`
- `ILS-dev/frontend/src/pages/MyBSAReviewPage.jsx`
- `ILS-dev/frontend/src/pages/BSACoordinatorDashboard.jsx`
- `ILS-dev/frontend/src/components/ProgressionReviewDefinitionsTab.jsx`

## Validatie en opmerkingen
- Dit document beschrijft uitsluitend bestaande code en artefacten. Alle bewerkbare documentatie wordt onder `ILS-doc/docs/` bijgehouden.
