# Monk – Mistweaver

Auto-generated from SimulationCraft APL | Last updated: 2026-04-19 05:33 UTC

Source: `apl/default/monk/mistweaver.simc`

---

## Overview

- **Action Lists:** 3
- **Total Actions:** 30
- **Lists:** `precombat`, `default`, `race_actions`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `potion` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `potion` | — |
| 3 | `use_item` | slot=trinket1 |
| 4 | `use_item` | slot=trinket2 |
| 5 | `call_action_list` | name=race_actions |
| 6 | `touch_of_death` | — |
| 7 | `thunder_focus_tea` | — |
| 8 | `invoke_chiji` | if=talent.invokers_delight |
| 9 | `invoke_yulon` | if=talent.invokers_delight |
| 10 | `sheiluns_gift` | if=talent.shaohaos_lessons&(buff.sheiluns_gift.stack>=10\|(buff.sheiluns_gift.stack*4>=fight_remains&buff.sheiluns_gift.stack>=3)\|(fight_style.dungeonslice&buff.sheiluns_gift.stack>=5&active_enemies>=4)) |
| 11 | `celestial_conduit` | — |
| 12 | `rising_sun_kick` | if=talent.secret_infusion&buff.thunder_focus_tea.up |
| 13 | `spinning_crane_kick` | if=buff.dance_of_chiji.up |
| 14 | `chi_burst` | if=active_enemies>=2 |
| 15 | `crackling_jade_lightning` | if=buff.jade_empowerment.up |
| 16 | `jadefire_stomp` | if=active_enemies>=4&active_enemies<=10 |
| 17 | `spinning_crane_kick` | if=active_enemies>=4 |
| 18 | `jadefire_stomp` | if=buff.jadefire_stomp.down |
| 19 | `rising_sun_kick` | if=active_enemies<=2 |
| 20 | `blackout_kick` | if=buff.teachings_of_the_monastery.stack>=3&(active_enemies>=2\|cooldown.rising_sun_kick.remains>gcd) |
| 21 | `tiger_palm` | — |

## Action List: `race_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blood_fury` | — |
| 2 | `berserking` | — |
| 3 | `arcane_torrent` | — |
| 4 | `lights_judgment` | — |
| 5 | `fireblood` | — |
| 6 | `ancestral_call` | — |
| 7 | `bag_of_tricks` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=snapshot_stats
actions.precombat+=/potion

# Executed every time the actor is available.
actions=auto_attack
actions+=/potion
actions+=/use_item,slot=trinket1
actions+=/use_item,slot=trinket2
actions+=/call_action_list,name=race_actions
actions+=/touch_of_death
actions+=/thunder_focus_tea
actions+=/invoke_chiji,if=talent.invokers_delight
actions+=/invoke_yulon,if=talent.invokers_delight
actions+=/sheiluns_gift,if=talent.shaohaos_lessons&(buff.sheiluns_gift.stack>=10|(buff.sheiluns_gift.stack*4>=fight_remains&buff.sheiluns_gift.stack>=3)|(fight_style.dungeonslice&buff.sheiluns_gift.stack>=5&active_enemies>=4))
actions+=/celestial_conduit
actions+=/rising_sun_kick,if=talent.secret_infusion&buff.thunder_focus_tea.up
actions+=/spinning_crane_kick,if=buff.dance_of_chiji.up
actions+=/chi_burst,if=active_enemies>=2
actions+=/crackling_jade_lightning,if=buff.jade_empowerment.up
actions+=/jadefire_stomp,if=active_enemies>=4&active_enemies<=10
actions+=/spinning_crane_kick,if=active_enemies>=4
actions+=/jadefire_stomp,if=buff.jadefire_stomp.down
actions+=/rising_sun_kick,if=active_enemies<=2
actions+=/blackout_kick,if=buff.teachings_of_the_monastery.stack>=3&(active_enemies>=2|cooldown.rising_sun_kick.remains>gcd)
actions+=/tiger_palm

actions.race_actions=blood_fury
actions.race_actions+=/berserking
actions.race_actions+=/arcane_torrent
actions.race_actions+=/lights_judgment
actions.race_actions+=/fireblood
actions.race_actions+=/ancestral_call
actions.race_actions+=/bag_of_tricks
```
