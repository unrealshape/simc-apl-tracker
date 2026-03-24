# Hunter – Beast Mastery

Auto-generated from SimulationCraft APL | Last updated: 2026-03-24 07:44 UTC

Source: `apl/default/hunter/beast_mastery.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 56
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
| 1 | `auto_shot` | — |
| 2 | `call_action_list` | name=cds |
| 3 | `call_action_list` | name=trinkets |
| 4 | `call_action_list` | name=drst,if=talent.black_arrow&(active_enemies<2\|!talent.beast_cleave&active_enemies<3) |
| 5 | `call_action_list` | name=drcleave,if=talent.black_arrow&(active_enemies>2\|talent.beast_cleave&active_enemies>1) |
| 6 | `call_action_list` | name=st,if=!talent.black_arrow&(active_enemies<2\|!talent.beast_cleave&active_enemies<3) |
| 7 | `call_action_list` | name=cleave,if=!talent.black_arrow&(active_enemies>2\|talent.beast_cleave&active_enemies>1) |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_external_buff` | name=power_infusion,if=buff.bestial_wrath.up\|cooldown.bestial_wrath.remains<30\|fight_remains<16 |
| 2 | `berserking` | if=buff.bestial_wrath.up\|fight_remains<13 |
| 3 | `blood_fury` | if=buff.bestial_wrath.up\|fight_remains<16 |
| 4 | `ancestral_call` | if=buff.bestial_wrath.up\|fight_remains<16 |
| 5 | `fireblood` | if=buff.bestial_wrath.up\|fight_remains<9 |
| 6 | `potion` | if=buff.bestial_wrath.up\|fight_remains<31 |

## Action List: `cleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `barbed_shot` | if=cooldown.bestial_wrath.remains<gcd |
| 2 | `wild_thrash` | — |
| 3 | `bestial_wrath` | — |
| 4 | `kill_command` | — |
| 5 | `cobra_shot` | if=cooldown.wild_thrash.remains>gcd&buff.hogstrider.up&active_enemies<4 |
| 6 | `barbed_shot` | — |
| 7 | `cobra_shot` | if=cooldown.wild_thrash.remains>gcd |

## Action List: `drcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `black_arrow` | if=buff.beast_cleave.remains<gcd |
| 2 | `bestial_wrath` | — |
| 3 | `wailing_arrow` | if=buff.bestial_wrath.remains<execute_time+gcd\|fight_remains<execute_time+gcd |
| 4 | `wild_thrash` | — |
| 5 | `kill_command` | if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.up\|!apex.3 |
| 6 | `black_arrow` | if=buff.withering_fire.up |
| 7 | `barbed_shot` | — |
| 8 | `wailing_arrow` | — |
| 9 | `black_arrow` | — |
| 10 | `cobra_shot` | — |

## Action List: `drst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `bestial_wrath` | — |
| 2 | `kill_command` | if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.up\|!apex.3 |
| 3 | `black_arrow` | if=buff.withering_fire.up |
| 4 | `cobra_shot` | if=talent.killer_cobra&buff.bestial_wrath.up&cooldown.barbed_shot.charges_fractional<1.4 |
| 5 | `wailing_arrow` | if=buff.withering_fire.remains<execute_time+gcd\|time_to_die.remains<execute_time+gcd |
| 6 | `barbed_shot` | — |
| 7 | `black_arrow` | — |
| 8 | `cobra_shot` | — |

## Action List: `st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `barbed_shot` | if=cooldown.bestial_wrath.remains<gcd |
| 2 | `bestial_wrath` | — |
| 3 | `kill_command` | if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&(buff.natures_ally.up\|howl_summon.ready)\|!apex.3 |
| 4 | `barbed_shot` | — |
| 5 | `cobra_shot` | — |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=light_company_guidon,if=buff.bestial_wrath.up\|fight_remains<21 |
| 2 | `use_item` | name=void_execution_mandate,if=buff.bestial_wrath.up\|fight_remains<21 |
| 3 | `use_item` | name=algethar_puzzle_box,if=cooldown.bestial_wrath.remains<2\|fight_remains<23 |
| 4 | `use_item` | name=emberwing_feather,if=buff.bestial_wrath.up\|fight_remains<16 |
| 5 | `use_item` | name=freightrunners_flask,if=cooldown.bestial_wrath.ready\|fight_remains<16 |
| 6 | `use_item` | name=sealed_chaos_urn,if=cooldown.bestial_wrath.ready\|fight_remains<21 |
| 7 | `use_item` | name=evercollapsing_void_fissure,if=cooldown.bestial_wrath.ready\|fight_remains<11 |
| 8 | `use_item` | name=rangercaptains_iridescent_insignia |
| 9 | `use_item` | name=void_stalkers_contract |
| 10 | `use_item` | name=latchs_crooked_hook |

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
actions=auto_shot
actions+=/call_action_list,name=cds
actions+=/call_action_list,name=trinkets
actions+=/call_action_list,name=drst,if=talent.black_arrow&(active_enemies<2|!talent.beast_cleave&active_enemies<3)
actions+=/call_action_list,name=drcleave,if=talent.black_arrow&(active_enemies>2|talent.beast_cleave&active_enemies>1)
actions+=/call_action_list,name=st,if=!talent.black_arrow&(active_enemies<2|!talent.beast_cleave&active_enemies<3)
actions+=/call_action_list,name=cleave,if=!talent.black_arrow&(active_enemies>2|talent.beast_cleave&active_enemies>1)

actions.cds=invoke_external_buff,name=power_infusion,if=buff.bestial_wrath.up|cooldown.bestial_wrath.remains<30|fight_remains<16
actions.cds+=/berserking,if=buff.bestial_wrath.up|fight_remains<13
actions.cds+=/blood_fury,if=buff.bestial_wrath.up|fight_remains<16
actions.cds+=/ancestral_call,if=buff.bestial_wrath.up|fight_remains<16
actions.cds+=/fireblood,if=buff.bestial_wrath.up|fight_remains<9
actions.cds+=/potion,if=buff.bestial_wrath.up|fight_remains<31

actions.cleave=barbed_shot,if=cooldown.bestial_wrath.remains<gcd
actions.cleave+=/wild_thrash
actions.cleave+=/bestial_wrath
actions.cleave+=/kill_command
actions.cleave+=/cobra_shot,if=cooldown.wild_thrash.remains>gcd&buff.hogstrider.up&active_enemies<4
actions.cleave+=/barbed_shot
actions.cleave+=/cobra_shot,if=cooldown.wild_thrash.remains>gcd

actions.drcleave=black_arrow,if=buff.beast_cleave.remains<gcd
actions.drcleave+=/bestial_wrath
actions.drcleave+=/wailing_arrow,if=buff.bestial_wrath.remains<execute_time+gcd|fight_remains<execute_time+gcd
actions.drcleave+=/wild_thrash
actions.drcleave+=/kill_command,if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.up|!apex.3
actions.drcleave+=/black_arrow,if=buff.withering_fire.up
actions.drcleave+=/barbed_shot
actions.drcleave+=/wailing_arrow
actions.drcleave+=/black_arrow
actions.drcleave+=/cobra_shot

actions.drst=bestial_wrath
actions.drst+=/kill_command,if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.up|!apex.3
actions.drst+=/black_arrow,if=buff.withering_fire.up
actions.drst+=/cobra_shot,if=talent.killer_cobra&buff.bestial_wrath.up&cooldown.barbed_shot.charges_fractional<1.4
actions.drst+=/wailing_arrow,if=buff.withering_fire.remains<execute_time+gcd|time_to_die.remains<execute_time+gcd
actions.drst+=/barbed_shot
actions.drst+=/black_arrow
actions.drst+=/cobra_shot

actions.st=barbed_shot,if=cooldown.bestial_wrath.remains<gcd
actions.st+=/bestial_wrath
actions.st+=/kill_command,if=cooldown.bestial_wrath.remains>full_recharge_time+gcd&(buff.natures_ally.up|howl_summon.ready)|!apex.3
actions.st+=/barbed_shot
actions.st+=/cobra_shot

actions.trinkets=use_item,name=light_company_guidon,if=buff.bestial_wrath.up|fight_remains<21
actions.trinkets+=/use_item,name=void_execution_mandate,if=buff.bestial_wrath.up|fight_remains<21
actions.trinkets+=/use_item,name=algethar_puzzle_box,if=cooldown.bestial_wrath.remains<2|fight_remains<23
actions.trinkets+=/use_item,name=emberwing_feather,if=buff.bestial_wrath.up|fight_remains<16
actions.trinkets+=/use_item,name=freightrunners_flask,if=cooldown.bestial_wrath.ready|fight_remains<16
actions.trinkets+=/use_item,name=sealed_chaos_urn,if=cooldown.bestial_wrath.ready|fight_remains<21
actions.trinkets+=/use_item,name=evercollapsing_void_fissure,if=cooldown.bestial_wrath.ready|fight_remains<11
actions.trinkets+=/use_item,name=rangercaptains_iridescent_insignia
actions.trinkets+=/use_item,name=void_stalkers_contract
actions.trinkets+=/use_item,name=latchs_crooked_hook
```
