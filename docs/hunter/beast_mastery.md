# Hunter – Beast Mastery

Auto-generated from SimulationCraft APL | Last updated: 2026-09-17 08:33 UTC

Source: `apl/default/hunter/beast_mastery.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 55
- **Lists:** `precombat`, `default`, `cds`, `cleave`, `drcleave`, `drst`, `st`, `trinkets`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `summon_pet` | — |
| 2 | `snapshot_stats` | — |
| 3 | `use_item` | name=algethar_puzzle_box |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `retarget` | target_if=max:target.health,line_cd=5,if=fight_style.dungeonroute |
| 2 | `auto_shot` | — |
| 3 | `call_action_list` | name=cds |
| 4 | `call_action_list` | name=trinkets |
| 5 | `call_action_list` | name=drst,if=talent.black_arrow&(active_enemies<2\|!talent.beast_cleave&active_enemies<3) |
| 6 | `call_action_list` | name=drcleave,if=talent.black_arrow&(active_enemies>2\|talent.beast_cleave&active_enemies>1) |
| 7 | `call_action_list` | name=st,if=!talent.black_arrow&(active_enemies<2\|!talent.beast_cleave&active_enemies<3) |
| 8 | `call_action_list` | name=cleave,if=!talent.black_arrow&(active_enemies>2\|talent.beast_cleave&active_enemies>1) |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_external_buff` | name=power_infusion,if=buff.bestial_wrath.up\|cooldown.bestial_wrath.remains<30\|fight_remains<16 |
| 2 | `berserking` | if=cooldown.bestial_wrath.ready\|fight_remains<13 |
| 3 | `blood_fury` | if=cooldown.bestial_wrath.ready\|fight_remains<16 |
| 4 | `ancestral_call` | if=cooldown.bestial_wrath.ready\|fight_remains<16 |
| 5 | `fireblood` | if=cooldown.bestial_wrath.ready\|fight_remains<9 |
| 6 | `potion` | if=cooldown.bestial_wrath.ready\|fight_remains<31 |

## Action List: `cleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `wild_thrash` | if=talent.beast_cleave&(prev_gcd.1.bestial_wrath\|!buff.beast_cleave.up) |
| 2 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage,if=full_recharge_time<gcd |
| 3 | `bestial_wrath` | if=buff.beast_cleave.remains\|!talent.beast_cleave\|!talent.wild_thrash |
| 4 | `wild_thrash` | if=talent.beast_cleave&cooldown.bestial_wrath.remains>buff.beast_cleave.remains\|!talent.beast_cleave |
| 5 | `kill_command` | if=buff.natures_ally.react\|talent.master_handler&(active_enemies>3\|howl_summon.ready)\|!apex.3 |
| 6 | `cobra_shot` | if=buff.cobra_fang.up&buff.beast_cleave.remains |
| 7 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage |
| 8 | `cobra_shot` | if=talent.beast_cleave&cooldown.wild_thrash.remains>gcd\|!talent.beast_cleave |

## Action List: `drcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `black_arrow` | if=buff.beast_cleave.remains<gcd&cooldown.bestial_wrath.remains<gcd&active_enemies>2 |
| 2 | `bestial_wrath` | if=buff.beast_cleave.remains\|!talent.beast_cleave |
| 3 | `wild_thrash` | if=talent.beast_cleave&(prev_gcd.1.bestial_wrath\|!buff.beast_cleave.up\|cooldown.bestial_wrath.remains>buff.beast_cleave.remains)\|!talent.beast_cleave |
| 4 | `kill_command` | if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react\|!apex.3 |
| 5 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage,if=full_recharge_time<1*gcd |
| 6 | `black_arrow` | if=buff.withering_fire.up |
| 7 | `wailing_arrow` | if=buff.withering_fire.remains<execute_time+gcd\|time_to_die.remains<execute_time+gcd |
| 8 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage |
| 9 | `black_arrow` | — |
| 10 | `wailing_arrow` | — |
| 11 | `cobra_shot` | — |

## Action List: `drst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage,if=(talent.bloody_frenzy&talent.snakeskin_quiver&talent.jagged_wounds)&cooldown.bestial_wrath.remains<2*gcd |
| 2 | `bestial_wrath` | — |
| 3 | `black_arrow` | if=buff.withering_fire.up&cooldown.kill_command.full_recharge_time>gcd |
| 4 | `kill_command` | if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react\|!apex.3 |
| 5 | `wailing_arrow` | if=buff.withering_fire.remains<execute_time+2*gcd\|time_to_die.remains<execute_time+gcd |
| 6 | `cobra_shot` | if=buff.cobra_fang.at_max_stacks |
| 7 | `cobra_shot` | if=talent.killer_cobra&buff.bestial_wrath.up&cooldown.barbed_shot.charges_fractional<1.4 |
| 8 | `black_arrow` | — |
| 9 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage |
| 10 | `cobra_shot` | if=cooldown.bestial_wrath.remains>gcd |

## Action List: `st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `barbed_shot` | target_if=min:dot.barbed_shot.remains\|max_prio_damage,if=cooldown.bestial_wrath.remains<gcd\|full_recharge_time<gcd |
| 2 | `bestial_wrath` | — |
| 3 | `wild_thrash` | if=active_enemies>1 |
| 4 | `kill_command` | if=howl_summon.ready\|(cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react\|!apex.3)&(buff.howl_of_the_pack_leader_cooldown.remains>4\|cooldown.kill_command.charges_fractional>1.8) |
| 5 | `cobra_shot` | if=buff.cobra_fang.at_max_stacks |
| 6 | `barbed_shot` | if=(focus<75\|full_recharge_time<gcd)&!talent.serpentine_strikes\|talent.serpentine_strikes |
| 7 | `cobra_shot` | if=cooldown.bestial_wrath.remains>gcd |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(cooldown.bestial_wrath.ready\|cooldown.bestial_wrath.remains<this_trinket.proc.any_dps.duration-15)\|fight_remains<21 |
| 2 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&!potion.liquid_luster\|!equipped.font_of_venomous_rage\|((buff.liquid_luster.up&buff.liquid_luster.remains<6)\|(fight_remains<cooldown.potion.remains&!buff.liquid_luster.up))\|fight_remains<10 |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=summon_pet
actions.precombat+=/snapshot_stats
actions.precombat+=/use_item,name=algethar_puzzle_box

# Executed every time the actor is available.
actions=retarget,target_if=max:target.health,line_cd=5,if=fight_style.dungeonroute
actions+=/auto_shot
actions+=/call_action_list,name=cds
actions+=/call_action_list,name=trinkets
actions+=/call_action_list,name=drst,if=talent.black_arrow&(active_enemies<2|!talent.beast_cleave&active_enemies<3)
actions+=/call_action_list,name=drcleave,if=talent.black_arrow&(active_enemies>2|talent.beast_cleave&active_enemies>1)
actions+=/call_action_list,name=st,if=!talent.black_arrow&(active_enemies<2|!talent.beast_cleave&active_enemies<3)
actions+=/call_action_list,name=cleave,if=!talent.black_arrow&(active_enemies>2|talent.beast_cleave&active_enemies>1)

actions.cds=invoke_external_buff,name=power_infusion,if=buff.bestial_wrath.up|cooldown.bestial_wrath.remains<30|fight_remains<16
actions.cds+=/berserking,if=cooldown.bestial_wrath.ready|fight_remains<13
actions.cds+=/blood_fury,if=cooldown.bestial_wrath.ready|fight_remains<16
actions.cds+=/ancestral_call,if=cooldown.bestial_wrath.ready|fight_remains<16
actions.cds+=/fireblood,if=cooldown.bestial_wrath.ready|fight_remains<9
actions.cds+=/potion,if=cooldown.bestial_wrath.ready|fight_remains<31

# Bestial Wrath spawns an Apex Pet which casts Bestial Wrath 1.5s after, but it does not get the Beast Cleave that was active prior to Bestial Wrath. Therefore, to ensure this hit cleaves, Wild Thrash needs to follow up Bestial Wrath.
actions.cleave=wild_thrash,if=talent.beast_cleave&(prev_gcd.1.bestial_wrath|!buff.beast_cleave.up)
actions.cleave+=/barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage,if=full_recharge_time<gcd
actions.cleave+=/bestial_wrath,if=buff.beast_cleave.remains|!talent.beast_cleave|!talent.wild_thrash
actions.cleave+=/wild_thrash,if=talent.beast_cleave&cooldown.bestial_wrath.remains>buff.beast_cleave.remains|!talent.beast_cleave
actions.cleave+=/kill_command,if=buff.natures_ally.react|talent.master_handler&(active_enemies>3|howl_summon.ready)|!apex.3
actions.cleave+=/cobra_shot,if=buff.cobra_fang.up&buff.beast_cleave.remains
actions.cleave+=/barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage
actions.cleave+=/cobra_shot,if=talent.beast_cleave&cooldown.wild_thrash.remains>gcd|!talent.beast_cleave

actions.drcleave=black_arrow,if=buff.beast_cleave.remains<gcd&cooldown.bestial_wrath.remains<gcd&active_enemies>2
actions.drcleave+=/bestial_wrath,if=buff.beast_cleave.remains|!talent.beast_cleave
actions.drcleave+=/wild_thrash,if=talent.beast_cleave&(prev_gcd.1.bestial_wrath|!buff.beast_cleave.up|cooldown.bestial_wrath.remains>buff.beast_cleave.remains)|!talent.beast_cleave
actions.drcleave+=/kill_command,if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react|!apex.3
actions.drcleave+=/barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage,if=full_recharge_time<1*gcd
actions.drcleave+=/black_arrow,if=buff.withering_fire.up
actions.drcleave+=/wailing_arrow,if=buff.withering_fire.remains<execute_time+gcd|time_to_die.remains<execute_time+gcd
actions.drcleave+=/barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage
actions.drcleave+=/black_arrow
actions.drcleave+=/wailing_arrow
actions.drcleave+=/cobra_shot

actions.drst=barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage,if=(talent.bloody_frenzy&talent.snakeskin_quiver&talent.jagged_wounds)&cooldown.bestial_wrath.remains<2*gcd
actions.drst+=/bestial_wrath
actions.drst+=/black_arrow,if=buff.withering_fire.up&cooldown.kill_command.full_recharge_time>gcd
actions.drst+=/kill_command,if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react|!apex.3
actions.drst+=/wailing_arrow,if=buff.withering_fire.remains<execute_time+2*gcd|time_to_die.remains<execute_time+gcd
actions.drst+=/cobra_shot,if=buff.cobra_fang.at_max_stacks
actions.drst+=/cobra_shot,if=talent.killer_cobra&buff.bestial_wrath.up&cooldown.barbed_shot.charges_fractional<1.4
actions.drst+=/black_arrow
actions.drst+=/barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage
actions.drst+=/cobra_shot,if=cooldown.bestial_wrath.remains>gcd

actions.st=barbed_shot,target_if=min:dot.barbed_shot.remains|max_prio_damage,if=cooldown.bestial_wrath.remains<gcd|full_recharge_time<gcd
actions.st+=/bestial_wrath
actions.st+=/wild_thrash,if=active_enemies>1
actions.st+=/kill_command,if=howl_summon.ready|(cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react|!apex.3)&(buff.howl_of_the_pack_leader_cooldown.remains>4|cooldown.kill_command.charges_fractional>1.8)
actions.st+=/cobra_shot,if=buff.cobra_fang.at_max_stacks
actions.st+=/barbed_shot,if=(focus<75|full_recharge_time<gcd)&!talent.serpentine_strikes|talent.serpentine_strikes
actions.st+=/cobra_shot,if=cooldown.bestial_wrath.remains>gcd

actions.trinkets=use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(cooldown.bestial_wrath.ready|cooldown.bestial_wrath.remains<this_trinket.proc.any_dps.duration-15)|fight_remains<21
actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&!potion.liquid_luster|!equipped.font_of_venomous_rage|((buff.liquid_luster.up&buff.liquid_luster.remains<6)|(fight_remains<cooldown.potion.remains&!buff.liquid_luster.up))|fight_remains<10
```
