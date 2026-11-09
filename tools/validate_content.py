#!/usr/bin/env python3
"""Zero-dependency repository consistency check for The Ashen Road."""
import json
from pathlib import Path
from collections import deque

ROOT = Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))
def require(test, message):
    if not test:
        raise AssertionError(message)

def validate():
    creatures = load("bestiary/creatures.json")["creatures"]
    heroes = load("pregens/characters.json")["heroes"]
    adventure = load("adventures/01-vanishing-mile/scenes.json")
    state = load("campaigns/ashen-road/state.json")
    monster_ids = [c["id"] for c in creatures]
    hero_ids = [h["id"] for h in heroes]
    scenes = {s["id"]: s for s in adventure["scenes"]}
    require(len(monster_ids) == len(set(monster_ids)) >= 6, "Need >=6 unique monster IDs")
    require(len(hero_ids) == len(set(hero_ids)) >= 4, "Need >=4 unique hero IDs")
    for mob in creatures:
        require(mob["ac"] >= 1 and mob["hp"] > 0 and mob["speed"] >= 0, f"Bad monster values: {mob['id']}")
        require(mob["attacks"] and all("to_hit" in a and "damage" in a for a in mob["attacks"]), f"Missing attack: {mob['id']}")
        require("goal" in mob and "morale" in mob and "noncombat" in mob, f"Missing behavior: {mob['id']}")
    for h in heroes:
        require(h["level"] == 2 and h["hp_max"] > 0 and h["ac"] >= 10, f"Bad hero values: {h['id']}")
        require(len(h["ability_scores"]) == 6 and h["hit_dice_total"] == h["level"], f"Bad sheet: {h['id']}")
        require(h["attacks"] and h["inventory"], f"Missing loadout: {h['id']}")
        require(h["spell_slots"] >= 0 and isinstance(h["known_spells"], list), f"Bad spell state: {h['id']}")
    require(len(scenes) == len(adventure["scenes"]), "Duplicate scene IDs")
    start = adventure["start_scene"]
    require(start in scenes, "Missing starting scene")
    for sid, scene in scenes.items():
        require(scene["essential_clues"], f"Scene lacks essential information: {sid}")
        require(all(x in scenes for x in scene["exits"]), f"Broken exit: {sid}")
        require(all(x in monster_ids for x in scene["encounter_ids"]), f"Unknown monster: {sid}")
        require(scene.get("ending", False) or scene["exits"], f"Dead-end scene: {sid}")
    seen={start}; queue=deque([start])
    while queue:
        s=queue.popleft()
        for nxt in scenes[s]["exits"]:
            if nxt not in seen:
                seen.add(nxt);queue.append(nxt)
    require(len(seen)==len(scenes), f"Unreachable scenes: {set(scenes)-seen}")
    require(sum(bool(x.get("ending")) for x in scenes.values()) >= 3, "Missing alternate endings")
    require(state["adventure_id"]==adventure["adventure_id"], "Save adventure mismatch")
    require(state["current_scene_id"] in scenes, "Save scene unknown")
    require(state["schema_version"] == adventure["schema_version"], "Schema versions differ")
    require(0 <= state["clocks"]["bell_attention"] <= adventure["clock"]["max"], "Clock out of bounds")
    if state["status"]=="not_started":
        require(state["player_character_id"] is None and state["player"]["hp"] is None, "Setup state falsely claims a character")
        require(not state["roll_log"] and not state["known_clues"], "Setup state falsely claims play")
    else:
        require(state["player_character_id"] in hero_ids, "Invalid chosen hero")
        require(isinstance(state["player"]["hp"], int), "Missing active HP")
    # Reject broken local Markdown file links. URL/anchor-only links are ignored.
    import re
    for md in ROOT.rglob("*.md"):
        for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            href=match.group(1).split("#",1)[0]
            if not href or "://" in href or href.startswith("mailto:"):
                continue
            destination=(md.parent / href).resolve()
            require(destination.is_relative_to(ROOT.resolve()) and destination.exists(),
                    f"Broken link in {md.relative_to(ROOT)}: {href}")
    print(f"PASS: {len(heroes)} heroes, {len(creatures)} monsters, {len(scenes)} reachable scenes; save and links valid")

if __name__ == "__main__":
    validate()
