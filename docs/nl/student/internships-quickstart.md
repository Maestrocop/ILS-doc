# Snelstart voor studenten — Stage zoeken en solliciteren

In deze snelstart lees je hoe je documenten uploadt, bij bedrijven solliciteert (registreren of versturen) en de uitkomst van een sollicitatie bijwerkt.

## De stagepagina openen

Open **Stagepagina** vanuit je hoofddashboard.
De pagina heeft twee hoofdpanelen: **Jouw documenten** en **Mijn sollicitaties**.

## Je cv uploaden

1. Selecteer **Cv** in de keuzelijst voor documenttypen in **Jouw documenten**.
2. Klik op **Bestand kiezen**, selecteer je cv (PDF of DOCX) en klik op **Uploaden**.
3. Na het uploaden toont de interface: **Cv ingediend — wacht op beoordeling**.

Opmerkingen:
- Het bestand wordt opgeslagen als een versiebeheerd `internship_document` en moet eerst door je begeleider worden goedgekeurd voordat je het voor sollicitaties kunt gebruiken.
- Alleen het paneel Documenten toont de uploadstatus.

## Feedback en goedkeuring van je begeleider bekijken

- Vernieuw `/student/internship` nadat je begeleider je cv heeft beoordeeld.
- Goedgekeurd: in het paneel Documenten verschijnt **✓ Cv goedgekeurd** (groen).
- Aanpassen: **⚠ Cv moet worden aangepast** (oranje) verschijnt samen met feedback van je begeleider.

Moet je je cv aanpassen? Werk het bestand dan bij en upload de nieuwe versie.

## Bij een bedrijf solliciteren (registreren of versturen)

1. Klik op **+ Solliciteren bij een bedrijf** in **Mijn sollicitaties**.
2. Vul de velden in: bedrijfsnaam, naam contactpersoon en e-mailadres van het bedrijf.
3. Selecteer een goedgekeurd cv in de keuzelijst met bijlagen.
4. Voeg eventueel een motivatiebrief toe of pas deze aan.
5. Kies een actie:
   - **Sollicitatie registreren** — slaat de sollicitatie op in het systeem; er wordt geen e-mail verstuurd.
   - **Sollicitatie versturen** — probeert de sollicitatie-e-mail vanuit de app te versturen.

Als je de sollicitatie verstuurt:
- Als de systeemmailrelay (SendGrid/Mailgun) of SMTP is ingesteld, verstuurt de backend een e-mail met het cv en de brief als bijlagen.
- Als het versturen lukt of wordt geregistreerd, wordt de sollicitatie opgeslagen met `sent_at = now()` en `sent_via_app = true`. Is de relay niet ingesteld, dan registreert de app de aanvraag als "Verzenden geregistreerd (relay niet ingesteld)".

Na het versturen of registreren verschijnt de sollicitatie in **Mijn sollicitaties**, met het bedrijf, de datum en de status.

## De uitkomst van je sollicitatie bijwerken (bijvoorbeeld een gesprek)

1. Zoek de sollicitatie in **Mijn sollicitaties** en klik op **Uitkomst bijwerken**.
2. Selecteer de nieuwe uitkomst (bijvoorbeeld **Gesprek ingepland**) en vul de datum in.
3. Klik op **Opslaan**.

Resultaat: de sollicitatiestatus en je studententijdlijn worden bijgewerkt. Begeleiders ontvangen meldingen, bijvoorbeeld: **"[Student] — Gesprek @ Bedrijf X — [datum]"**.

## Problemen oplossen en veelgestelde vragen

- Staat je cv niet in de keuzelijst met bijlagen? Het cv is nog niet **Goedgekeurd**. Wacht op de beoordeling van je begeleider of upload een aangepaste versie.
- Heb je op Versturen geklikt, maar heeft het bedrijf de e-mail niet ontvangen? Controleer de sollicitatie. Staat er "Verzenden geregistreerd (relay niet ingesteld)"? Vraag dan je coördinator de SMTP/relay in de backend `.env` in te schakelen.
- Kun je je sollicitatie niet zien? Controleer je inschrijving voor de klas of campagne en de filters op `/student/internship`.

## Privacy en zichtbaarheid voor je begeleider

- Sollicitaties die je via de app verstuurt, krijgen een tijdstempel en zijn zichtbaar voor je begeleider. Zo kan die je ondersteunen bij het zoeken naar een stage.
- Antwoorden van bedrijven komen binnen op de mailbox van de school. De antwoorden worden op de juiste manier doorgestuurd via het ingestelde Reply-To-adres.

---

Wil je een afdrukbare checklist van één pagina of een korte tekst voor een in-app-helpvenster voor deze werkwijze? Laat het me weten, dan maak ik die voor je.
