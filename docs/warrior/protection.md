# Warrior – Protection

Auto-generated from SimulationCraft APL | Last updated: 2026-09-25 08:42 UTC

Source: `apl/default/warrior/protection.simc`

---

## Overview

- **Action Lists:** 7
- **Total Actions:** 71
- **Lists:** `precombat`, `default`, `colossus_aoe`, `colossus_st`, `thane_aoe`, `thane_st`, `variables`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `battle_stance` | toggle=on |
| 3 | `use_item` | name=algethar_puzzle_box |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `call_action_list` | name=variables |
| 3 | `charge` | if=time=0 |
| 4 | `use_item` | name=tome_of_lights_devotion,if=buff.inner_resilience.up |
| 5 | `use_items` | — |
| 6 | `avatar` | if=buff.thunder_blast.down\|buff.thunder_blast.stack<=2 |
| 7 | `shield_wall` | — |
| 8 | `blood_fury` | — |
| 9 | `berserking` | — |
| 10 | `arcane_torrent` | — |
| 11 | `lights_judgment` | — |
| 12 | `fireblood` | — |
| 13 | `ancestral_call` | — |
| 14 | `bag_of_tricks` | — |
| 15 | `potion` | if=buff.avatar.up\|buff.avatar.up&target.health.pct<=20 |
| 16 | `ignore_pain` | if=target.health.pct>=20&(rage.deficit<=15&cooldown.shield_slam.ready\|rage.deficit<=20&cooldown.shield_charge.ready\|rage.deficit<=20&cooldown.demoralizing_shout.ready&talent.booming_voice.enabled\|rage.deficit<=15\|rage.deficit<=40&cooldown.shield_slam.ready&buff.violent_outburst.up&talent.heavy_repercussions.enabled&talent.practiced_strikes.enabled\|rage.deficit<=17&cooldown.shield_slam.ready&talent.heavy_repercussions.enabled\|rage.deficit<=18&cooldown.shield_slam.ready&talent.practiced_strikes.enabled)\|(rage>=70\|buff.seeing_red.stack=7&rage>=35)&cooldown.shield_slam.remains<=1&buff.shield_block.remains,use_off_gcd=1 |
| 17 | `ravager` | — |
| 18 | `thunder_blast` | if=talent.booming_voice.enabled&buff.thunder_blast.stack=2&talent.snap_induction.enabled |
| 19 | `demoralizing_shout` | if=talent.booming_voice.enabled |
| 20 | `champions_leap` | — |
| 21 | `champions_spear` | — |
| 22 | `thunder_blast` | if=spell_targets.thunder_blast>=2&buff.thunder_blast.stack=2 |
| 23 | `demolish` | if=buff.colossal_might.stack>=3 |
| 24 | `shield_charge` | — |
| 25 | `shield_block` | if=buff.shield_block.remains<=10 |
| 26 | `run_action_list` | name=colossus_aoe,if=hero_tree.colossus&spell_targets.thunder_clap>=3 |
| 27 | `run_action_list` | name=thane_aoe,if=hero_tree.mountain_thane&spell_targets.thunder_clap>=3 |
| 28 | `run_action_list` | name=colossus_st,if=talent.demolish |
| 29 | `run_action_list` | name=thane_st,if=talent.lightning_strikes |

## Action List: `colossus_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `thunder_clap` | if=buff.ravager.up&!dot.rend_dot.ticking |
| 2 | `revenge` | if=buff.revenge.up |
| 3 | `shield_slam` | if=buff.phalanx.up&(buff.violent_outburst.up\|rage<30) |
| 4 | `thunder_clap` | if=rage<30 |
| 5 | `revenge` | if=spell_targets.revenge>=3 |
| 6 | `shield_slam` | — |
| 7 | `thunder_clap` | — |
| 8 | `revenge` | if=rage>=30 |
| 9 | `execute` | if=spell_targets.execute>=2&(rage>=50\|buff.sudden_death.up)&talent.heavy_handed.enabled |

## Action List: `colossus_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `shield_slam` | — |
| 2 | `thunder_clap` | if=!buff.phalanx.up |
| 3 | `execute` | — |
| 4 | `revenge` | if=buff.revenge.up |
| 5 | `thunder_clap` | — |
| 6 | `revenge` | — |
| 7 | `thunder_clap` | if=(spell_targets.thunder_clap>=1\|cooldown.shield_slam.remains)&hero_tree.mountain_thane&rage<=80 |
| 8 | `revenge` | if=rage>=80&!variable.execute_phase\|buff.revenge.up&variable.execute_phase&rage<=18&cooldown.shield_slam.remains\|buff.revenge.up&!variable.execute_phase |
| 9 | `wrecking_throw` | if=talent.javelineer.enabled |
| 10 | `shattering_throw` | if=talent.javelineer.enabled |
| 11 | `devastate` | — |
| 12 | `thunder_clap` | if=!buff.phalanx.up |

## Action List: `thane_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `thunder_blast` | — |
| 2 | `shield_slam` | if=buff.phalanx.up |
| 3 | `thunder_clap` | — |
| 4 | `revenge` | if=buff.revenge.up |
| 5 | `shield_slam` | — |
| 6 | `revenge` | — |
| 7 | `execute` | if=spell_targets.execute=3&(rage>=50\|buff.sudden_death.up)&talent.heavy_handed.enabled |

## Action List: `thane_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `thunder_blast` | — |
| 2 | `shield_slam` | — |
| 3 | `execute` | — |
| 4 | `revenge` | if=buff.revenge.up |
| 5 | `thunder_clap` | — |
| 6 | `thunder_blast` | if=(spell_targets.thunder_clap>=1\|cooldown.shield_slam.remains) |
| 7 | `wrecking_throw` | if=talent.javelineer.enabled |
| 8 | `shattering_throw` | if=talent.javelineer.enabled |
| 9 | `revenge` | — |
| 10 | `devastate` | — |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=execute_phase,value=(talent.massacre.enabled&target.health.pct<35)\|target.health.pct<20 |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=snapshot_stats
actions.precombat+=/battle_stance,toggle=on
actions.precombat+=/use_item,name=algethar_puzzle_box

# Executed every time the actor is available.
actions=auto_attack
actions+=/call_action_list,name=variables
actions+=/charge,if=time=0
actions+=/use_item,name=tome_of_lights_devotion,if=buff.inner_resilience.up
actions+=/use_items
actions+=/avatar,if=buff.thunder_blast.down|buff.thunder_blast.stack<=2
actions+=/shield_wall
actions+=/blood_fury
actions+=/berserking
actions+=/arcane_torrent
actions+=/lights_judgment
actions+=/fireblood
actions+=/ancestral_call
actions+=/bag_of_tricks
actions+=/potion,if=buff.avatar.up|buff.avatar.up&target.health.pct<=20
actions+=/ignore_pain,if=target.health.pct>=20&(rage.deficit<=15&cooldown.shield_slam.ready|rage.deficit<=20&cooldown.shield_charge.ready|rage.deficit<=20&cooldown.demoralizing_shout.ready&talent.booming_voice.enabled|rage.deficit<=15|rage.deficit<=40&cooldown.shield_slam.ready&buff.violent_outburst.up&talent.heavy_repercussions.enabled&talent.practiced_strikes.enabled|rage.deficit<=17&cooldown.shield_slam.ready&talent.heavy_repercussions.enabled|rage.deficit<=18&cooldown.shield_slam.ready&talent.practiced_strikes.enabled)|(rage>=70|buff.seeing_red.stack=7&rage>=35)&cooldown.shield_slam.remains<=1&buff.shield_block.remains,use_off_gcd=1
actions+=/ravager
actions+=/thunder_blast,if=talent.booming_voice.enabled&buff.thunder_blast.stack=2&talent.snap_induction.enabled
actions+=/demoralizing_shout,if=talent.booming_voice.enabled
actions+=/champions_leap
actions+=/champions_spear
actions+=/thunder_blast,if=spell_targets.thunder_blast>=2&buff.thunder_blast.stack=2
actions+=/demolish,if=buff.colossal_might.stack>=3
actions+=/shield_charge
actions+=/shield_block,if=buff.shield_block.remains<=10
actions+=/run_action_list,name=colossus_aoe,if=hero_tree.colossus&spell_targets.thunder_clap>=3
actions+=/run_action_list,name=thane_aoe,if=hero_tree.mountain_thane&spell_targets.thunder_clap>=3
actions+=/run_action_list,name=colossus_st,if=talent.demolish
actions+=/run_action_list,name=thane_st,if=talent.lightning_strikes

actions.colossus_aoe=thunder_clap,if=buff.ravager.up&!dot.rend_dot.ticking
actions.colossus_aoe+=/revenge,if=buff.revenge.up
actions.colossus_aoe+=/shield_slam,if=buff.phalanx.up&(buff.violent_outburst.up|rage<30)
actions.colossus_aoe+=/thunder_clap,if=rage<30
actions.colossus_aoe+=/revenge,if=spell_targets.revenge>=3
actions.colossus_aoe+=/shield_slam
actions.colossus_aoe+=/thunder_clap
actions.colossus_aoe+=/revenge,if=rage>=30
actions.colossus_aoe+=/execute,if=spell_targets.execute>=2&(rage>=50|buff.sudden_death.up)&talent.heavy_handed.enabled

actions.colossus_st=shield_slam
actions.colossus_st+=/thunder_clap,if=!buff.phalanx.up
actions.colossus_st+=/execute
actions.colossus_st+=/revenge,if=buff.revenge.up
actions.colossus_st+=/thunder_clap
actions.colossus_st+=/revenge
actions.colossus_st+=/thunder_clap,if=(spell_targets.thunder_clap>=1|cooldown.shield_slam.remains)&hero_tree.mountain_thane&rage<=80
actions.colossus_st+=/revenge,if=rage>=80&!variable.execute_phase|buff.revenge.up&variable.execute_phase&rage<=18&cooldown.shield_slam.remains|buff.revenge.up&!variable.execute_phase
actions.colossus_st+=/wrecking_throw,if=talent.javelineer.enabled
actions.colossus_st+=/shattering_throw,if=talent.javelineer.enabled
actions.colossus_st+=/devastate
actions.colossus_st+=/thunder_clap,if=!buff.phalanx.up

actions.thane_aoe=thunder_blast
actions.thane_aoe+=/shield_slam,if=buff.phalanx.up
actions.thane_aoe+=/thunder_clap
actions.thane_aoe+=/revenge,if=buff.revenge.up
actions.thane_aoe+=/shield_slam
actions.thane_aoe+=/revenge
actions.thane_aoe+=/execute,if=spell_targets.execute=3&(rage>=50|buff.sudden_death.up)&talent.heavy_handed.enabled

actions.thane_st=thunder_blast
actions.thane_st+=/shield_slam
actions.thane_st+=/execute
actions.thane_st+=/revenge,if=buff.revenge.up
actions.thane_st+=/thunder_clap
actions.thane_st+=/thunder_blast,if=(spell_targets.thunder_clap>=1|cooldown.shield_slam.remains)
actions.thane_st+=/wrecking_throw,if=talent.javelineer.enabled
actions.thane_st+=/shattering_throw,if=talent.javelineer.enabled
actions.thane_st+=/revenge
actions.thane_st+=/devastate

actions.variables=variable,name=execute_phase,value=(talent.massacre.enabled&target.health.pct<35)|target.health.pct<20
```
