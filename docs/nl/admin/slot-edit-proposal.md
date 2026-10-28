# Voorstel voor het bewerken van tijdslots (rooster)

Doel: tijdslots in het rooster bewerkbaar maken, zodat beheerders fouten in dag of tijd kunnen corrigeren zonder handmatig te verwijderen en opnieuw aan te maken.

Waarom

- Huidig gedrag: sessies genereren voegt alleen nieuwe rijen toe; om een tijdslot te bewerken, moeten bestaande sessies worden verwijderd en opnieuw worden gegenereerd. De UI ondersteunt nu alleen verwijderen en toevoegen, wat omslachtig is.

Voorstel — server-API

- PATCH `/api/timetable/slots/:slotId`
  - Body: `{ "day_of_week": "Mon", "start_time": "08:30", "end_time": "10:00" }` (schemavelden moeten overeenkomen met de bestaande database)
  - Auth: beheerder of rol timetable-manager
  - Gedrag:
    1. Valideer de nieuwe tijden (geen overlap binnen dezelfde klas/campus/periode).
    2. Start een databasetransactie.
    3. Verwijder bestaande gegenereerde sessies die aan het tijdslot zijn gekoppeld (of markeer ze als gearchiveerd), bijvoorbeeld `DELETE FROM timetable_sessions WHERE slot_id = :slotId` (pas dit aan de werkelijke structuur aan).
    4. Werk de rij van het tijdslot bij met de nieuwe tijden.
    5. Genereer de sessies voor het tijdslot opnieuw (gebruik dezelfde generator als bij de eerste aanmaak).
    6. Rond de transactie af en retourneer het bijgewerkte tijdslot en de opnieuw gegenereerde sessies.

Implementatieopmerkingen

- Gebruik een databasetransactie om gedeeltelijke wijzigingen te voorkomen als het genereren mislukt.
- Als andere entiteiten naar gegenereerde sessies verwijzen (aanwezigheidsregistraties, cijfers), overweeg dan soft delete of een migratie die die koppelingen behoudt en ze naar de nieuwe sessierijen kopieert.
- Als het systeem momenteel geen `slot_id` opslaat bij gegenereerde sessies, voeg dan een kleine migratie toe om het oorspronkelijke tijdslot vast te leggen en dit veilig te maken.

Frontend-UI

- Inline bewerken op elk tijdslotlabel (geen dialoogvenster): klik → velden `day`, `start`, `end` uitklappen → Opslaan / Annuleren
- Bij Opslaan: toon een bevestiging: "Hierdoor worden de sessies voor dit tijdslot verwijderd en opnieuw gegenereerd. Doorgaan?" met een lijst van betrokken weken/datumbereiken.
- Als er vaak wordt bewerkt, voeg dan een stap voor ongedaan maken/voorbeeld toe die de betrokken sessies toont voordat de wijziging wordt vastgelegd.

Acceptatietests

- PATCH werkt het tijdslot en de vervangen sessies bij binnen één transactie.
- Bewerken van een tijdslot met overlappende tijden wordt geweigerd (400).
- Bewerken behoudt historische aanwezigheidsregistraties/cijfers volgens de gekozen strategie (archiveren of opnieuw aanmaken).

Op te leveren door ontwikkelaars

- Backend: nieuwe route-handler `PATCH /api/timetable/slots/:slotId`, unit-tests en een integratietest die het opnieuw genereren van sessies controleert.
- Frontend: inline component voor tijdslotbewerking, bevestigingsinteractie en een integratietest die de opnieuw gegenereerde sessies toont.

Opmerkingen

- De exacte tabel- en kolomnamen voor sessies en tijdslots zijn niet gecontroleerd in ILS-dev als onderdeel van dit document; raadpleeg het schema voordat je SQL schrijft. Als je wilt, kan ik de exacte SQL en een patch opstellen in een afzonderlijke branch — ik wijzig ILS-dev niet tenzij je daar expliciet om vraagt.


**Laatst bijgewerkt:** 2026-07-08
