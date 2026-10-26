# Agenda voor studenten

Deze gids legt uit hoe je de agenda gebruikt om bijeenkomsten, deadlines en verplaatste of ingehaalde lessen bij te houden.

## De agenda bekijken

1. Open **Agenda** in de hoofdnavigatie.
2. Kies de weergave `Month`, `Week` of `Day`.
3. Gebruik de filters om alleen de klassen waarvoor je bent ingeschreven of alle modulesessies te tonen.

## Details van een bijeenkomst

- Klik op een bijeenkomst om de locatie, docent, gekoppelde leeruitkomsten en bijgevoegde bronnen te bekijken.
- Is een bijeenkomst geannuleerd of verplaatst? Dan toont de kaart de status en een link naar de ingehaalde les, als die is ingepland.

## Deadlines en inleverdatums van opdrachten

- Deadlines van opdrachten staan met een paperclippictogram in de agenda.
- Klik op de deadline om de opdracht te openen en je werk in te leveren.

## Synchroniseren met externe agenda's

- Als je school agendasynchronisatie heeft ingeschakeld, kun je je abonneren via een iCal-feed of via agenda-integraties in `Settings → Calendar`.
- Opnieuw synchroniseren: open `Settings → Calendar` en klik op **Opnieuw synchroniseren**. Loopt een externe agenda achter? Vraag het dan aan de IT-afdeling of controleer de status van de integratie.

## Meldingen

- Je stelt agendameldingen in via `Settings → Notifications`.
- Schakel herinneringen voor aankomende bijeenkomsten en deadlines van opdrachten in.

## Problemen oplossen

- "Ik zie geen bijeenkomst": controleer de zichtbaarheid en publicatiedatum van de module. Gepubliceerde bijeenkomsten zijn zichtbaar; niet-gepubliceerde bijeenkomsten niet.
- "Mijn agenda is niet gesynchroniseerd": controleer je iCal-URL en synchroniseer opnieuw via de instellingen.

**Laatst bijgewerkt:** 2026-07-06
# Agenda voor studenten

Je agenda toont al je deadlines, lessen en belangrijke datums in één tijdlijn.

## Wat je in de agenda ziet

- **Deadlines van opdrachten** — wanneer je opdrachten moet inleveren
- **Quizdatums** — wanneer quizzen zijn ingepland en wanneer je ze moet afronden
- **Lessen** — wanneer je lessen plaatsvinden
- **Agenda-items** — speciale bijeenkomsten, feestdagen of mededelingen van je docenten of instelling

## De agenda gebruiken

1. Open **Mijn agenda** op je dashboard.
2. Bekijk vandaag en de aankomende gebeurtenissen voor de komende vier maanden.
3. Klik op een gebeurtenis om meer informatie te bekijken of de bijbehorende opdracht of quiz te openen.

## Soorten gebeurtenissen

- **Opdracht beschikbaar** — de dag waarop je met een opdracht kunt beginnen
- **Deadline opdracht** — de uiterste datum om je werk in te leveren
- **Quiz beschikbaar** — de dag waarop je de quiz kunt maken
- **Deadline quiz** — de uiterste datum om de quiz af te ronden
- **Les** — het tijdstip van je gewone les
- **Onderwijsactiviteit** — feestdagen, examenperiodes, begin of einde van een semester en andere datums voor de hele campus

## Tip voor je planning

Bekijk je agenda minstens één keer per week om je deadlines bij te houden. Zet opdrachten met hoge prioriteit in je persoonlijke agenda, zodat je ze niet vergeet.

## Terugkerende gebeurtenissen

Sommige gebeurtenissen komen elke week terug, zoals gewone lessen of wekelijkse voortgangsgesprekken. De agenda toont elke keer dat zo'n terugkerende gebeurtenis plaatsvindt, zodat je het volledige patroon kunt zien.
3. Studenten bekijken gebeurtenissen en datums. Kleurcodering geeft aan bij welke klas een gebeurtenis hoort (`useClassColor=true`).
4. Studenten kunnen via de agenda-interface geen gebeurtenissen toevoegen (`canAddEvent=false`). Alleen docenten en beheerders kunnen agendagebeurtenissen aanmaken.

Toelichting op onduidelijkheden en toegangsbeperkingen

- Onduidelijkheid: het exacte pad of label voor **Mijn agenda** in de studentennavigatie. Als je de exacte tekst wilt, kan ik die in de actieve gebruikersinterface controleren.
- Onduidelijkheid: of lessen in een aparte tabel worden opgeslagen of daaruit worden afgeleid. De code wijst erop dat koppelingen tussen lesmodules en klassen worden gebruikt om opdrachten en quizzen aan klasagenda's te koppelen.

Bronnen (alleen ter inzage)

- `frontend/src/pages/StudentCalendarPage.jsx`
- `frontend/src/components/CalendarWidget.jsx`
- `backend/routes/events.js`

---

Volgende stappen: ik wacht op je bevestiging of `Student Cockpit` hier moet worden beschreven of beter bij de docentenpagina hoort. De code in `frontend/src/pages/StudentCockpitPage.jsx` laat zien dat de pagina scopes voor docenten en managers heeft. Wil je dat ik `Student Cockpit` onder de docentenhandleiding beschrijf? Dan maak ik daar een eerste versie en controleer ik deze met `mkdocs build --strict`.
