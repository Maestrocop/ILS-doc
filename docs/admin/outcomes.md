# Outcomes

Learning outcomes define what students should be able to do after completing a module or assignment. Use the Outcomes page to create and maintain these outcome definitions.

## What you can do

Go to **Outcomes** in the admin menu to:

- View all learning outcomes
- Create new outcome definitions
- Edit outcome descriptions and labels
- Archive outcomes that are no longer in use

## How outcomes work

- Outcomes are assigned to modules and assignments
- Teachers use them to track student mastery
- The system uses them for progress reporting and intelligence panels

## How to duplicate an outcome

Duplicating is useful when you want to create a similar outcome with slight modifications.

### The workflow

1. Open **Outcomes**
2. Find the outcome you want to duplicate
3. Click **Duplicate**
4. The system **opens the copy in Edit mode automatically**

### Why the copy opens in edit mode

When you duplicate an outcome:
- The copy gets an auto-generated name like "LO-IBDK.1-copy" 
- The copy has the same description as the original
- **You almost always want to change something** — the name, description, or both

The system saves time by opening the copy in edit mode immediately. You don't need to find it in the list and click edit again.

### Edit the copy

- **Rename it** — give it a meaningful code or label
- **Update the description** — make it specific to your new context
- **Save** when done

The copy is now a separate outcome that can be assigned to different modules or assignments.

## How to import outcomes from CSV

You can bulk import outcomes using a CSV file. This is useful when you have many outcomes to add from a curriculum document or standards list.

### Prepare your CSV file

Create a `.csv` file with outcomes. The file should have these columns:

| Column | Required | Example |
|--------|----------|---------|
| `code` | Yes | LO-IBDK.3 |
| `friendly_name` | Yes | Strategisch Advies |
| `description` | Yes | De student kan op basis van... |
| `level` | No | Advanced |
| `type` | No | Competency |
| `mastery_threshold` | No | 2 |
| `calculation_method` | No | decaying_average |

**Example CSV:**
```csv
code,friendly_name,description,mastery_threshold,calculation_method
LO-IBDK.3,"Strategisch Advies","De student kan op basis van de confrontatiematrix haalbare, concrete strategische aanbevelingen formuleren.","2","decaying_average"
LO-IBDK.4,"Stakeholder Management","De student kan effectief communiceren met interne en externe stakeholders.","2","decaying_average"
```

### Import the file

1. Go to **Outcomes**
2. Click **Import CSV**
3. Select your CSV file
4. **Preview:** Review the outcomes in the preview table (shows code, friendly_name, description, level, type)
5. **Select Category:** Choose which category these outcomes belong to
6. Click **Import X outcomes**

### What gets imported in Step 1

✅ Imported:
- Outcome code
- Friendly name
- Description
- Level
- Type
- Mastery threshold (points required for mastery)
- Calculation method (e.g., `decaying_average`, `average`)

❌ Not imported yet (Step 2 — future):
- Mastery level definitions (Exemplary, Proficient, Developing, Beginning)

### Mastery levels

The point scale (Exemplary = 3 pts, Proficient = 2 pts, etc.) is defined once globally and applies to all outcomes.

**Set or modify mastery levels separately:**
1. Go to **Settings** → **Mastery Levels**
2. Edit the level definitions, points, and colors
3. Save

All outcomes automatically use this same scale.

### Tips

- **One outcome per row** — each row must have a unique code
- **Descriptions can be long** — wrap them in quotes if they contain commas or line breaks
- **Duplicate check** — if an outcome code already exists, the import will skip that row (no overwrite)
- **Round-trip** — you can export outcomes as CSV from the Outcomes page, modify them, and re-import


**Last updated:** 2026-07-08
