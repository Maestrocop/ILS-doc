# Leeruitkomsten

Leeruitkomsten beschrijven wat studenten na een module of opdracht moeten kunnen. Gebruik de pagina Leeruitkomsten om definities aan te maken en te beheren.

## Wat je kunt doen

Ga in het beheermenu naar **Leeruitkomsten** om:

- alle leeruitkomsten te bekijken
- definities van leeruitkomsten aan te maken
- beschrijvingen en labels van leeruitkomsten te bewerken
- leeruitkomsten die niet meer worden gebruikt te archiveren

## Hoe leeruitkomsten werken

- Leeruitkomsten worden aan modules en opdrachten toegewezen.
- Docenten gebruiken ze om de beheersing door studenten te volgen.
- Het systeem gebruikt ze voor voortgangsrapportages en analysepanelen.

## Een leeruitkomst dupliceren

Dupliceren is handig als je een vergelijkbare leeruitkomst met kleine aanpassingen wilt maken.

### Werkwijze

1. Open **Leeruitkomsten**.
2. Zoek de leeruitkomst die je wilt dupliceren.
3. Klik op **Dupliceren**.
4. Het systeem opent de kopie automatisch in de bewerkingsmodus.

### Waarom de kopie in de bewerkingsmodus wordt geopend

Wanneer je een leeruitkomst dupliceert:
- krijgt de kopie een automatisch gegenereerde naam, zoals "LO-IBDK.1-copy"
- heeft de kopie dezelfde beschrijving als het origineel
- **wil je bijna altijd iets aanpassen** — de naam, beschrijving of allebei

Het systeem bespaart tijd door de kopie direct in de bewerkingsmodus te openen. Je hoeft deze niet eerst in de lijst op te zoeken en daarna nogmaals op Bewerken te klikken.

### De kopie bewerken

- **Geef de kopie een nieuwe naam** — kies een duidelijke code of aanduiding.
- **Werk de beschrijving bij** — maak deze specifiek voor de nieuwe context.
- **Sla op** wanneer je klaar bent.

De kopie is nu een afzonderlijke leeruitkomst die je aan andere modules of opdrachten kunt toewijzen.

## Leeruitkomsten importeren vanuit CSV

Je kunt leeruitkomsten in bulk importeren met een CSV-bestand. Dit is handig wanneer je veel leeruitkomsten uit een curriculumdocument of normenlijst wilt toevoegen.

### Het CSV-bestand voorbereiden

Maak een `.csv`-bestand met leeruitkomsten. Het bestand moet de volgende kolommen bevatten:

| Kolom | Verplicht | Voorbeeld |
|--------|----------|---------|
| `code` | Ja | LO-IBDK.3 |
| `friendly_name` | Ja | Strategisch Advies |
| `description` | Ja | De student kan op basis van... |
| `level` | Nee | Advanced |
| `type` | Nee | Competency |
| `mastery_threshold` | Nee | 2 |
| `calculation_method` | Nee | decaying_average |

**Voorbeeld van een CSV-bestand:**
```csv
code,friendly_name,description,mastery_threshold,calculation_method
LO-IBDK.3,"Strategisch Advies","De student kan op basis van de confrontatiematrix haalbare, concrete strategische aanbevelingen formuleren.","2","decaying_average"
LO-IBDK.4,"Stakeholder Management","De student kan effectief communiceren met interne en externe stakeholders.","2","decaying_average"
```

### Het bestand importeren

1. Ga naar **Leeruitkomsten**.
2. Klik op **CSV importeren**.
3. Selecteer je CSV-bestand.
4. **Voorbeeld bekijken:** controleer de leeruitkomsten in de voorbeeldtabel (code, friendly_name, description, level en type).
5. **Categorie selecteren:** kies de categorie waartoe de leeruitkomsten behoren.
6. Klik op **X leeruitkomsten importeren**.

### Wat wordt geïmporteerd in stap 1?

✅ Wordt geïmporteerd:
- code van de leeruitkomst
- herkenbare naam
- beschrijving
- niveau
- type
- beheersingsdrempel (het aantal punten dat nodig is om een leeruitkomst te beheersen)
- berekeningsmethode (bijvoorbeeld `decaying_average` of `average`)

❌ Wordt nog niet geïmporteerd (stap 2 — toekomstig):
- definities van beheersingsniveaus (Exemplary, Proficient, Developing, Beginning)

### Beheersingsniveaus

De puntenschaal (Exemplary = 3 punten, Proficient = 2 punten enzovoort) wordt één keer globaal ingesteld en geldt voor alle leeruitkomsten.

**Beheersingsniveaus instellen of wijzigen:**
1. Ga naar **Settings** → **Mastery Levels**.
2. Bewerk de definities, punten en kleuren van de niveaus.
3. Sla op.

Alle leeruitkomsten gebruiken automatisch dezelfde schaal.

### Tips

- **Eén leeruitkomst per rij** — elke rij moet een unieke code hebben.
- **Beschrijvingen mogen lang zijn** — zet ze tussen aanhalingstekens als ze komma's of regeleinden bevatten.
- **Controleren op duplicaten** — bestaat de code van een leeruitkomst al? Dan slaat de import die rij over en wordt de bestaande leeruitkomst niet overschreven.
- **Rondgang** — je kunt leeruitkomsten vanuit de pagina Leeruitkomsten naar CSV exporteren, bewerken en opnieuw importeren.


**Laatst bijgewerkt:** 2026-07-08
