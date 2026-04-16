# Warrior – Arms

Auto-generated from SimulationCraft APL | Last updated: 2026-04-16 05:34 UTC

Source: `apl/default/warrior/arms.simc`

---

## Overview

- **Action Lists:** 10
- **Total Actions:** 157
- **Lists:** `precombat`, `default`, `colossus_aoe`, `colossus_execute`, `colossus_st`, `slayer_aoe`, `slayer_execute`, `slayer_st`, `trinkets`, `variables`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `variable` | name=trinket_1_exclude,value=trinket.1.is.algethar_puzzle_box |
| 3 | `variable` | name=trinket_2_exclude,value=trinket.2.is.algethar_puzzle_box |
| 4 | `variable` | name=trinket_1_buffs,value=trinket.1.has_use_buff |
| 5 | `variable` | name=trinket_2_buffs,value=trinket.2.has_use_buff |
| 6 | `variable` | name=trinket_1_duration,op=setif,value=0,value_else=trinket.1.proc.any_dps.duration,condition=0 |
| 7 | `variable` | name=trinket_2_duration,op=setif,value=0,value_else=trinket.2.proc.any_dps.duration,condition=0 |
| 8 | `variable` | name=trinket_1_high_value,op=setif,value=2,value_else=1,condition=trinket.1.is.treacherous_transmitter |
| 9 | `variable` | name=trinket_2_high_value,op=setif,value=2,value_else=1,condition=trinket.2.is.treacherous_transmitter |
| 10 | `variable` | name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&talent.avatar&trinket.1.cooldown.duration%%cooldown.avatar.duration=0 |
| 11 | `variable` | name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&talent.avatar&trinket.2.cooldown.duration%%cooldown.avatar.duration=0 |
| 12 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs&(trinket.2.has_cooldown\|!trinket.1.has_cooldown)\|variable.trinket_2_buffs&((trinket.2.cooldown.duration%variable.trinket_2_duration)*(1.5+trinket.2.has_buff.strength)*(variable.trinket_2_sync)*(variable.trinket_2_high_value)*(1+((trinket.2.ilvl-trinket.1.ilvl)%100)))>((trinket.1.cooldown.duration%variable.trinket_1_duration)*(1.5+trinket.1.has_buff.strength)*(variable.trinket_1_sync)*(variable.trinket_1_high_value)*(1+((trinket.1.ilvl-trinket.2.ilvl)%100))) |
| 13 | `variable` | name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl |
| 14 | `battle_stance` | toggle=on |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `charge` | if=time<=0.5\|movement.distance>5 |
| 2 | `auto_attack` | — |
| 3 | `potion` | if=gcd.remains=0&debuff.colossus_smash.remains>8\|target.time_to_die<25 |
| 4 | `pummel` | if=target.debuff.casting.react |
| 5 | `call_action_list` | name=variables |
| 6 | `call_action_list` | name=trinkets |
| 7 | `arcane_torrent` | if=cooldown.mortal_strike.remains>1.5&rage<50 |
| 8 | `lights_judgment` | if=debuff.colossus_smash.down&cooldown.mortal_strike.remains |
| 9 | `bag_of_tricks` | if=debuff.colossus_smash.down&cooldown.mortal_strike.remains |
| 10 | `berserking` | if=target.time_to_die>180&debuff.colossus_smash.up\|target.time_to_die<180&variable.execute_phase&debuff.colossus_smash.up\|target.time_to_die<20 |
| 11 | `blood_fury` | if=debuff.colossus_smash.up |
| 12 | `fireblood` | if=debuff.colossus_smash.up |
| 13 | `ancestral_call` | if=debuff.colossus_smash.up |
| 14 | `invoke_external_buff` | name=power_infusion,if=debuff.colossus_smash.up&fight_remains>=135\|variable.execute_phase&buff.avatar.up\|fight_remains<=25 |
| 15 | `run_action_list` | name=colossus_aoe,if=talent.demolish&active_enemies>2 |
| 16 | `run_action_list` | name=colossus_execute,target_if=min:target.health.pct,if=talent.demolish&variable.execute_phase |
| 17 | `run_action_list` | name=colossus_st,if=talent.demolish |
| 18 | `run_action_list` | name=slayer_aoe,if=talent.slayers_dominance&active_enemies>2 |
| 19 | `run_action_list` | name=slayer_execute,target_if=min:target.health.pct,if=talent.slayers_dominance&variable.execute_phase |
| 20 | `run_action_list` | name=slayer_st,if=talent.slayers_dominance |

## Action List: `colossus_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `thunder_clap` | if=!dot.rend_dot.remains |
| 2 | `rend` | if=!dot.rend_dot.remains |
| 3 | `sweeping_strikes` | if=cooldown.colossus_smash.remains>10&buff.sweeping_strikes.down\|!talent.broad_strokes |
| 4 | `ravager` | if=cooldown.colossus_smash.remains<3 |
| 5 | `avatar` | — |
| 6 | `colossus_smash` | — |
| 7 | `champions_spear` | — |
| 8 | `demolish` | if=buff.colossal_might.stack=10 |
| 9 | `cleave` | — |
| 10 | `demolish` | if=debuff.colossus_smash.remains>=2 |
| 11 | `whirlwind` | if=talent.fervor_of_battle&buff.collateral_damage.stack=3 |
| 12 | `mortal_strike` | — |
| 13 | `execute` | if=buff.sudden_death.remains |
| 14 | `rend` | if=dot.rend_dot.remains<4 |
| 15 | `overpower` | — |
| 16 | `heroic_strike` | — |
| 17 | `rend` | — |
| 18 | `execute` | — |
| 19 | `slam` | — |
| 20 | `bladestorm` | — |
| 21 | `wrecking_throw` | — |
| 22 | `whirlwind` | — |

## Action List: `colossus_execute`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `sweeping_strikes` | if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down\|!talent.broad_strokes) |
| 2 | `rend` | if=dot.rend_dot.remains<=gcd&!talent.bloodletting |
| 3 | `champions_spear` | — |
| 4 | `ravager` | if=cooldown.colossus_smash.remains<=gcd |
| 5 | `avatar` | — |
| 6 | `colossus_smash` | — |
| 7 | `heroic_strike` | — |
| 8 | `demolish` | if=buff.colossal_might.stack=10&debuff.colossus_smash.up |
| 9 | `mortal_strike` | if=buff.executioners_precision.stack=2\|!talent.executioners_precision\|talent.battlelord |
| 10 | `execute` | if=talent.deep_wounds&rage>75\|buff.sudden_death.up |
| 11 | `overpower` | — |
| 12 | `execute` | if=rage>75 |
| 13 | `cleave` | if=buff.ravager.remains\|talent.mass_execution&active_enemies=2 |
| 14 | `execute` | — |
| 15 | `bladestorm` | — |
| 16 | `wrecking_throw` | — |

## Action List: `colossus_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `rend` | if=dot.rend_dot.remains<=gcd\|cooldown.colossus_smash.remains<2&dot.rend_dot.remains<=10 |
| 2 | `sweeping_strikes` | if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down\|!talent.broad_strokes) |
| 3 | `ravager` | if=cooldown.colossus_smash.remains<=gcd |
| 4 | `avatar` | — |
| 5 | `colossus_smash` | — |
| 6 | `cleave` | if=buff.ravager.remains&buff.collateral_damage.stack=3 |
| 7 | `champions_spear` | — |
| 8 | `demolish` | if=debuff.colossus_smash.up&buff.colossal_might.stack>0 |
| 9 | `heroic_strike` | if=active_enemies=2 |
| 10 | `mortal_strike` | — |
| 11 | `heroic_strike` | — |
| 12 | `overpower` | if=active_enemies=2 |
| 13 | `cleave` | if=buff.ravager.remains\|buff.collateral_damage.stack=3 |
| 14 | `overpower` | — |
| 15 | `cleave` | if=talent.mass_execution&target.health.pct<35 |
| 16 | `execute` | — |
| 17 | `whirlwind` | if=active_enemies=2&buff.collateral_damage.stack=3 |
| 18 | `wrecking_throw` | if=active_enemies=1 |
| 19 | `rend` | if=dot.rend_dot.remains<=gcd*5 |
| 20 | `cleave` | if=active_enemies=2 |
| 21 | `slam` | — |

## Action List: `slayer_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `rend` | if=!dot.rend_dot.remains&talent.rend |
| 2 | `sweeping_strikes` | if=!buff.sweeping_strikes.up&cooldown.colossus_smash.remains>10\|!talent.broad_strokes |
| 3 | `avatar` | — |
| 4 | `champions_spear` | — |
| 5 | `ravager` | if=debuff.colossus_smash.up |
| 6 | `colossus_smash` | — |
| 7 | `cleave` | — |
| 8 | `whirlwind` | if=talent.fervor_of_battle&buff.collateral_damage.stack=3 |
| 9 | `execute` | if=buff.sudden_death.up |
| 10 | `bladestorm` | if=debuff.colossus_smash.up |
| 11 | `mortal_strike` | — |
| 12 | `thunder_clap` | if=dot.rend_dot.remains<8&talent.rend |
| 13 | `overpower` | if=talent.dreadnaught |
| 14 | `whirlwind` | if=talent.fervor_of_battle |
| 15 | `overpower` | — |
| 16 | `mortal_strike` | — |
| 17 | `rend` | if=dot.rend_dot.remains |
| 18 | `execute` | — |
| 19 | `wrecking_throw` | — |
| 20 | `whirlwind` | — |
| 21 | `slam` | — |
| 22 | `storm_bolt` | if=buff.bladestorm.up |

## Action List: `slayer_execute`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `sweeping_strikes` | if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down\|!talent.broad_strokes) |
| 2 | `rend` | if=dot.rend_dot.remains<2&!talent.bloodletting |
| 3 | `avatar` | — |
| 4 | `colossus_smash` | — |
| 5 | `heroic_strike` | — |
| 6 | `bladestorm` | if=debuff.colossus_smash.up |
| 7 | `mortal_strike` | if=buff.executioners_precision.stack=2\|debuff.colossus_smash.up |
| 8 | `overpower` | if=buff.opportunist.up&talent.opportunist |
| 9 | `overpower` | if=talent.fierce_followthrough&!buff.battlelord.up&rage<90 |
| 10 | `execute` | if=rage>40\|buff.sudden_death.up |
| 11 | `overpower` | — |
| 12 | `execute` | if=talent.improved_execute |
| 13 | `cleave` | if=talent.mass_execution |
| 14 | `slam` | if=!talent.critical_thinking |
| 15 | `execute` | — |
| 16 | `wrecking_throw` | — |
| 17 | `storm_bolt` | if=buff.bladestorm.up |

## Action List: `slayer_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `sweeping_strikes` | if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down\|!talent.broad_strokes) |
| 2 | `avatar` | — |
| 3 | `champions_spear` | if=debuff.colossus_smash.up\|buff.avatar.up |
| 4 | `ravager` | if=cooldown.colossus_smash.remains<=gcd |
| 5 | `colossus_smash` | — |
| 6 | `bladestorm` | if=debuff.colossus_smash.up |
| 7 | `mortal_strike` | — |
| 8 | `execute` | if=buff.sudden_death.up |
| 9 | `heroic_strike` | — |
| 10 | `cleave` | if=active_enemies=2&buff.collateral_damage.stack=3 |
| 11 | `overpower` | — |
| 12 | `cleave` | if=talent.mass_execution&target.health.pct<35 |
| 13 | `whirlwind` | if=active_enemies=2&buff.collateral_damage.stack=3 |
| 14 | `rend` | if=dot.rend_dot.remains<=5 |
| 15 | `wrecking_throw` | if=active_enemies=1 |
| 16 | `slam` | — |
| 17 | `storm_bolt` | if=buff.bladestorm.up |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | slot=trinket1,if=variable.trinket_1_buffs&(variable.trinket_priority=1\|!variable.trinket_2_buffs\|!trinket.2.has_cooldown)&(buff.avatar.up) |
| 2 | `use_item` | slot=trinket2,if=variable.trinket_2_buffs&(variable.trinket_priority=2\|!variable.trinket_1_buffs\|!trinket.1.has_cooldown)&(buff.avatar.up) |
| 3 | `use_item` | slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1\|!variable.trinket_2_buffs\|!trinket.2.has_cooldown) |
| 4 | `use_item` | slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2\|!variable.trinket_1_buffs\|!trinket.1.has_cooldown) |
| 5 | `use_item` | name=algethar_puzzle_box,if=cooldown.avatar.remains<2\|cooldown.colossus_smash.remains<2 |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=st_planning,value=active_enemies=1&(raid_event.adds.in>15\|!raid_event.adds.exists) |
| 2 | `variable` | name=adds_remain,value=active_enemies>=2&(!raid_event.adds.exists\|raid_event.adds.exists&raid_event.adds.remains>5) |
| 3 | `variable` | name=execute_phase,value=(talent.massacre.enabled&target.health.pct<35)\|target.health.pct<20 |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat=snapshot_stats
actions.precombat+=/variable,name=trinket_1_exclude,value=trinket.1.is.algethar_puzzle_box
actions.precombat+=/variable,name=trinket_2_exclude,value=trinket.2.is.algethar_puzzle_box
actions.precombat+=/variable,name=trinket_1_buffs,value=trinket.1.has_use_buff
actions.precombat+=/variable,name=trinket_2_buffs,value=trinket.2.has_use_buff
actions.precombat+=/variable,name=trinket_1_duration,op=setif,value=0,value_else=trinket.1.proc.any_dps.duration,condition=0
actions.precombat+=/variable,name=trinket_2_duration,op=setif,value=0,value_else=trinket.2.proc.any_dps.duration,condition=0
actions.precombat+=/variable,name=trinket_1_high_value,op=setif,value=2,value_else=1,condition=trinket.1.is.treacherous_transmitter
actions.precombat+=/variable,name=trinket_2_high_value,op=setif,value=2,value_else=1,condition=trinket.2.is.treacherous_transmitter
actions.precombat+=/variable,name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&talent.avatar&trinket.1.cooldown.duration%%cooldown.avatar.duration=0
actions.precombat+=/variable,name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&talent.avatar&trinket.2.cooldown.duration%%cooldown.avatar.duration=0
actions.precombat+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs&(trinket.2.has_cooldown|!trinket.1.has_cooldown)|variable.trinket_2_buffs&((trinket.2.cooldown.duration%variable.trinket_2_duration)*(1.5+trinket.2.has_buff.strength)*(variable.trinket_2_sync)*(variable.trinket_2_high_value)*(1+((trinket.2.ilvl-trinket.1.ilvl)%100)))>((trinket.1.cooldown.duration%variable.trinket_1_duration)*(1.5+trinket.1.has_buff.strength)*(variable.trinket_1_sync)*(variable.trinket_1_high_value)*(1+((trinket.1.ilvl-trinket.2.ilvl)%100)))
actions.precombat+=/variable,name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl
actions.precombat+=/battle_stance,toggle=on

# Executed every time the actor is available.
actions=charge,if=time<=0.5|movement.distance>5
actions+=/auto_attack
actions+=/potion,if=gcd.remains=0&debuff.colossus_smash.remains>8|target.time_to_die<25
actions+=/pummel,if=target.debuff.casting.react
actions+=/call_action_list,name=variables
actions+=/call_action_list,name=trinkets
actions+=/arcane_torrent,if=cooldown.mortal_strike.remains>1.5&rage<50
actions+=/lights_judgment,if=debuff.colossus_smash.down&cooldown.mortal_strike.remains
actions+=/bag_of_tricks,if=debuff.colossus_smash.down&cooldown.mortal_strike.remains
actions+=/berserking,if=target.time_to_die>180&debuff.colossus_smash.up|target.time_to_die<180&variable.execute_phase&debuff.colossus_smash.up|target.time_to_die<20
actions+=/blood_fury,if=debuff.colossus_smash.up
actions+=/fireblood,if=debuff.colossus_smash.up
actions+=/ancestral_call,if=debuff.colossus_smash.up
actions+=/invoke_external_buff,name=power_infusion,if=debuff.colossus_smash.up&fight_remains>=135|variable.execute_phase&buff.avatar.up|fight_remains<=25
actions+=/run_action_list,name=colossus_aoe,if=talent.demolish&active_enemies>2
actions+=/run_action_list,name=colossus_execute,target_if=min:target.health.pct,if=talent.demolish&variable.execute_phase
actions+=/run_action_list,name=colossus_st,if=talent.demolish
actions+=/run_action_list,name=slayer_aoe,if=talent.slayers_dominance&active_enemies>2
actions+=/run_action_list,name=slayer_execute,target_if=min:target.health.pct,if=talent.slayers_dominance&variable.execute_phase
actions+=/run_action_list,name=slayer_st,if=talent.slayers_dominance

actions.colossus_aoe=thunder_clap,if=!dot.rend_dot.remains
actions.colossus_aoe+=/rend,if=!dot.rend_dot.remains
actions.colossus_aoe+=/sweeping_strikes,if=cooldown.colossus_smash.remains>10&buff.sweeping_strikes.down|!talent.broad_strokes
actions.colossus_aoe+=/ravager,if=cooldown.colossus_smash.remains<3
actions.colossus_aoe+=/avatar
actions.colossus_aoe+=/colossus_smash
actions.colossus_aoe+=/champions_spear
actions.colossus_aoe+=/demolish,if=buff.colossal_might.stack=10
actions.colossus_aoe+=/cleave
actions.colossus_aoe+=/demolish,if=debuff.colossus_smash.remains>=2
actions.colossus_aoe+=/whirlwind,if=talent.fervor_of_battle&buff.collateral_damage.stack=3
actions.colossus_aoe+=/mortal_strike
actions.colossus_aoe+=/execute,if=buff.sudden_death.remains
actions.colossus_aoe+=/rend,if=dot.rend_dot.remains<4
actions.colossus_aoe+=/overpower
actions.colossus_aoe+=/heroic_strike
actions.colossus_aoe+=/rend
actions.colossus_aoe+=/execute
actions.colossus_aoe+=/slam
actions.colossus_aoe+=/bladestorm
actions.colossus_aoe+=/wrecking_throw
actions.colossus_aoe+=/whirlwind

actions.colossus_execute=sweeping_strikes,if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down|!talent.broad_strokes)
actions.colossus_execute+=/rend,if=dot.rend_dot.remains<=gcd&!talent.bloodletting
actions.colossus_execute+=/champions_spear
actions.colossus_execute+=/ravager,if=cooldown.colossus_smash.remains<=gcd
actions.colossus_execute+=/avatar
actions.colossus_execute+=/colossus_smash
actions.colossus_execute+=/heroic_strike
actions.colossus_execute+=/demolish,if=buff.colossal_might.stack=10&debuff.colossus_smash.up
actions.colossus_execute+=/mortal_strike,if=buff.executioners_precision.stack=2|!talent.executioners_precision|talent.battlelord
actions.colossus_execute+=/execute,if=talent.deep_wounds&rage>75|buff.sudden_death.up
actions.colossus_execute+=/overpower
actions.colossus_execute+=/execute,if=rage>75
actions.colossus_execute+=/cleave,if=buff.ravager.remains|talent.mass_execution&active_enemies=2
actions.colossus_execute+=/execute
actions.colossus_execute+=/bladestorm
actions.colossus_execute+=/wrecking_throw

actions.colossus_st=rend,if=dot.rend_dot.remains<=gcd|cooldown.colossus_smash.remains<2&dot.rend_dot.remains<=10
actions.colossus_st+=/sweeping_strikes,if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down|!talent.broad_strokes)
actions.colossus_st+=/ravager,if=cooldown.colossus_smash.remains<=gcd
actions.colossus_st+=/avatar
actions.colossus_st+=/colossus_smash
actions.colossus_st+=/cleave,if=buff.ravager.remains&buff.collateral_damage.stack=3
actions.colossus_st+=/champions_spear
actions.colossus_st+=/demolish,if=debuff.colossus_smash.up&buff.colossal_might.stack>0
actions.colossus_st+=/heroic_strike,if=active_enemies=2
actions.colossus_st+=/mortal_strike
actions.colossus_st+=/heroic_strike
actions.colossus_st+=/overpower,if=active_enemies=2
actions.colossus_st+=/cleave,if=buff.ravager.remains|buff.collateral_damage.stack=3
actions.colossus_st+=/overpower
actions.colossus_st+=/cleave,if=talent.mass_execution&target.health.pct<35
actions.colossus_st+=/execute
actions.colossus_st+=/whirlwind,if=active_enemies=2&buff.collateral_damage.stack=3
actions.colossus_st+=/wrecking_throw,if=active_enemies=1
actions.colossus_st+=/rend,if=dot.rend_dot.remains<=gcd*5
actions.colossus_st+=/cleave,if=active_enemies=2
actions.colossus_st+=/slam

actions.slayer_aoe=rend,if=!dot.rend_dot.remains&talent.rend
actions.slayer_aoe+=/sweeping_strikes,if=!buff.sweeping_strikes.up&cooldown.colossus_smash.remains>10|!talent.broad_strokes
actions.slayer_aoe+=/avatar
actions.slayer_aoe+=/champions_spear
actions.slayer_aoe+=/ravager,if=debuff.colossus_smash.up
actions.slayer_aoe+=/colossus_smash
actions.slayer_aoe+=/cleave
actions.slayer_aoe+=/whirlwind,if=talent.fervor_of_battle&buff.collateral_damage.stack=3
actions.slayer_aoe+=/execute,if=buff.sudden_death.up
actions.slayer_aoe+=/bladestorm,if=debuff.colossus_smash.up
actions.slayer_aoe+=/mortal_strike
actions.slayer_aoe+=/thunder_clap,if=dot.rend_dot.remains<8&talent.rend
actions.slayer_aoe+=/overpower,if=talent.dreadnaught
actions.slayer_aoe+=/whirlwind,if=talent.fervor_of_battle
actions.slayer_aoe+=/overpower
actions.slayer_aoe+=/mortal_strike
actions.slayer_aoe+=/rend,if=dot.rend_dot.remains
actions.slayer_aoe+=/execute
actions.slayer_aoe+=/wrecking_throw
actions.slayer_aoe+=/whirlwind
actions.slayer_aoe+=/slam
actions.slayer_aoe+=/storm_bolt,if=buff.bladestorm.up

actions.slayer_execute=sweeping_strikes,if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down|!talent.broad_strokes)
actions.slayer_execute+=/rend,if=dot.rend_dot.remains<2&!talent.bloodletting
actions.slayer_execute+=/avatar
actions.slayer_execute+=/colossus_smash
actions.slayer_execute+=/heroic_strike
actions.slayer_execute+=/bladestorm,if=debuff.colossus_smash.up
actions.slayer_execute+=/mortal_strike,if=buff.executioners_precision.stack=2|debuff.colossus_smash.up
actions.slayer_execute+=/overpower,if=buff.opportunist.up&talent.opportunist
actions.slayer_execute+=/overpower,if=talent.fierce_followthrough&!buff.battlelord.up&rage<90
actions.slayer_execute+=/execute,if=rage>40|buff.sudden_death.up
actions.slayer_execute+=/overpower
actions.slayer_execute+=/execute,if=talent.improved_execute
actions.slayer_execute+=/cleave,if=talent.mass_execution
actions.slayer_execute+=/slam,if=!talent.critical_thinking
actions.slayer_execute+=/execute
actions.slayer_execute+=/wrecking_throw
actions.slayer_execute+=/storm_bolt,if=buff.bladestorm.up

actions.slayer_st=sweeping_strikes,if=active_enemies=2&(cooldown.colossus_smash.remains&buff.sweeping_strikes.down|!talent.broad_strokes)
actions.slayer_st+=/avatar
actions.slayer_st+=/champions_spear,if=debuff.colossus_smash.up|buff.avatar.up
actions.slayer_st+=/ravager,if=cooldown.colossus_smash.remains<=gcd
actions.slayer_st+=/colossus_smash
actions.slayer_st+=/bladestorm,if=debuff.colossus_smash.up
actions.slayer_st+=/mortal_strike
actions.slayer_st+=/execute,if=buff.sudden_death.up
actions.slayer_st+=/heroic_strike
actions.slayer_st+=/cleave,if=active_enemies=2&buff.collateral_damage.stack=3
actions.slayer_st+=/overpower
actions.slayer_st+=/cleave,if=talent.mass_execution&target.health.pct<35
actions.slayer_st+=/whirlwind,if=active_enemies=2&buff.collateral_damage.stack=3
actions.slayer_st+=/rend,if=dot.rend_dot.remains<=5
actions.slayer_st+=/wrecking_throw,if=active_enemies=1
actions.slayer_st+=/slam
actions.slayer_st+=/storm_bolt,if=buff.bladestorm.up

# Trinkets
actions.trinkets=use_item,slot=trinket1,if=variable.trinket_1_buffs&(variable.trinket_priority=1|!variable.trinket_2_buffs|!trinket.2.has_cooldown)&(buff.avatar.up)
actions.trinkets+=/use_item,slot=trinket2,if=variable.trinket_2_buffs&(variable.trinket_priority=2|!variable.trinket_1_buffs|!trinket.1.has_cooldown)&(buff.avatar.up)
actions.trinkets+=/use_item,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1|!variable.trinket_2_buffs|!trinket.2.has_cooldown)
actions.trinkets+=/use_item,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2|!variable.trinket_1_buffs|!trinket.1.has_cooldown)
actions.trinkets+=/use_item,name=algethar_puzzle_box,if=cooldown.avatar.remains<2|cooldown.colossus_smash.remains<2

# Variables
actions.variables=variable,name=st_planning,value=active_enemies=1&(raid_event.adds.in>15|!raid_event.adds.exists)
actions.variables+=/variable,name=adds_remain,value=active_enemies>=2&(!raid_event.adds.exists|raid_event.adds.exists&raid_event.adds.remains>5)
actions.variables+=/variable,name=execute_phase,value=(talent.massacre.enabled&target.health.pct<35)|target.health.pct<20
```
