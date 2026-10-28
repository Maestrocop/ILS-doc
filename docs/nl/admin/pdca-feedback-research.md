# PDCA-cyclus en feedback — domein Feedback & Onderzoek (voorstel)

Deze pagina introduceert de PDCA-cyclus (Plan-Do-Check-Act) en een voorgesteld domein `Feedback & Research` voor ILS. Dit is uitsluitend een product- en documentatievoorstel — `ILS-dev` wordt niet aangepast.

## Waarom PDCA voor ILS?

PDCA (Plan → Do → Check → Act) biedt een eenvoudige, herhaalbare cyclus voor continue verbetering. Voor een onderwijsplatform sluit deze cyclus vanzelfsprekend aan op curriculumontwerp, lesgeven, feedback verzamelen en curriculumupdates.

Koppeling op hoofdlijnen:

- Plan: Curriculum Composer — ontwerp modules, blokken en leeruitkomsten
- Do: lesgeven — klassen, roosters en lesmomenten
- Check: Session Feedback + enquêtes — verzamel gegevens van studenten en docenten
- Act: curriculumupdates, wijzigingen in rubrics en interventies voor extra ondersteuning

---

## Voorgestelde productindeling

Verdeel feedback over twee verwante producten:

1) Session Feedback (hoge prioriteit)

- Trigger: een actie van een docent of het systeem voor een lesmoment in het rooster (bijvoorbeeld de docent klikt op `Request Feedback` op een lesmomentkaart).
- Vraag aan de student (voorbeeld):

  - Hoe duidelijk was de les van vandaag? (1–5)
  - Hoe betrokken voelde je je? (1–5)
  - Wat is nog onduidelijk? (open tekstveld)

- Gegevensstroom: lesmoment → feedback van studenten → analyses van onderwijskwaliteit → Intelligence Hub
- Gebruik: directe verbeteringen in het onderwijs, coaching van docenten en waarschuwingen bij kleine aantallen in Intelligence Hub

2) Enquêtes op instellingsniveau (lagere prioriteit / later)

- module-evaluatie, cursusevaluatie, welzijn, afgestudeerdenenquête en docenttevredenheid
- grotere steekproeven, geplande verspreiding, langere looptijd en analyse op onderzoeksniveau

---

## Domein Feedback & Research (aanbevolen map)

Maak een toekomstig domein `Feedback & Research` met daarin:

- Session Feedback (gebeurtenisgestuurd)
- module-evaluaties
- cursusevaluaties
- enquêtes op instellingsniveau
- vragenbank (herbruikbare vragen)
- enquêteanalyses en rapporten

Dit domein moet logisch gescheiden zijn van curriculum en roosters, maar daar wel mee integreren.

---

## PDCA in de praktijk (voorbeeldproces)

1. Plan: een ontwerper definieert module A en de verwachte leeruitkomsten in Curriculum Composer.
2. Do: een docent verzorgt lesmoment S voor module A (het lesmoment in het rooster wordt gegenereerd op basis van roosterregels).
3. Check: de docent vraagt feedback over het lesmoment aan; studenten reageren; analyses signaleren lage scores voor duidelijkheid of betrokkenheid.
4. Act: de ontwerper past module A aan (andere volgorde, rubrics), of de docent past het lesplan aan; de wijzigingen worden opnieuw uitgerold via Composer; de PDCA-cyclus begint opnieuw.

---

## Analyse en Intelligence

- Realtime-indicatoren (kleine aantallen): gemiddelden per lesmoment en waarschuwingen voor docenten wanneer een drempelwaarde wordt onderschreden
- Geaggregeerde meetwaarden: tevredenheidstrends per module en NPS-achtige scores per cursus
- Verdieping: filter op klas, onderwijsperiode, docent en demografische segmenten

---

## UX-suggesties (kort)

- Docentenproces: plaats in de weergave van een lesmoment een knop `Request Feedback` die voor studenten een lichtgewicht dialoogvenster opent om mobiel te reageren.
- Studentenproces: gebruik een link in het LMS of via sms/e-mail waarmee studenten met 1–3 tikken kunnen reageren; houd het kort om het responspercentage te verhogen.
- Rapportage: een dashboardkaart per lesmoment, een wekelijkse samenvatting voor coördinatoren en signalen in Intelligence Hub.

---

Als je wilt, voeg ik een eenvoudige UI-mock-up en een PDCA-poster van één pagina toe voor de onboardingdocumentatie. Ik wijzig `ILS-dev` niet — ik voeg alleen documentatie toe onder `ILS-doc`.


**Laatst bijgewerkt:** 2026-07-08
