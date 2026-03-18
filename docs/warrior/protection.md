# Warrior – Protection

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:18 UTC

Source: `apl/default/warrior/protection.simc`

---

## Overview

- **Action Lists:** 4
- **Total Actions:** 53
- **Lists:** `precombat`, `default`, `aoe`, `generic`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `battle_stance` | toggle=on |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `charge` | if=time=0 |
| 3 | `use_item` | name=tome_of_lights_devotion,if=buff.inner_resilience.up |
| 4 | `use_items` | — |
| 5 | `avatar` | if=buff.thunder_blast.down\|buff.thunder_blast.stack<=2 |
| 6 | `shield_wall` | if=talent.immovable_object.enabled&buff.avatar.down |
| 7 | `blood_fury` | — |
| 8 | `berserking` | — |
| 9 | `arcane_torrent` | — |
| 10 | `lights_judgment` | — |
| 11 | `fireblood` | — |
| 12 | `ancestral_call` | — |
| 13 | `bag_of_tricks` | — |
| 14 | `potion` | if=buff.avatar.up\|buff.avatar.up&target.health.pct<=20 |
| 15 | `ignore_pain` | if=target.health.pct>=20&(rage.deficit<=15&cooldown.shield_slam.ready\|rage.deficit<=40&cooldown.shield_charge.ready\|rage.deficit<=20&cooldown.shield_charge.ready\|rage.deficit<=30&cooldown.demoralizing_shout.ready&talent.booming_voice.enabled\|rage.deficit<=20&cooldown.avatar.ready\|rage.deficit<=45&cooldown.demoralizing_shout.ready&talent.booming_voice.enabled&buff.last_stand.up&talent.unnerving_focus.enabled\|rage.deficit<=30&cooldown.avatar.ready&buff.last_stand.up&talent.unnerving_focus.enabled\|rage.deficit<=20\|rage.deficit<=40&cooldown.shield_slam.ready&buff.violent_outburst.up&talent.heavy_repercussions.enabled&talent.impenetrable_wall.enabled\|rage.deficit<=55&cooldown.shield_slam.ready&buff.violent_outburst.up&buff.last_stand.up&talent.unnerving_focus.enabled&talent.heavy_repercussions.enabled&talent.impenetrable_wall.enabled\|rage.deficit<=17&cooldown.shield_slam.ready&talent.heavy_repercussions.enabled\|rage.deficit<=18&cooldown.shield_slam.ready&talent.impenetrable_wall.enabled)\|(rage>=70\|buff.seeing_red.stack=7&rage>=35)&cooldown.shield_slam.remains<=1&buff.shield_block.remains>=4&set_bonus.tier31_2pc,use_off_gcd=1 |
| 16 | `last_stand` | if=(target.health.pct>=90&talent.unnerving_focus.enabled\|target.health.pct<=20&talent.unnerving_focus.enabled)\|talent.bolster.enabled\|set_bonus.tier30_2pc\|set_bonus.tier30_4pc |
| 17 | `ravager` | — |
| 18 | `demoralizing_shout` | if=talent.booming_voice.enabled |
| 19 | `champions_spear` | — |
| 20 | `thunder_blast` | if=spell_targets.thunder_blast>=2&buff.thunder_blast.stack=2 |
| 21 | `demolish` | if=buff.colossal_might.stack>=3 |
| 22 | `thunderous_roar` | — |
| 23 | `shield_charge` | — |
| 24 | `shield_block` | if=buff.shield_block.remains<=10 |
| 25 | `run_action_list` | name=aoe,if=spell_targets.thunder_clap>=3 |
| 26 | `call_action_list` | name=generic |

## Action List: `aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `thunder_blast` | if=dot.rend.remains<=1 |
| 2 | `thunder_clap` | if=dot.rend.remains<=1 |
| 3 | `thunder_blast` | if=buff.violent_outburst.up&spell_targets.thunderclap>=2&buff.avatar.up&talent.unstoppable_force.enabled |
| 4 | `execute` | if=spell_targets.execute>=2&(rage>=50\|buff.sudden_death.up)&talent.heavy_handed.enabled |
| 5 | `thunder_clap` | if=buff.violent_outburst.up&spell_targets.thunderclap>=4&buff.avatar.up&talent.unstoppable_force.enabled&talent.crashing_thunder.enabled\|buff.violent_outburst.up&spell_targets.thunderclap>6&buff.avatar.up&talent.unstoppable_force.enabled |
| 6 | `revenge` | if=rage>=70&talent.seismic_reverberation.enabled&spell_targets.revenge>=3 |
| 7 | `shield_slam` | if=rage<=60\|buff.violent_outburst.up&spell_targets.thunderclap<=4&talent.crashing_thunder.enabled |
| 8 | `thunder_blast` | — |
| 9 | `thunder_clap` | — |
| 10 | `revenge` | if=rage>=30\|rage>=40&talent.barbaric_training.enabled |

## Action List: `generic`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `thunder_blast` | if=(buff.thunder_blast.stack=2&buff.burst_of_power.stack<=1&buff.avatar.up&talent.unstoppable_force.enabled) |
| 2 | `shield_slam` | if=(buff.burst_of_power.stack=2&buff.thunder_blast.stack<=1\|buff.violent_outburst.up)\|rage<=70&talent.demolish.enabled |
| 3 | `execute` | if=rage>=70\|(rage>=40&cooldown.shield_slam.remains&talent.demolish.enabled\|rage>=50&cooldown.shield_slam.remains)\|buff.sudden_death.up&talent.sudden_death.enabled |
| 4 | `shield_slam` | — |
| 5 | `thunder_blast` | if=dot.rend.remains<=2&buff.violent_outburst.down |
| 6 | `thunder_blast` | — |
| 7 | `thunder_clap` | if=dot.rend.remains<=2&buff.violent_outburst.down |
| 8 | `thunder_blast` | if=(spell_targets.thunder_clap>1\|cooldown.shield_slam.remains&!buff.violent_outburst.up) |
| 9 | `thunder_clap` | if=(spell_targets.thunder_clap>1\|cooldown.shield_slam.remains&!buff.violent_outburst.up) |
| 10 | `revenge` | if=(rage>=80&target.health.pct>20\|buff.revenge.up&target.health.pct<=20&rage<=18&cooldown.shield_slam.remains\|buff.revenge.up&target.health.pct>20)\|(rage>=80&target.health.pct>35\|buff.revenge.up&target.health.pct<=35&rage<=18&cooldown.shield_slam.remains\|buff.revenge.up&target.health.pct>35)&talent.massacre.enabled |
| 11 | `execute` | — |
| 12 | `revenge` | — |
| 13 | `thunder_blast` | if=(spell_targets.thunder_clap>=1\|cooldown.shield_slam.remains&buff.violent_outburst.up) |
| 14 | `thunder_clap` | if=(spell_targets.thunder_clap>=1\|cooldown.shield_slam.remains&buff.violent_outburst.up) |
| 15 | `devastate` | — |

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

# Executed every time the actor is available.
actions=auto_attack
actions+=/charge,if=time=0
actions+=/use_item,name=tome_of_lights_devotion,if=buff.inner_resilience.up
actions+=/use_items
actions+=/avatar,if=buff.thunder_blast.down|buff.thunder_blast.stack<=2
actions+=/shield_wall,if=talent.immovable_object.enabled&buff.avatar.down
actions+=/blood_fury
actions+=/berserking
actions+=/arcane_torrent
actions+=/lights_judgment
actions+=/fireblood
actions+=/ancestral_call
actions+=/bag_of_tricks
actions+=/potion,if=buff.avatar.up|buff.avatar.up&target.health.pct<=20
actions+=/ignore_pain,if=target.health.pct>=20&(rage.deficit<=15&cooldown.shield_slam.ready|rage.deficit<=40&cooldown.shield_charge.ready|rage.deficit<=20&cooldown.shield_charge.ready|rage.deficit<=30&cooldown.demoralizing_shout.ready&talent.booming_voice.enabled|rage.deficit<=20&cooldown.avatar.ready|rage.deficit<=45&cooldown.demoralizing_shout.ready&talent.booming_voice.enabled&buff.last_stand.up&talent.unnerving_focus.enabled|rage.deficit<=30&cooldown.avatar.ready&buff.last_stand.up&talent.unnerving_focus.enabled|rage.deficit<=20|rage.deficit<=40&cooldown.shield_slam.ready&buff.violent_outburst.up&talent.heavy_repercussions.enabled&talent.impenetrable_wall.enabled|rage.deficit<=55&cooldown.shield_slam.ready&buff.violent_outburst.up&buff.last_stand.up&talent.unnerving_focus.enabled&talent.heavy_repercussions.enabled&talent.impenetrable_wall.enabled|rage.deficit<=17&cooldown.shield_slam.ready&talent.heavy_repercussions.enabled|rage.deficit<=18&cooldown.shield_slam.ready&talent.impenetrable_wall.enabled)|(rage>=70|buff.seeing_red.stack=7&rage>=35)&cooldown.shield_slam.remains<=1&buff.shield_block.remains>=4&set_bonus.tier31_2pc,use_off_gcd=1
actions+=/last_stand,if=(target.health.pct>=90&talent.unnerving_focus.enabled|target.health.pct<=20&talent.unnerving_focus.enabled)|talent.bolster.enabled|set_bonus.tier30_2pc|set_bonus.tier30_4pc
actions+=/ravager
actions+=/demoralizing_shout,if=talent.booming_voice.enabled
actions+=/champions_spear
actions+=/thunder_blast,if=spell_targets.thunder_blast>=2&buff.thunder_blast.stack=2
actions+=/demolish,if=buff.colossal_might.stack>=3
actions+=/thunderous_roar
actions+=/shield_charge
actions+=/shield_block,if=buff.shield_block.remains<=10
actions+=/run_action_list,name=aoe,if=spell_targets.thunder_clap>=3
actions+=/call_action_list,name=generic

actions.aoe=thunder_blast,if=dot.rend.remains<=1
actions.aoe+=/thunder_clap,if=dot.rend.remains<=1
actions.aoe+=/thunder_blast,if=buff.violent_outburst.up&spell_targets.thunderclap>=2&buff.avatar.up&talent.unstoppable_force.enabled
actions.aoe+=/execute,if=spell_targets.execute>=2&(rage>=50|buff.sudden_death.up)&talent.heavy_handed.enabled
actions.aoe+=/thunder_clap,if=buff.violent_outburst.up&spell_targets.thunderclap>=4&buff.avatar.up&talent.unstoppable_force.enabled&talent.crashing_thunder.enabled|buff.violent_outburst.up&spell_targets.thunderclap>6&buff.avatar.up&talent.unstoppable_force.enabled
actions.aoe+=/revenge,if=rage>=70&talent.seismic_reverberation.enabled&spell_targets.revenge>=3
actions.aoe+=/shield_slam,if=rage<=60|buff.violent_outburst.up&spell_targets.thunderclap<=4&talent.crashing_thunder.enabled
actions.aoe+=/thunder_blast
actions.aoe+=/thunder_clap
actions.aoe+=/revenge,if=rage>=30|rage>=40&talent.barbaric_training.enabled

actions.generic=thunder_blast,if=(buff.thunder_blast.stack=2&buff.burst_of_power.stack<=1&buff.avatar.up&talent.unstoppable_force.enabled)
actions.generic+=/shield_slam,if=(buff.burst_of_power.stack=2&buff.thunder_blast.stack<=1|buff.violent_outburst.up)|rage<=70&talent.demolish.enabled
actions.generic+=/execute,if=rage>=70|(rage>=40&cooldown.shield_slam.remains&talent.demolish.enabled|rage>=50&cooldown.shield_slam.remains)|buff.sudden_death.up&talent.sudden_death.enabled
actions.generic+=/shield_slam
actions.generic+=/thunder_blast,if=dot.rend.remains<=2&buff.violent_outburst.down
actions.generic+=/thunder_blast
actions.generic+=/thunder_clap,if=dot.rend.remains<=2&buff.violent_outburst.down
actions.generic+=/thunder_blast,if=(spell_targets.thunder_clap>1|cooldown.shield_slam.remains&!buff.violent_outburst.up)
actions.generic+=/thunder_clap,if=(spell_targets.thunder_clap>1|cooldown.shield_slam.remains&!buff.violent_outburst.up)
actions.generic+=/revenge,if=(rage>=80&target.health.pct>20|buff.revenge.up&target.health.pct<=20&rage<=18&cooldown.shield_slam.remains|buff.revenge.up&target.health.pct>20)|(rage>=80&target.health.pct>35|buff.revenge.up&target.health.pct<=35&rage<=18&cooldown.shield_slam.remains|buff.revenge.up&target.health.pct>35)&talent.massacre.enabled
actions.generic+=/execute
actions.generic+=/revenge
actions.generic+=/thunder_blast,if=(spell_targets.thunder_clap>=1|cooldown.shield_slam.remains&buff.violent_outburst.up)
actions.generic+=/thunder_clap,if=(spell_targets.thunder_clap>=1|cooldown.shield_slam.remains&buff.violent_outburst.up)
actions.generic+=/devastate
```
