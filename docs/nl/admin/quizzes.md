# Quizzen

Gebruik de pagina Quizzen om quizbeoordelingen voor studenten aan te maken en te beheren.

## Wat je kunt doen

Ga in het beheermenu naar **Quizzen** om:

- alle quizzen te bekijken
- quizzen aan te maken
- quizinhoud, vragen en score-instellingen te bewerken
- quizzen te verwijderen of te archiveren

## Pogingen en inzendingen terugsturen

Het aantal quizpogingen wordt bepaald door de instelling `Attempts allowed` in het quizformulier. Docenten kunnen deze waarde verhogen zodat alle studenten extra pogingen krijgen.

Een inzending terugsturen is een afzonderlijke actie per student:

- Een teruggestuurde inzending wordt met feedback naar de student teruggestuurd.
- De teruggestuurde poging verhindert niet dat de student een volgende poging start wanneer die beschikbaar is.
- Pogingsnummers lopen altijd door, ook na terugsturen (`Attempt 1`, `Attempt 2`, `Attempt 3`), zodat de pogingengeschiedenis duidelijk blijft.
- Quizzen met onbeperkte pogingen (`attempts_allowed = -1`) blijven onbeperkt.
- Voor het terugsturen gelden beperkingen: docenten kunnen een inzending alleen terugsturen als de student nog pogingen over heeft. Zo kan een docent geen inzending terugsturen voor een quiz met één poging die daadwerkelijk is opgebruikt.

Voor extra pogingen voor alle studenten moet de docent `Attempts allowed` in het quizformulier verhogen. Heeft één student een extra kans nodig, dan kan de docent de inzending van die student terugsturen.

### Praktische logica voor nieuwe pogingen

- Bij automatisch beoordeelde quizzen kunnen studenten direct opnieuw beginnen zolang ze nog pogingen over hebben.
- Bij quizzen met rubrics of open vragen moet een student met de status `submitted` wachten tot de docent heeft beoordeeld; er wordt dan nog geen knop voor een nieuwe poging getoond.
- Zodra de docent de inzending heeft beoordeeld en/of teruggestuurd, komen nieuwe pogingen beschikbaar als er nog pogingen over zijn.
- Als de student nog pogingen over heeft maar de quiz op beoordeling wacht, moet de UI een duidelijke melding tonen dat een nieuwe poging na beoordeling door de docent beschikbaar is.

## Werkwijze

1. Open Quizzen.
2. Bekijk bestaande quizzen of maak een nieuwe quiz aan.
3. Bewerk de quizinhoud, de volgorde van vragen en de koppeling met leeruitkomsten.
4. Sla de wijzigingen op en controleer of de quiz beschikbaar is voor studenten.

## Quizzen en opdrachten

- Quizzen zijn bedoeld voor meerkeuzevragen (MCQ) en automatisch beoordeelde toetsen.
- Bij quizzen met alleen meerkeuzevragen geldt de quizscore als bewijs voor leeruitkomsten; een rubric is niet nodig.
- Rubrics zijn alleen nodig voor essay- of korte-antwoordvragen.
- Gemengde quizzen kunnen automatisch beoordeelde scores combineren met open vragen die met rubrics worden beoordeeld.


**Laatst bijgewerkt:** 2026-07-08
