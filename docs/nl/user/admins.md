# Beheerdersgids

Documentatie voor systeembeheerders en sitebeheerders: installatie, gegevensuitwisseling, sjablonen, rechten en operationele draaiboeken.

Systeem instellen
- Eerste installatie: volg de stappen in `backend/README` voor de database en server (alleen voor beheerders).

Centrum voor gegevensuitwisseling
- Exporteren: `Data Exchange` → `Export` → selecteer een entiteit (Students, Grades, Outcomes) en een sjabloon.
- Importeren: `Data Exchange` → `Import` → volg de stappen in ImportShell (Upload → Map → Validate → Preview → Confirm). Gebruik de voorbeeldsjablonen in `docs/admin/templates/`.

Rechten
- Rollen: `Teacher`, `Coordinator`, `Admin`. Wijs rollen toe via `Admin` → `Users` → `Manage Roles`.

Back-ups en migraties
- Back-ups: voer volgens planning databaseback-ups uit naar de ingestelde back-upmap. Zie `Internal > Backups` voor de operationele stappen.

Laatst bijgewerkt: 2026-07-08
