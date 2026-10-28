# Stages — end-to-endwerkwijze

Deze pagina beschrijft de geverifieerde werkwijze voor het zoeken naar een stage en solliciteren via de app. Deze is zichtbaar voor coördinatoren, begeleiders en studenten.

---

## Overzicht

Het platform ondersteunt de geverifieerde werkwijze "verzenden vanuit de app". Sollicitaties van studenten krijgen zo een tijdstempel, zijn te volgen door de begeleider en reacties komen binnen op de mailbox van de school. Hieronder staat de normale werkwijze voor het instellen door een coördinator, het beheren van studentdocumenten, het beoordelen door een begeleider en het registreren of versturen van sollicitaties.

---

## De stage doorloopt vier fasen

Het stageproces is verdeeld in vier fasen die aansluiten bij de verantwoordelijkheden van de rollen die al in het product zichtbaar zijn:

### 1. Zoeken

- **Student**: uploadt een cv en motivatiebrief, solliciteert bij bedrijven en volgt de uitkomsten, zoals in afwachting, gesprek ingepland, afgewezen of aangenomen.
- **School**: beoordeelt het cv en de motivatiebrief en houdt in de gaten of de student actief solliciteert. Hier hoort het signaal **risico — geen sollicitaties** thuis.
- **Bedrijf**: nog niet betrokken; in deze fase is er nog geen begeleider.
- **Door naar Geplaatst wanneer**: de uitkomst van een sollicitatie **aangenomen** wordt.

### 2. Geplaatst

- **Student**: bevestigt de gegevens van de stageplaats.
- **School**: controleert de bedrijfsgegevens en werkt de checklist voor de stageplaats af: begeleider toegewezen, datums vastgesteld, leerdoelen ingesteld en afspraken ondertekend.
- **Bedrijf**: wijst een begeleider toe, ontvangt de link naar het portaal met token, bevestigt de bedrijfsgegevens en bevestigt het werkschema.
- **Door naar Op locatie wanneer**: de checklist voldoende is ingevuld en/of de startdatum is aangebroken.

### 3. Op locatie

- **Student**: dient regelmatig activiteitenlogboeken in. Dit is de belangrijkste bewijsregistratie.
- **School**: volgt de betrokkenheid op basis van het aantal dagen sinds het laatste logboek en het aantal geregistreerde uren, en grijpt in als de student niet meer actief is. Hier ontbreekt nu nog een dashboard voor bewaking van de uitvoering en risico's.
- **Bedrijf**: de begeleider bevestigt logboeken of geeft er opmerkingen bij via de portaal-link.
- **Door naar Evalueren wanneer**: de einddatum is bereikt of de school de evaluatie expliciet start.

### 4. Evalueren

- **Student**: kan eventueel een zelfreflectie indienen.
- **School**: dient de beoordelingsscore en feedback in.
- **Bedrijf**: de begeleider dient een onafhankelijke beoordeling in. Het verschil tussen beide scores is op zichzelf een nuttig signaal om beoordelingen te kalibreren en te toetsen aan de praktijk.
- **Afgerond wanneer**: beide beoordelingen zijn ingediend of de school het proces afsluit.

---

## Stap 1: Coördinator maakt een programma aan (beheerder)

- Ga naar `/admin/internships`.
- Klik op **+ Nieuw programma**.
- Selecteer: klas, studiejaar, type, programmanaam en begin- en einddatum voor het zoeken.
- Klik op **Campagne aanmaken**.

Resultaat: er wordt een campagnerecord aangemaakt en je gaat naar de detailpagina van de campagne.

---

## Stap 2: Coördinator schrijft studenten in (beheerder)

- Open het programma dat je net hebt aangemaakt (`/admin/internships` → selecteer de campagne).
- Klik op **+ Studenten inschrijven**.
- Selecteer een of meer studenten met de selectievakjes.
- Klik op **N studenten inschrijven**.

Resultaat: voor elke ingeschreven student wordt een `internship`-record aangemaakt. De studenten verschijnen in de zoekfase van de campagne.

---

## Stap 3: Student uploadt een cv (student)

- De student meldt zich aan en gaat naar `/student/internship`.
- Scrolt naar het onderdeel **Jouw documenten**.
- Kiest **Cv** in de keuzelijst voor documenttypen.
- Klikt op **Bestand kiezen** en selecteert het cv (PDF/DOCX).
- Klikt op **Uploaden**.

De app toont: **Cv ingediend — wacht op beoordeling** (de status staat in het paneel Documenten).

Opmerking: het geüploade bestand wordt als versiebeheerd `internship_document` opgeslagen en wacht op beoordeling door een begeleider.

---

## Stap 4: Begeleider beoordeelt het cv (beheerder / begeleider)

- Ga naar `/admin/internships/campaigns/[id]`.
- Klik op de naam van de student om de detailweergave te openen.
- Zoek het onderdeel **Documenten** en klik op het cv van de student.
- Kies de status: **Goedgekeurd ✓** of **Aanpassing nodig**.
- Voeg eventueel feedback voor de student toe.
- Klik op **Beoordeling opslaan**.

Resultaat: de documentstatus wordt bijgewerkt. Na goedkeuring kan de student het cv voor sollicitaties selecteren.

---

## Stap 5: Student ziet de bijgewerkte cv-status (student)

- De student vernieuwt `/student/internship`.
- In **Jouw documenten** heeft het cv nu een van deze statussen:
  - `✓ CV approved` (groen)
  - `⚠ CV needs revision` (oranje) — feedback van de begeleider wordt getoond

Belangrijk: de documentstatus wordt alleen in het paneel Documenten bijgewerkt, niet in de kop van de pagina.

---

## Stap 6: Student solliciteert bij bedrijven (student)

- Klik op **+ Solliciteren bij een bedrijf** op `/student/internship`.
- Vul de bedrijfsgegevens in: naam, contactpersoon en e-mailadres van het bedrijf.
- Selecteer een goedgekeurd cv in de keuzelijst met bijlagen.
- Upload eventueel een motivatiebrief of pas deze aan.
- Kies een actie: **Sollicitatie registreren** (alleen registreren) of **Sollicitatie versturen** (versturen via de app).

Werking bij versturen:
- Als je **Sollicitatie versturen** kiest, legt de backend `sent_at = now()` en `sent_via_app = true` vast en voegt deze de geselecteerde document-ID's als bijlage toe.
- Als SMTP of een relay niet is ingesteld, wordt de actie geregistreerd met de status "Verzenden geregistreerd (relay niet ingesteld)".

Studentweergave: de sollicitatie verschijnt onder **Mijn sollicitaties**, met bedrijf, datum en status.

Weergave voor begeleiders: op het risicopaneel of updatepaneel van de campagne ziet de begeleider een tijdlijn of melding, bijvoorbeeld: **"Lars heeft bij Bedrijf X gesolliciteerd — 10 min geleden"**.

---

## Reactie van een bedrijf en uitkomst bijwerken

- Het bedrijf antwoordt op de mailbox van de school (het antwoordadres wordt ingesteld door de functie Verzenden vanuit de app).
- De student opent de sollicitatie in de app en klikt in de rij van de sollicitatie op **Uitkomst bijwerken**.
- Selecteer **Gesprek ingepland** en vul een datum in (bijvoorbeeld volgende dinsdag).
- Klik op **Opslaan**.

Resultaat: het risicobord van de campagne en de tijdlijn van de student tonen bijvoorbeeld: **"Lars — gesprek bij Bedrijf X — volgende dinsdag"**. De registratie van de student gaat verder in de zoekfase.

---

## Statussen en waar je ze ziet

- `CV submitted — awaiting review` — verschijnt na het uploaden in het paneel Documenten van de student
- `✓ CV approved` — verschijnt na goedkeuring door de begeleider in het paneel Documenten van de student
- `⚠ CV needs revision` — verschijnt samen met feedback van de begeleider in het paneel Documenten
- De aanvraag wordt opgeslagen met de tijdstempel `sent_at` en de waarde `sent_via_app = true`

Opmerking: deze statussen staan in de panelen Documenten en Sollicitaties en worden bewust niet herhaald in de kop van de pagina.

---

## Opmerkingen voor ontwikkelaars en QA (kort)

- Verwijzingen naar pagina's:
  - lijst met campagnes voor beheerders: `/admin/internships`
  - campagnedetails: `/admin/internships/campaigns/[id]`
  - studentendashboard: `/student/internship`
- Betrokken database-entiteiten: `internship_documents`, `internship_applications`, `internships` (inschrijvingen)
- E-mail versturen: gebruik in eerste instantie een relay (SendGrid/Mailgun). Voeg later eventueel een blok met SMTP_*-omgevingsvariabelen toe voor rechtstreeks verzenden vanuit de school.

---

Wil je dat ik dit opsplits in twee bestanden (snelstart voor `admin` en voor `student`), screenshots toevoeg of een QA-checklist maak? Geef aan wat je wilt, dan ga ik verder.
