# Snel aan de slag voor beheerders

Essentiële stappen om ILS voor gebruik op school voor te bereiden.

## 1. Omgeving en geheimen
- Stel de productie-omgevingsvariabelen in (gebruik GEEN `.env`-bestand in Git).
- Wijzig bij het inrichten het JWT-geheim en de wachtwoorden voor SMTP en de database.

## 2. Gebruikers en instellingen
- Maak instellingen, campussen en cursussen aan via **Admin → Institutions**.
- Stel `Mastery Levels` in via **Settings** voordat je leeruitkomsten importeert.

## 3. Rooster en klassen instellen
- Gebruik **Class Setup** om klassen aan te maken en `class_module_teachers` toe te wijzen.
- Maak in **Timetable** roosterregels aan en **Publiceer** de roosters. Gepubliceerde roosters zijn zichtbaar voor docenten en studenten.

## 4. Back-ups en bewaking
- Controleer de automatische back-ups en test het terugzetten op een aparte server.
- Schakel bewaking en foutmeldingen in (Sentry en controles op beschikbaarheid).

## 5. Beveiligingscontrole (voor de pilot)
- HTTPS en HSTS zijn ingeschakeld.
- Inloggen en gevoelige eindpunten zijn beveiligd met snelheidsbeperking.
- Controlelogboeken voor cijfers en aanwezigheid zijn ingeschakeld.
- Toegangscontrole voor downloaden en verwijderen van bestanden is afgedwongen.

## Problemen oplossen en ondersteuning
- Gebruik voor problemen met het exporteren of importeren van gegevens de pagina Admin Tools.
- Controleer bij verdachte toegang de Security Logs en trek sessies in.

**Laatst bijgewerkt:** 2026-07-03
