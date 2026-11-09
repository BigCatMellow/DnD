# Project brief — The Ashen Road

**Owner:** human player. **Execution:** assistant GM / content editor. **Method:** MAPS_Lean [PROJECT_BOOTSTRAP](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/PROJECT_BOOTSTRAP.md) under its [AGENTS](https://github.com/BigCatMellow/MAPS_Lean/blob/main/AGENTS.md). That method guides work; it grants no additional repository or human authority.

## Verified initial state (2026-11-09)
- `BigCatMellow/DnD` was an empty public repo when the task began; no canon, rulebooks, game engine or saved campaign existed.
- `BigCatMellow/MAPS_Lean` provides a bootstrap method and favors evidence, limited scope, single authorities and verification.
- Public reference options exist: Wizards of the Coast SRD 5.2.1 (CC BY 4.0) and Paizo PF2e Remaster via its official rules links.

## Parent DONE definition
A player can select a prepared level-2 hero, start the first scene in chat, resolve a challenge, fight or negotiate with at least one appropriately scaled opponent, make a consequential choice, save, and resume in a later chat from durable state **without improvised missing core rules**. The GM can locate each rules, world, NPC, monster and scene source with one index hop.

## Authorized scope
Original text-first fantasy campaign; D&D-style d20 core with bounded PF-inspired procedures; initial setting, key factions, local lore, original creatures, structured encounter stats, branching level-2 starter adventure, premade heroes, standardized saves and journal, basic content validation, a staged roadmap. Use a branch/PR for substantive changes. Do not alter MAPS_Lean, import proprietary books wholesale, deploy a service, claim license rights over protected settings, invent player history, or force a narrative outcome.

## Acceptance criteria
1. A single canonical document owns each rule/data family; README and section indexes route readers.
2. Action, movement, hit, save, rest, ability checks, damage, death, spells, level-up and solo balancing are defined.
3. Original location, three factions, supporting NPCs, at least six creatures, and a complete opening mystery with at least two viable resolutions exist.
4. Four valid level-2 pregens are available; their math and resource definitions match the rules.
5. Adventure scenes form a traversable graph; essential clues are recoverable without a single required die success.
6. Initial save is explicitly `not_started`, not a fictitious playthrough.
7. Content validator passes; manual first-scene and encounter dry runs find no blockers.
8. PR is ready for outside review; merging/production acceptance follows review and appropriate repository authority.

## Known risks and responses
- **Hybrid balance:** keep D&D-style combat economy/scale; borrow PF procedures only. Version house rules explicitly.
- **Solo lethality:** start at level 2 with optional low-power ally; cap early enemy action count and provide retreat/negotiation routes.
- **Hallucinated continuity:** journal plus structured state with explicit UNKNOWNs; never claim GitHub save when writes fail.
- **Spoilers:** separate player brief from GM adventure files; only player-known facts enter chat.
- **IP/licensing:** original lore/monsters and concise paraphrased mechanical procedures; source and attribution links in SOURCES.
- **Expansion debt:** use staged roadmap; no promise that a starter is a complete monster manual.

## Verification
Run `python3 tools/validate_content.py`. Then simulate a non-combat and combat resolution using the house rules, check a save/resume roundtrip and check that player-facing text contains no GM-only reveal. An external reviewer should scrutinize solo balance, rules consistency, replayability and hidden-information handling before main-branch merge.
