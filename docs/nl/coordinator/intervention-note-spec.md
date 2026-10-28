# Specificatie interventie- / contactnotitie

Doel: het gegevensmodel, de rechten, de UI-processen en de acceptatiecriteria voor de functie Interventie- / contactnotitie definiëren (specificatie uitsluitend voor documentatie).

## Overzicht

Coördinatoren, begeleiders en bevoegd personeel kunnen korte interventienotities vastleggen die gekoppeld zijn aan studenten, docenten, modules of klassen. De notities vormen een blijvende registratie van contact en ondernomen acties.

## Gegevensmodel (documentatie)

- `id` (string)
- `author_id` (string) — personeelslid dat de notitie heeft aangemaakt
- `author_role` (string) — bijvoorbeeld Coordinator, Advisor
- `linked_student_id` (string, nullable)
- `linked_teacher_id` (string, nullable)
- `module_id` (string, nullable)
- `class_id` (string, nullable)
- `note_text` (text)
- `tags` (array of strings)
- `visibility` (enum: `private`, `staff`, `public`)
- `created_at` (timestamp)
- `updated_at` (timestamp)

## Rechten (documentatie)

- Wie kan aanmaken: coördinatoren, begeleiders en toegewezen medewerkers.
- Wie kan bekijken: coördinatoren en de aan de student toegewezen begeleiders; docenten kunnen notities bekijken die aan hun klassen zijn gekoppeld, tenzij ze als `private` zijn gemarkeerd.
- Wie kan bewerken/verwijderen: de auteur en sitebeheerders. Verwijderingen moeten controleerbaar zijn; geef de voorkeur aan soft delete.

## UI-processen (documentatie)

1. Notitie aanmaken: de coördinator opent een student of module, klikt op **Interventienotitie toevoegen**, vult `note_text` in, selecteert koppelingen (student/docent/module), stelt de zichtbaarheid in en slaat op.
2. Lijst en filters: de coördinator ziet een gepagineerde lijst met notities en filters (student, docent, module, tag, datumbereik).
3. Bekijken: open een notitie om de volledige tekst, auteur en audittrail te bekijken.

## Audit en bewaartermijn (documentatie)

- Alle notities moeten onveranderbaar worden geregistreerd in een audittabel: wie heeft wat en wanneer gewijzigd.
- Bewaartermijn: volg het AVG-beleid van de school; documenteer de bewaartermijn (bijvoorbeeld 7 jaar) en de werkwijze voor verwijdering.

## Acceptatiecriteria

- De coördinator kan een notitie aanmaken die aan een student en module is gekoppeld, en deze terugzien in de tijdlijn van de student.
- Notities verschijnen in coördinatorlijsten en zijn doorzoekbaar op tag en tekst.
- Zichtbaarheidsregels worden afgedwongen: `private`-notities zijn niet zichtbaar voor docenten.
- De audittrail registreert gebeurtenissen voor aanmaken, bewerken en verwijderen.

## Voorbeeldpayloads (alleen documentatie)

Payload voor het aanmaken van een notitie (voorbeeld):

```json
{
  "author_id": "staff_123",
  "linked_student_id": "student_456",
  "module_id": "module_789",
  "note_text": "Contacted student about missing assignments; arranged advisor meeting.",
  "tags": ["attendance","follow-up"],
  "visibility": "staff"
}
```

---

**Laatst bijgewerkt:** 2026-07-06
