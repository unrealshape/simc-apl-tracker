# Mage – Frost

Auto-generated from SimulationCraft APL | Last updated: 2026-05-02 05:41 UTC

Source: `apl/default/mage/frost.simc`

---

## Overview

- **Action Lists:** 9
- **Total Actions:** 104
- **Lists:** `precombat`, `default`, `cds`, `ff_aoe`, `ff_st`, `movement`, `ss_aoe`, `ss_st`, `ss_tarswap`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `arcane_intellect` | — |
| 2 | `snapshot_stats` | — |
| 3 | `variable` | name=target_swapping,op=reset,default=0 |
| 4 | `summon_water_elemental` | — |
| 5 | `blizzard` | if=active_enemies>=(4-talent.frostfire_bolt)\|talent.freezing_rain\|talent.freezing_winds |
| 6 | `glacial_spike` | — |
| 7 | `frostbolt` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=cds |
| 2 | `run_action_list` | name=ff_aoe,if=talent.frostfire_bolt&active_enemies>=3 |
| 3 | `run_action_list` | name=ff_st,if=talent.frostfire_bolt |
| 4 | `run_action_list` | name=ss_tarswap,if=variable.target_swapping |
| 5 | `run_action_list` | name=ss_aoe,if=active_enemies>=4 |
| 6 | `run_action_list` | name=ss_st |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=ff_trinket_timing,value=talent.frostfire_bolt |
| 2 | `variable` | name=ss_trinket_timing,value=talent.splinterstorm&(time=0\|fight_remains<15\|prev_gcd.1.frozen_orb\|cooldown.ray_of_frost.charges>=1&debuff.freezing.react<6&!buff.fingers_of_frost.react&(icicles<3\|time-action.potion.last_used<25)) |
| 3 | `use_item` | name=nevermelting_ice_crystal,if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 4 | `use_item` | name=freightrunners_flask,if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 5 | `use_item` | name=vaelgors_final_stare,if=(variable.ff_trinket_timing\|variable.ss_trinket_timing)&(stat.haste_rating>stat.crit_rating\|stat.versatility_rating>stat.crit_rating) |
| 6 | `potion` | if=variable.ff_trinket_timing\|variable.ss_trinket_timing\|fight_remains<35 |
| 7 | `use_item` | name=vaelgors_final_stare,if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 8 | `use_items` | — |
| 9 | `blood_fury` | if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 10 | `berserking` | if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 11 | `fireblood` | if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 12 | `ancestral_call` | if=variable.ff_trinket_timing\|variable.ss_trinket_timing |
| 13 | `flurry` | if=active_enemies>=3&talent.wintertide&talent.frostfire_bolt,line_cd=9999 |
| 14 | `ray_of_frost` | if=talent.frostfire_bolt,line_cd=9999 |
| 15 | `flurry` | if=active_enemies>=4&talent.wintertide&talent.splinterstorm&!variable.target_swapping,line_cd=9999 |
| 16 | `flurry` | target_if=min:debuff.freezing.react,if=active_enemies>=4&talent.wintertide&talent.splinterstorm&variable.target_swapping,line_cd=9999 |
| 17 | `frozen_orb` | if=active_enemies>=4&talent.splinterstorm,line_cd=9999 |
| 18 | `ray_of_frost` | if=talent.splinterstorm&!variable.target_swapping,line_cd=9999 |
| 19 | `ray_of_frost` | target_if=min:debuff.freezing.react,if=talent.splinterstorm&variable.target_swapping,line_cd=9999 |
| 20 | `ray_of_frost` | if=fight_remains<12&(!variable.target_swapping\|talent.frostfire_bolt) |
| 21 | `ray_of_frost` | target_if=min:debuff.freezing.react,if=fight_remains<12&variable.target_swapping |
| 22 | `invoke_external_buff` | name=power_infusion,if=buff.power_infusion.down |

## Action List: `ff_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blizzard` | if=buff.freezing_rain.up |
| 2 | `flurry` | if=buff.brain_freeze.react&buff.thermal_void.down |
| 3 | `frozen_orb` | — |
| 4 | `glacial_spike` | — |
| 5 | `comet_storm` | — |
| 6 | `blizzard` | if=active_enemies>=(5-talent.freezing_rain-talent.freezing_winds) |
| 7 | `ice_lance` | if=buff.fingers_of_frost.react |
| 8 | `ice_lance` | if=debuff.freezing.stack>=10 |
| 9 | `flurry` | if=cooldown_react |
| 10 | `ray_of_frost` | if=!buff.frostfire_empowerment.react |
| 11 | `frostbolt` | — |
| 12 | `call_action_list` | name=movement |

## Action List: `ff_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `flurry` | if=buff.brain_freeze.react&buff.thermal_void.down |
| 2 | `frozen_orb` | — |
| 3 | `glacial_spike` | — |
| 4 | `comet_storm` | — |
| 5 | `ice_lance` | if=buff.fingers_of_frost.react |
| 6 | `ice_lance` | if=debuff.freezing.stack>=10 |
| 7 | `flurry` | if=cooldown_react |
| 8 | `ray_of_frost` | if=active_enemies=1\|!buff.frostfire_empowerment.react |
| 9 | `frostbolt` | — |
| 10 | `call_action_list` | name=movement |

## Action List: `movement`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `any_blink` | if=movement.distance>5 |
| 2 | `blizzard` | if=buff.freezing_rain.up |
| 3 | `ice_nova` | if=talent.cone_of_frost |
| 4 | `cone_of_cold` | if=talent.cone_of_frost |
| 5 | `ice_lance` | — |

## Action List: `ss_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `comet_storm` | — |
| 2 | `blizzard` | if=buff.freezing_rain.up |
| 3 | `flurry` | if=buff.brain_freeze.react&buff.thermal_void.down |
| 4 | `ice_lance` | if=buff.fingers_of_frost.react=2 |
| 5 | `frozen_orb` | — |
| 6 | `glacial_spike` | — |
| 7 | `ice_lance` | if=buff.fingers_of_frost.react |
| 8 | `ice_lance` | if=debuff.freezing.react>=6 |
| 9 | `ice_nova` | if=talent.cone_of_frost |
| 10 | `cone_of_cold` | if=talent.cone_of_frost |
| 11 | `blizzard` | if=talent.freezing_winds |
| 12 | `ray_of_frost` | if=icicles<3\|time-action.potion.last_used<25 |
| 13 | `flurry` | if=cooldown_react |
| 14 | `frostbolt` | — |
| 15 | `call_action_list` | name=movement |

## Action List: `ss_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `comet_storm` | — |
| 2 | `flurry` | if=buff.brain_freeze.react&buff.thermal_void.down |
| 3 | `ice_lance` | if=buff.fingers_of_frost.react=2 |
| 4 | `frozen_orb` | — |
| 5 | `glacial_spike` | — |
| 6 | `ice_lance` | if=buff.fingers_of_frost.react |
| 7 | `ice_lance` | if=debuff.freezing.react>=6 |
| 8 | `ray_of_frost` | if=icicles<3\|time-action.potion.last_used<25 |
| 9 | `flurry` | if=cooldown_react |
| 10 | `frostbolt` | — |
| 11 | `call_action_list` | name=movement |

## Action List: `ss_tarswap`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `comet_storm` | — |
| 2 | `blizzard` | target_if=active_enemies>=4&buff.freezing_rain.up |
| 3 | `flurry` | target_if=min:debuff.freezing.react,if=buff.brain_freeze.react&buff.thermal_void.down |
| 4 | `ice_lance` | if=buff.fingers_of_frost.react=2 |
| 5 | `frozen_orb` | — |
| 6 | `glacial_spike` | target_if=min:debuff.freezing.react |
| 7 | `ice_lance` | if=buff.fingers_of_frost.react |
| 8 | `ice_lance` | target_if=min:debuff.freezing.react>=6,if=active_enemies<=2&debuff.freezing.react>=6 |
| 9 | `ice_lance` | target_if=debuff.freezing.react>=6,if=active_enemies>=3 |
| 10 | `ice_nova` | if=active_enemies>=4&talent.cone_of_frost |
| 11 | `cone_of_cold` | if=active_enemies>=4&talent.cone_of_frost |
| 12 | `blizzard` | if=active_enemies>=4&talent.freezing_winds |
| 13 | `ray_of_frost` | target_if=min:debuff.freezing.react,if=icicles<3\|time-action.potion.last_used<25 |
| 14 | `flurry` | target_if=min:debuff.freezing.react,if=cooldown_react |
| 15 | `frostbolt` | target_if=min:debuff.freezing.react |
| 16 | `call_action_list` | name=movement |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=arcane_intellect
actions.precombat+=/snapshot_stats
actions.precombat+=/variable,name=target_swapping,op=reset,default=0
actions.precombat+=/summon_water_elemental
# Precast Blizzard against all targets if you have any of the Blizzard talents. In AoE (3+ for FF, 4+ for SS) Blizzard is always the precast.
actions.precombat+=/blizzard,if=active_enemies>=(4-talent.frostfire_bolt)|talent.freezing_rain|talent.freezing_winds
actions.precombat+=/glacial_spike
actions.precombat+=/frostbolt

# Executed every time the actor is available.
actions=call_action_list,name=cds
# Frostfire AoE starts at 3+ targets.
actions+=/run_action_list,name=ff_aoe,if=talent.frostfire_bolt&active_enemies>=3
actions+=/run_action_list,name=ff_st,if=talent.frostfire_bolt
actions+=/run_action_list,name=ss_tarswap,if=variable.target_swapping
# Spellslinger AoE starts at 4+ targets
actions+=/run_action_list,name=ss_aoe,if=active_enemies>=4
actions+=/run_action_list,name=ss_st

# Potion, Items and Racials are used on cd for Frostfire and paired with either Orb or Ray as Spellslinger.
actions.cds=variable,name=ff_trinket_timing,value=talent.frostfire_bolt
actions.cds+=/variable,name=ss_trinket_timing,value=talent.splinterstorm&(time=0|fight_remains<15|prev_gcd.1.frozen_orb|cooldown.ray_of_frost.charges>=1&debuff.freezing.react<6&!buff.fingers_of_frost.react&(icicles<3|time-action.potion.last_used<25))
# Use Haste trinkets always after pot, Crit trinkets always before pot, and Mastery trinkets after pot if Crit is your highest stat and before pot otherwise.
actions.cds+=/use_item,name=nevermelting_ice_crystal,if=variable.ff_trinket_timing|variable.ss_trinket_timing
actions.cds+=/use_item,name=freightrunners_flask,if=variable.ff_trinket_timing|variable.ss_trinket_timing
actions.cds+=/use_item,name=vaelgors_final_stare,if=(variable.ff_trinket_timing|variable.ss_trinket_timing)&(stat.haste_rating>stat.crit_rating|stat.versatility_rating>stat.crit_rating)
actions.cds+=/potion,if=variable.ff_trinket_timing|variable.ss_trinket_timing|fight_remains<35
actions.cds+=/use_item,name=vaelgors_final_stare,if=variable.ff_trinket_timing|variable.ss_trinket_timing
actions.cds+=/use_items
actions.cds+=/blood_fury,if=variable.ff_trinket_timing|variable.ss_trinket_timing
actions.cds+=/berserking,if=variable.ff_trinket_timing|variable.ss_trinket_timing
actions.cds+=/fireblood,if=variable.ff_trinket_timing|variable.ss_trinket_timing
actions.cds+=/ancestral_call,if=variable.ff_trinket_timing|variable.ss_trinket_timing
# Opener Frostfire
actions.cds+=/flurry,if=active_enemies>=3&talent.wintertide&talent.frostfire_bolt,line_cd=9999
actions.cds+=/ray_of_frost,if=talent.frostfire_bolt,line_cd=9999
# Opener Spellslinger
actions.cds+=/flurry,if=active_enemies>=4&talent.wintertide&talent.splinterstorm&!variable.target_swapping,line_cd=9999
actions.cds+=/flurry,target_if=min:debuff.freezing.react,if=active_enemies>=4&talent.wintertide&talent.splinterstorm&variable.target_swapping,line_cd=9999
actions.cds+=/frozen_orb,if=active_enemies>=4&talent.splinterstorm,line_cd=9999
actions.cds+=/ray_of_frost,if=talent.splinterstorm&!variable.target_swapping,line_cd=9999
actions.cds+=/ray_of_frost,target_if=min:debuff.freezing.react,if=talent.splinterstorm&variable.target_swapping,line_cd=9999
# End-Of-Fight Actions
actions.cds+=/ray_of_frost,if=fight_remains<12&(!variable.target_swapping|talent.frostfire_bolt)
actions.cds+=/ray_of_frost,target_if=min:debuff.freezing.react,if=fight_remains<12&variable.target_swapping
# Externals
actions.cds+=/invoke_external_buff,name=power_infusion,if=buff.power_infusion.down

actions.ff_aoe=blizzard,if=buff.freezing_rain.up
actions.ff_aoe+=/flurry,if=buff.brain_freeze.react&buff.thermal_void.down
actions.ff_aoe+=/frozen_orb
actions.ff_aoe+=/glacial_spike
actions.ff_aoe+=/comet_storm
actions.ff_aoe+=/blizzard,if=active_enemies>=(5-talent.freezing_rain-talent.freezing_winds)
actions.ff_aoe+=/ice_lance,if=buff.fingers_of_frost.react
actions.ff_aoe+=/ice_lance,if=debuff.freezing.stack>=10
actions.ff_aoe+=/flurry,if=cooldown_react
actions.ff_aoe+=/ray_of_frost,if=!buff.frostfire_empowerment.react
actions.ff_aoe+=/frostbolt
actions.ff_aoe+=/call_action_list,name=movement

actions.ff_st=flurry,if=buff.brain_freeze.react&buff.thermal_void.down
actions.ff_st+=/frozen_orb
actions.ff_st+=/glacial_spike
actions.ff_st+=/comet_storm
actions.ff_st+=/ice_lance,if=buff.fingers_of_frost.react
actions.ff_st+=/ice_lance,if=debuff.freezing.stack>=10
actions.ff_st+=/flurry,if=cooldown_react
actions.ff_st+=/ray_of_frost,if=active_enemies=1|!buff.frostfire_empowerment.react
actions.ff_st+=/frostbolt
actions.ff_st+=/call_action_list,name=movement

actions.movement=any_blink,if=movement.distance>5
actions.movement+=/blizzard,if=buff.freezing_rain.up
actions.movement+=/ice_nova,if=talent.cone_of_frost
actions.movement+=/cone_of_cold,if=talent.cone_of_frost
actions.movement+=/ice_lance

actions.ss_aoe=comet_storm
actions.ss_aoe+=/blizzard,if=buff.freezing_rain.up
actions.ss_aoe+=/flurry,if=buff.brain_freeze.react&buff.thermal_void.down
actions.ss_aoe+=/ice_lance,if=buff.fingers_of_frost.react=2
actions.ss_aoe+=/frozen_orb
actions.ss_aoe+=/glacial_spike
actions.ss_aoe+=/ice_lance,if=buff.fingers_of_frost.react
actions.ss_aoe+=/ice_lance,if=debuff.freezing.react>=6
actions.ss_aoe+=/ice_nova,if=talent.cone_of_frost
actions.ss_aoe+=/cone_of_cold,if=talent.cone_of_frost
actions.ss_aoe+=/blizzard,if=talent.freezing_winds
actions.ss_aoe+=/ray_of_frost,if=icicles<3|time-action.potion.last_used<25
actions.ss_aoe+=/flurry,if=cooldown_react
actions.ss_aoe+=/frostbolt
actions.ss_aoe+=/call_action_list,name=movement

actions.ss_st=comet_storm
actions.ss_st+=/flurry,if=buff.brain_freeze.react&buff.thermal_void.down
actions.ss_st+=/ice_lance,if=buff.fingers_of_frost.react=2
actions.ss_st+=/frozen_orb
actions.ss_st+=/glacial_spike
actions.ss_st+=/ice_lance,if=buff.fingers_of_frost.react
actions.ss_st+=/ice_lance,if=debuff.freezing.react>=6
actions.ss_st+=/ray_of_frost,if=icicles<3|time-action.potion.last_used<25
actions.ss_st+=/flurry,if=cooldown_react
actions.ss_st+=/frostbolt
actions.ss_st+=/call_action_list,name=movement

# Played when the variable target_swapping=1. It's the ST/AoE rotation but always targets the enemy with the lowest Freezing stacks when casting a spell that generates Freezing.
actions.ss_tarswap=comet_storm
actions.ss_tarswap+=/blizzard,target_if=active_enemies>=4&buff.freezing_rain.up
actions.ss_tarswap+=/flurry,target_if=min:debuff.freezing.react,if=buff.brain_freeze.react&buff.thermal_void.down
actions.ss_tarswap+=/ice_lance,if=buff.fingers_of_frost.react=2
actions.ss_tarswap+=/frozen_orb
actions.ss_tarswap+=/glacial_spike,target_if=min:debuff.freezing.react
actions.ss_tarswap+=/ice_lance,if=buff.fingers_of_frost.react
# Against 2 targets, wait for both to have 6+ freezing stacks before casting IL. Against 3+ targets cast IL as soon as any one target has 6+ stacks.
actions.ss_tarswap+=/ice_lance,target_if=min:debuff.freezing.react>=6,if=active_enemies<=2&debuff.freezing.react>=6
actions.ss_tarswap+=/ice_lance,target_if=debuff.freezing.react>=6,if=active_enemies>=3
actions.ss_tarswap+=/ice_nova,if=active_enemies>=4&talent.cone_of_frost
actions.ss_tarswap+=/cone_of_cold,if=active_enemies>=4&talent.cone_of_frost
actions.ss_tarswap+=/blizzard,if=active_enemies>=4&talent.freezing_winds
actions.ss_tarswap+=/ray_of_frost,target_if=min:debuff.freezing.react,if=icicles<3|time-action.potion.last_used<25
actions.ss_tarswap+=/flurry,target_if=min:debuff.freezing.react,if=cooldown_react
actions.ss_tarswap+=/frostbolt,target_if=min:debuff.freezing.react
actions.ss_tarswap+=/call_action_list,name=movement
```
