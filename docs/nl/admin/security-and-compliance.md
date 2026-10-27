# Beveiliging en naleving

Deze gids helpt de IT-beheerders van je instelling ILS voor te bereiden op implementatie en gebruik.

## Voordat je live gaat

### Essentiële eisen voor implementatie

**Omgeving instellen**
- [ ] Beveiligde hosting ingericht (datacenter in de EU als je ILS voor Europese scholen gebruikt)
- [ ] HTTPS ingesteld (geen HTTP)
- [ ] Database niet openbaar toegankelijk (firewallregels ingesteld)
- [ ] Beheerdersinterfaces (pgAdmin, SSH) alleen toegankelijk vanaf bekende IP-adressen
- [ ] Alleen aanmelden met SSH-sleutels ingesteld

**Geheimen beheren**
- [ ] Alle omgevingsvariabelen zijn ingesteld voor productie (nooit vanuit `.env`-bestanden)
- [ ] Databasewachtwoord aangemaakt (sterk, willekeurig en minimaal 32 tekens)
- [ ] E-mailwachtwoord ingesteld in een beveiligde opslag voor geheimen
- [ ] JWT-geheim aangemaakt (willekeurige tekenreeks van 256 bits, nooit hergebruiken)

**Database en back-ups**
- [ ] Databasemigraties uitgevoerd bij de eerste start
- [ ] Automatische back-ups ingepland (minimaal dagelijks)
- [ ] Back-ups buiten de server opgeslagen (niet op dezelfde machine als de applicatie)
- [ ] Back-ups versleuteld wanneer ze zijn opgeslagen
- [ ] Terugzetten getest op een andere server (essentieel!)
- [ ] Procedure voor terugzetten vastgelegd

**Bewaking en meldingen**
- [ ] Bewaking van beschikbaarheid ingesteld (bijvoorbeeld UptimeRobot)
- [ ] Foutregistratie ingeschakeld (bijvoorbeeld Sentry)
- [ ] Meldingen ingesteld voor schijfruimte
- [ ] Meldingen ingesteld voor de status van back-ups
- [ ] Bezorgstatus van e-mail bewaakt

**E-mailbezorging**
- [ ] DNS-records SPF, DKIM en DMARC ingesteld voor het verzenddomein
- [ ] Testmail succesvol verzonden en ontvangen
- [ ] Gecontroleerd of e-mails niet in de spammap terechtkomen

---

## Dashboard Systeemstatus (beheerpagina)

Controleer als beheerder na ingebruikname dagelijks de pagina **Systeemstatus**. Hier zie je:

### Operationele status
- percentage aanwezigheid dat vandaag is geregistreerd
- opdrachten die nog beoordeeld moeten worden (oudste eerst)
- studenten met risico (interventie nodig)
- docenten met achterstallige beoordelingen (meer dan 7 dagen)

### Systeemstatus
- status van de meldingenwachtrij
- tijdstip waarop de laatste back-up is afgerond
- status van de e-mailservice
- schijfruimtegebruik

### Beveiligingsstatus (afgelopen 24 uur)
- mislukte aanmeldpogingen
- vergrendelde accounts
- wachtwoordresets
- meldingen over verdachte activiteiten

**Actie:** is een indicator rood of oranje? Neem dan onmiddellijk contact op met je systeembeheerder.

---

## Gegevensbescherming en naleving van de AVG

### Jouw verantwoordelijkheden als verwerkingsverantwoordelijke

ILS is een **verwerker**. Je school is de **verwerkingsverantwoordelijke**. Je bent verantwoordelijk voor:

1. **Toestemming** — zorg dat studenten en medewerkers toestemming hebben gegeven om hun gegevens in ILS op te nemen.
2. **Privacybeleid** — publiceer hoe studentgegevens worden gebruikt, opgeslagen en beschermd.
3. **Bewaartermijn** — bepaal hoelang gegevens worden bewaard (gebruikelijk: 7 jaar na afstuderen).
4. **Rechten van betrokkenen** — zorg dat je verzoeken kunt afhandelen om studentgegevens te exporteren of verwijderen.
5. **Incidentrespons** — maak een plan voor het geval gegevens uitlekken of verloren gaan.

### Dataminimalisatie

ILS verzamelt:
- ✅ Naam, ID, e-mailadres en cohort van studenten (vereist voor de werking)
- ✅ Cijfers en aanwezigheid (essentiële onderwijsgegevens)
- ❓ Foto's van studenten (hiervoor is expliciete toestemming nodig)
- ❓ Aanwezigheidspatronen en analyses (hiervoor is toestemming nodig als je ze voor andere doelen dan beoordeling gebruikt)

**Zorg dat je expliciete toestemming hebt van studenten of hun ouders voordat je gedragsanalyses of optionele functies gebruikt.**

### Bewaartermijnen

**Aanbevolen bewaartermijnen:**
- Cijfers en aanwezigheid: 7 jaar na afstuderen
- Persoonsgegevens (namen, e-mailadressen): 7 jaar na afstuderen
- Tijdelijke bestanden (concepten, back-ups): 30 dagen

Neem contact op met je systeembeheerder om bewaarbeleid in te stellen.

### Gegevens exporteren (recht op overdraagbaarheid)

Studenten en medewerkers kunnen een volledige export van hun gegevens uit ILS aanvragen. De export bevat:
- cijfers
- aanwezigheidsgegevens
- inzendingen en feedback
- gebeurtenissen op de tijdlijn
- alle persoonsgegevens in het systeem

**Een export aanvragen:**
1. Ga naar **Instellingen** → **Gegevensexport**.
2. Klik op **Export aanvragen**.
3. Het systeem e-mailt je exportbestand binnen 24 uur.

### Gegevens verwijderen (recht op vergetelheid)

Studenten en medewerkers kunnen verzoeken om hun account en bijbehorende gegevens te verwijderen.

**Belangrijk:** sommige gegevens moeten mogelijk wettelijk worden bewaard (besluiten over BSA en eindcijfers). De administratie van je school beoordeelt verwijderverzoeken voordat ze worden uitgevoerd.

---

## Controlelogboeken en betrouwbaarheid van cijfers

Alle wijzigingen in studentgegevens worden vastgelegd:

- **Wijzigingen van cijfers** — wie het cijfer heeft gewijzigd, van welke waarde naar welke waarde, wanneer en waarom
- **Wijzigingen van aanwezigheid** — wie de aanwezigheid heeft geregistreerd en de wijzigingsgeschiedenis
- **Wijzigingen van rollen** — wie een rol heeft gewijzigd, voor wie, door wie en wanneer
- **Bestandstoegang** — wie welk bestand van een inzending heeft gedownload en wanneer

Deze logboeken zijn **onveranderbaar**: ze kunnen niet worden aangepast of verwijderd. Ze zijn bedoeld om:
- docenten te beschermen tegen beschuldigingen van manipulatie van cijfers
- scholen vertrouwen te geven in de betrouwbaarheid van beoordelingen
- audits en onderzoeken te ondersteunen

**Logboeken bekijken:** neem contact op met je systeembeheerder voor rapporten uit het controlelogboek.

---

## Back-ups en herstel na een storing

### Hersteldoelen

- **RPO (Recovery Point Objective):** maximaal 24 uur gegevensverlies
- **RTO (Recovery Time Objective):** maximaal 4 uur om de normale werking te herstellen

### Back-upplanning

- **Dagelijks:** volledige databaseback-up (01.00 uur)
- **Elk uur:** incrementele back-ups van transactielogboeken
- **Wekelijks:** hersteltest op een aparte server

### Procedure voor terugzetten

Als je database verloren gaat of beschadigd raakt:

1. **Stop de applicatie** (voorkom dat er verder gegevens worden weggeschreven).
2. **Richt een schone server in** met hetzelfde besturingssysteem en dezelfde PostgreSQL-versie.
3. **Zet de meest recente back-up terug** (procedure voor de IT-beheerder).
4. **Controleer de gegevens** — kijk of studenten, klassen en cijfers aanwezig zijn.
5. **Start de applicatie opnieuw**.
6. **Voer een test uit** — meld je aan en controleer of de belangrijkste werkwijzen werken.

**Benodigde tijd:** 1–4 uur, afhankelijk van de databasegrootte.

Neem contact op met je systeembeheerder voor de volledige procedure voor terugzetten.

---

## Aanbevolen beveiligingsmaatregelen voor je school

### Voor alle gebruikers
- ✅ Gebruik een sterk, uniek wachtwoord (minimaal 12 tekens, met hoofdletters, kleine letters, cijfers en symbolen).
- ✅ Deel je aanmeldgegevens nooit met anderen.
- ✅ Meld je af wanneer je een computer verlaat.
- ✅ Meld verdachte activiteiten bij je IT-beheerder.

### Voor docenten en coördinatoren
- ✅ Controleer of inzendingen van studenten authentiek zijn (controleer tijdstempels en metadata).
- ✅ Bekijk de beoordelingsgeschiedenis als een cijfer van een student ongebruikelijk lijkt.
- ✅ Gebruik controlelogboeken om zorgvuldigheid bij belangrijke beslissingen aan te tonen.

### Voor beheerders
- ✅ Controleer mislukte aanmeldpogingen (dashboard Systeemstatus).
- ✅ Bekijk toegangslogboeken als toegang tot gevoelige gegevens ter discussie staat.
- ✅ Verplicht gebruikers jaarlijks hun wachtwoord te wijzigen.
- ✅ Archiveer of verwijder accounts wanneer medewerkers of studenten vertrekken.
- ✅ Test back-ups elk kwartaal.

---

## Reageren op incidenten

### Als er iets misgaat

**Gegevensverlies of beschadiging**
1. Neem onmiddellijk contact op met je systeembeheerder.
2. Probeer niet zonder ondersteuning van IT een back-up terug te zetten.
3. Het systeem wordt hersteld vanaf de meest recente back-up (maximaal 24 uur gegevensverlies).

**Datalek of onbevoegde toegang**
1. Neem contact op met je systeembeheerder.
2. De systeembeheerder onderzoekt de controlelogboeken om vast te stellen welke gegevens zijn bekeken en door wie.
3. Betrokkenen worden geïnformeerd.

**Systeem niet beschikbaar**
1. Controleer het dashboard Systeemstatus.
2. Neem contact op met je systeembeheerder als de status aangeeft dat het systeem niet werkt.
3. Je krijgt informatie over de verwachte hersteltijd.

**E-mail werkt niet**
1. Controleer of de SPF- en DKIM-records zijn ingesteld.
2. Controleer of de firewall of antivirussoftware voor e-mail de berichten niet blokkeert.
3. Stuur vanuit ILS een testmail via (Instellingen → Testmail verzenden).

---

## Contact en ondersteuning

**Systeembeheerder:** [vul hier je contactgegevens in]  
**E-mailondersteuning:** [e-mailadres voor ondersteuning]  
**Noodnummer:** [telefoonnummer]  

---

**Laatst bijgewerkt:** 2026-06-27  
**Versie:** 1.0 (klaar voor pilot)
