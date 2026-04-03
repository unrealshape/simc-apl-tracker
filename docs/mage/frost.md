# Mage – Frost

Auto-generated from SimulationCraft APL | Last updated: 2026-04-03 05:09 UTC

Source: `apl/default/mage/frost.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 87
- **Lists:** `precombat`, `default`, `cds`, `ff_aoe`, `ff_st`, `movement`, `ss_aoe`, `ss_st`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `arcane_intellect` | — |
| 2 | `snapshot_stats` | — |
| 3 | `summon_water_elemental` | — |
| 4 | `blizzard` | if=talent.frostfire_bolt\|active_enemies>=4&talent.freezing_rain |
| 5 | `glacial_spike` | — |
| 6 | `frostbolt` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=cds |
| 2 | `run_action_list` | name=ff_aoe,if=talent.frostfire_bolt&active_enemies>=3 |
| 3 | `run_action_list` | name=ff_st,if=talent.frostfire_bolt |
| 4 | `run_action_list` | name=ss_aoe,if=active_enemies>=4 |
| 5 | `run_action_list` | name=ss_st |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=nevermelting_ice_crystal,if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 2 | `use_item` | name=freightrunners_flask,if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 3 | `use_item` | name=vaelgors_final_stare,if=(stat.haste_rating>stat.crit_rating\|stat.versatility_rating>stat.crit_rating)&(time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20) |
| 4 | `potion` | if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<35 |
| 5 | `use_item` | name=vaelgors_final_stare,if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 6 | `use_items` | if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 7 | `blood_fury` | if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 8 | `berserking` | if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 9 | `fireblood` | if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 10 | `ancestral_call` | if=time=0\|talent.frostfire_bolt\|prev_gcd.1.frozen_orb\|prev_gcd.1.ray_of_frost\|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1\|fight_remains<20 |
| 11 | `flurry` | if=talent.frostfire_bolt,line_cd=9999 |
| 12 | `glacial_spike` | if=talent.frostfire_bolt,line_cd=9999 |
| 13 | `flurry` | if=talent.frostfire_bolt,line_cd=9999 |
| 14 | `ray_of_frost` | if=talent.frostfire_bolt,line_cd=9999 |
| 15 | `frozen_orb` | if=talent.frostfire_bolt,line_cd=9999 |
| 16 | `ice_lance` | if=active_enemies<=3&talent.flash_freeze&talent.splinterstorm,line_cd=9999 |
| 17 | `ray_of_frost` | if=active_enemies<=3&talent.splinterstorm,line_cd=9999 |
| 18 | `flurry` | if=active_enemies>=4&talent.wintertide&talent.splinterstorm,line_cd=9999 |
| 19 | `frozen_orb` | if=active_enemies>=4&talent.splinterstorm,line_cd=9999 |
| 20 | `ray_of_frost` | if=active_enemies>=4&talent.splinterstorm,line_cd=9999 |
| 21 | `ray_of_frost` | if=fight_remains<12 |
| 22 | `ice_lance` | if=fight_remains<gcd.max*1.5 |
| 23 | `invoke_external_buff` | name=power_infusion,if=buff.power_infusion.down |

## Action List: `ff_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blizzard` | if=buff.freezing_rain.up |
| 2 | `flurry` | if=buff.brain_freeze.react&buff.thermal_void.down |
| 3 | `frozen_orb` | — |
| 4 | `glacial_spike` | — |
| 5 | `comet_storm` | — |
| 6 | `blizzard` | if=active_enemies>=(5-talent.freezing_rain-talent.freezing_winds)&(cooldown.frozen_orb.remains>12*spell_haste\|!talent.freezing_rain) |
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
| 11 | `blizzard` | if=active_enemies>=5&talent.freezing_winds&talent.freezing_rain |
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
actions.precombat+=/summon_water_elemental
# Frostfire can open with a precast Blizzard against all target counts. Spellslinger AoE starts at 4+, but Blizzard is only cast with Freezing Rain.
actions.precombat+=/blizzard,if=talent.frostfire_bolt|active_enemies>=4&talent.freezing_rain
actions.precombat+=/glacial_spike
actions.precombat+=/frostbolt

# Executed every time the actor is available.
actions=call_action_list,name=cds
# Frostfire AoE starts at 3+ targets.
actions+=/run_action_list,name=ff_aoe,if=talent.frostfire_bolt&active_enemies>=3
actions+=/run_action_list,name=ff_st,if=talent.frostfire_bolt
# Spellslinger AoE starts at 4+ targets.
actions+=/run_action_list,name=ss_aoe,if=active_enemies>=4
actions+=/run_action_list,name=ss_st

# Potion, Items and Racials are used on cd for Frostfire and paired with either Orb or Ray as Spellslinger. Use Haste trinkets always after pot, Crit trinkets always before pot, and Mastery trinkets after pot if crit is your highest stat and before pot otherwise.
actions.cds=use_item,name=nevermelting_ice_crystal,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/use_item,name=freightrunners_flask,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/use_item,name=vaelgors_final_stare,if=(stat.haste_rating>stat.crit_rating|stat.versatility_rating>stat.crit_rating)&(time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20)
actions.cds+=/potion,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<35
actions.cds+=/use_item,name=vaelgors_final_stare,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/use_items,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/blood_fury,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/berserking,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/fireblood,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
actions.cds+=/ancestral_call,if=time=0|talent.frostfire_bolt|prev_gcd.1.frozen_orb|prev_gcd.1.ray_of_frost|debuff.freezing.react<6&cooldown.ray_of_frost.charges>=1|fight_remains<20
# Opener Frostfire
actions.cds+=/flurry,if=talent.frostfire_bolt,line_cd=9999
actions.cds+=/glacial_spike,if=talent.frostfire_bolt,line_cd=9999
actions.cds+=/flurry,if=talent.frostfire_bolt,line_cd=9999
actions.cds+=/ray_of_frost,if=talent.frostfire_bolt,line_cd=9999
actions.cds+=/frozen_orb,if=talent.frostfire_bolt,line_cd=9999
# Opener Spellslinger ST
actions.cds+=/ice_lance,if=active_enemies<=3&talent.flash_freeze&talent.splinterstorm,line_cd=9999
actions.cds+=/ray_of_frost,if=active_enemies<=3&talent.splinterstorm,line_cd=9999
# Opener Spellslinger AoE
actions.cds+=/flurry,if=active_enemies>=4&talent.wintertide&talent.splinterstorm,line_cd=9999
actions.cds+=/frozen_orb,if=active_enemies>=4&talent.splinterstorm,line_cd=9999
actions.cds+=/ray_of_frost,if=active_enemies>=4&talent.splinterstorm,line_cd=9999
# End-Of-Fight Actions
actions.cds+=/ray_of_frost,if=fight_remains<12
actions.cds+=/ice_lance,if=fight_remains<gcd.max*1.5
# Externals
actions.cds+=/invoke_external_buff,name=power_infusion,if=buff.power_infusion.down

actions.ff_aoe=blizzard,if=buff.freezing_rain.up
actions.ff_aoe+=/flurry,if=buff.brain_freeze.react&buff.thermal_void.down
actions.ff_aoe+=/frozen_orb
actions.ff_aoe+=/glacial_spike
actions.ff_aoe+=/comet_storm
actions.ff_aoe+=/blizzard,if=active_enemies>=(5-talent.freezing_rain-talent.freezing_winds)&(cooldown.frozen_orb.remains>12*spell_haste|!talent.freezing_rain)
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
actions.ss_aoe+=/blizzard,if=active_enemies>=5&talent.freezing_winds&talent.freezing_rain
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
```
