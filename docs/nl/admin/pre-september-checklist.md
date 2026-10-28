# Checklist voor de voorbereiding op september

Status: gebruik deze checklist om de laatste taken vóór de start van het studiejaar in september bij te houden.

Afgerond ✅

- Academische kalender — feestdagen, vakanties en examenperiodes
- Academische periodes — studiejaar 2026–2027 is aangemaakt
- Klassen aangemaakt — WILISE1A enzovoort
- Roosters → bijeenkomsten gegenereerd (rekening houdend met feestdagen)

Huidige stap — Je bent hier

- Studenten inschrijven bij klassen (vereist voordat je kunt beoordelen en Student Cockpit en Classroom Intelligence kunt gebruiken)

Studenten inschrijven

- De backend biedt een beheer-API om studenten in te schrijven:

- POST `/api/classes/:id/students` (alleen beheerder)
- Implementatie: bekijk `ILS-dev/backend/routes/classes.js` (regels ~200–246) voor de SQL en werking. Het eindpunt voegt een rij toe aan `class_enrollments` en gebruikt `ON CONFLICT` om bestaande inschrijvingen opnieuw te activeren.

Voorbeeld (beheertoken vereist):

```bash
curl -X POST "http://localhost:4000/api/classes/123/students" \
  -H "Authorization: Bearer <ADMIN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{"user_id":456}'
```

Inschrijven in bulk (CSV)

Wil je veel studenten tegelijk inschrijven? Maak dan een CSV-bestand en voer de API-aanroepen in een batch uit. Het backend-eindpunt accepteert één `user_id` per aanvraag (`class_id` staat in de URL). Aanbevolen CSV-indeling:

```
user_id
456
457
458
```

PowerShell (Windows) — in bulk inschrijven vanuit `students.csv`:

```powershell
# Set your admin token in an environment variable first
#$env:ADMIN_JWT = '<ADMIN_JWT>'
$csv = Import-Csv -Path "students.csv"
foreach ($row in $csv) {
  $body = @{ user_id = [int]$row.user_id } | ConvertTo-Json
  Invoke-RestMethod -Method Post -Uri "http://localhost:4000/api/classes/123/students" `
    -Headers @{ Authorization = "Bearer $env:ADMIN_JWT"; "Content-Type" = "application/json" } `
    -Body $body
  Start-Sleep -Milliseconds 200
}
```

Bash (Linux / WSL / Git Bash) — eenvoudige lus:

```bash
ADMIN_JWT="<ADMIN_JWT>"
while IFS=, read -r user_id; do
  curl -s -X POST "http://localhost:4000/api/classes/123/students" \
    -H "Authorization: Bearer $ADMIN_JWT" \
    -H "Content-Type: application/json" \
    -d "{\"user_id\":${user_id}}"
  sleep 0.2
done < students.csv
```

Opmerkingen en aandachtspunten

- Vervang `123` door het ID van de doelklas (bijvoorbeeld de ID van `WILISE1A`).
- Heb je alleen e-mailadressen? Zoek dan eerst het `user_id` op. Mogelijk biedt het project een eindpunt om gebruikers op te zoeken; anders gebruik je de beheerinterface.
- Voor sommige klassen dwingt de server exclusiviteit van `enrollment_type` af. Als je een gebruiker probeert in te schrijven die elders al een exclusieve inschrijving heeft, krijg je een `409` met een toelichting.
- Gebruik `DELETE /api/classes/:id/students/:userId` (alleen beheerder) om een student uit te schrijven.
- Wacht steeds even tussen aanvragen om de ontwikkelserver niet te overbelasten.

Opmerkingen en aandachtspunten

- Zonder studenten die zijn ingeschreven, leveren de rest van de werkwijze (inzendingen, beoordelingen, Student Cockpit, Heatmap) geen betekenisvolle resultaten op.
- Het is niet bevestigd of de beheerinterface in `ILS-dev` studenten kan inschrijven. Het servereindpunt bestaat wel; zie de broncodekoppeling hierboven.

Volgende stappen (in deze volgorde)

1. Schrijf studenten in bij klas WILISE1A (je bent hier).
2. Wijs het curriculum (cursussen en modules) toe aan de klas.
3. Wijs docenten toe aan de klas.
4. Zodra de lessen plaatsvinden: registreer dat ze zijn gegeven, maak opdrachten aan, laat studenten werk inleveren en laat docenten dit beoordelen.
5. De leer- en beoordelingslaag (snapshots, Heatmap, Student Cockpit) levert inzichten op zodra er beoordeeld bewijs is verzameld.

Voorstel voor het bewerken van tijdsloten

- Wil je een tijdslot in het rooster (tijd of dag) aanpassen? Bekijk dan het voorgestelde API- en interfaceontwerp in `admin/slot-edit-proposal.md`.

Veiligheid

- Herinnering: wijzig tijdens documentatiewerkzaamheden niet rechtstreeks de broncode van `ILS-dev`. Deze checklist beschrijft de huidige status en voorgestelde wijzigingen.


**Laatst bijgewerkt:** 2026-07-08
