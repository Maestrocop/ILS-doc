# Controle van de beheeromgeving — verweesde periodes vinden en herstellen

Op deze pagina staan snelle controles waarmee beheerders academische periodes zonder datums kunnen vinden, verwijzingen vanuit de cursusstructuur kunnen bekijken en dit veilig kunnen herstellen. Alleen-lezen: deze documentatie wijzigt niets in `ILS-dev`.

## Snelle checklist

- Voer de query `Orphan periods` uit en bekijk de resultaten.
- Zoek rijen in `course_structure` die verwijzen naar periodes zonder datums.
- Bepaal hoe je dit herstelt: datums en een bovenliggende periode toevoegen, `course_structure` opnieuw koppelen of de verweesde periode verwijderen.
- Maak een back-up van de database voordat je wijzigingen uitvoert die gegevens kunnen verwijderen.

---

## Voorbeeldquery's voor SQL (hulpmiddelen voor alleen-lezen)

1) Periodes `academic_periods` zonder datums (verweesde periodes) vinden

```sql
SELECT id, name, parent_id
FROM academic_periods
WHERE start_date IS NULL OR end_date IS NULL
ORDER BY id;
```

2) Rijen in `course_structure` vinden die verwijzen naar periodes zonder datums

```sql
SELECT cs.id AS course_structure_id, cs.course_id, cs.module_id, ap.id AS period_id, ap.name
FROM course_structure cs
JOIN academic_periods ap ON ap.id = cs.academic_period_id
WHERE ap.start_date IS NULL OR ap.end_date IS NULL
ORDER BY cs.course_id;
```

3) Roosterregels vinden die verwijzen naar periodes zonder datums

```sql
SELECT tsr.id AS rule_id, tsr.class_id, tsr.academic_period_id, ap.name
FROM timetable_schedule_rules tsr
JOIN academic_periods ap ON ap.id = tsr.academic_period_id
WHERE ap.start_date IS NULL OR ap.end_date IS NULL;
```

---

## Opmerkingen over de implementatie (waar je in de code op let)

Dit is het huidige gedrag van `ILS-dev`. Zo kun je de resultaten van een controle vergelijken met de pagina's en API's:

- Composer maakt periodes aan die bij een cursus horen via `POST /api/curriculum/courses/:courseId/periods`. Als de datums zo zijn ingevuld, kunnen `start_date` en `end_date` leeg blijven.
- Eindpunten voor het aanmaken van de cursusstructuur (`POST /api/curriculum/courses/:courseId/structure`) accepteren een `period_id` en voegen rijen toe die modules aan die periode koppelen. Aan de API-grens wordt niet gecontroleerd of de periode datums heeft.
- Gebruik de pagina Periodes in de beheeromgeving om periodes te bekijken en te bewerken. Deze gebruikt `GET /api/periods` en `GET /api/periods/tree`. Wijzigingen lopen via `PUT /api/periods/:id` of, voor periodes die bij een cursus horen, via `PATCH /api/curriculum/periods/:periodId`.

Als je wilt, kan ik exacte voorbeelden van eindpunten toevoegen (curl en request body) om beheerders te helpen het herstel via de API uit te voeren. Ik wijzig `ILS-dev` niet.

---

## Veilige stappen om dit te herstellen

1. Maak een back-up van de database (dump of migratie die de betreffende rijen kopieert).
2. Was de verweesde periode bedoeld voor het juiste studiejaar? Stel dan `start_date` en `end_date` in en wijs met `parent_id` de rij van het studiejaar als bovenliggende periode toe.
3. Moet de verweesde periode worden verwijderd? Koppel `course_structure` dan opnieuw aan de juiste periodes met datums, test dit en verwijder daarna de verweesde periode.
4. Genereer de roosters opnieuw voor de betreffende klassen en controleer of de bijeenkomsten verschijnen.

---

## Automatische controles (wat de pagina Gezondheid moet tonen)

- Aantal periodes zonder datums.
- Lijst met rijen in `course_structure` die verwijzen naar periodes zonder datums (cursus, module en periode-ID).
- Lijst met `timetable_schedule_rules` die verwijzen naar periodes zonder datums en de informatie of ze geen bijeenkomsten genereren.

---

Wil je dat ik ook een kleine mock-up van een checklist voor beheerders en een voorbeeldsjabloon voor een migratiescript toevoeg? Ik wijzig `ILS-dev` niet; ik pas alleen documentatie in `ILS-doc` aan.


**Laatst bijgewerkt:** 2026-07-08
