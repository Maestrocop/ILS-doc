# Timetable Engine — stapsgewijze handleiding van begin tot eind

Volg deze stappen in de aangegeven volgorde — elke rol gaat verder waar de vorige is gebleven. Dit is een alleen-lezen handleiding voor gebruikers; er wordt geen code in `ILS-dev` aangepast.

## Vereisten
- Er bestaat ten minste één klas (bijvoorbeeld BK Jaar 1 — 2025/2026).
- Er is ten minste één onderwijsperiode ingesteld (bijvoorbeeld Semester 1).
- De academische kalender bevat ten minste één vakantiegebeurtenis (om de oversla-logica te testen).
- De klas heeft ten minste één ingeschreven student en één toegewezen docent.

---

## Fase 1 — Beheerder/coördinator: rooster aanmaken en activeren

1. Open de pagina Rooster: `/admin/timetable` en selecteer de klas — je ziet "Er is nog geen rooster geconfigureerd".
2. Maak een rooster aan: klik op **Nieuw rooster**, selecteer de klas en onderwijsperiode en sla op → het rooster verschijnt met de status `draft`.
3. Voeg terugkerende tijdslots toe: klik op **Tijdslot toevoegen**; bijvoorbeeld maandag 09:00–11:00 en woensdag 14:00–16:00; sla op — de tijdslots worden weergegeven.
4. Activeer het rooster: klik op **Activeren** → het systeem genereert sessierijen tot het einde van de periode; vakantiedatums krijgen de status `cancelled` en tonen de naam van de vakantie.
5. Controleer de sessies: controleer de statussen ingepland, geannuleerd en inhaalsessie, en het verwachte aantal sessies.

## Proces voor het toewijzen van docenten (belangrijke opmerking)

Controleer voordat je roosterregels aanmaakt of docenten op klasniveau zijn toegewezen:

1. Open `/admin/my-classes` → selecteer de klas (bijvoorbeeld BK-J1-2526) → ga naar **Curriculum instellen** en controleer of aan elke module een docent is toegewezen (hierdoor wordt een rij `class_module_teachers` aangemaakt).
2. Open nu `/admin/timetable` → selecteer de klas → de matrix met roosterregels haalt modules op uit het curriculum van de klas. Wanneer je een regel aanmaakt en een module kiest, wordt het docentveld automatisch ingevuld op basis van de toewijzing in `class_module_teachers`. Als meerdere docenten aan dezelfde module zijn toegewezen, kies je welke docent voor die regel wordt gebruikt.

Gecorrigeerde stappen van begin tot eind:

1. `/admin/my-classes` → BK-J1-2526 → **Curriculum instellen** → controleer of aan modules een docent is toegewezen.
2. `/admin/timetable` → BK-J1-2526 → de matrix toont de rij Semester 2 / kolom ma → klik op `+ Add` → kies een module → docent wordt automatisch ingevuld → Opslaan.
3. Klik op **Sessies genereren** → bevestig het aantal.
4. Controleer de docentenkalender op `/teacher/calendar`.
5. Controleer de studentenkalender op `/student/calendar`.

Vraag: zijn de docenten al toegewezen in `my-classes`, of moet dat eerst gebeuren? Kort antwoord: ja — wijs docenten eerst toe in `my-classes`; de roosterregels lezen die toewijzingen.

---

## Fase 2 — Docent: aanwezigheid registreren

6. Open het docentrooster: log in als toegewezen docent → weekweergave op `/admin/my-schedule`, met blokken voor sessies.
7. Markeer een sessie als gegeven: klik op een sessieblok → **Als gegeven markeren**; de status wordt `held`.
8. Registreer de aanwezigheid: open de sessie → **Aanwezigheid**, markeer Aanwezig/Afwezig en sla op → bevestigingsbadge verschijnt.
9. Annuleer een sessie: selecteer een toekomstige sessie → **Annuleren**, voer een reden in → de status wordt `cancelled`.
10. Voeg een inhaalsessie toe: selecteer een geannuleerde sessie → **Inhaalsessie plannen**, kies datum en tijd → nieuwe sessie met de status `makeup`.

---

## Fase 3 — Sessie bewerken (deze sessie / deze en volgende)

11. Bewerk één sessie: kies **Alleen deze sessie** wanneer je tijd of lokaal wijzigt — alleen die sessie wordt aangepast.
12. Bewerk deze en volgende sessies: kies **Deze en alle volgende** om sessies vanaf dit moment bij te werken.

---

## Fase 4 — Studentenweergave

13. Studentenkalender: log in als ingeschreven student → de kalender toont sessies met kleurcodering en statusbadges.
14. Aanwezigheidsbadge op het dashboard: het studentendashboard toont een ringdiagram met het aantal gegeven sessies tegenover het aantal bijgewoonde sessies.

---

## Fase 5 — Koppeling met het curriculum (optioneel)

15. Koppel een sessie aan curriculuminhoud: open een sessie (docent/beheerder) → tabblad Lessen/Curriculum → voeg een gepland moduleonderdeel toe; markeer het na de sessie als behandeld.

---

## Waar je tijdens het testen op moet letten
- Noteer elke stap die een fout geeft of een leeg scherm toont.
- Noteer onduidelijke UI-teksten.
- Noteer ontbrekende functionaliteit.

Deze hiaten vormen het resterende werk aan Timetable Engine.


**Laatst bijgewerkt:** 2026-07-08
