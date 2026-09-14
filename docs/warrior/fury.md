# Warrior – Fury

Auto-generated from SimulationCraft APL | Last updated: 2026-09-14 08:47 UTC

Source: `apl/default/warrior/fury.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 121
- **Lists:** `precombat`, `default`, `slayer`, `slayer_aoe`, `thane`, `thane_aoe`, `trinkets`, `variables`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `berserker_stance` | toggle=on |
| 3 | `variable` | name=trinket_1_exclude,value=trinket.1.is.algethar_puzzle_box |
| 4 | `variable` | name=trinket_2_exclude,value=trinket.2.is.algethar_puzzle_box |
| 5 | `variable` | name=trinket_1_buffs,value=trinket.1.has_use_buff |
| 6 | `variable` | name=trinket_2_buffs,value=trinket.2.has_use_buff |
| 7 | `variable` | name=trinket_1_duration,op=setif,value=0,value_else=trinket.1.proc.any_dps.duration,condition=0 |
| 8 | `variable` | name=trinket_2_duration,op=setif,value=0,value_else=trinket.2.proc.any_dps.duration,condition=0 |
| 9 | `variable` | name=trinket_1_high_value,op=setif,value=2,value_else=1,condition=trinket.1.is.treacherous_transmitter |
| 10 | `variable` | name=trinket_2_high_value,op=setif,value=2,value_else=1,condition=trinket.2.is.treacherous_transmitter |
| 11 | `variable` | name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&talent.recklessness&trinket.1.cooldown.duration%%cooldown.recklessness.duration=0 |
| 12 | `variable` | name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&talent.recklessness&trinket.2.cooldown.duration%%cooldown.recklessness.duration=0 |
| 13 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs&(trinket.2.has_cooldown\|!trinket.1.has_cooldown)\|variable.trinket_2_buffs&((trinket.2.cooldown.duration%variable.trinket_2_duration)*(1.5+trinket.2.has_buff.strength)*(variable.trinket_2_sync)*(variable.trinket_2_high_value)*(1+((trinket.2.ilvl-trinket.1.ilvl)%100)))>((trinket.1.cooldown.duration%variable.trinket_1_duration)*(1.5+trinket.1.has_buff.strength)*(variable.trinket_1_sync)*(variable.trinket_1_high_value)*(1+((trinket.1.ilvl-trinket.2.ilvl)%100))) |
| 14 | `variable` | name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl |
| 15 | `variable` | name=trinket_1_manual,value=trinket.1.is.algethar_puzzle_box |
| 16 | `variable` | name=trinket_1_manual,value=trinket.2.is.algethar_puzzle_box |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `charge` | if=time<=0.5\|movement.distance>5 |
| 3 | `heroic_leap` | if=(raid_event.movement.distance>25&raid_event.movement.in>45) |
| 4 | `potion` | if=target.time_to_die>300\|buff.recklessness.up\|target.time_to_die<25 |
| 5 | `pummel` | if=target.debuff.casting.react |
| 6 | `call_action_list` | name=trinkets |
| 7 | `call_action_list` | name=variables |
| 8 | `lights_judgment` | if=variable.on_gcd_racials |
| 9 | `bag_of_tricks` | if=variable.on_gcd_racials |
| 10 | `berserking` | if=buff.recklessness.up |
| 11 | `blood_fury` | — |
| 12 | `fireblood` | — |
| 13 | `ancestral_call` | — |
| 14 | `invoke_external_buff` | name=power_infusion,if=buff.recklessness.remains>15&fight_remains>=135\|variable.execute_phase&buff.recklessness.up\|fight_remains<=25 |
| 15 | `run_action_list` | name=slayer,if=talent.slayers_dominance&active_enemies=1 |
| 16 | `run_action_list` | name=slayer_aoe,if=talent.slayers_dominance&active_enemies>1 |
| 17 | `run_action_list` | name=thane,if=talent.lightning_strikes&active_enemies=1 |
| 18 | `run_action_list` | name=thane_aoe,if=talent.lightning_strikes&active_enemies>1 |

## Action List: `slayer`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `recklessness` | — |
| 2 | `rampage` | if=buff.enrage.remains<gcd |
| 3 | `rampage` | if=buff.recklessness.up&rage>=100 |
| 4 | `rampage` | if=buff.recklessness.up&cooldown.bladestorm.ready |
| 5 | `bladestorm` | if=buff.recklessness.up\|target.time_to_die<=5 |
| 6 | `execute` | if=buff.recklessness.up&buff.sudden_death.up |
| 7 | `rampage` | if=buff.recklessness.up&!buff.hack_and_slash.up |
| 8 | `crushing_blow` | — |
| 9 | `odyns_fury` | if=buff.recklessness.up |
| 10 | `execute` | if=buff.recklessness.up |
| 11 | `bloodbath` | — |
| 12 | `odyns_fury` | if=buff.recklessness.up |
| 13 | `rampage` | if=rage>100 |
| 14 | `execute` | — |
| 15 | `execute` | if=buff.sudden_death.up |
| 16 | `odyns_fury` | — |
| 17 | `execute` | — |
| 18 | `raging_blow` | — |
| 19 | `rampage` | — |
| 20 | `bloodthirst` | — |
| 21 | `whirlwind` | — |
| 22 | `storm_bolt` | if=buff.bladestorm.up |

## Action List: `slayer_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `whirlwind` | if=talent.improved_whirlwind&buff.whirlwind.stack=0 |
| 2 | `recklessness` | — |
| 3 | `avatar` | — |
| 4 | `rampage` | — |
| 5 | `bladestorm` | if=buff.recklessness.up\|target.time_to_die<=5 |
| 6 | `execute` | if=buff.sudden_death.up |
| 7 | `odyns_fury` | — |
| 8 | `crushing_blow` | — |
| 9 | `bloodbath` | — |
| 10 | `execute` | — |
| 11 | `raging_blow` | — |
| 12 | `bloodthirst` | — |
| 13 | `whirlwind` | — |
| 14 | `storm_bolt` | if=buff.bladestorm.up |

## Action List: `thane`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `recklessness` | — |
| 2 | `avatar` | — |
| 3 | `rampage` | if=buff.enrage.remains<gcd\|rage>=100 |
| 4 | `bloodbath` | if=buff.recklessness.up&buff.fury_mid2_4pc_crit.stack<2 |
| 5 | `thunder_blast` | if=buff.thunder_blast.stack=2\|buff.avatar.remains<2\|buff.thunder_blast.remains<2 |
| 6 | `crushing_blow` | if=buff.hack_and_slash.up |
| 7 | `bloodbath` | — |
| 8 | `rampage` | if=buff.recklessness.up |
| 9 | `thunder_blast` | if=buff.avatar.up |
| 10 | `crushing_blow` | — |
| 11 | `raging_blow` | if=buff.hack_and_slash.up |
| 12 | `thunder_blast` | — |
| 13 | `rampage` | — |
| 14 | `bloodthirst` | — |
| 15 | `execute` | if=talent.deep_wounds |
| 16 | `raging_blow` | — |
| 17 | `odyns_fury` | — |
| 18 | `thunder_clap` | if=buff.avatar.up&!talent.wrath_and_fury |
| 19 | `execute` | — |
| 20 | `thunder_clap` | — |

## Action List: `thane_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `odyns_fury` | — |
| 2 | `recklessness` | — |
| 3 | `avatar` | — |
| 4 | `rampage` | if=!buff.enrage.up |
| 5 | `thunder_blast` | — |
| 6 | `thunder_blast` | if=buff.thunder_blast.stack=2 |
| 7 | `thunder_blast` | if=buff.avatar.up |
| 8 | `thunder_clap` | if=talent.improved_whirlwind&buff.whirlwind.stack=0\|(buff.avatar.up&active_enemies>6) |
| 9 | `rampage` | if=buff.enrage.remains<gcd\|rage>=100 |
| 10 | `bloodbath` | — |
| 11 | `crushing_blow` | if=buff.hack_and_slash.up |
| 12 | `rampage` | if=buff.recklessness.up |
| 13 | `thunder_clap` | if=buff.avatar.up |
| 14 | `crushing_blow` | — |
| 15 | `bloodthirst` | — |
| 16 | `thunder_blast` | — |
| 17 | `raging_blow` | if=buff.hack_and_slash.up |
| 18 | `execute` | — |
| 19 | `rampage` | — |
| 20 | `thunder_clap` | — |
| 21 | `raging_blow` | — |
| 22 | `whirlwind` | — |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=algethar_puzzle_box,if=cooldown.recklessness.remains<2 |
| 2 | `use_item` | slot=trinket1,if=variable.trinket_1_buffs&(variable.trinket_priority=1\|!variable.trinket_2_buffs\|!trinket.2.has_cooldown)&(buff.recklessness.up) |
| 3 | `use_item` | slot=trinket2,if=variable.trinket_2_buffs&(variable.trinket_priority=2\|!variable.trinket_1_buffs\|!trinket.1.has_cooldown)&(buff.recklessness.up) |
| 4 | `use_item` | slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1\|!variable.trinket_2_buffs\|!trinket.2.has_cooldown) |
| 5 | `use_item` | slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2\|!variable.trinket_1_buffs\|!trinket.1.has_cooldown) |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=st_planning,value=active_enemies=1&(raid_event.adds.in>15\|!raid_event.adds.exists) |
| 2 | `variable` | name=adds_remain,value=active_enemies>=2&(!raid_event.adds.exists\|raid_event.adds.exists&raid_event.adds.remains>5) |
| 3 | `variable` | name=execute_phase,value=(talent.massacre.enabled&target.health.pct<35)\|target.health.pct<20 |
| 4 | `variable` | name=on_gcd_racials,value=buff.recklessness.down&buff.recklessness.down&rage<80&buff.sudden_death.down&!cooldown.bladestorm.ready&(!cooldown.execute.ready\|!variable.execute_phase) |

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
actions.precombat+=/berserker_stance,toggle=on
actions.precombat+=/variable,name=trinket_1_exclude,value=trinket.1.is.algethar_puzzle_box
actions.precombat+=/variable,name=trinket_2_exclude,value=trinket.2.is.algethar_puzzle_box
actions.precombat+=/variable,name=trinket_1_buffs,value=trinket.1.has_use_buff
actions.precombat+=/variable,name=trinket_2_buffs,value=trinket.2.has_use_buff
actions.precombat+=/variable,name=trinket_1_duration,op=setif,value=0,value_else=trinket.1.proc.any_dps.duration,condition=0
actions.precombat+=/variable,name=trinket_2_duration,op=setif,value=0,value_else=trinket.2.proc.any_dps.duration,condition=0
actions.precombat+=/variable,name=trinket_1_high_value,op=setif,value=2,value_else=1,condition=trinket.1.is.treacherous_transmitter
actions.precombat+=/variable,name=trinket_2_high_value,op=setif,value=2,value_else=1,condition=trinket.2.is.treacherous_transmitter
actions.precombat+=/variable,name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&talent.recklessness&trinket.1.cooldown.duration%%cooldown.recklessness.duration=0
actions.precombat+=/variable,name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&talent.recklessness&trinket.2.cooldown.duration%%cooldown.recklessness.duration=0
actions.precombat+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs&(trinket.2.has_cooldown|!trinket.1.has_cooldown)|variable.trinket_2_buffs&((trinket.2.cooldown.duration%variable.trinket_2_duration)*(1.5+trinket.2.has_buff.strength)*(variable.trinket_2_sync)*(variable.trinket_2_high_value)*(1+((trinket.2.ilvl-trinket.1.ilvl)%100)))>((trinket.1.cooldown.duration%variable.trinket_1_duration)*(1.5+trinket.1.has_buff.strength)*(variable.trinket_1_sync)*(variable.trinket_1_high_value)*(1+((trinket.1.ilvl-trinket.2.ilvl)%100)))
actions.precombat+=/variable,name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl
actions.precombat+=/variable,name=trinket_1_manual,value=trinket.1.is.algethar_puzzle_box
actions.precombat+=/variable,name=trinket_1_manual,value=trinket.2.is.algethar_puzzle_box

# Executed every time the actor is available.
actions=auto_attack
actions+=/charge,if=time<=0.5|movement.distance>5
actions+=/heroic_leap,if=(raid_event.movement.distance>25&raid_event.movement.in>45)
actions+=/potion,if=target.time_to_die>300|buff.recklessness.up|target.time_to_die<25
actions+=/pummel,if=target.debuff.casting.react
actions+=/call_action_list,name=trinkets
actions+=/call_action_list,name=variables
actions+=/lights_judgment,if=variable.on_gcd_racials
actions+=/bag_of_tricks,if=variable.on_gcd_racials
actions+=/berserking,if=buff.recklessness.up
actions+=/blood_fury
actions+=/fireblood
actions+=/ancestral_call
actions+=/invoke_external_buff,name=power_infusion,if=buff.recklessness.remains>15&fight_remains>=135|variable.execute_phase&buff.recklessness.up|fight_remains<=25
actions+=/run_action_list,name=slayer,if=talent.slayers_dominance&active_enemies=1
actions+=/run_action_list,name=slayer_aoe,if=talent.slayers_dominance&active_enemies>1
actions+=/run_action_list,name=thane,if=talent.lightning_strikes&active_enemies=1
actions+=/run_action_list,name=thane_aoe,if=talent.lightning_strikes&active_enemies>1

actions.slayer=recklessness
actions.slayer+=/rampage,if=buff.enrage.remains<gcd
actions.slayer+=/rampage,if=buff.recklessness.up&rage>=100
actions.slayer+=/rampage,if=buff.recklessness.up&cooldown.bladestorm.ready
actions.slayer+=/bladestorm,if=buff.recklessness.up|target.time_to_die<=5
actions.slayer+=/execute,if=buff.recklessness.up&buff.sudden_death.up
actions.slayer+=/rampage,if=buff.recklessness.up&!buff.hack_and_slash.up
actions.slayer+=/crushing_blow
actions.slayer+=/odyns_fury,if=buff.recklessness.up
actions.slayer+=/execute,if=buff.recklessness.up
actions.slayer+=/bloodbath
actions.slayer+=/odyns_fury,if=buff.recklessness.up
actions.slayer+=/rampage,if=rage>100
actions.slayer+=/execute
actions.slayer+=/execute,if=buff.sudden_death.up
actions.slayer+=/odyns_fury
actions.slayer+=/execute
actions.slayer+=/raging_blow
actions.slayer+=/rampage
actions.slayer+=/bloodthirst
actions.slayer+=/whirlwind
actions.slayer+=/storm_bolt,if=buff.bladestorm.up

actions.slayer_aoe=whirlwind,if=talent.improved_whirlwind&buff.whirlwind.stack=0
actions.slayer_aoe+=/recklessness
actions.slayer_aoe+=/avatar
actions.slayer_aoe+=/rampage
actions.slayer_aoe+=/bladestorm,if=buff.recklessness.up|target.time_to_die<=5
actions.slayer_aoe+=/execute,if=buff.sudden_death.up
actions.slayer_aoe+=/odyns_fury
actions.slayer_aoe+=/crushing_blow
actions.slayer_aoe+=/bloodbath
actions.slayer_aoe+=/execute
actions.slayer_aoe+=/raging_blow
actions.slayer_aoe+=/bloodthirst
actions.slayer_aoe+=/whirlwind
actions.slayer_aoe+=/storm_bolt,if=buff.bladestorm.up

actions.thane=recklessness
actions.thane+=/avatar
actions.thane+=/rampage,if=buff.enrage.remains<gcd|rage>=100
actions.thane+=/bloodbath,if=buff.recklessness.up&buff.fury_mid2_4pc_crit.stack<2
actions.thane+=/thunder_blast,if=buff.thunder_blast.stack=2|buff.avatar.remains<2|buff.thunder_blast.remains<2
actions.thane+=/crushing_blow,if=buff.hack_and_slash.up
actions.thane+=/bloodbath
actions.thane+=/rampage,if=buff.recklessness.up
actions.thane+=/thunder_blast,if=buff.avatar.up
actions.thane+=/crushing_blow
actions.thane+=/raging_blow,if=buff.hack_and_slash.up
actions.thane+=/thunder_blast
actions.thane+=/rampage
actions.thane+=/bloodthirst
actions.thane+=/execute,if=talent.deep_wounds
actions.thane+=/raging_blow
actions.thane+=/odyns_fury
actions.thane+=/thunder_clap,if=buff.avatar.up&!talent.wrath_and_fury
actions.thane+=/execute
actions.thane+=/thunder_clap

actions.thane_aoe=odyns_fury
actions.thane_aoe+=/recklessness
actions.thane_aoe+=/avatar
actions.thane_aoe+=/rampage,if=!buff.enrage.up
actions.thane_aoe+=/thunder_blast
actions.thane_aoe+=/thunder_blast,if=buff.thunder_blast.stack=2
actions.thane_aoe+=/thunder_blast,if=buff.avatar.up
actions.thane_aoe+=/thunder_clap,if=talent.improved_whirlwind&buff.whirlwind.stack=0|(buff.avatar.up&active_enemies>6)
actions.thane_aoe+=/rampage,if=buff.enrage.remains<gcd|rage>=100
actions.thane_aoe+=/bloodbath
actions.thane_aoe+=/crushing_blow,if=buff.hack_and_slash.up
actions.thane_aoe+=/rampage,if=buff.recklessness.up
actions.thane_aoe+=/thunder_clap,if=buff.avatar.up
actions.thane_aoe+=/crushing_blow
actions.thane_aoe+=/bloodthirst
actions.thane_aoe+=/thunder_blast
actions.thane_aoe+=/raging_blow,if=buff.hack_and_slash.up
actions.thane_aoe+=/execute
actions.thane_aoe+=/rampage
actions.thane_aoe+=/thunder_clap
actions.thane_aoe+=/raging_blow
actions.thane_aoe+=/whirlwind

actions.trinkets=use_item,name=algethar_puzzle_box,if=cooldown.recklessness.remains<2
# Trinkets
actions.trinkets+=/use_item,slot=trinket1,if=variable.trinket_1_buffs&(variable.trinket_priority=1|!variable.trinket_2_buffs|!trinket.2.has_cooldown)&(buff.recklessness.up)
actions.trinkets+=/use_item,slot=trinket2,if=variable.trinket_2_buffs&(variable.trinket_priority=2|!variable.trinket_1_buffs|!trinket.1.has_cooldown)&(buff.recklessness.up)
actions.trinkets+=/use_item,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1|!variable.trinket_2_buffs|!trinket.2.has_cooldown)
actions.trinkets+=/use_item,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2|!variable.trinket_1_buffs|!trinket.1.has_cooldown)

# Variables
actions.variables=variable,name=st_planning,value=active_enemies=1&(raid_event.adds.in>15|!raid_event.adds.exists)
actions.variables+=/variable,name=adds_remain,value=active_enemies>=2&(!raid_event.adds.exists|raid_event.adds.exists&raid_event.adds.remains>5)
actions.variables+=/variable,name=execute_phase,value=(talent.massacre.enabled&target.health.pct<35)|target.health.pct<20
actions.variables+=/variable,name=on_gcd_racials,value=buff.recklessness.down&buff.recklessness.down&rage<80&buff.sudden_death.down&!cooldown.bladestorm.ready&(!cooldown.execute.ready|!variable.execute_phase)
```
