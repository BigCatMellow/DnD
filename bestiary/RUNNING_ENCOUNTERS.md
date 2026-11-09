# Enemy procedures and solo encounter policy

## Scaling, not assumed victory
A level-2 hero with full resources and Pip can plausibly face one moderate enemy. An unsupported low-HP mage might lose to the same enemy; the GM must telegraph dangerous approaches and allow stealth, diplomacy and escape. Do not change enemy numbers after dice are seen.

- **Harmless pressure / tutorial:** one `ash_mite` or one `lantern_wisp`; can be avoided.
- **Standard confrontation:** one `roadknife`, `mire_wolf` or `bell_husk`, with terrain, a negotiation angle or a weakness.
- **Hard finale:** one `gaunt_toller` alone; the nearby bell can be disabled via established interaction, its objective is to protect the bell rather than kill intruders, and it will not chase beyond the tollhouse.
- **Two-foe option:** two `ash_mite` only when hero has room, resources and clear retreat; do **not** add them as surprise reinforcements to an elite fight.
- **No automatic attrition:** a player choosing careful negotiation or a successful bypass need not face a compensating combat.

## Morale and turn procedure
Roll initiative once per encounter. Each foe has one action, movement, and only those special actions in its JSON entry. When bloodied (HP at or below half), roadknives prefer surrender/flee, mire wolves seek a retreat and bell constructs defend their objective. At 0 HP the GM describes defeat appropriate to the player's stated intent; a subdued sentient enemy can remain alive.

## Environment counterplay
At the tollhouse, spending an action to jam the bell lever or a successful DC13 Strength/Investigation action to wedge its striker suppresses the toller's bell peal for the encounter. Failure still identifies the lever but advances `bell_attention`. The toller is not immune to dialogue with a resonant phrase discovered from the essential clues.

## Enemy card requirements
Stats include `id`, `name`, `tier`, `ac`, `hp`, `speed`, `initiative`, `passive_perception`, `attacks`, `abilities`, `goal`, `morale`. An attack includes `to_hit`, `damage`, `range`. Ability descriptions are intentionally compact but must be interpreted through [rules](../rules/INDEX.md).
