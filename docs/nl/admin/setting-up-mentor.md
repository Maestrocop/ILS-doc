## Beheerdersgids — een mentor instellen

### Stap 1 — De rol Mentor toewijzen (pagina Gebruikers)

1. Ga naar **Instellingen → Gebruikers**.
2. Zoek de medewerker (bijvoorbeeld Peter Groen).
3. Open het menu met de drie puntjes → **Bewerken** (of de knop voor rollen).
4. Vink `mentor` aan in de rollenlijst. De medewerker kan daarnaast ook de rol `teacher` houden.
5. Sla op.

> De rol `mentor` is de algemene toegangscontrole. Zonder deze rol heeft iemand geen toegang tot het beoordelingssysteem.

---

### Stap 2 — Studenten toewijzen (pagina Student Advisors)

1. Ga naar **Student Support → Student Advisors**.
2. Klik op **In bulk toewijzen** en selecteer de klas.
3. Kies als type adviseur **mentor**.
4. Selecteer de medewerker en de studenten voor wie deze verantwoordelijk is.
5. Sla op.

> Dit is de specifieke toegangscontrole. Een mentor kan alleen een BSA-beoordeling openen voor studenten die hier expliciet aan die mentor zijn toegewezen. Staat een student niet in de lijst, dan blokkeert het systeem de actie met de melding "Je bent niet de toegewezen adviseur voor deze student".

---

### De regel

Beide onderdelen moeten zijn ingesteld:

- `Settings → Users` → `users.roles` moet `mentor` bevatten (algemene toegangscontrole).
- `Student Advisors` → de rij in `student_advisors` moet de student(en) bevatten die aan de mentor zijn toegewezen (specifieke toegangscontrole).

Een van beide is niet voldoende: om een beoordeling van een student te behandelen, heeft de medewerker zowel de rol `mentor` als de toewijzing aan die student nodig.
