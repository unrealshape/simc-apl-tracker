# Druid – Balance

Auto-generated from SimulationCraft APL | Last updated: 2026-03-25 04:59 UTC

Source: `apl/default/druid/balance.simc`

---

## Overview

- **Action Lists:** 5
- **Total Actions:** 81
- **Lists:** `precombat`, `default`, `aoe`, `ec_st`, `kotg_st`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `variable` | name=no_cd_talent,value=!talent.celestial_alignment&!talent.incarnation_chosen_of_elune\|druid.no_cds |
| 3 | `variable` | name=opener,op=set,value=1 |
| 4 | `variable` | name=ec,op=set,value=1,if=talent.boundless_moonlight |
| 5 | `variable` | name=on_use_trinket,value=0 |
| 6 | `variable` | name=on_use_trinket,op=add,value=trinket.1.has_use_buff |
| 7 | `variable` | name=on_use_trinket,op=add,value=(trinket.2.has_use_buff)*2 |
| 8 | `variable` | name=prio,op=set,value=0 |
| 9 | `variable` | name=inc_charge,op=set,value=0 |
| 10 | `moonkin_form` | — |
| 11 | `wrath` | — |
| 12 | `wrath` | — |
| 13 | `wrath` | if=talent.dream_surge&enemies=1 |
| 14 | `starfire` | if=hero_tree.elunes_chosen\|enemies>1 |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | if=buff.ca_inc.up&(buff.harmony_of_the_grove.up\|!talent.dream_surge)\|fight_remains<cooldown.ca_inc.remains |
| 2 | `potion` | if=buff.harmony_of_the_grove.up&buff.ca_inc.up&!variable.ec\|buff.ca_inc.up&variable.ec\|variable.opener&prev_gcd.1.solar_eclipse\|fight_remains<=30 |
| 3 | `berserking` | if=buff.ca_inc.up&(buff.harmony_of_the_grove.up\|!talent.dream_surge)\|fight_remains<cooldown.ca_inc.remains |
| 4 | `invoke_external_buff` | name=power_infusion,if=buff.ca_inc.up |
| 5 | `variable` | name=inc_charge,op=set,value=1,if=cooldown.ca_inc.charges_fractional<1 |
| 6 | `variable` | name=opener,op=set,value=0,if=buff.ca_inc.up |
| 7 | `variable` | name=eclipse_down,value=!buff.eclipse_lunar.up&!buff.eclipse_solar.up |
| 8 | `variable` | name=cd_window,value=cooldown.force_of_nature.remains>15\|cooldown.ca_inc.remains<44 |
| 9 | `variable` | name=cd_window_narrow,value=cooldown.force_of_nature.remains>30\|cooldown.ca_inc.remains>10&cooldown.ca_inc.remains<20 |
| 10 | `variable` | name=no_weaver_procs,value=!buff.touch_the_cosmos.react&!buff.starweavers_warp.react |
| 11 | `variable` | name=ca_soon,value=cooldown.ca_inc.remains<3\|cooldown.ca_inc.charges_fractional>1 |
| 12 | `run_action_list` | name=ec_st,if=hero_tree.elunes_chosen&spell_targets=1 |
| 13 | `run_action_list` | name=kotg_st,if=spell_targets=1 |
| 14 | `run_action_list` | name=aoe,if=spell_targets>1 |

## Action List: `aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `celestial_alignment` | if=prev_gcd.1.force_of_nature&!variable.ec\|variable.ec&prev_gcd.1.fury_of_elune&buff.eclipse.down&(variable.on_use_trinket=0\|trinket.1.cooldown.remains>60\|trinket.1.cooldown.ready\|fight_remains<trinket.1.cooldown.remains\|trinket.2.cooldown.remains>60\|trinket.2.cooldown.ready\|fight_remains<trinket.2.cooldown.remains)\|fight_remains<20 |
| 2 | `moonfire` | target_if=remains<2\|refreshable&variable.eclipse_down |
| 3 | `sunfire` | target_if=remains<2\|refreshable&variable.eclipse_down |
| 4 | `fury_of_elune` | if=variable.ec\|!variable.ec&(variable.opener&!variable.eclipse_down&buff.ascendant_stars.down\|!variable.opener&(!variable.ec&(buff.harmony_of_the_grove.up\|cooldown.force_of_nature.remains<gcd.max\|talent.radiant_moonlight&cooldown.force_of_nature.remains>20))) |
| 5 | `solar_eclipse` | if=variable.opener&cooldown.eclipse.charges_fractional=2\|!variable.opener&cooldown.solar_eclipse.charges_fractional>1.5&variable.cd_window\|cooldown.solar_eclipse.ready&variable.cd_window_narrow\|fight_remains<15 |
| 6 | `lunar_eclipse` | if=!variable.prio&spell_targets>2&!variable.ec&(variable.opener&cooldown.eclipse.charges_fractional=2\|!variable.opener&cooldown.lunar_eclipse.charges_fractional>1.5&variable.cd_window\|cooldown.lunar_eclipse.ready&variable.cd_window_narrow)\|variable.ec&(variable.opener\|cooldown.ca_inc.full_recharge_time>15)\|fight_remains<15 |
| 7 | `convoke_the_spirits` | if=buff.ca_inc.up&astral_power<40\|cooldown.ca_inc.remains>50&buff.harmony_of_the_grove.up&buff.ca_inc.down |
| 8 | `wrath` | if=!talent.convoke_the_spirits&spell_targets<3&buff.ascendant_stars.down&(variable.opener&astral_power<50\|!variable.opener&astral_power<80&variable.no_weaver_procs&cooldown.force_of_nature.remains<15) |
| 9 | `sunfire` | target_if=!talent.aetherial_kindling&(variable.opener&buff.ascendant_stars.down\|!variable.opener&dot.sunfire.remains<10&variable.ca_soon&cooldown.force_of_nature.remains<3),line_cd=10 |
| 10 | `force_of_nature` | if=!variable.opener\|buff.ascendant_stars.down |
| 11 | `starfall` | if=astral_power>80\|!variable.eclipse_down\|!buff.starweavers_weft.react |
| 12 | `starsurge` | if=buff.starweavers_weft.react |
| 13 | `starfire` | if=buff.ascendant_fires.up&buff.eclipse_lunar.up |
| 14 | `new_moon` | if=astral_power.deficit>energize_amount |
| 15 | `half_moon` | if=astral_power.deficit>energize_amount |
| 16 | `full_moon` | if=astral_power.deficit>energize_amount |
| 17 | `wild_mushroom` | if=buff.eclipse_solar.up\|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains |
| 18 | `starfire` | if=variable.ec\|variable.eclipse_down&spell_targets.starfire>6\|buff.eclipse_lunar.up&(spell_targets.starfire>2&buff.ca_inc.up\|spell_targets.starfire<=2&!buff.ca_inc.up) |
| 19 | `wrath` | — |

## Action List: `ec_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `celestial_alignment` | if=buff.ca_inc.down&cooldown.eclipse.charges_fractional<1.5&buff.ascendant_stars.down |
| 2 | `moonfire` | target_if=remains<2\|refreshable&variable.eclipse_down |
| 3 | `sunfire` | target_if=remains<2\|refreshable&variable.eclipse_down |
| 4 | `convoke_the_spirits` | if=buff.ca_inc.up&astral_power<40\|cooldown.ca_inc.remains>50\|fight_remains<30 |
| 5 | `lunar_eclipse` | if=cooldown.ca_inc.full_recharge_time>15\|variable.opener |
| 6 | `starfall` | if=buff.starweavers_warp.react\|buff.touch_the_cosmos.react&talent.starweaver&buff.ascendant_stars.down |
| 7 | `starsurge` | if=astral_power>80\|!variable.eclipse_down\|buff.starweavers_weft.react\|buff.touch_the_cosmos.react&buff.ascendant_stars.up |
| 8 | `fury_of_elune` | — |
| 9 | `force_of_nature` | — |
| 10 | `new_moon` | if=astral_power.deficit>energize_amount |
| 11 | `half_moon` | if=astral_power.deficit>energize_amount |
| 12 | `full_moon` | if=astral_power.deficit>energize_amount |
| 13 | `wild_mushroom` | if=buff.eclipse_solar.up\|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains |
| 14 | `starfire` | if=!variable.eclipse_down |
| 15 | `wrath` | if=variable.eclipse_down |

## Action List: `kotg_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `celestial_alignment` | if=prev_gcd.1.force_of_nature\|fight_remains<20&buff.ca_inc.down |
| 2 | `moonfire` | target_if=remains<2\|refreshable&variable.eclipse_down |
| 3 | `sunfire` | target_if=remains<2\|refreshable&variable.eclipse_down |
| 4 | `sunfire` | target_if=variable.opener&buff.eclipse.up&buff.ascendant_stars.down&!buff.harmony_of_the_grove.up,line_cd=20 |
| 5 | `sunfire` | target_if=!variable.opener&dot.sunfire.remains<10&variable.ca_soon&cooldown.force_of_nature.remains<3,line_cd=20 |
| 6 | `fury_of_elune` | if=variable.opener\|!variable.opener&(buff.harmony_of_the_grove.up\|cooldown.force_of_nature.remains<gcd.max\|talent.radiant_moonlight&cooldown.force_of_nature.remains>20) |
| 7 | `solar_eclipse` | if=!variable.opener&cooldown.solar_eclipse.charges_fractional>1.5&variable.cd_window\|cooldown.solar_eclipse.ready&variable.cd_window_narrow\|fight_remains<20+(20*cooldown.ca_inc.ready) |
| 8 | `force_of_nature` | if=talent.aetherial_kindling&buff.eclipse.remains<8\|((buff.eclipse.down&!talent.early_spring\|talent.early_spring)&(cooldown.eclipse.remains<gcd.max\|cooldown.ca_inc.ready&(!talent.convoke_the_spirits\|cooldown.convoke_the_spirits.remains<gcd.max*5)))\|fight_remains<21 |
| 9 | `convoke_the_spirits` | if=buff.ca_inc.up&astral_power<40\|cooldown.ca_inc.remains>50&buff.harmony_of_the_grove.up&buff.ca_inc.down&astral_power<50\|fight_remains<action.convoke_the_spirits.execute_time+1 |
| 10 | `wrath` | if=!talent.convoke_the_spirits&buff.ascendant_stars.down&(astral_power<50\|astral_power<80&variable.no_weaver_procs&cooldown.force_of_nature.remains<15) |
| 11 | `sunfire` | target_if=dot.sunfire.remains<10&variable.ca_soon&cooldown.force_of_nature.remains<3,line_cd=10 |
| 12 | `starfall` | if=buff.starweavers_warp.react |
| 13 | `starsurge` | if=buff.eclipse.down&astral_power.deficit<20\|buff.eclipse.up&action.starsurge.cost>1&(buff.eclipse.remains>5\|astral_power.deficit<20)\|buff.touch_the_cosmos.react\|buff.starweavers_weft.react |
| 14 | `starfire` | if=buff.ascendant_fires.up&buff.eclipse_lunar.up |
| 15 | `new_moon` | if=astral_power.deficit>energize_amount |
| 16 | `half_moon` | if=astral_power.deficit>energize_amount |
| 17 | `full_moon` | if=astral_power.deficit>energize_amount |
| 18 | `wild_mushroom` | if=buff.eclipse.up\|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains |
| 19 | `wrath` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Balance APL can be found at https://github.com/dreamgrove/dreamgrove/blob/master/sims/owl/balance.txt

# Executed before combat begins. Accepts non-harmful actions only.
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat=snapshot_stats
# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat+=/variable,name=no_cd_talent,value=!talent.celestial_alignment&!talent.incarnation_chosen_of_elune|druid.no_cds
actions.precombat+=/variable,name=opener,op=set,value=1
actions.precombat+=/variable,name=ec,op=set,value=1,if=talent.boundless_moonlight
actions.precombat+=/variable,name=on_use_trinket,value=0
actions.precombat+=/variable,name=on_use_trinket,op=add,value=trinket.1.has_use_buff
actions.precombat+=/variable,name=on_use_trinket,op=add,value=(trinket.2.has_use_buff)*2
actions.precombat+=/variable,name=prio,op=set,value=0
actions.precombat+=/variable,name=inc_charge,op=set,value=0
actions.precombat+=/moonkin_form
# Pre-Cast
actions.precombat+=/wrath
actions.precombat+=/wrath
actions.precombat+=/wrath,if=talent.dream_surge&enemies=1
actions.precombat+=/starfire,if=hero_tree.elunes_chosen|enemies>1

# Executed every time the actor is available.
# Items, Racials & PI
actions=use_items,if=buff.ca_inc.up&(buff.harmony_of_the_grove.up|!talent.dream_surge)|fight_remains<cooldown.ca_inc.remains
actions+=/potion,if=buff.harmony_of_the_grove.up&buff.ca_inc.up&!variable.ec|buff.ca_inc.up&variable.ec|variable.opener&prev_gcd.1.solar_eclipse|fight_remains<=30
actions+=/berserking,if=buff.ca_inc.up&(buff.harmony_of_the_grove.up|!talent.dream_surge)|fight_remains<cooldown.ca_inc.remains
actions+=/invoke_external_buff,name=power_infusion,if=buff.ca_inc.up
# Variables Definition
actions+=/variable,name=inc_charge,op=set,value=1,if=cooldown.ca_inc.charges_fractional<1
actions+=/variable,name=opener,op=set,value=0,if=buff.ca_inc.up
actions+=/variable,name=eclipse_down,value=!buff.eclipse_lunar.up&!buff.eclipse_solar.up
actions+=/variable,name=cd_window,value=cooldown.force_of_nature.remains>15|cooldown.ca_inc.remains<44
actions+=/variable,name=cd_window_narrow,value=cooldown.force_of_nature.remains>30|cooldown.ca_inc.remains>10&cooldown.ca_inc.remains<20
actions+=/variable,name=no_weaver_procs,value=!buff.touch_the_cosmos.react&!buff.starweavers_warp.react
actions+=/variable,name=ca_soon,value=cooldown.ca_inc.remains<3|cooldown.ca_inc.charges_fractional>1
# Run the APL
actions+=/run_action_list,name=ec_st,if=hero_tree.elunes_chosen&spell_targets=1
actions+=/run_action_list,name=kotg_st,if=spell_targets=1
actions+=/run_action_list,name=aoe,if=spell_targets>1

# Cooldowns
actions.aoe=celestial_alignment,if=prev_gcd.1.force_of_nature&!variable.ec|variable.ec&prev_gcd.1.fury_of_elune&buff.eclipse.down&(variable.on_use_trinket=0|trinket.1.cooldown.remains>60|trinket.1.cooldown.ready|fight_remains<trinket.1.cooldown.remains|trinket.2.cooldown.remains>60|trinket.2.cooldown.ready|fight_remains<trinket.2.cooldown.remains)|fight_remains<20
# Dots
actions.aoe+=/moonfire,target_if=remains<2|refreshable&variable.eclipse_down
actions.aoe+=/sunfire,target_if=remains<2|refreshable&variable.eclipse_down
# Fury of Elune
actions.aoe+=/fury_of_elune,if=variable.ec|!variable.ec&(variable.opener&!variable.eclipse_down&buff.ascendant_stars.down|!variable.opener&(!variable.ec&(buff.harmony_of_the_grove.up|cooldown.force_of_nature.remains<gcd.max|talent.radiant_moonlight&cooldown.force_of_nature.remains>20)))
# Enter Solar
actions.aoe+=/solar_eclipse,if=variable.opener&cooldown.eclipse.charges_fractional=2|!variable.opener&cooldown.solar_eclipse.charges_fractional>1.5&variable.cd_window|cooldown.solar_eclipse.ready&variable.cd_window_narrow|fight_remains<15
# Enter Lunar
actions.aoe+=/lunar_eclipse,if=!variable.prio&spell_targets>2&!variable.ec&(variable.opener&cooldown.eclipse.charges_fractional=2|!variable.opener&cooldown.lunar_eclipse.charges_fractional>1.5&variable.cd_window|cooldown.lunar_eclipse.ready&variable.cd_window_narrow)|variable.ec&(variable.opener|cooldown.ca_inc.full_recharge_time>15)|fight_remains<15
# Convoke
actions.aoe+=/convoke_the_spirits,if=buff.ca_inc.up&astral_power<40|cooldown.ca_inc.remains>50&buff.harmony_of_the_grove.up&buff.ca_inc.down
# Cast Wrath if Going Solar
actions.aoe+=/wrath,if=!talent.convoke_the_spirits&spell_targets<3&buff.ascendant_stars.down&(variable.opener&astral_power<50|!variable.opener&astral_power<80&variable.no_weaver_procs&cooldown.force_of_nature.remains<15)
# Cast Sunfire Before Cooldowns
actions.aoe+=/sunfire,target_if=!talent.aetherial_kindling&(variable.opener&buff.ascendant_stars.down|!variable.opener&dot.sunfire.remains<10&variable.ca_soon&cooldown.force_of_nature.remains<3),line_cd=10
# Treants
actions.aoe+=/force_of_nature,if=!variable.opener|buff.ascendant_stars.down
# Spenders
actions.aoe+=/starfall,if=astral_power>80|!variable.eclipse_down|!buff.starweavers_weft.react
actions.aoe+=/starsurge,if=buff.starweavers_weft.react
# Builders
actions.aoe+=/starfire,if=buff.ascendant_fires.up&buff.eclipse_lunar.up
actions.aoe+=/new_moon,if=astral_power.deficit>energize_amount
actions.aoe+=/half_moon,if=astral_power.deficit>energize_amount
actions.aoe+=/full_moon,if=astral_power.deficit>energize_amount
actions.aoe+=/wild_mushroom,if=buff.eclipse_solar.up|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains
actions.aoe+=/starfire,if=variable.ec|variable.eclipse_down&spell_targets.starfire>6|buff.eclipse_lunar.up&(spell_targets.starfire>2&buff.ca_inc.up|spell_targets.starfire<=2&!buff.ca_inc.up)
actions.aoe+=/wrath

# Cooldowns
actions.ec_st=celestial_alignment,if=buff.ca_inc.down&cooldown.eclipse.charges_fractional<1.5&buff.ascendant_stars.down
# Dots
actions.ec_st+=/moonfire,target_if=remains<2|refreshable&variable.eclipse_down
actions.ec_st+=/sunfire,target_if=remains<2|refreshable&variable.eclipse_down
# Convoke
actions.ec_st+=/convoke_the_spirits,if=buff.ca_inc.up&astral_power<40|cooldown.ca_inc.remains>50|fight_remains<30
# Enter Lunar
actions.ec_st+=/lunar_eclipse,if=cooldown.ca_inc.full_recharge_time>15|variable.opener
# Spenders
actions.ec_st+=/starfall,if=buff.starweavers_warp.react|buff.touch_the_cosmos.react&talent.starweaver&buff.ascendant_stars.down
actions.ec_st+=/starsurge,if=astral_power>80|!variable.eclipse_down|buff.starweavers_weft.react|buff.touch_the_cosmos.react&buff.ascendant_stars.up
# Fury of Elune
actions.ec_st+=/fury_of_elune
# Builders
actions.ec_st+=/force_of_nature
actions.ec_st+=/new_moon,if=astral_power.deficit>energize_amount
actions.ec_st+=/half_moon,if=astral_power.deficit>energize_amount
actions.ec_st+=/full_moon,if=astral_power.deficit>energize_amount
actions.ec_st+=/wild_mushroom,if=buff.eclipse_solar.up|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains
actions.ec_st+=/starfire,if=!variable.eclipse_down
actions.ec_st+=/wrath,if=variable.eclipse_down

# Cooldowns
actions.kotg_st=celestial_alignment,if=prev_gcd.1.force_of_nature|fight_remains<20&buff.ca_inc.down
# Dots
actions.kotg_st+=/moonfire,target_if=remains<2|refreshable&variable.eclipse_down
actions.kotg_st+=/sunfire,target_if=remains<2|refreshable&variable.eclipse_down
# Cast Sunfire Before Cooldowns
actions.kotg_st+=/sunfire,target_if=variable.opener&buff.eclipse.up&buff.ascendant_stars.down&!buff.harmony_of_the_grove.up,line_cd=20
actions.kotg_st+=/sunfire,target_if=!variable.opener&dot.sunfire.remains<10&variable.ca_soon&cooldown.force_of_nature.remains<3,line_cd=20
# Fury of Elune
actions.kotg_st+=/fury_of_elune,if=variable.opener|!variable.opener&(buff.harmony_of_the_grove.up|cooldown.force_of_nature.remains<gcd.max|talent.radiant_moonlight&cooldown.force_of_nature.remains>20)
actions.kotg_st+=/solar_eclipse,if=!variable.opener&cooldown.solar_eclipse.charges_fractional>1.5&variable.cd_window|cooldown.solar_eclipse.ready&variable.cd_window_narrow|fight_remains<20+(20*cooldown.ca_inc.ready)
# Treants
actions.kotg_st+=/force_of_nature,if=talent.aetherial_kindling&buff.eclipse.remains<8|((buff.eclipse.down&!talent.early_spring|talent.early_spring)&(cooldown.eclipse.remains<gcd.max|cooldown.ca_inc.ready&(!talent.convoke_the_spirits|cooldown.convoke_the_spirits.remains<gcd.max*5)))|fight_remains<21
# Convoke
actions.kotg_st+=/convoke_the_spirits,if=buff.ca_inc.up&astral_power<40|cooldown.ca_inc.remains>50&buff.harmony_of_the_grove.up&buff.ca_inc.down&astral_power<50|fight_remains<action.convoke_the_spirits.execute_time+1
# Cast Wrath if Going Solar
actions.kotg_st+=/wrath,if=!talent.convoke_the_spirits&buff.ascendant_stars.down&(astral_power<50|astral_power<80&variable.no_weaver_procs&cooldown.force_of_nature.remains<15)
# Cast Sunfire Before Cooldowns
actions.kotg_st+=/sunfire,target_if=dot.sunfire.remains<10&variable.ca_soon&cooldown.force_of_nature.remains<3,line_cd=10
# Spenders
actions.kotg_st+=/starfall,if=buff.starweavers_warp.react
actions.kotg_st+=/starsurge,if=buff.eclipse.down&astral_power.deficit<20|buff.eclipse.up&action.starsurge.cost>1&(buff.eclipse.remains>5|astral_power.deficit<20)|buff.touch_the_cosmos.react|buff.starweavers_weft.react
# Instant Builder
actions.kotg_st+=/starfire,if=buff.ascendant_fires.up&buff.eclipse_lunar.up
# Builders
actions.kotg_st+=/new_moon,if=astral_power.deficit>energize_amount
actions.kotg_st+=/half_moon,if=astral_power.deficit>energize_amount
actions.kotg_st+=/full_moon,if=astral_power.deficit>energize_amount
actions.kotg_st+=/wild_mushroom,if=buff.eclipse.up|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains
actions.kotg_st+=/wrath
```
