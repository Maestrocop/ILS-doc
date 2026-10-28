# ILS — End-to-endgids voor inrichting

Deze gids beschrijft de volledige werkwijze voor het inrichten van een nieuw studiejaar, een cursus en het curriculum. De gids is bedoeld voor beheerders, curriculumontwerpers en docenten.

## Fase 1 — Eenmalige inrichting (beheerder)

### Stap 1 — Een instelling aanmaken
- Ga naar: **Instellingen** → Nieuw.
- Verplicht: alleen **Naam**. Alle andere velden zijn optioneel en kun je later invullen via de bewerkpagina van de instelling.
- Velden op het formulier: Naam, Code, Locatie (vrije tekst, bijvoorbeeld "Amsterdam"; geen landenkiezer), Website, Contact-e-mail, URL van logo en Beschrijving.
- Ook op dit formulier: **Status** (Actief/Inactief), **Standaardtaal** (taal van de gebruikersinterface voor alle gebruikers bij deze instelling: English, Nederlands, Deutsch, Français, Español), **Cijferschaal** (10/20/100 — interne scores blijven altijd 0–100; dit bepaalt alleen de weergave) en **Drempelwaarden voor leeruitkomsten** (grenzen voor Risico/Sterk die de scores van studenten in dashboards een kleur geven — standaard 5,5 en 7,0 op een schaal van 10).
- De onderdelen **Beheer van cijfers** en **Functievlaggen** verschijnen pas nadat de instelling is aangemaakt; ze zijn verborgen op het formulier Nieuw. Stel deze daarna in via de bewerkpagina van de instelling.

![Bewerkformulier instelling — gegevens en drempelwaarden voor leeruitkomsten](../images/Foundation/institution-form-details.png)

![Bewerkformulier instelling — beheer van cijfers en functievlaggen](../images/Foundation/institution-form-governance-features.png)

*(De instelling hierboven is een voorbeeld met fictieve demogegevens en is geen echte school.)*

### Stap 2 — Een campus aanmaken
- Ga naar: **Campussen** → Nieuwe campus (opent een dialoogvenster, geen aparte pagina).
- Verplicht: **Naam** en **Instelling** (keuzelijst — selecteer de instelling die je in stap 1 hebt aangemaakt).
- Ook op het formulier: Code, Stad, Status (Actief/Inactief) en Locatie.

![Dialoogvenster Nieuwe campus](../images/Foundation/Campus-new-modal.png)

![Lijst met campussen](../images/Foundation/Campus-list.png)

> **Instellingen voor joint ventures of partnerscholen:** de naam van een campus hoeft niet overeen te komen met de naam van de instelling waartoe deze behoort. Is je school een gezamenlijke organisatie die lesgeeft in gebouwen van een of meer partnerorganisaties? Dan kan de campus de naam van de partner krijgen die eigenaar is van het *gebouw* (bijvoorbeeld "Partnerschool - Campus Noord"), terwijl de instelling in ILS je eigen school blijft. Noem de campus naar de fysieke locatie, niet naar de instelling. Maak één campus aan voor elke fysieke leslocatie die je klassen echt gebruiken. Een klas is gekoppeld aan precies één campus. De leslocatie van een klas kan per schooljaar veranderen; een klas die eerder in een gedeeld gebouw les had, kan het volgende jaar bijvoorbeeld volledig naar een eigen gebouw van een partner verhuizen.

### Stap 3 — Academische periodes aanmaken
- Ga naar: **Periodes** → Nieuwe periode.
- Verplicht: alleen **Naam**. Geldige waarden voor **Type**: Year, Semester, Block, Quarter, Custom.
- Ook op het formulier: Actief (selectievakje), Begin-/Einddatum, Instelling (of "— Globaal —" om de periode met alle instellingen op het platform te delen; laat je eigen instelling staan als je maar één school hebt), Campus (laat "— Geen —" staan, tenzij een specifiek gebouw echt een andere kalender heeft dan de rest van de school) en Bovenliggende periode.
- **Maak eerst het academische jaar op het hoogste niveau aan** (type **Year**, zonder bovenliggende periode, met datums voor het hele schooljaar). Maak **daarna** de onderliggende periodes aan (Bovenliggende periode = het record van het studiejaar). Het record van het studiejaar is niet alleen voor de organisatie: de studentenagenda zoekt de bovenliggende periode op om de kop "Academisch jaar" te tonen. Zonder deze koppeling wordt de kop minder duidelijk.
- Stem **Type** af op het aantal periodes in het studiejaar: een school met twee halfjaartermijnen gebruikt **Semester**; een school met vier gebruikt **Quarter**. "Semester" past niet bij vier delen van één jaar. Voorbeeld: academisch jaar 2026–2027 (type Year) → Periode 1, Periode 2, Periode 3, Periode 4 (type Quarter; elke periode is onderliggend aan het studiejaar).
- Zijn een studiejaar en de onderliggende periodes gekoppeld aan dezelfde instelling (niet Globaal)? Dan kunnen klassen op elke campus van die instelling deze gebruiken. De keuzelijst met periodes bij het aanmaken van een klas filtert niet op campus. Eén gedeelde set periodes is dus bruikbaar voor alle campussen als ze dezelfde kalender volgen.
- **"Schoolweken" kun je momenteel nergens in de beheerinterface instellen**, hoewel de studentenagenda deze waarde gebruikt. Als de waarde ontbreekt, berekent de agenda de periodebreedte op basis van modulegegevens. Dit is een open vraag waarover nog geen besluit is genomen (zie de projectregistratie).

![Dialoogvenster Periode bewerken — onderliggende periode van het type Quarter](../images/Academic/Periode.png)

## Fase 2 — De cursus opbouwen

### Stap 4 — Een cursus aanmaken
- Ga naar: **Cursussen** → Nieuwe cursus.
- Verplicht: alleen **Volledige naam**. Alle andere velden zijn optioneel.
- Velden op het formulier: Volledige naam, Code, Korte code, Niveau (keuzelijst — MBO 1-4, HBO, Associate Degree of niveaus die je instelling zelf heeft ingesteld), Duur, Beschrijving, Status (Draft/Published/Archived), Type inschrijving (Open Enrollment/Invite Only), Studiepunten en Cursuskleur.
- Laat **Status** bij voorkeur op Draft staan totdat de cursus modules en opdrachten bevat (stappen 5–6). Zet de cursus daarna op Published wanneer deze klaar is voor gebruik.
- **Type inschrijving heeft momenteel geen effect.** Er is nog geen aanmeldproces waarmee studenten zichzelf inschrijven; inschrijven gebeurt altijd via een beheerder (zie stap 13). Het veld wordt opgeslagen, maar heeft verder geen werking in de app. Je kunt de standaardwaarde Open Enrollment laten staan, ongeacht hoe je programma in werkelijkheid is ingericht.
- **Instellingen:** er staat een lijst met selectievakjes voor alle instellingen op het platform. De gebruikersinterface maakt geen onderscheid tussen een hoofdinstelling en een partnerinstelling; alle instellingen staan in één lijst en je kunt er meerdere selecteren. Wordt de cursus alleen door je eigen school aangeboden? Selecteer dan alleen je eigen instelling. Gaat het echt om een gezamenlijk programma (zie de opmerking over campussen hierboven)? Selecteer dan je eigen instelling **en** die van de partner. De partner moet eerst als afzonderlijk, minimaal ingericht instellingsrecord zijn aangemaakt om in de lijst te verschijnen.
- **Coördinatoren:** een lijst met selectievakjes voor gebruikers met de rol Coordinator, zodat je toezicht op programmaniveau aan deze cursus kunt toewijzen.
- Sla op.

![Formulier Nieuwe cursus](../images/Academic/Course.png)

### Stap 5 — Modules aanmaken
- Ga naar: **Modules** → Nieuwe module.
- Verplicht: **Modulenaam** en **Duur (weken)**. Op het formulier heet dit veld "Duration (weeks)" en intern wordt de waarde opgeslagen als `planned_weeks`. Het formulier blokkeert opslaan en toont een melding als Duur leeg is.
- Ook op het formulier: Modulecode, Cursus, Niveau en Beschrijving.
- **Duur (weken) is belangrijk:** deze bepaalt de breedte van de Gantt-balk op het tabblad Rooster voor studenten. Dit is het enige moduleveld dat daadwerkelijk invloed heeft op de studentenweergave.
- Herhaal dit voor elke module in de cursus.

Alles onder het onderdeel Identiteit is nuttig voor planning en communicatie tussen medewerkers, maar **verschijnt momenteel niet in de studentenweergave**. Alleen de naam en code van de module en de echte opdrachten en quizzen (die je apart aanmaakt; zie stap 6) zijn zichtbaar:
- **Thema's:** selecteer bestaande thema's in de keuzelijst of checklist. Hiermee koppel je alleen thema's die al ergens anders zijn aangemaakt (Beheer → Thema's); je kunt vanuit dit formulier geen nieuw thema aanmaken.
- **Moduledoelen:** geven de bedoeling van het curriculumontwerp aan ("wat deze module moet onderwijzen"). Dit zijn uitdrukkelijk niet dezelfde gegevens als de werkelijke, gemeten leeruitkomsten van het platform.
- **Modulestructuur:** een vrij in te vullen weekplanning (Week / Onderwerp / Activiteit / Opbrengst-in te leveren werk) voor eigen gebruik. Deze is **niet gekoppeld aan echte opdrachten**. Als je in de kolom Opbrengst "Opdracht 1" typt, wordt er geen opdracht aangemaakt of gekoppeld. Maak zo nodig apart een echte opdracht die kan worden beoordeeld (stap 6).
- **Beoordeling:** een beschrijvend overzicht (Type / Beschrijving / Weging %) van de beoordeling van een module. Dit wordt momenteel **niet** gebruikt voor de berekening van cijfers in het platform.
- **Verdieping/didactiek:** de onderwijsmethoden voor deze module (college, workshop, practicum enzovoort). Dit is alleen beschrijvend.
- **Bronnen:** koppel lesmateriaal uit de gedeelde bibliotheek aan deze module. Studenten krijgen de bronnen te zien via afzonderlijke bijeenkomsten, een apart en gedetailleerder onderdeel, niet rechtstreeks vanuit deze lijst.

![Bewerkformulier module — van Identiteit tot Bronnen](../images/Academic/module.png)

*(De voorbeeldmodule hierboven bevat demogegevens en geen echt cursusmateriaal.)*

### Stap 6 — Opdrachten aanmaken (voor elke module)
- Ga naar de pagina **Opdrachten** van de module en kies Nieuwe opdracht (de module wordt dan automatisch gekoppeld), of ga naar **Beheer → Opdrachten → Nieuwe opdracht**. Dit algemene formulier vraagt je eerst een cursus en daarna de **Origin Module** in een keuzelijst te selecteren. Dit is de echte koppeling tussen een opdracht en een module (zie de opmerking over Modulestructuur in stap 5).
- Verplicht: **Titel** en **Vakgebied** (vrije tekst, met automatische aanvulsuggesties op basis van eerder gebruikte vakgebieden; er is geen vaste lijst, je kunt een nieuw vakgebied typen).
- Status: schakelaar Draft/Published bovenaan. Studenten zien alleen gepubliceerde opdrachten.
- **Details:** Titel, Vakgebied, Cursus, Origin Module, Beschrijving, Doelen, Instructies en Casus.
- **Beoordeling:** Punten, Opdrachten­groep (categorie, bijvoorbeeld "Wekelijkse opdrachten"), Cijfer weergeven als (punten/percentage/lettercijfer) en **Rubric**. Koppel hier een of meer echte rubrics als je beoordelingscriteria nodig hebt.
- **Inzending:** Deadline, Beschikbaar vanaf/tot en toegestane inzendmethoden (tekst, website-URL, mediaopname, studentannotatie of bestanden uploaden; kies er een of meer), plus het aantal pogingen.
- **Samenwerken en peerreview:** stel de opdracht desgewenst in als groepsopdracht (de hele groep krijgt dezelfde beoordeling) of laat studenten elkaars werk beoordelen.
- **Bronnen:** koppel lesmateriaal uit de gedeelde bibliotheek, op dezelfde manier als bij Bronnen van een module.
- **Reflectie** (optioneel): vragen die een student na het indienen beantwoordt. Dit is een apart systeem en mag niet worden samengevoegd met feedback op het onderwijs.

### Stap 7 — Quizzen aanmaken (optioneel, voor elke module)
- Ga naar: **Quizzen** → Nieuwe quiz.
- Voeg vragen toe: meerkeuze (stel het juiste antwoord in!) of open vraag/essay.
- Meerkeuzequizzen worden automatisch beoordeeld na het indienen. Dit werkt alleen als voor elke vraag het juiste antwoord is ingesteld.

## Fase 3 — Het curriculum ontwerpen

### Stap 8 — Curriculum Composer openen
- Ga naar: **Curriculum Composer** → selecteer de cursus.

### Stap 9 — De periodestructuur opbouwen (stap 2 in Composer)
- Maak de hiërarchie aan: Jaar-1 → Periode-1, Periode-2, Periode-3, Periode-4.
- De namen van periodes moeten exact overeenkomen met de periodes in de kalender (bijvoorbeeld "Periode-1"), zodat de planning goed synchroniseert.
- Je kunt ook een template toepassen als er een beschikbaar is.

### Stap 10 — Modules aan periodes toewijzen (stap 3 in Composer)
- Sleep modules uit de bibliotheek naar de juiste periode.
- Stel de beginweek in (week binnen die periode; 1 = eerste schoolweek).
- Het selectievakje "Ook aan actieve klassen toewijzen?" is standaard ingeschakeld. Laat het aan als de klas al bestaat; schakel het uit als je de modules later handmatig wilt toewijzen.
- Je kunt hier ook modules uit andere cursussen toevoegen (delen tussen cursussen).

## Fase 4 — De klas instellen

### Stap 11 — Een klas aanmaken
- Ga naar: **Klassen** → Nieuwe klas (of gebruik stap 4 in Curriculum Composer).
- Velden: Naam (bijvoorbeeld WIL-ISE1A - Year-1 BOL4), Code, Periode (koppeling met de periode van het studiejaar), Campus en Type inschrijving.
- Koppel de klas aan een cursus.

### Stap 12 — Modules aan de klas toewijzen
- Ga naar: **Mijn klassen** → [naam van de klas] (klaspagina voor docenten).
- De curriculumblauwdruk stelt modules voor op basis van de cursusstructuur.
- Voeg modules één voor één toe of accepteer de voorgestelde modules.
- Wijs aan elke module een docent toe.
- Sla op.
- **Opmerking:** als je bij stap 10 het selectievakje "Ook aan actieve klassen toewijzen?" hebt gebruikt, staan de modules hier al. In deze stap controleer je de toewijzingen en wijs je docenten toe.

### Stap 13 — Studenten inschrijven
- Ga naar: **Klassen** → [naam van de klas] (pagina Klasdetails).
- Zoek in het paneel Studenten op naam of studentnummer.
- Selecteer studenten en klik op Geselecteerde N studenten inschrijven.
- Stel zo nodig per student het type inschrijving in (BOL, BBL enzovoort).
- Sla de wijzigingen op.

## Fase 5 — De ervaring van studenten

### Wat de student na het inloggen ziet:

#### Tabblad Curriculum
- Selecteert de cursus in de keuzelijst.
- Ziet modules gegroepeerd per academisch jaar → periode (in- en uitklapbaar).
- Elke module toont de bijbehorende opdrachten, de inzendstatus en scores.
- Quizscores worden getoond als X.X / 10.

#### Tabblad Rooster
- Gantt-diagram gegroepeerd per academisch jaar → periode.
- Elke periode toont alleen de eigen schoolweken.
- Modules worden als gekleurde balken getoond vanaf hun week_from.
- Loopt een module door in de volgende periode? Dan staat › in de eerste periode en ‹ vervolg in de volgende.
- Als je op een balk klikt, ga je naar die module op het tabblad Curriculum.

---

## Belangrijke regels

| Regel | Waarom |
|------|-----|
| course_structure = didactische laag | Wat de ontwerper heeft gepland |
| course_timeline = planningslaag | Wanneer het daadwerkelijk plaatsvindt |
| class_modules = uitvoeringslaag | Wat elke klas daadwerkelijk onderwezen krijgt |
| Deze drie worden NIET automatisch gesynchroniseerd | Elke klas kan afwijken van het curriculumontwerp |
| planned_weeks op de module | Bepaalt de breedte van de Gantt-balk |
| school_weeks op de periode | Bepaalt het aantal kolommen in de Gantt |
| correct_answer moet bij meerkeuzevragen zijn ingesteld | Anders wordt de quiz automatisch met 0 beoordeeld |
| Een module verwijderen uit Composer verwijdert deze uit de studentenweergave | Maar NIET uit class_modules — de klas "heeft" de module dan nog steeds |

---

# Sessieoverzicht — 2026-05-28 (technische referentie voor ontwikkelaars)

## Opgeloste fouten
- Op de quizbeoordelingspagina staan nu alle quizzen; alleen meerkeuzequizzen zijn gelabeld als "Automatisch beoordeeld".
- Dubbele studenten in de beoordeling zijn opgelost: per student wordt nu alleen de meest recente inzending getoond.
- Quizscores in het studentencurriculum worden nu correct weergegeven (de meest recente poging per module-item wordt getoond).

## Belangrijke architectuur: `course_timeline` (migratie 0075)
- **course_structure**: didactiek (Composer-interface — volgorde, groepering en hiërarchie van modules)
- **course_timeline**: planning (wanneer modules worden gegeven — academic_period_id, study_year, week_from)
- `school_weeks` toegevoegd aan `academic_periods`.
- Vier echte kalenderperiodes met Nederlandse academische kalenderdatums aangemaakt onder studiejaar 2026–2027.
- `course_timeline` gevuld op basis van bestaande curriculumgegevens.

## Tabblad Rooster voor studenten — volledig vernieuwd
- Academische jaren zijn inklapbare koppen.
- Elke periode toont alleen de eigen schoolweken.
- Modules die meerdere periodes beslaan, lopen visueel door (balken ›/‹).
- Lege periodes blijven zichtbaar om uitloop weer te geven.

## Synchronisatie van Curriculum Composer naar `course_timeline`
- Alle wijzigingen in Composer (verplaatsen, verwijderen) werken `course_timeline` bij.
- Een module verwijderen uit Composer verwijdert deze uit de studentenweergave.

## Modules tussen cursussen delen
- Je kunt via Composer modules uit andere cursussen aan een curriculum toevoegen.
- Selectievakje "Ook aan actieve klassen toewijzen?": ingeschakeld = toewijzen aan alle actieve klassen; uitgeschakeld = alleen opnemen in het ontwerp.

## Architectuurbesluit: leveringsmodel met drie lagen
- **Ontwerpen**: `course_structure` / `course_timeline` (curriculumontwerper)
- **Aanbieden**: `course_module_offerings` (toekomst, fase 4+)
- **Uitvoeren**: `class_modules` (wat elke klas daadwerkelijk onderwezen krijgt)
- Het selectievakje "Ook aan actieve klassen toewijzen?" is een tijdelijke koppeling. Toekomstige versies gebruiken `course_module_offerings` voor flexibelere uitvoering.

**Laatst bijgewerkt:** 2026-07-08
