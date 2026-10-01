# Using the BSA Review Feature for Other Institutions

The BSA (Bindend Studieadvies) workflow was implemented for Dutch MBO. The good news: the architecture is generic — BSA is a configured instance of the review engine. This document explains how other institutions can use the same feature with different settings.

## Core idea
BSA is not a hardcoded workflow; it's a configuration: local name, binding flag, timing, and policy rules. The review engine enforces the workflow; the definition drives behaviour and labels.

## Example configurations
- Dutch MBO
  - Local name: "BSA"
  - Binding: yes
  - Timing: 9 months
  - Policy: Warning + Intervention + Acknowledgment required
- UK university
  - Local name: "Academic Progress Review"
  - Binding: no
  - Timing: End of year
  - Policy: Meeting only
- US college
  - Local name: "Academic Probation"
  - Binding: yes
  - Timing: Per semester
  - Policy: Faculty recommendation

All institutions share the same four outcome types (continue / continue with conditions / transfer / exit) though labels may differ.

## How to onboard a new school (practical)
1. Admin: Settings → Progression Review Types → Create a new type
   - Set local name, whether the decision is binding, timing, and required policy steps.
2. SLB / coordinator: continue using the SLB dashboard and Student Cockpit as usual — the same workflow applies.
3. Optionally: add institution‑specific labels in UI copy where needed.

## Implementation note (current limitation)
- Definitions are currently global (visible to all institutions). Architecturally the DB has `institution_id` available; the missing piece is a query filter so types are scoped per institution.
- Small change: apply `WHERE institution_id = ?` on the review-type queries and surface types only for the current institution. This is a minor backend change; no UI changes required aside from filtered lists.

**Settings → Progression Review Types**

You'll see the tab with the BSA definition you created. That's where any admin can create a new review type for their institution, set the local name, binding or not, and configure the policy requirements.

The only missing piece is the `institution_id` filter so each school only sees their own definitions — right now all institutions would see each other's types. But that's a one-line fix when you need it.

## Recommendation
- For immediate onboarding, create a new review type that matches the institution's policy and use the existing workflow.
- For multi-tenant correctness, plan the small backend filter update to scope review definitions to `institution_id` before onboarding multiple institutions.

## Notes
- Do NOT change `ILS-dev` from this docs update. This doc describes observed behaviour and recommended fixes only.


**Last updated:** 2026-07-08
