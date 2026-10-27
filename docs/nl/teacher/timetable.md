# Rooster

Op de roosterpagina zie je ingeplande lessen en bijeenkomsten. Je kunt er sessies beheren.

## Functies

- Roosters per periode en week bekijken
- Gehouden lessen registreren en inhaallessen inplannen

## Recente wijzigingen (juni 2026)

- Verbeteringen in de levenscyclus van roosteritems: de gebruikersinterface ondersteunt nu volledig het inplannen van inhaallessen en het registreren van gehouden lessen. Docenten kunnen registreren dat een les is gehouden en zo nodig een inhaalbijeenkomst toevoegen.

## Problemen oplossen

### Melding "Geen module gekoppeld aan deze bijeenkomst"

**Betekenis:** het systeem kan geen module vinden die aan dit tijdslot is toegewezen. Dit gebeurt meestal in de volgende gevallen:
- inhaallessen zijn aangemaakt voordat er een module aan was toegewezen
- bijeenkomsten zijn gegenereerd voordat de roosterregels waren ingesteld

**Wat kun je doen?**

1. **Sluit het venster van de bijeenkomst** (klik erbuiten of druk op Escape).
2. **Ga naar Roosterregels** (via het roostermenu).
3. **Wijs een module toe** aan het juiste tijdslot of klasrooster.
4. **Klik op "Sessies opnieuw synchroniseren"** om bijeenkomsten opnieuw te genereren met de bijgewerkte regels.
5. **Open de bijeenkomst opnieuw**. De module hoort nu zichtbaar te zijn.

Verschijnen bijeenkomsten nog steeds niet of tonen ze geen module? Neem dan contact op met je systeembeheerder.

## Stapsgewijze uitleg voor docenten

### Je rooster openen (vandaag)

1. Kies **Rooster** in het hoofdmenu voor docenten of open `/teacher/timetable`.
2. Standaard zie je de huidige week en de klassen waaraan je bent toegewezen.
3. Gebruik **Vandaag** of de weekkiezer om naar de gewenste datum te gaan.

### Filteren op klas, periode of week

1. Kies een klas waaraan je lesgeeft in de klassenlijst links.
2. Gebruik de periodeknoppen rechtsboven om een andere onderwijsperiode te bekijken.
3. Gebruik de snelle filters voor dagen van de week om bijvoorbeeld alleen maandag of dinsdag te bekijken.

### Details van een bijeenkomst bekijken

1. Klik op een lesblok in de agenda of in de lijst met bijeenkomsten.
2. Er verschijnt een venster met:
	- naam van de module
	- docent (eigenaar)
	- lokaal
	- aanwezigheidsstatus (als deze is geregistreerd)
	- gekoppelde opdrachten of activiteiten

### Een les registreren als gehouden

1. Open het venster van de les die je hebt gegeven.
2. Klik op **Gegeven registreren** of **Als gehouden markeren**.
3. Voeg desgewenst opmerkingen toe over de behandelde stof.
4. Sla op. De les wordt als gehouden geregistreerd en de opties van Delivery Planner worden beschikbaar (deadlines zijn standaard vier dagen na de lesdatum).

### Een les annuleren

Gebruik dit als een les helemaal niet doorgaat, bijvoorbeeld als studenten die dag deelnemen aan een andere schoolactiviteit. Verwijder de les niet. Door de les te annuleren, blijft deze zichtbaar in de roosterhistorie en wordt de registratie dat de les gepland stond niet gewist. Verwijderen kan ook problemen veroorzaken met de logica voor terugkerende lessen die bijeenkomsten op basis van roosterregels aanmaakt.

1. Open het venster van de les die niet doorgaat.
2. Klik op **Bewerken**.
3. Stel **Status** in op **Geannuleerd**.
4. Vul een korte **reden voor annulering** in (bijvoorbeeld "Studenten doen mee aan een andere activiteit").
5. Sla op.

Na annulering hoeft de aanwezigheid niet meer te worden geregistreerd. De les verschijnt onder het filter **Geannuleerd** in plaats van **Ingepland**.

### Een inhaalbijeenkomst aanmaken

Plan een inhaalbijeenkomst als de klas een extra les nodig heeft.

1. Open het venster van de oorspronkelijke les of ga naar **+ Nieuwe bijeenkomst**.
2. Selecteer **Inhaalbijeenkomst** (of schakel `Is makeup` in).
3. Kies de nieuwe datum, tijd en het lokaal.
4. Wijs indien nodig een module en docent toe.
5. Sla op. De inhaalbijeenkomst verschijnt op die datum in de agenda.

### Een les aanpassen (docent, module of tijd wijzigen)

1. Open het venster van de les.
2. Klik op **Bewerken**.
3. Wijzig de velden (docent, module, lokaal, begin- of eindtijd).
4. Sla op.

Opmerkingen over bewerken:
- Is de aanwezigheid al geregistreerd? Dan worden wijzigingen die de historische verantwoordelijkheid veranderen geblokkeerd. In plaats daarvan kun je een uitzondering aanmaken.

### Bijeenkomsten opnieuw synchroniseren na wijzigingen in roosterregels

Zijn de roosterregels bijgewerkt in het beheergedeelte? Dan moet je de bijeenkomsten mogelijk opnieuw synchroniseren:

1. Sluit eventuele geopende vensters van bijeenkomsten.
2. Ga naar **Roosterregels** (via het roostermenu).
3. Pas de regels aan (wijs een module of docent toe).
4. Klik op **Sessies opnieuw synchroniseren** om bijeenkomsten opnieuw te genereren op basis van de regels.
5. Open bijeenkomsten opnieuw om te controleren of de module en docent zijn toegewezen.

### Snelle acties

- **Naar vandaag gaan**: klik op Vandaag.
- **Filteren op docent**: gebruik het docentfilter als je meerdere klassen begeleidt.
- **Publiceren / publicatie ongedaan maken**: docenten zien alleen gepubliceerde roosters. Neem contact op met de beheerder als je onverwachte bijeenkomsten ziet.

### Veelvoorkomende problemen

- "Bij de les staat geen module": volg de stappen bij Problemen oplossen hierboven.
- "De les staat niet in mijn agenda": controleer of het rooster is gepubliceerd en of je als docent aan de betreffende klas of periode bent toegewezen.
- "De inhaalbijeenkomst ontbreekt": controleer de doeldatum en het klasfilter. Controleer ook of de inhaalbijeenkomst is opgeslagen en niet is geannuleerd.

---

**Laatst bijgewerkt:** 2026-10-01
