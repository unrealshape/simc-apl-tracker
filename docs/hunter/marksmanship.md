# Hunter – Marksmanship

Auto-generated from SimulationCraft APL | Last updated: 2026-04-08 05:17 UTC

Source: `apl/default/hunter/marksmanship.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 64
- **Lists:** `precombat`, `default`, `cds`, `draoe`, `drst`, `sentaoe`, `sentst`, `trinkets`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `summon_pet` | if=talent.unbreakable_bond |
| 3 | `use_item` | name=algethar_puzzle_box |
| 4 | `aimed_shot` | if=active_enemies<3\|talent.black_arrow&talent.headshot |
| 5 | `steady_shot` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=trueshot_ready,value=!talent.bullseye\|fight_remains>cooldown.trueshot.duration+10\|buff.bullseye.stack=buff.bullseye.max_stack\|fight_remains<25\|time<10 |
| 2 | `auto_shot` | — |
| 3 | `call_action_list` | name=cds |
| 4 | `call_action_list` | name=trinkets |
| 5 | `call_action_list` | name=draoe,if=active_enemies>2&talent.trick_shots&hero_tree.dark_ranger |
| 6 | `call_action_list` | name=sentaoe,if=active_enemies>2&talent.trick_shots&hero_tree.sentinel |
| 7 | `call_action_list` | name=drst,if=hero_tree.dark_ranger |
| 8 | `call_action_list` | name=sentst,if=hero_tree.sentinel |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_external_buff` | name=power_infusion,if=buff.trueshot.remains>12\|fight_remains<13 |
| 2 | `berserking` | if=buff.trueshot.up\|fight_remains<13 |
| 3 | `blood_fury` | if=buff.trueshot.up\|cooldown.trueshot.remains>30\|fight_remains<16 |
| 4 | `ancestral_call` | if=buff.trueshot.up\|cooldown.trueshot.remains>30\|fight_remains<16 |
| 5 | `fireblood` | if=buff.trueshot.up\|cooldown.trueshot.remains>30\|fight_remains<9 |
| 6 | `lights_judgment` | if=buff.trueshot.down |
| 7 | `potion` | if=buff.trueshot.up&(buff.bloodlust.up\|fight_remains<120-30*talent.calling_the_shots)\|fight_remains<31 |

## Action List: `draoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `black_arrow` | — |
| 2 | `multishot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target\|max_prio_damage,if=buff.precise_shots.up&!talent.aspect_of_the_hydra\|buff.trick_shots.down |
| 3 | `rapid_fire` | if=buff.trick_shots.remains>execute_time&(talent.unload&(talent.no_scope&buff.bulletstorm.stack<10\|target.health.pct<20)\|buff.bulletstorm.remains<action.aimed_shot.execute_time) |
| 4 | `trueshot` | if=!buff.double_tap.up&variable.trueshot_ready |
| 5 | `volley` | if=!buff.double_tap.up |
| 6 | `aimed_shot` | target_if=max:debuff.spotters_mark.up\|max_prio_damage,if=buff.trick_shots.remains>cast_time |
| 7 | `wailing_arrow` | — |
| 8 | `rapid_fire` | if=buff.trick_shots.remains>execute_time |
| 9 | `steady_shot` | — |

## Action List: `drst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `black_arrow` | — |
| 2 | `trueshot` | if=!buff.double_tap.up&variable.trueshot_ready |
| 3 | `rapid_fire` | if=talent.unload&(talent.no_scope&buff.bulletstorm.stack<10\|target.health.pct<20) |
| 4 | `aimed_shot` | target_if=max:debuff.sentinels_mark.up\|max_prio_damage,if=buff.volley.remains%action.aimed_shot.execute_time>action.arcane_shot.execute_time&buff.trueshot.down |
| 5 | `arcane_shot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target\|max_prio_damage,if=buff.precise_shots.up |
| 6 | `rapid_fire` | if=buff.bulletstorm.remains<action.aimed_shot.execute_time |
| 7 | `volley` | if=!buff.double_tap.up |
| 8 | `aimed_shot` | target_if=max:debuff.spotters_mark.up\|max_prio_damage |
| 9 | `wailing_arrow` | — |
| 10 | `rapid_fire` | — |
| 11 | `steady_shot` | — |

## Action List: `sentaoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `multishot` | target_if=max:debuff.sentinels_mark.down\|action.aimed_shot.in_flight_to_target,if=buff.precise_shots.up&!talent.aspect_of_the_hydra\|buff.trick_shots.down |
| 2 | `rapid_fire` | if=buff.bulletstorm.remains<action.aimed_shot.execute_time |
| 3 | `trueshot` | if=!buff.double_tap.up&variable.trueshot_ready |
| 4 | `volley` | if=!buff.double_tap.up |
| 5 | `aimed_shot` | target_if=max:debuff.sentinels_mark.up\|max_prio_damage |
| 6 | `moonlight_chakram` | — |
| 7 | `rapid_fire` | — |
| 8 | `steady_shot` | — |

## Action List: `sentst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `volley` | if=!buff.double_tap.up&active_enemies=1 |
| 2 | `trueshot` | if=!buff.double_tap.up&active_enemies=1&variable.trueshot_ready |
| 3 | `rapid_fire` | if=talent.unload&((buff.precise_shots.up&!talent.no_scope)&buff.bulletstorm.stack<10\|target.health.pct<20) |
| 4 | `aimed_shot` | target_if=max:debuff.sentinels_mark.up\|max_prio_damage,if=active_enemies>2&buff.volley.remains%action.aimed_shot.execute_time>action.arcane_shot.execute_time&buff.trueshot.down |
| 5 | `arcane_shot` | target_if=max:debuff.sentinels_mark.down\|action.aimed_shot.in_flight_to_target\|max_prio_damage,if=buff.precise_shots.up |
| 6 | `rapid_fire` | if=buff.bulletstorm.remains<action.aimed_shot.execute_time |
| 7 | `trueshot` | if=!buff.double_tap.up&active_enemies>1&variable.trueshot_ready |
| 8 | `volley` | if=!buff.double_tap.up&active_enemies>1 |
| 9 | `aimed_shot` | target_if=max:debuff.sentinels_mark.up\|max_prio_damage,if=cooldown.volley.remains>2\|buff.trueshot.up\|!talent.volley |
| 10 | `moonlight_chakram` | — |
| 11 | `rapid_fire` | — |
| 12 | `steady_shot` | — |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&this_trinket.cooldown.duration%%cooldown.trueshot.duration=0&(buff.trueshot.remains>14\|this_trinket.is.algethar_puzzle_box&variable.trueshot_ready&cooldown.trueshot.remains<5) |
| 2 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&other_trinket.cooldown.duration%%cooldown.trueshot.duration=0&(buff.trueshot.remains>14&other_trinket.cooldown.remains\|cooldown.trueshot.remains>20&other_trinket.cooldown.remains<=cooldown.trueshot.remains) |
| 3 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(buff.trueshot.remains>14\|buff.trueshot.up&fight_remains<cooldown.trueshot.remains+15\|fight_remains<21) |
| 4 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&cooldown.trueshot.remains>20 |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=snapshot_stats
actions.precombat+=/summon_pet,if=talent.unbreakable_bond
actions.precombat+=/use_item,name=algethar_puzzle_box
actions.precombat+=/aimed_shot,if=active_enemies<3|talent.black_arrow&talent.headshot
actions.precombat+=/steady_shot

# Executed every time the actor is available.
actions=variable,name=trueshot_ready,value=!talent.bullseye|fight_remains>cooldown.trueshot.duration+10|buff.bullseye.stack=buff.bullseye.max_stack|fight_remains<25|time<10
actions+=/auto_shot
actions+=/call_action_list,name=cds
actions+=/call_action_list,name=trinkets
actions+=/call_action_list,name=draoe,if=active_enemies>2&talent.trick_shots&hero_tree.dark_ranger
actions+=/call_action_list,name=sentaoe,if=active_enemies>2&talent.trick_shots&hero_tree.sentinel
actions+=/call_action_list,name=drst,if=hero_tree.dark_ranger
actions+=/call_action_list,name=sentst,if=hero_tree.sentinel

actions.cds=invoke_external_buff,name=power_infusion,if=buff.trueshot.remains>12|fight_remains<13
actions.cds+=/berserking,if=buff.trueshot.up|fight_remains<13
actions.cds+=/blood_fury,if=buff.trueshot.up|cooldown.trueshot.remains>30|fight_remains<16
actions.cds+=/ancestral_call,if=buff.trueshot.up|cooldown.trueshot.remains>30|fight_remains<16
actions.cds+=/fireblood,if=buff.trueshot.up|cooldown.trueshot.remains>30|fight_remains<9
actions.cds+=/lights_judgment,if=buff.trueshot.down
actions.cds+=/potion,if=buff.trueshot.up&(buff.bloodlust.up|fight_remains<120-30*talent.calling_the_shots)|fight_remains<31

actions.draoe=black_arrow
actions.draoe+=/multishot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up&!talent.aspect_of_the_hydra|buff.trick_shots.down
actions.draoe+=/rapid_fire,if=buff.trick_shots.remains>execute_time&(talent.unload&(talent.no_scope&buff.bulletstorm.stack<10|target.health.pct<20)|buff.bulletstorm.remains<action.aimed_shot.execute_time)
actions.draoe+=/trueshot,if=!buff.double_tap.up&variable.trueshot_ready
actions.draoe+=/volley,if=!buff.double_tap.up
actions.draoe+=/aimed_shot,target_if=max:debuff.spotters_mark.up|max_prio_damage,if=buff.trick_shots.remains>cast_time
actions.draoe+=/wailing_arrow
actions.draoe+=/rapid_fire,if=buff.trick_shots.remains>execute_time
actions.draoe+=/steady_shot

actions.drst=black_arrow
actions.drst+=/trueshot,if=!buff.double_tap.up&variable.trueshot_ready
actions.drst+=/rapid_fire,if=talent.unload&(talent.no_scope&buff.bulletstorm.stack<10|target.health.pct<20)
actions.drst+=/aimed_shot,target_if=max:debuff.sentinels_mark.up|max_prio_damage,if=buff.volley.remains%action.aimed_shot.execute_time>action.arcane_shot.execute_time&buff.trueshot.down
actions.drst+=/arcane_shot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up
actions.drst+=/rapid_fire,if=buff.bulletstorm.remains<action.aimed_shot.execute_time
actions.drst+=/volley,if=!buff.double_tap.up
actions.drst+=/aimed_shot,target_if=max:debuff.spotters_mark.up|max_prio_damage
actions.drst+=/wailing_arrow
actions.drst+=/rapid_fire
actions.drst+=/steady_shot

actions.sentaoe=multishot,target_if=max:debuff.sentinels_mark.down|action.aimed_shot.in_flight_to_target,if=buff.precise_shots.up&!talent.aspect_of_the_hydra|buff.trick_shots.down
actions.sentaoe+=/rapid_fire,if=buff.bulletstorm.remains<action.aimed_shot.execute_time
actions.sentaoe+=/trueshot,if=!buff.double_tap.up&variable.trueshot_ready
actions.sentaoe+=/volley,if=!buff.double_tap.up
actions.sentaoe+=/aimed_shot,target_if=max:debuff.sentinels_mark.up|max_prio_damage
actions.sentaoe+=/moonlight_chakram
actions.sentaoe+=/rapid_fire
actions.sentaoe+=/steady_shot

actions.sentst=volley,if=!buff.double_tap.up&active_enemies=1
actions.sentst+=/trueshot,if=!buff.double_tap.up&active_enemies=1&variable.trueshot_ready
actions.sentst+=/rapid_fire,if=talent.unload&((buff.precise_shots.up&!talent.no_scope)&buff.bulletstorm.stack<10|target.health.pct<20)
actions.sentst+=/aimed_shot,target_if=max:debuff.sentinels_mark.up|max_prio_damage,if=active_enemies>2&buff.volley.remains%action.aimed_shot.execute_time>action.arcane_shot.execute_time&buff.trueshot.down
actions.sentst+=/arcane_shot,target_if=max:debuff.sentinels_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up
actions.sentst+=/rapid_fire,if=buff.bulletstorm.remains<action.aimed_shot.execute_time
actions.sentst+=/trueshot,if=!buff.double_tap.up&active_enemies>1&variable.trueshot_ready
actions.sentst+=/volley,if=!buff.double_tap.up&active_enemies>1
actions.sentst+=/aimed_shot,target_if=max:debuff.sentinels_mark.up|max_prio_damage,if=cooldown.volley.remains>2|buff.trueshot.up|!talent.volley
actions.sentst+=/moonlight_chakram
actions.sentst+=/rapid_fire
actions.sentst+=/steady_shot

actions.trinkets=use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&this_trinket.cooldown.duration%%cooldown.trueshot.duration=0&(buff.trueshot.remains>14|this_trinket.is.algethar_puzzle_box&variable.trueshot_ready&cooldown.trueshot.remains<5)
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&other_trinket.cooldown.duration%%cooldown.trueshot.duration=0&(buff.trueshot.remains>14&other_trinket.cooldown.remains|cooldown.trueshot.remains>20&other_trinket.cooldown.remains<=cooldown.trueshot.remains)
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(buff.trueshot.remains>14|buff.trueshot.up&fight_remains<cooldown.trueshot.remains+15|fight_remains<21)
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&cooldown.trueshot.remains>20
```
