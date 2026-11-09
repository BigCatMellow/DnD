# GM guide — The Vanishing Mile
**GM-only. Spoilers.** Source of truth for scene motives and consequences; structured IDs and graph: [scenes.json](scenes.json).

## Outcome and constraints
Designed for one **level-2** hero (optional Pip), one main session or two short sessions, 60–150 minutes depending on play. A satisfying conclusion requires finding what happened to Elowen and making or deferring a consequential choice about the tollhouse bell. There is **no mandatory combat** and **no single required skill success**. Never force an ending or rush a player with hidden clocks.

## Behind the veil
The road's old warding bell keeps its distances stable by holding a living memory. A loosened iron seal shifted its resonance into the vanished mile. **Elowen Rusk** found the failing ward and tried to unfasten a trapped memory-plate; they are now alive but tethered to the ringing below the tollhouse. The **Gaunt Toller** is the bell's bound keeper, acting on an old duty, not a simple villain. Warden Ada Vell knows the ward's cost but fears catastrophic road loss. Lio Quill removed the seal while measuring and is ashamed.

Keep this information hidden until earned. Don't invent secretly culpable NPCs after the player forms a theory; established facts stand.

## Scene order is non-linear
`briefing` -> `archive`, `north_gate`, or `reed_track`; branches converge through `milestone` and `wayhouse` to `chamber`. Any described scene can be revisited using the graph. If a plausible shortcut bypasses an edge, adjudicate travel with reasonable cost and note a provisional new edge in the journal.

### 1. Briefing
**Read aloud basis:** use [PLAYER_START](PLAYER_START.md). The keeper is Ada Vell, who offers 15 silver for credible evidence. She warns of fog at dusk and can point to either route. She will not initially disclose the memory toll.
**Leads:** Elowen's name, their route, two paths. No check needed.
**Questions:** Ada admits an old tollhouse on DC13 Insight/Persuasion, but a strong argument or relevant Warden past also works without a roll. On failure she gives useful directions while urging haste.
**Turn:** questioning costs no time unless extended.

### 2. Archive
Orren Fen has four contradicting maps. On inspection, provide the unmarked milestone and toll phrase automatically. A DC13 Investigation/History check reveals the relay sketches and grants the **relay_map** flag; failure still yields the inscription but costs 10 minutes or a promise to bring proof.
Lio Quill can be met here. Gentle but specific questions elicit his moved-marker confession, no compulsory roll. This earns **seal_confession**. Social hostility makes him withdraw, not erase the ability to find the physical marker.

### 3. North gate
Fresh survey boots lead to the wayhouse; the old rut leads to milestone. No roll needed to discover both. A `lantern_wisp` is a possible signal: it attacks only if the hero touches uncovered bell metal or corners it. `ash_mite` can complicate unprotected lanterns. Avoid rolling both into combat. Perception DC13 reveals a note of under-water bell sound, but its absence does not block progression.

### 4. Reed track
The safe stones lead to milestone or wayhouse, clearly marked by reeds of different height. A `mire_wolf` defends its den; give teeth, pawprints and escape options before initiative. It fights only if approached aggressively or trapped. Nessa's boat service may bypass the den after a conversation. Crossing carefully takes 20 minutes, risky direct crossing 10.

### 5. Milestone
The relay grooves match the tollhouse lever, and the toll phrase **'A road is kept by those who return'** can be copied automatically. A DC13 Arcana/Investigation check reveals a potential consequence of redirection (flooded reedland), even on failure with a time cost; never hide this cost until after the irreversible choice. Engraved marks point toward chamber. Obtain **relay_known** and possibly **relay_map** (the latter may also come from physically sketching the relay here, requiring ten minutes, no roll).

### 6. Wayhouse
Elowen's survey cord leads to the lower chamber. A page supplies the toll phrase, the three solution categories and a warning of collateral effects. No check required if the page is examined. A `bell_husk` guards the memory plate but can be stalled with a steady three-beat rhythm on an accessible handbell (the rhythm is revealed by listening for a turn or deciphering the notes). A `roadknife` sheltering upstairs can bargain for food; never force both enemies at once. Elowen's voice may be heard through the floor and supplies a third independent route to the truth.

### 7. Chamber — decision point
The Gaunt Toller protects the large bell. **A direct fight is intentionally dangerous**, especially for Iven or Sera; say so through damaged stone, the keeper's strength and a visible safe retreat before any attack. The mystery does not require combat. Before any roll, reveal visible positions: Toller by the threshold, bell and lever within reach via movement, memory-plate near the wall, exit behind hero. It is willing to state its duty if asked; toll phrase calms it. An action to jam the striker is DC13 Strength or Investigation; after failure the hero identifies the mechanism but incurs one clock segment (retry or another approach). The Toller will not pursue outside the chamber.

**Choices (not exhaustive):**
- **Renew toll (`ending_renew`):** a **voluntary**, explicitly chosen personal memory is surrendered; never select it for the player. The bell stabilizes for the season, Elowen returns, and Warden trust rises. The player may refuse. If no willing offering, this ending is unavailable.
- **Break striker (`ending_break`):** disrupt the mechanism through force, tools or clever positioning. If resisted, use `gaunt_toller` (solo elite) or environmental DC13; repeat failures advance the clock but must not make success impossible. Elowen and stored memories are released; the road wanders and Reedwater Guild gains leverage.
- **Redirect to relay (`ending_relay`):** requires knowledge of the relay and a credible map/grooves (`relay_known` and `relay_map`), or equivalent player-devised proof. Prepare relay outside first or work with Elowen. Two successful DC13 Investigation/Arcana/Survival contributions (one can come from established fictional leverage or Pip's Help); failure yields partial progress but advances one segment. **Tell player before final action** that the redirected road will flood some reedland; Elowen is freed but residents may need help.
- **Retreat (`ending_retreat`):** always possible along the known route; report evidence, recruit help and return. It is a **temporary exit**, not completed campaign resolution.

If the Toller is defeated, the bell choice still belongs to the hero. If a player invents a coherent fourth solution, judge according to causal structure, give known risks and add its result as new canon after resolution.

## Pressure clock `bell_attention` (0/4)
Only advance from explicit noisy failure, failed repeated intervention or provoked bell-guardian response, at most once per distinct action. At four, fog thickens and a return trip takes an extra 10 minutes; tracks blur, but the Reedwater route stays viable. **Never close all exits, erase clues or force combat.** If a rest is taken in safe Briarford, local pressure may reset; physical discoveries remain.

## Rewards / wrap
Credible findings earn **15 silver** from Ada (even if returning without Elowen but with verifiable facts, subject to what Ada actually knows). Endings change faction attitudes: renew raises Warden attitude; break raises Reedwater attitude and lowers Warden attitude; relay raises Survey attitude and produces contested local consequences. No automatic level advancement until level-3 mechanics are authored. Log ending, clue sources, memory offered (if any), NPC status, remaining HP/resources and unresolved leads.

## Solo and safety checklist
A first session should need zero required combats. For a solo mage, telegraph threats, keep Pip optional, and present the exit before boss initiative. Do not treat 'good ending' as synonymous with winning a fight. The player can `pause`, `rewind`, `fade out` or `skip` at any time.
