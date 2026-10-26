# Data Exchange (exporteren / importeren / sjablonen)

Overzicht: breid de bestaande pagina `Export Data` uit tot één centrum voor gegevensuitwisseling met drie tabbladen: `Export`, `Import` en `Templates`.

Belangrijke uitgangspunten
- Hergebruik de bestaande exportlijsten; ontwerp de gebruikersinterface voor Export niet opnieuw.
- Bouw een `ImportShell` die het uploaden, koppelen, valideren, bekijken, bevestigen en rapporteren op dezelfde manier laat verlopen.
- Bied voor elke entiteit downloadbare bestanden van het type `Template` en `Example` aan.

Aanbevolen volgorde van tabbladen (voor alle tabbladen gelijk):
- Studenten
- Modules
- Opdrachten
- Leeruitkomsten
- Rubrics
- Cijfers

Export: behoud de huidige functionaliteit.

## Export

Het tabblad Export bevat de bestaande exportlijsten. Gebruik deze snelkoppeling:

<a id="grades"></a>

### Cijfers

Open het tabblad Cijfers om CSV-bestanden met cijfers te exporteren voor de klassen waartoe je toegang hebt.

Import: de eerste ondersteunde imports moeten zijn: leeruitkomsten, modules, opdrachten, rubrics en cijfers. Begin met de import van leeruitkomsten om de shell te valideren.

Templates: bied voor elke entiteit de opties `Download Template` en `Download Example` aan.

Stap Kolommen koppelen: voeg na het uploaden eventueel een stap Map toe voor niet-standaardindelingen (CSV-kolom → ILS-veld). Sla koppelingen op zodat je ze opnieuw kunt gebruiken.

Import rapport: een downloadbaar rapport met de aantallen geïmporteerd, bijgewerkt, overgeslagen en fouten, inclusief details per rij.

Toegang: de pagina is zichtbaar voor alle rollen, maar elke rol ziet alleen de gegevens waartoe die rol toegang heeft. Docenten en coördinatoren komen direct op het tabblad **Cijfers**, omdat dit voor hen de relevantste export is. De keuzelijst voor klassen wordt op de backend gefilterd op basis van de rol (`class_teachers` voor docenten, `coordinator_programs` voor coördinatoren). Docenten en coördinatoren zien maar één modusknop (Export); daarom wordt de rij met de moduswisselaar voor hen verborgen.

Rollenmatrix (wat elke rol ziet):

| Actie / rol | Beheerder | Ontwerper | Coördinator | Docent |
|---|---:|---:|---:|---:|
| Export: studenten | ✓ | — | ✓ (eigen programmaklassen) | — |
| Export: modules/opdrachten/leeruitkomsten/rubrics | ✓ | ✓ | — | — |
| Export: cijfers | ✓ | — | ✓ (eigen programmaklassen) | ✓ (eigen klassen) |
| Export: aanwezigheid | ✓ | — | ✓ (eigen programmaklassen) | ✓ (eigen klassen) |
| Tabblad Import | ✓ | ✓ | — | — |
| Tabblad Templates | ✓ | ✓ | — | — |

Het blok met beperkte toegang is verwijderd. Docenten en coördinatoren komen direct op het tabblad **Cijfers**, omdat dit voor hen de relevantste export is. De keuzelijst voor klassen wordt op de backend al gefilterd op basis van de rol (`class_teachers` voor docenten, `coordinator_programs` voor coördinatoren). Docenten en coördinatoren zien maar één modusknop (Export); daarom wordt de rij met de moduswisselaar helemaal verborgen.

Opmerking over gecombineerde rollen

Heeft een gebruiker zowel de rol `Teacher` als `Designer` (bijvoorbeeld `P. Goen`)? Dan ziet die gebruiker vanwege de rol `Designer` de hulpmiddelen voor het beheren van het curriculum: Export, Import, Templates, Modules, Assignments, Outcomes en Rubrics. `Grades & Submissions` en `Attendance` blijven beperkt tot de weergave voor docenten en tonen alleen de klassen waaraan die gebruiker lesgeeft. De keuzelijst `class` wordt aan de serverkant gefilterd via de relatie `class_teachers` wanneer `isTeacher=true`. De gebruiker ziet daardoor alleen de eigen klas (bijvoorbeeld "BK Jaar 1 — 2025/2026").

Voorbeeld van de verwachte gebruikersinterface voor een docent met de rol designer:

- Tabbladen: `Export | Import | Templates`
- Subcategorieën onder Export: `Modules, Assignments, Outcomes & Frameworks, Rubrics, Grades & Submissions, Attendance`
- Keuzelijst voor klassen: `BK Jaar 1 — 2025/2026` (alleen de eigen klas)
- Acties: `Download CSV` voor de huidige selectie


**Laatst bijgewerkt:** 2026-07-07
