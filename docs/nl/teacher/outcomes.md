# Leeruitkomsten — docentenhandleiding

Op deze pagina lees je hoe je in ILS met leeruitkomsten werkt: wat labels betekenen, hoe je een leeruitkomst dupliceert en wat docenten moeten weten over CSV-import.

## Een kaart met een leeruitkomst lezen

Wanneer je een leeruitkomst bekijkt, zie je:

- **Code** — korte aanduiding (bijvoorbeeld `LO-IBDK.1`) bovenaan de kaart
- **Beheersing** — de drempel voor beheersing in punten (bijvoorbeeld "Beheersing: 2 punten")
  - Is er geen drempel ingesteld, dan wordt deze regel niet getoond.
  - Betekenis: het aantal punten dat studenten moeten halen om deze leeruitkomst als beheerst te beschouwen.
- **Titel en beschrijving** — wat de leeruitkomst in de praktijk betekent
- **Contextlabels** — leergebied (bijvoorbeeld strategisch management) en niveau (bijvoorbeeld hbo)
- **Trend / gemiddelde** — de huidige trend voor de klas, indien beschikbaar

Waarom dit belangrijk is: docenten gebruiken de beheersingsdrempel als streefwaarde om te bepalen of studenten de beoogde vaardigheid beheersen. De duidelijke aanduiding in de interface voorkomt giswerk.

## Bewijsgeschiedenis (opmerking voor docenten)

Het onderdeel Bewijsgeschiedenis toonde eerder tijdelijke voorbeeldgegevens, zoals "1 students", en kon daardoor misleidend zijn. Het is verwijderd totdat er echte, betrouwbare gegevens uit `student_outcome_snapshots` kunnen worden getoond.

Wil je weten welke studenten op dit moment bewijs voor een leeruitkomst hebben? Gebruik dan de pagina's Grading of Submissions. Daar zie je bewijs dat via rubrics aan een opdracht is gekoppeld.

## Een leeruitkomst dupliceren (aanbevolen werkwijze)

Waarom dupliceren? Je dupliceert meestal een leeruitkomst als je een vergelijkbare leeruitkomst wilt maken en de tekst, beheersingsdrempel of koppeling aan opdrachten wilt aanpassen.

Werkwijze:
1. Zoek op de pagina **Outcomes** de leeruitkomst die je wilt kopiëren.
2. Klik op **Duplicate**.
3. Het systeem opent de kopie direct in de **Edit mode**. Zo hoef je niet nog een keer te klikken.
4. Pas de code, herkenbare naam en beschrijving aan zodat de kopie duidelijk is.
5. Sla de nieuwe leeruitkomst op en wijs deze toe waar nodig.

Opmerkingen:
- De kopie krijgt een tijdelijke naam, bijvoorbeeld `LO-IBDK.1-copy`. Geef deze meteen een andere naam.
- Doordat de kopie in de bewerkingsmodus wordt geopend, verschijnen er geen verwarrende, identieke leeruitkomsten in de lijst.

## CSV-import — wat docenten moeten weten

Beheerders en coördinatoren kunnen leeruitkomsten in bulk importeren via CSV. Houd rekening met het volgende:

- De import is bedoeld om in één keer veel leeruitkomsten toe te voegen, bijvoorbeeld vanuit een curriculum- of normenlijst.
- Ondersteunde kolommen in stap 1: `code`, `friendly_name`, `description`, `level`, `type`, `mastery_threshold`, `calculation_method`.
- **Beheersingsniveaus** (de koppeling tussen punten en labels, zoals Exemplary=3 en Proficient=2) worden niet geïmporteerd in stap 1. De instelling bepaalt de beheersingsniveaus voor de hele instelling. Je stelt ze in via **Settings → Mastery Levels**.
- In het importvoorbeeld zie je een deel van de velden (code, naam, beschrijving, niveau en type). Geavanceerdere velden, zoals `calculation_method`, worden wel geïmporteerd, ook als ze niet in het voorbeeld staan.

Verwacht je na een import door een beheerder een andere schaal voor beheersing? Vraag dan om eerst de beheersingsniveaus in te stellen of de geïmporteerde leeruitkomsten na de import bij te werken.

## Snelle probleemoplossing

- "Ik heb een leeruitkomst gedupliceerd, maar ik zie deze niet": controleer of je de kopie hebt opgeslagen en of deze niet is gearchiveerd. Controleer de filters bij de lijst met leeruitkomsten (Actief / Gearchiveerd).
- "Het beheersingslabel ontbreekt": er is geen drempel ingesteld voor deze leeruitkomst. Open Edit en stel zo nodig `Mastery threshold` in.
- "De bewijsgeschiedenis ontbreekt": dat is bewust. Bekijk Grading of Submissions voor bewijs dat aan opdrachten is gekoppeld.


**Laatst bijgewerkt:** 2026-07-03
