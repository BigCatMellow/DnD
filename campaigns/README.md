# Campaign state — one active game

- [Active save JSON](ashen-road/state.json): current machine-readable truth for character resources, facts and position.
- [Journal](ashen-road/JOURNAL.md): append-only player-action/roll/consequence ledger.
- [Character status](ashen-road/CHARACTER.md): player-facing sheet **pointer** and editable backstory only; numbers belong to `pregens/characters.json` and live resources to `state.json`.
- [Current adventure](../adventures/INDEX.md): scene definitions; GM-only secrets stay in GM guide, not in player recap.

## Save protocol
After hero selection, copy their canonical HP, hit dice, charges, equipment, silver and spell slots from `pregens/characters.json`. Set `status: active` and `open_decision` to the current pending choice. After each meaningful turn, atomically reconcile state and journal as far as connector permits. Journal must record decisions, dice rolls, resource changes, clue acquisition, and new canon. Never silently reset a game or infer a user decision from a previous scenario template.

If a GitHub update is impossible, output the full updated save in the conversation and say it has **not** been committed; later resume must reconcile the two copies. Public repo saves contain no private personal information.
