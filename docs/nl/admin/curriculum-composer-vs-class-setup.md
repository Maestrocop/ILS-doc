# Curriculum Composer V2 tegenover Klas instellen (advies voor beheerders)

Op deze pagina lees je het verschil tussen Curriculum Composer V2 (wizard) en de eenvoudigere pagina Klas instellen. Ook vind je aanbevolen werkwijzen voor beheerders.

## Samenvatting

- Curriculum Composer V2 (`/admin/curriculum-v2/:courseId`) is de standaardwizard met een vaste structuur voor de eerste inrichting van een curriculum. Werkwijze: cursus → periodes → modules → klassen → controleren.
- Klas instellen (`/admin/classes/:classId`) is bedoeld voor snelle, eenmalige aanpassingen ("Snel toevoegen"). Het is geen vervanging voor Composer.

## Waarom zijn er beide?

- Composer V2 dwingt het volledige curriculummodel af en wordt aanbevolen voor de eerste inrichting en het in bulk toewijzen van modules.
- Klas instellen is bedoeld om snel één module toe te voegen of te verwijderen of docenten opnieuw toe te wijzen, zonder de volledige wizard opnieuw te doorlopen.

## Aanbevolen beleid voor beheerders

1. Gebruik Curriculum Composer V2 voor de eerste inrichting van het curriculum en wanneer je meerdere modules toevoegt of opnieuw ordent.
2. Gebruik Klas instellen alleen voor operationele aanpassingen (één module toevoegen of verwijderen, of een docent opnieuw toewijzen) nadat het curriculum is ingericht.
3. Voeg bovenaan de pagina Klas instellen een korte tip toe die beheerders voor de volledige inrichting naar Composer verwijst (zie het voorstel hieronder).

## De 10 HRD-modules aan klas 18 koppelen

Optie A — standaard (aanbevolen): Curriculum Composer V2

1. Open `/admin/curriculum-v2/<courseId>` (selecteer de juiste cursus).
2. Ga naar stap 3 — Modules: voeg modules 12 tot en met 21 toe (Inleiding Bedrijfskunde → Ondernemen).
3. Ga naar stap 4 — Klassen: wijs de ingestelde moduleset toe aan klas 18.
4. Controleer en sla op.

Optie B — Snel toevoegen (voor een snelle operationele wijziging)

1. Open `/admin/classes/18`.
2. Ga naar het tabblad Curriculum → klik op **+ Module handmatig toevoegen…**.
3. Voeg de modules één voor één toe: 12, 13, 14, …, 21.
4. Sla op.

## Voorstel voor tekst in de gebruikersinterface (voor ontwikkelaars/product)

Voeg bovenaan het tabblad Curriculum van Klas instellen de volgende melding toe:


Voeg een kleine link naar `/admin/curriculum-v2/` toe met de knoptekst: **Curriculum Composer openen**.

### Exacte tekst en code voor de interface (klaar voor ontwikkelaars)

Tekst (kort):

"Tip: Gebruik Curriculum Composer voor de volledige inrichting van het curriculum → Op deze pagina kun je na de inrichting snel één module aanpassen."

Knoptekst: `Open Curriculum Composer`

Voorgesteld HTML/Tailwind-fragment (plaats bovenaan het tabblad Curriculum):

<div class="bg-blue-50 border-l-4 border-blue-400 p-3 rounded-md mb-4">
	<div class="flex items-start gap-3">
		<svg class="w-5 h-5 text-blue-500 mt-0.5" fill="currentColor" viewBox="0 0 20 20"><path d="M9 12l2-2 4 4-1 1-3-3-1 1-1-1z"/></svg>
		<div>
			<p class="text-sm text-slate-800">Tip: For full curriculum setup use the <strong>Curriculum Composer</strong>. This page is a quick-add for single-module changes.</p>
			<a href="/admin/curriculum-v2/" class="inline-block mt-2 text-sm text-blue-600 hover:underline">Open Curriculum Composer</a>
		</div>
	</div>
</div>

Opmerkingen voor ontwikkelaars:

- Plaats het fragment bovenaan het tabblad Curriculum, boven de modulelijst.
- Je kunt de link eventueel uitbreiden met de ID van de huidige cursus: `/admin/curriculum-v2/${courseId}`.
- Houd de tekst kort en neutraal. De melding moet richting geven, niet blokkeren.


## Vervolgacties voor de documentatie

- Voeg op de indexpagina van de Admin Guide een korte verwijzing naar deze pagina toe.
- Overweeg een beknopt script voor het in bulk toevoegen van modules (hulpmiddel voor ontwikkelaars/beheerders), maar alleen als dit via de gebruikersinterface te langzaam gaat.


**Laatst bijgewerkt:** 2026-07-08
