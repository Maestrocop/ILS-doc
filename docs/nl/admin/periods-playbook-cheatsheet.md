# Perioden draaiboek — korte, duidelijke checklist

Praktisch en actiegericht draaiboek voor beheerders, ontwerpers en docenten. Alleen-lezen: ik wijzig `ILS-dev` niet.

## Regel in één zin

Maak eerst periodes met datums aan in de Academische kalender, bouw daarna het curriculum op en maak vervolgens de roosterregels aan.

---

## Snelle checklist (wat doe je nu?)

- Beheerder: voer de SQL-query `Orphan periods` hieronder uit. Verschijnen er rijen? Kies dan Hersteloptie A of B.
- Ontwerper: gebruik altijd de periodekiezer in Composer. Typ geen nieuwe periodelabels.
- Docent: ontbreken er bijeenkomsten? Stuur een screenshot en het klas-ID naar de beheerder.

---

## Voorbeeld-SQL (kopiëren en plakken)

Periodes zonder datums vinden:

```sql
SELECT id, name, parent_id FROM academic_periods WHERE start_date IS NULL OR end_date IS NULL ORDER BY id;
```

Rijen in `course_structure` vinden die verwijzen naar periodes zonder datums:

```sql
SELECT cs.id AS cs_id, cs.course_id, cs.module_id, ap.id AS period_id, ap.name
FROM course_structure cs
JOIN academic_periods ap ON ap.id = cs.period_id
WHERE ap.start_date IS NULL OR ap.end_date IS NULL;
```

---

## Herstel — twee veilige opties

Optie A — Datums toevoegen (aanbevolen als de periode wel bedoeld is):

1. Open Beheer → Periodes → bewerk de verweesde periode.
2. Stel `start_date` en `end_date` in en stel `parent_id` in op het academische jaar.
3. Genereer de roosters voor de klas opnieuw en controleer of de bijeenkomsten verschijnen.

Optie B — `course_structure` opnieuw koppelen (aanbevolen als semesters worden gebruikt):

1. Werk `course_structure.period_id` bij naar de juiste ID van het semester (via de gebruikersinterface of API).
2. Controleer in Composer of de slot in `course_structure` de naam van het semester toont.
3. Genereer het rooster opnieuw en controleer of dit lukt.

---

## Voorbeeld van herstel via de API (curl)

Datums toevoegen aan periode-ID 185:

```bash
curl -X PATCH "http://localhost:4000/api/curriculum/periods/185" \
  -H "Content-Type: application/json" \
  -d '{"start_date":"2025-09-01","end_date":"2026-02-28","parent_id":123}'
```

Een slot in `course_structure` (ID 999) opnieuw koppelen aan semester-ID 32:

```bash
curl -X PATCH "http://localhost:4000/api/curriculum/structure/999" \
  -H "Content-Type: application/json" \
  -d '{"period_id":32}'
```

> Opmerking: maak altijd een back-up van de database voordat je API-wijzigingen uitvoert op de productieomgeving.

---

## Kleine illustratie — gegevensstroom

Periodes (Academische kalender) → Cursusstructuur (Composer) → Roosterregels → Bijeenkomsten

Verwijst een pijl naar een periode zonder datums? Dan worden er geen bijeenkomsten gegenereerd.

---

## Snelle dagelijkse controles voor beheerders

1. Wekelijks: voer de SQL-query `undated periods` uit en herstel nieuwe rijen meteen.
2. Vóór elk semester: controleer of er periodes met datums voor het studiejaar zijn.
3. Na wijzigingen in Composer: voer `GET /api/curriculum/courses/:courseId/structure` uit en controleer de namen van de periodes.

---

Wil je dat ik ook een klein sjabloon voor een migratiescript toevoeg om verweesde rijen in `course_structure` in bulk opnieuw te koppelen? Ik wijzig geen code in `ILS-dev`.


**Laatst bijgewerkt:** 2026-07-08
