# Hunter – Marksmanship

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:18 UTC

Source: `apl/default/hunter/marksmanship.simc`

---

## Overview

- **Action Lists:** 10
- **Total Actions:** 105
- **Lists:** `precombat`, `default`, `cds`, `drcleave`, `drst`, `drtrickshots`, `sentcleave`, `sentst`, `senttrickshots`, `trinkets`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `summon_pet` | if=talent.unbreakable_bond |
| 3 | `aimed_shot` | if=active_enemies<3\|talent.black_arrow&talent.headshot |
| 4 | `steady_shot` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=trueshot_ready,value=!talent.bullseye\|fight_remains>cooldown.trueshot.duration+10\|buff.bullseye.stack=buff.bullseye.max_stack\|fight_remains<25 |
| 2 | `variable` | name=trueshot_ready,op=setif,condition=fight_style.dungeonroute,value_else=variable.trueshot_ready,value=raid_event.pull.remains>30\|raid_event.pull.in>60 |
| 3 | `variable` | name=buffer_deathblow,value=hero_tree.dark_ranger&action.aimed_shot.in_flight&!action.black_arrow.ready |
| 4 | `auto_shot` | — |
| 5 | `call_action_list` | name=cds |
| 6 | `call_action_list` | name=trinkets |
| 7 | `call_action_list` | name=drtrickshots,if=active_enemies>2&talent.trick_shots&hero_tree.dark_ranger |
| 8 | `call_action_list` | name=senttrickshots,if=active_enemies>2&talent.trick_shots&hero_tree.sentinel |
| 9 | `call_action_list` | name=drcleave,if=active_enemies>1&hero_tree.dark_ranger |
| 10 | `call_action_list` | name=sentcleave,if=active_enemies>1&hero_tree.sentinel |
| 11 | `call_action_list` | name=drst,if=hero_tree.dark_ranger |
| 12 | `call_action_list` | name=sentst,if=hero_tree.sentinel |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_external_buff` | name=power_infusion,if=buff.trueshot.remains>12\|fight_remains<13 |
| 2 | `berserking` | if=buff.trueshot.up\|fight_remains<13 |
| 3 | `blood_fury` | if=buff.trueshot.up\|cooldown.trueshot.remains>30\|fight_remains<16 |
| 4 | `ancestral_call` | if=buff.trueshot.up\|cooldown.trueshot.remains>30\|fight_remains<16 |
| 5 | `fireblood` | if=buff.trueshot.up\|cooldown.trueshot.remains>30\|fight_remains<9 |
| 6 | `lights_judgment` | if=buff.trueshot.down |
| 7 | `potion` | if=buff.trueshot.up&(buff.bloodlust.up\|target.health.pct<20)\|fight_remains<31 |

## Action List: `drcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `wait` | sec=0.05,if=talent.aspect_of_the_hydra&talent.shrapnel_shot&time=0&action.aimed_shot.in_flight |
| 2 | `explosive_shot` | if=buff.trueshot.down&talent.precision_detonation&(!talent.shrapnel_shot\|buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1) |
| 3 | `black_arrow` | if=buff.precise_shots.up\|!talent.headshot |
| 4 | `rapid_fire` | if=talent.bulletstorm&buff.bulletstorm.down&(talent.aspect_of_the_hydra\|!talent.volley\|cooldown.volley.remains) |
| 5 | `volley` | if=buff.double_tap.down&(!talent.double_tap\|buff.precise_shots.down)&(!talent.shrapnel_shot\|!talent.salvo\|buff.lock_and_load.down) |
| 6 | `trueshot` | if=variable.trueshot_ready&buff.double_tap.down&(!talent.volley\|cooldown.volley.remains) |
| 7 | `steady_shot` | if=variable.buffer_deathblow&buff.trueshot.down |
| 8 | `aimed_shot` | if=buff.trueshot.up&buff.precise_shots.down\|buff.lock_and_load.up&buff.moving_target.up |
| 9 | `rapid_fire` | if=buff.double_tap.down |
| 10 | `arcane_shot` | if=buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down) |
| 11 | `aimed_shot` | if=buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up |
| 12 | `explosive_shot` | if=!talent.shrapnel_shot\|buff.lock_and_load.down |
| 13 | `steady_shot` | — |

## Action List: `drst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `volley` | if=buff.double_tap.down&(!raid_event.adds.exists\|raid_event.adds.in>cooldown)&(!talent.shrapnel_shot\|!talent.salvo\|buff.lock_and_load.down) |
| 2 | `explosive_shot` | if=talent.precision_detonation&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1&buff.trueshot.down |
| 3 | `steady_shot` | if=variable.buffer_deathblow&buff.trueshot.down&cooldown.trueshot.remains |
| 4 | `trueshot` | if=variable.trueshot_ready&buff.double_tap.down&!action.black_arrow.ready&(!talent.bulletstorm\|buff.bulletstorm.up) |
| 5 | `black_arrow` | if=talent.headshot&buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down)\|!talent.headshot |
| 6 | `aimed_shot` | if=(buff.trueshot.up\|action.black_arrow.ready)&buff.precise_shots.down\|buff.lock_and_load.up&buff.moving_target.up |
| 7 | `rapid_fire` | if=!action.black_arrow.ready |
| 8 | `trueshot` | if=variable.trueshot_ready&buff.double_tap.down |
| 9 | `aimed_shot` | if=buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up |
| 10 | `arcane_shot` | if=buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down)&(cooldown.black_arrow.remains>action.steady_shot.execute_time\|target.health.pct<80&target.health.pct>20) |
| 11 | `explosive_shot` | if=talent.shrapnel_shot&buff.lock_and_load.down |
| 12 | `steady_shot` | — |

## Action List: `drtrickshots`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `volley` | if=buff.double_tap.down&(!talent.shrapnel_shot\|!talent.salvo\|buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1) |
| 2 | `explosive_shot` | if=talent.precision_detonation&buff.trueshot.down&(!talent.shrapnel_shot\|buff.lock_and_load.down&(cooldown.aimed_shot.charges_fractional<=1.1\|talent.focused_aim)) |
| 3 | `black_arrow` | if=buff.trick_shots.down\|!talent.headshot\|buff.precise_shots.up |
| 4 | `rapid_fire` | if=buff.trick_shots.remains>execute_time&talent.bulletstorm&buff.bulletstorm.down |
| 5 | `trueshot` | if=variable.trueshot_ready&buff.double_tap.down |
| 6 | `steady_shot` | if=variable.buffer_deathblow&buff.trueshot.down |
| 7 | `multishot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target,if=buff.trick_shots.down\|buff.precise_shots.up&(buff.moving_target.down\|debuff.spotters_mark.down) |
| 8 | `aimed_shot` | if=buff.trick_shots.remains>cast_time&(buff.trueshot.up&buff.precise_shots.down\|buff.lock_and_load.up&buff.moving_target.up) |
| 9 | `rapid_fire` | if=buff.trick_shots.remains>execute_time&(talent.no_scope\|talent.bulletstorm&buff.bulletstorm.down) |
| 10 | `aimed_shot` | if=buff.trick_shots.remains>cast_time&(buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up) |
| 11 | `explosive_shot` | if=talent.shrapnel_shot&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1 |
| 12 | `steady_shot` | — |

## Action List: `sentcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `explosive_shot` | if=talent.precision_detonation&action.aimed_shot.in_flight&(buff.trueshot.down\|!talent.windrunner_quiver) |
| 2 | `volley` | if=(talent.double_tap&buff.double_tap.down\|!talent.aspect_of_the_hydra)&(buff.precise_shots.down\|buff.moving_target.up) |
| 3 | `rapid_fire` | if=talent.bulletstorm&buff.bulletstorm.down&(!talent.double_tap\|buff.double_tap.up\|!talent.aspect_of_the_hydra&buff.trick_shots.remains>execute_time)&(buff.precise_shots.down\|buff.moving_target.up\|!talent.volley) |
| 4 | `volley` | if=!talent.double_tap&(buff.precise_shots.down\|buff.moving_target.up) |
| 5 | `trueshot` | if=variable.trueshot_ready&(buff.double_tap.down\|!talent.volley)&(buff.lunar_storm_ready.down\|!talent.double_tap\|!talent.volley)&(buff.precise_shots.down\|buff.moving_target.up\|!talent.volley) |
| 6 | `rapid_fire` | if=talent.lunar_storm&buff.lunar_storm_cooldown.down&(buff.precise_shots.down\|buff.moving_target.up\|cooldown.volley.remains&cooldown.trueshot.remains\|!talent.volley) |
| 7 | `kill_shot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target\|max_prio_damage,if=talent.headshot&buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down)\|!talent.headshot&buff.razor_fragments.up |
| 8 | `multishot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target\|max_prio_damage,if=buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down)&!talent.aspect_of_the_hydra |
| 9 | `arcane_shot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target\|max_prio_damage,if=buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down) |
| 10 | `aimed_shot` | target_if=max:debuff.spotters_mark.up,if=(buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up)&full_recharge_time<action.rapid_fire.execute_time+cast_time&(!talent.bulletstorm\|buff.bulletstorm.up)&talent.windrunner_quiver |
| 11 | `rapid_fire` | if=!talent.bulletstorm\|buff.bulletstorm.stack<=10\|talent.aspect_of_the_hydra |
| 12 | `aimed_shot` | target_if=max:debuff.spotters_mark.up\|max_prio_damage,if=buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up |
| 13 | `rapid_fire` | — |
| 14 | `explosive_shot` | if=talent.precision_detonation\|buff.trueshot.down |
| 15 | `steady_shot` | — |

## Action List: `sentst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `volley` | if=buff.double_tap.down&(!raid_event.adds.exists\|raid_event.adds.in>cooldown)&(!talent.shrapnel_shot\|!talent.salvo\|buff.lock_and_load.down) |
| 2 | `explosive_shot` | if=talent.shrapnel_shot&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1&buff.trueshot.down |
| 3 | `rapid_fire` | if=talent.lunar_storm&buff.lunar_storm_cooldown.down |
| 4 | `trueshot` | if=variable.trueshot_ready&buff.double_tap.down&(!talent.bulletstorm\|buff.bulletstorm.up) |
| 5 | `kill_shot` | if=talent.headshot&buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down)\|!talent.headshot&buff.razor_fragments.up |
| 6 | `aimed_shot` | if=buff.trueshot.up&buff.precise_shots.down\|buff.lock_and_load.up&buff.moving_target.up |
| 7 | `rapid_fire` | if=!talent.no_scope\|buff.precise_shots.down |
| 8 | `arcane_shot` | if=buff.precise_shots.up&(debuff.spotters_mark.down\|buff.moving_target.down) |
| 9 | `rapid_fire` | — |
| 10 | `aimed_shot` | if=buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up |
| 11 | `explosive_shot` | if=talent.precision_detonation\|buff.trueshot.down |
| 12 | `steady_shot` | — |

## Action List: `senttrickshots`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `explosive_shot` | if=talent.shrapnel_shot&buff.trueshot.down&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1 |
| 2 | `volley` | if=buff.double_tap.down&(!talent.shrapnel_shot\|!talent.salvo\|buff.lock_and_load.down) |
| 3 | `rapid_fire` | if=buff.trick_shots.remains>execute_time&(talent.bulletstorm&buff.bulletstorm.down\|buff.lunar_storm_cooldown.down) |
| 4 | `kill_shot` | if=talent.headshot&buff.trick_shots.up&buff.razor_fragments.up&buff.precise_shots.up |
| 5 | `multishot` | target_if=max:debuff.spotters_mark.down\|action.aimed_shot.in_flight_to_target,if=buff.trick_shots.down\|buff.precise_shots.up&(buff.moving_target.down\|debuff.spotters_mark.down) |
| 6 | `trueshot` | if=variable.trueshot_ready&buff.double_tap.down |
| 7 | `aimed_shot` | if=buff.trick_shots.remains>cast_time&(buff.trueshot.up&buff.precise_shots.down\|buff.lock_and_load.up&buff.moving_target.up) |
| 8 | `rapid_fire` | if=buff.trick_shots.remains>execute_time |
| 9 | `aimed_shot` | if=buff.trick_shots.remains>cast_time&(buff.precise_shots.down\|debuff.spotters_mark.up&buff.moving_target.up) |
| 10 | `explosive_shot` | — |
| 11 | `steady_shot` | if=focus+cast_regen<focus.max |
| 12 | `multishot` | — |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=!equipped.unyielding_netherprism&this_trinket.has_use_buff&this_trinket.cooldown.duration%%cooldown.trueshot.duration=0&buff.trueshot.remains>14 |
| 2 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=!equipped.unyielding_netherprism&this_trinket.has_use_buff&other_trinket.cooldown.duration%%cooldown.trueshot.duration=0&(buff.trueshot.remains>14&other_trinket.cooldown.remains\|cooldown.trueshot.remains>20&other_trinket.cooldown.remains<=cooldown.trueshot.remains) |
| 3 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.is.unyielding_netherprism&(buff.trueshot.remains>14&(buff.latent_energy.stack>(19-cooldown.trueshot.duration%10)\|fight_remains<(cooldown.trueshot.duration+20))\|fight_remains<22&(buff.latent_energy.stack>8\|!other_trinket.has_use_buff\|other_trinket.cooldown.remains)) |
| 4 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=!this_trinket.is.unyielding_netherprism&this_trinket.has_use_buff&(other_trinket.is.unyielding_netherprism&fight_remains<cooldown.trueshot.remains+cooldown.trueshot.duration+10&cooldown.trueshot.remains>20\|buff.trueshot.remains>14\|buff.trueshot.up&fight_remains<cooldown.trueshot.remains+15\|fight_remains<21) |
| 5 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.is.unyielding_netherprism&buff.trueshot.remains>14&buff.latent_energy.stack>3&(buff.latent_energy.stack+floor((fight_remains-20)%cooldown.trueshot.duration)*(cooldown.trueshot.duration%10))>17 |
| 6 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&cooldown.trueshot.remains>20 |

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
actions.precombat+=/aimed_shot,if=active_enemies<3|talent.black_arrow&talent.headshot
actions.precombat+=/steady_shot

# Executed every time the actor is available.
# Hold the final Trueshot for Bullseye stacks if necessary.
actions=variable,name=trueshot_ready,value=!talent.bullseye|fight_remains>cooldown.trueshot.duration+10|buff.bullseye.stack=buff.bullseye.max_stack|fight_remains<25
# For DungeonRoute, hold Trueshot at the end of pulls.
actions+=/variable,name=trueshot_ready,op=setif,condition=fight_style.dungeonroute,value_else=variable.trueshot_ready,value=raid_event.pull.remains>30|raid_event.pull.in>60
actions+=/variable,name=buffer_deathblow,value=hero_tree.dark_ranger&action.aimed_shot.in_flight&!action.black_arrow.ready
actions+=/auto_shot
actions+=/call_action_list,name=cds
actions+=/call_action_list,name=trinkets
actions+=/call_action_list,name=drtrickshots,if=active_enemies>2&talent.trick_shots&hero_tree.dark_ranger
actions+=/call_action_list,name=senttrickshots,if=active_enemies>2&talent.trick_shots&hero_tree.sentinel
actions+=/call_action_list,name=drcleave,if=active_enemies>1&hero_tree.dark_ranger
actions+=/call_action_list,name=sentcleave,if=active_enemies>1&hero_tree.sentinel
actions+=/call_action_list,name=drst,if=hero_tree.dark_ranger
actions+=/call_action_list,name=sentst,if=hero_tree.sentinel

actions.cds=invoke_external_buff,name=power_infusion,if=buff.trueshot.remains>12|fight_remains<13
actions.cds+=/berserking,if=buff.trueshot.up|fight_remains<13
actions.cds+=/blood_fury,if=buff.trueshot.up|cooldown.trueshot.remains>30|fight_remains<16
actions.cds+=/ancestral_call,if=buff.trueshot.up|cooldown.trueshot.remains>30|fight_remains<16
actions.cds+=/fireblood,if=buff.trueshot.up|cooldown.trueshot.remains>30|fight_remains<9
actions.cds+=/lights_judgment,if=buff.trueshot.down
actions.cds+=/potion,if=buff.trueshot.up&(buff.bloodlust.up|target.health.pct<20)|fight_remains<31

# 2 targets (2+ without Trick Shots)  With Shrapnel Shot don't queue Explosive Shot after the precast since the Aspect of the Hydra secondary Aimed Shot will consume the Lock and Load.
actions.drcleave=wait,sec=0.05,if=talent.aspect_of_the_hydra&talent.shrapnel_shot&time=0&action.aimed_shot.in_flight
actions.drcleave+=/explosive_shot,if=buff.trueshot.down&talent.precision_detonation&(!talent.shrapnel_shot|buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1)
actions.drcleave+=/black_arrow,if=buff.precise_shots.up|!talent.headshot
actions.drcleave+=/rapid_fire,if=talent.bulletstorm&buff.bulletstorm.down&(talent.aspect_of_the_hydra|!talent.volley|cooldown.volley.remains)
actions.drcleave+=/volley,if=buff.double_tap.down&(!talent.double_tap|buff.precise_shots.down)&(!talent.shrapnel_shot|!talent.salvo|buff.lock_and_load.down)
actions.drcleave+=/trueshot,if=variable.trueshot_ready&buff.double_tap.down&(!talent.volley|cooldown.volley.remains)
actions.drcleave+=/steady_shot,if=variable.buffer_deathblow&buff.trueshot.down
actions.drcleave+=/aimed_shot,if=buff.trueshot.up&buff.precise_shots.down|buff.lock_and_load.up&buff.moving_target.up
actions.drcleave+=/rapid_fire,if=buff.double_tap.down
actions.drcleave+=/arcane_shot,if=buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)
actions.drcleave+=/aimed_shot,if=buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up
actions.drcleave+=/explosive_shot,if=!talent.shrapnel_shot|buff.lock_and_load.down
actions.drcleave+=/steady_shot

# 1 target
actions.drst=volley,if=buff.double_tap.down&(!raid_event.adds.exists|raid_event.adds.in>cooldown)&(!talent.shrapnel_shot|!talent.salvo|buff.lock_and_load.down)
actions.drst+=/explosive_shot,if=talent.precision_detonation&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1&buff.trueshot.down
# Queue Steady Shot after Aimed Shot if a Deathblow hasn't already been up long enough to be reacted to.
actions.drst+=/steady_shot,if=variable.buffer_deathblow&buff.trueshot.down&cooldown.trueshot.remains
actions.drst+=/trueshot,if=variable.trueshot_ready&buff.double_tap.down&!action.black_arrow.ready&(!talent.bulletstorm|buff.bulletstorm.up)
actions.drst+=/black_arrow,if=talent.headshot&buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)|!talent.headshot
actions.drst+=/aimed_shot,if=(buff.trueshot.up|action.black_arrow.ready)&buff.precise_shots.down|buff.lock_and_load.up&buff.moving_target.up
actions.drst+=/rapid_fire,if=!action.black_arrow.ready
actions.drst+=/trueshot,if=variable.trueshot_ready&buff.double_tap.down
actions.drst+=/aimed_shot,if=buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up
actions.drst+=/arcane_shot,if=buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)&(cooldown.black_arrow.remains>action.steady_shot.execute_time|target.health.pct<80&target.health.pct>20)
actions.drst+=/explosive_shot,if=talent.shrapnel_shot&buff.lock_and_load.down
actions.drst+=/steady_shot

# 3+ targets (with Trick Shots)
actions.drtrickshots=volley,if=buff.double_tap.down&(!talent.shrapnel_shot|!talent.salvo|buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1)
actions.drtrickshots+=/explosive_shot,if=talent.precision_detonation&buff.trueshot.down&(!talent.shrapnel_shot|buff.lock_and_load.down&(cooldown.aimed_shot.charges_fractional<=1.1|talent.focused_aim))
actions.drtrickshots+=/black_arrow,if=buff.trick_shots.down|!talent.headshot|buff.precise_shots.up
actions.drtrickshots+=/rapid_fire,if=buff.trick_shots.remains>execute_time&talent.bulletstorm&buff.bulletstorm.down
actions.drtrickshots+=/trueshot,if=variable.trueshot_ready&buff.double_tap.down
actions.drtrickshots+=/steady_shot,if=variable.buffer_deathblow&buff.trueshot.down
actions.drtrickshots+=/multishot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target,if=buff.trick_shots.down|buff.precise_shots.up&(buff.moving_target.down|debuff.spotters_mark.down)
actions.drtrickshots+=/aimed_shot,if=buff.trick_shots.remains>cast_time&(buff.trueshot.up&buff.precise_shots.down|buff.lock_and_load.up&buff.moving_target.up)
actions.drtrickshots+=/rapid_fire,if=buff.trick_shots.remains>execute_time&(talent.no_scope|talent.bulletstorm&buff.bulletstorm.down)
actions.drtrickshots+=/aimed_shot,if=buff.trick_shots.remains>cast_time&(buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up)
actions.drtrickshots+=/explosive_shot,if=talent.shrapnel_shot&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1
actions.drtrickshots+=/steady_shot

actions.sentcleave=explosive_shot,if=talent.precision_detonation&action.aimed_shot.in_flight&(buff.trueshot.down|!talent.windrunner_quiver)
actions.sentcleave+=/volley,if=(talent.double_tap&buff.double_tap.down|!talent.aspect_of_the_hydra)&(buff.precise_shots.down|buff.moving_target.up)
actions.sentcleave+=/rapid_fire,if=talent.bulletstorm&buff.bulletstorm.down&(!talent.double_tap|buff.double_tap.up|!talent.aspect_of_the_hydra&buff.trick_shots.remains>execute_time)&(buff.precise_shots.down|buff.moving_target.up|!talent.volley)
actions.sentcleave+=/volley,if=!talent.double_tap&(buff.precise_shots.down|buff.moving_target.up)
actions.sentcleave+=/trueshot,if=variable.trueshot_ready&(buff.double_tap.down|!talent.volley)&(buff.lunar_storm_ready.down|!talent.double_tap|!talent.volley)&(buff.precise_shots.down|buff.moving_target.up|!talent.volley)
actions.sentcleave+=/rapid_fire,if=talent.lunar_storm&buff.lunar_storm_cooldown.down&(buff.precise_shots.down|buff.moving_target.up|cooldown.volley.remains&cooldown.trueshot.remains|!talent.volley)
actions.sentcleave+=/kill_shot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=talent.headshot&buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)|!talent.headshot&buff.razor_fragments.up
actions.sentcleave+=/multishot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)&!talent.aspect_of_the_hydra
actions.sentcleave+=/arcane_shot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)
actions.sentcleave+=/aimed_shot,target_if=max:debuff.spotters_mark.up,if=(buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up)&full_recharge_time<action.rapid_fire.execute_time+cast_time&(!talent.bulletstorm|buff.bulletstorm.up)&talent.windrunner_quiver
actions.sentcleave+=/rapid_fire,if=!talent.bulletstorm|buff.bulletstorm.stack<=10|talent.aspect_of_the_hydra
actions.sentcleave+=/aimed_shot,target_if=max:debuff.spotters_mark.up|max_prio_damage,if=buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up
actions.sentcleave+=/rapid_fire
actions.sentcleave+=/explosive_shot,if=talent.precision_detonation|buff.trueshot.down
actions.sentcleave+=/steady_shot

actions.sentst=volley,if=buff.double_tap.down&(!raid_event.adds.exists|raid_event.adds.in>cooldown)&(!talent.shrapnel_shot|!talent.salvo|buff.lock_and_load.down)
actions.sentst+=/explosive_shot,if=talent.shrapnel_shot&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1&buff.trueshot.down
actions.sentst+=/rapid_fire,if=talent.lunar_storm&buff.lunar_storm_cooldown.down
actions.sentst+=/trueshot,if=variable.trueshot_ready&buff.double_tap.down&(!talent.bulletstorm|buff.bulletstorm.up)
actions.sentst+=/kill_shot,if=talent.headshot&buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)|!talent.headshot&buff.razor_fragments.up
actions.sentst+=/aimed_shot,if=buff.trueshot.up&buff.precise_shots.down|buff.lock_and_load.up&buff.moving_target.up
actions.sentst+=/rapid_fire,if=!talent.no_scope|buff.precise_shots.down
actions.sentst+=/arcane_shot,if=buff.precise_shots.up&(debuff.spotters_mark.down|buff.moving_target.down)
actions.sentst+=/rapid_fire
actions.sentst+=/aimed_shot,if=buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up
actions.sentst+=/explosive_shot,if=talent.precision_detonation|buff.trueshot.down
actions.sentst+=/steady_shot

actions.senttrickshots=explosive_shot,if=talent.shrapnel_shot&buff.trueshot.down&buff.lock_and_load.down&cooldown.aimed_shot.charges_fractional<=1.1
actions.senttrickshots+=/volley,if=buff.double_tap.down&(!talent.shrapnel_shot|!talent.salvo|buff.lock_and_load.down)
actions.senttrickshots+=/rapid_fire,if=buff.trick_shots.remains>execute_time&(talent.bulletstorm&buff.bulletstorm.down|buff.lunar_storm_cooldown.down)
actions.senttrickshots+=/kill_shot,if=talent.headshot&buff.trick_shots.up&buff.razor_fragments.up&buff.precise_shots.up
actions.senttrickshots+=/multishot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target,if=buff.trick_shots.down|buff.precise_shots.up&(buff.moving_target.down|debuff.spotters_mark.down)
actions.senttrickshots+=/trueshot,if=variable.trueshot_ready&buff.double_tap.down
actions.senttrickshots+=/aimed_shot,if=buff.trick_shots.remains>cast_time&(buff.trueshot.up&buff.precise_shots.down|buff.lock_and_load.up&buff.moving_target.up)
actions.senttrickshots+=/rapid_fire,if=buff.trick_shots.remains>execute_time
actions.senttrickshots+=/aimed_shot,if=buff.trick_shots.remains>cast_time&(buff.precise_shots.down|debuff.spotters_mark.up&buff.moving_target.up)
actions.senttrickshots+=/explosive_shot
actions.senttrickshots+=/steady_shot,if=focus+cast_regen<focus.max
actions.senttrickshots+=/multishot

# A buff trinket that lines up cleanly with Trueshot; use with Trueshot.
actions.trinkets=use_items,check_existing=0,slots=trinket1:trinket2,if=!equipped.unyielding_netherprism&this_trinket.has_use_buff&this_trinket.cooldown.duration%%cooldown.trueshot.duration=0&buff.trueshot.remains>14
# A buff trinket paired with a trinket that matches the above line; use with Trueshot if the other trinket is not ready or use without Trueshot if the other trinket will come up for the next Trueshot.
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=!equipped.unyielding_netherprism&this_trinket.has_use_buff&other_trinket.cooldown.duration%%cooldown.trueshot.duration=0&(buff.trueshot.remains>14&other_trinket.cooldown.remains|cooldown.trueshot.remains>20&other_trinket.cooldown.remains<=cooldown.trueshot.remains)
# Netherprism higher prioroty; use with Trueshot if waiting for the next Trueshot will waste stacks or if it's the final Trueshot of the fight. Also use in the last ~20 seconds of the fight if there is no other buff trinket ready or if there are over 8 stacks.
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.is.unyielding_netherprism&(buff.trueshot.remains>14&(buff.latent_energy.stack>(19-cooldown.trueshot.duration%10)|fight_remains<(cooldown.trueshot.duration+20))|fight_remains<22&(buff.latent_energy.stack>8|!other_trinket.has_use_buff|other_trinket.cooldown.remains))
# A buff trinket that is not Netherprism; if the other trinket is Netherprism, use without Trueshot if there will only be one more Trueshot in the fight. Otherwise use with Trueshot or in the last ~20 seconds of the fight.
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=!this_trinket.is.unyielding_netherprism&this_trinket.has_use_buff&(other_trinket.is.unyielding_netherprism&fight_remains<cooldown.trueshot.remains+cooldown.trueshot.duration+10&cooldown.trueshot.remains>20|buff.trueshot.remains>14|buff.trueshot.up&fight_remains<cooldown.trueshot.remains+15|fight_remains<21)
# Netherprism lower priority; use with Trueshot if using it now will still allow stacking it back up for the final Trueshot of the fight.
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.is.unyielding_netherprism&buff.trueshot.remains>14&buff.latent_energy.stack>3&(buff.latent_energy.stack+floor((fight_remains-20)%cooldown.trueshot.duration)*(cooldown.trueshot.duration%10))>17
# A damage trinket; use when Trueshot has at least 20 seconds remaining on its cooldown.
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&cooldown.trueshot.remains>20
```
