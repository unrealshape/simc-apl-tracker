# Druid – Balance

Auto-generated from SimulationCraft APL | Last updated: 2026-09-21 08:49 UTC

Source: `apl/default/druid/balance.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 102
- **Lists:** `precombat`, `default`, `aoe`, `cooldowns`, `ec_st`, `kotg_st`, `mini`, `opener`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `variable` | name=Starfall_talents,value=(spell_targets<3&(talent.starweaver&!talent.aetherial_kindling&!talent.meteorites&(talent.stellar_amplification&talent.power_of_goldrinn\|talent.stellar_amplification&talent.power_of_goldrinn&talent.meteor_storm\|talent.power_of_goldrinn&!talent.meteor_storm))\|(talent.rattle_the_stars&!talent.meteorites&((talent.stellar_amplification\|talent.power_of_goldrinn)&!talent.aetherial_kindling))) |
| 3 | `variable` | name=no_cd_talent,value=!talent.celestial_alignment&!talent.incarnation_chosen_of_elune\|druid.no_cds |
| 4 | `variable` | name=ca_opener,op=set,value=1 |
| 5 | `variable` | name=opener,op=set,value=1 |
| 6 | `variable` | name=on_use_trinket,op=add,value=trinket.1.has_use_buff |
| 7 | `variable` | name=on_use_trinket,op=add,value=(trinket.2.has_use_buff)*2 |
| 8 | `moonkin_form` | — |
| 9 | `wrath` | — |
| 10 | `wrath` | — |
| 11 | `wrath` | if=talent.dream_surge&enemies<=2 |
| 12 | `starfire` | if=hero_tree.elunes_chosen\|enemies>2 |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `potion` | if=buff.harmony_of_the_grove.up&buff.ca_inc.up&hero_tree.keeper_of_the_grove\|buff.ca_inc.up&hero_tree.elunes_chosen\|variable.opener&prev_gcd.1.eclipse\|fight_remains<=30 |
| 2 | `use_items` | if=!trinket.1.is.wraps_of_cosmic_madness&!trinket.2.is.wraps_of_cosmic_madness&!trinket.1.is.font_of_venomous_rage&!trinket.2.is.font_of_venomous_rage&buff.ca_inc.up&(buff.harmony_of_the_grove.up\|hero_tree.elunes_chosen)\|fight_remains<20 |
| 3 | `use_item` | name=wraps_of_cosmic_madness,if=!buff.eclipse.up |
| 4 | `use_item` | name=font_of_venomous_rage,if=!buff.eclipse.up |
| 5 | `berserking` | if=buff.ca_inc.up&(buff.harmony_of_the_grove.up\|!talent.dream_surge)\|fight_remains<cooldown.ca_inc.remains |
| 6 | `invoke_external_buff` | name=power_infusion,if=buff.ca_inc.up |
| 7 | `variable` | name=eclipse_timings,value=((cooldown.eclipse.full_recharge_time<(cooldown.force_of_nature.remains<?(cooldown.fury_of_elune.remains*hero_tree.elunes_chosen*!talent.lunation)<?((buff.eclipse.duration+2)))\|cooldown.ca_inc.remains<(cooldown.force_of_nature.remains<?(cooldown.fury_of_elune.remains*hero_tree.elunes_chosen*!talent.lunation)<?(buff.eclipse.duration+2)))\|fight_remains<buff.eclipse.duration)&(buff.eclipse.remains<2&fight_style.dungeonroute\|!fight_style.dungeonroute) |
| 8 | `variable` | name=opener,op=set,value=0,if=buff.ca_inc.up |
| 9 | `variable` | name=starfall_cosmos,value=(talent.starweaver&(talent.meteorites&(talent.incarnation_chosen_of_elune&talent.meteor_storm&!talent.power_of_goldrinn\|buff.ca_inc.down&(talent.incarnation_chosen_of_elune\|talent.stellar_amplification\|!talent.power_of_goldrinn))\|buff.eclipse.down&(talent.meteorites\|talent.aetherial_kindling\|talent.stellar_amplification&!talent.power_of_goldrinn))\|buff.ca_inc.down&talent.meteorites&talent.aetherial_kindling&talent.stellar_amplification&!talent.power_of_goldrinn\|buff.eclipse.down&talent.meteorites&(talent.aetherial_kindling\|talent.stellar_amplification\|!talent.power_of_goldrinn))&buff.touch_the_cosmos.react&!buff.starweavers_weft.react |
| 10 | `variable` | name=cds,op=set,value=1,if=((((cooldown.force_of_nature.remains*hero_tree.keeper_of_the_grove)<?(cooldown.fury_of_elune.remains*hero_tree.elunes_chosen*!talent.lunation)<?cooldown.ca_inc.remains<?(buff.eclipse.remains-(10*(buff.bloodlust.up*buff.ascendant_stars.down)))<?buff.ca_inc.remains)<1)&(active_dot.moonfire>=active_enemies\|active_dots.moonfire>=10\|spell_targets=1&hero_tree.keeper_of_the_grove\|hero_tree.elunes_chosen&variable.opener&spell_targets=1))&target.time_to_die>20 |
| 11 | `variable` | name=cds,op=set,value=0,if=buff.ca_inc.up |
| 12 | `variable` | name=mini,op=set,value=1,if=(((cooldown.eclipse.remains<?cooldown.force_of_nature.remains<?cooldown.fury_of_elune.remains-15<?buff.eclipse.remains)<1)&(cooldown.ca_inc.remains+10>(cooldown.force_of_nature.duration<?cooldown.fury_of_elune.duration-15)))&hero_tree.keeper_of_the_grove |
| 13 | `variable` | name=mini,op=set,value=0,if=prev_gcd.1.eclipse |
| 14 | `run_action_list` | name=opener,if=variable.opener |
| 15 | `run_action_list` | name=mini,if=variable.mini&!variable.opener |
| 16 | `run_action_list` | name=cooldowns,if=variable.cds&!variable.opener |
| 17 | `run_action_list` | name=ec_st,if=hero_tree.elunes_chosen&spell_targets=1 |
| 18 | `run_action_list` | name=kotg_st,if=spell_targets=1 |
| 19 | `run_action_list` | name=aoe,if=spell_targets>1 |

## Action List: `aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `celestial_alignment` | if=fight_remains<20 |
| 2 | `wrath` | if=eclipse.lunar&spell_targets<=2&hero_tree.keeper_of_the_grove&buff.eclipse.down |
| 3 | `starfire` | if=eclipse.solar&spell_targets>2&hero_tree.keeper_of_the_grove&buff.eclipse.down |
| 4 | `eclipse` | if=!variable.opener&(cooldown.eclipse.full_recharge_time<gcd.max) |
| 5 | `moonfire` | target_if=refreshable&(target.time_to_die-remains)>6&active_dots.moonfire<10&buff.eclipse.down |
| 6 | `sunfire` | target_if=(remains<2\|refreshable&buff.eclipse.down)&target.time_to_die>5 |
| 7 | `fury_of_elune` | if=fight_remains<10\|cooldown.ca_inc.remains>10\|talent.lunation |
| 8 | `force_of_nature` | if=hero_tree.elunes_chosen&astral_power<50&cooldown.ca_inc.remains>10&buff.eclipse.up\|fight_remains<15 |
| 9 | `eclipse` | if=variable.eclipse_timings |
| 10 | `convoke_the_spirits` | if=(buff.ca_inc.up&astral_power<40\|cooldown.ca_inc.remains>50&buff.harmony_of_the_grove.up&buff.ca_inc.down)&(buff.orbit_breaker.stack<10\|hero_tree.keeper_of_the_grove) |
| 11 | `starsurge` | if=(astral_power>80\|buff.eclipse.up&action.starsurge.cost>1)&variable.Starfall_talents&!buff.starweavers_warp.react&!buff.touch_the_cosmos.react\|buff.starweavers_weft.react |
| 12 | `starfall` | if=((astral_power>80-79*hero_tree.elunes_chosen\|buff.eclipse.up&action.starfall.cost>1)&spell_targets>=2\|buff.starweavers_warp.react\|buff.touch_the_cosmos.react)&target.time_to_die>5 |
| 13 | `starfire` | if=buff.ascendant_fires.up&buff.eclipse_lunar.up |
| 14 | `new_moon` | if=astral_power.deficit>energize_amount&debuff.atmospheric_exposure.remains<execute_time+0.5 |
| 15 | `half_moon` | if=astral_power.deficit>energize_amount&debuff.atmospheric_exposure.remains<execute_time+0.5 |
| 16 | `full_moon` | if=astral_power.deficit>energize_amount&debuff.atmospheric_exposure.remains<execute_time+0.5 |
| 17 | `wild_mushroom` | if=buff.eclipse_solar.up\|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains |
| 18 | `starfire` | if=hero_tree.elunes_chosen\|buff.eclipse.down&spell_targets.starfire>2\|buff.eclipse_lunar.up&spell_targets.starfire>2 |
| 19 | `wrath` | if=spell_targets<=2 |

## Action List: `cooldowns`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `moonfire` | target_if=hero_tree.elunes_chosen&dot.moonfire.remains<12&spell_targets=1,line_cd=20 |
| 2 | `moonfire` | target_if=refreshable&(target.time_to_die-remains)>6&active_dots.moonfire<10&spell_targets>1 |
| 3 | `sunfire` | if=dot.sunfire.remains<15,line_cd=10 |
| 4 | `fury_of_elune` | — |
| 5 | `force_of_nature` | if=hero_tree.keeper_of_the_grove |
| 6 | `celestial_alignment` | add_queue_lag=1 |

## Action List: `ec_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `sunfire` | target_if=remains<2\|refreshable&buff.eclipse.down&target.time_to_die>10 |
| 2 | `moonfire` | target_if=(remains<2\|refreshable&!buff.eclipse.up&!cooldown.force_of_nature.remains<dot.moonfire.remains)&target.time_to_die>10 |
| 3 | `celestial_alignment` | if=fight_remains<20 |
| 4 | `convoke_the_spirits` | if=(buff.balance_of_all_things_arcane.stack<5\|buff.balance_of_all_things_nature.stack<5\|astral_power<40)&buff.ca_inc.up\|cooldown.ca_inc.remains>40&buff.eclipse.up |
| 5 | `fury_of_elune` | if=fight_remains<10\|cooldown.ca_inc.remains>cooldown.fury_of_elune.duration-5\|talent.lunation |
| 6 | `force_of_nature` | if=fight_remains<10\|cooldown.force_of_nature.duration<cooldown.ca_inc.remains |
| 7 | `eclipse` | if=variable.eclipse_timings |
| 8 | `starfall` | if=buff.starweavers_warp.react |
| 9 | `starfall` | if=variable.starfall_cosmos |
| 10 | `starsurge` | if=buff.eclipse.down&astral_power.deficit<20\|buff.eclipse.up&action.starsurge.cost>1\|buff.touch_the_cosmos.react\|buff.starweavers_weft.react |
| 11 | `new_moon` | if=astral_power.deficit>energize_amount |
| 12 | `half_moon` | if=astral_power.deficit>energize_amount |
| 13 | `full_moon` | if=astral_power.deficit>energize_amount |
| 14 | `wild_mushroom` | if=buff.eclipse.up\|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains |
| 15 | `starfire` | — |

## Action List: `kotg_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `sunfire` | target_if=remains<2\|refreshable&buff.eclipse.down&target.time_to_die>10 |
| 2 | `moonfire` | target_if=buff.harmony_of_the_grove.down&(remains<2\|refreshable&!buff.eclipse.up&!cooldown.force_of_nature.remains<dot.moonfire.remains)&target.time_to_die>10 |
| 3 | `celestial_alignment` | if=fight_remains<25 |
| 4 | `fury_of_elune` | if=fight_remains<10\|cooldown.force_of_nature.remains>5\|!talent.radiant_moonlight |
| 5 | `force_of_nature` | if=fight_remains<10 |
| 6 | `convoke_the_spirits` | if=astral_power<40&buff.harmony_of_the_grove.up\|fight_remains<10 |
| 7 | `eclipse` | if=variable.eclipse_timings&(astral_power>60\|charges_fractional=2) |
| 8 | `starfall` | if=buff.starweavers_warp.react |
| 9 | `starfall` | if=variable.starfall_cosmos |
| 10 | `starsurge` | if=buff.eclipse.down&astral_power.deficit<20\|buff.eclipse.up&action.starsurge.cost>1&(astral_power.deficit<10\|cooldown.force_of_nature.remains>5+buff.eclipse.remains\|buff.ascendant_stars.up)\|buff.touch_the_cosmos.react\|buff.starweavers_weft.react |
| 11 | `new_moon` | if=astral_power.deficit>energize_amount |
| 12 | `half_moon` | if=astral_power.deficit>energize_amount |
| 13 | `full_moon` | if=astral_power.deficit>energize_amount |
| 14 | `wild_mushroom` | if=buff.eclipse.up\|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains |
| 15 | `wrath` | — |

## Action List: `mini`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `fury_of_elune` | — |
| 2 | `force_of_nature` | — |
| 3 | `eclipse` | — |

## Action List: `opener`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `moonfire` | if=!talent.convoke_the_spirits,line_cd=999 |
| 2 | `moonfire` | target_if=refreshable&(target.time_to_die-remains)>6&active_dots.moonfire<10&spell_targets>1 |
| 3 | `sunfire` | line_cd=999 |
| 4 | `eclipse` | if=!talent.convoke_the_spirits,line_cd=999 |
| 5 | `starsurge` | if=buff.ascendant_stars.up&!talent.convoke_the_spirits&((variable.Starfall_talents&!buff.starweavers_warp.react&!buff.touch_the_cosmos.react\|buff.starweavers_weft.react)&spell_targets>1\|spell_targets=1) |
| 6 | `starfall` | if=buff.ascendant_stars.up&!talent.convoke_the_spirits&((action.starfall.cost>1)\|buff.starweavers_warp.react\|buff.touch_the_cosmos.react)&spell_targets>=2 |
| 7 | `wrath` | if=(buff.ascendant_stars.up\|buff.ascendant_stars.down&astral_power<80)&!talent.convoke_the_spirits&hero_tree.keeper_of_the_grove&spell_targets.starfire<3 |
| 8 | `starfire` | if=(buff.ascendant_stars.up\|buff.ascendant_stars.down&astral_power<80)&!talent.convoke_the_spirits&(hero_tree.elunes_chosen\|spell_targets.starfire>=3) |
| 9 | `moonfire` | if=buff.ascendant_stars.down&hero_tree.elunes_chosen,line_cd=999 |
| 10 | `sunfire` | if=buff.ascendant_stars.down&!talent.convoke_the_spirits,line_cd=999 |
| 11 | `fury_of_elune` | — |
| 12 | `force_of_nature` | — |
| 13 | `celestial_alignment` | add_queue_lag=1 |

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
actions.precombat+=/variable,name=Starfall_talents,value=(spell_targets<3&(talent.starweaver&!talent.aetherial_kindling&!talent.meteorites&(talent.stellar_amplification&talent.power_of_goldrinn|talent.stellar_amplification&talent.power_of_goldrinn&talent.meteor_storm|talent.power_of_goldrinn&!talent.meteor_storm))|(talent.rattle_the_stars&!talent.meteorites&((talent.stellar_amplification|talent.power_of_goldrinn)&!talent.aetherial_kindling)))
actions.precombat+=/variable,name=no_cd_talent,value=!talent.celestial_alignment&!talent.incarnation_chosen_of_elune|druid.no_cds
actions.precombat+=/variable,name=ca_opener,op=set,value=1
actions.precombat+=/variable,name=opener,op=set,value=1
actions.precombat+=/variable,name=on_use_trinket,op=add,value=trinket.1.has_use_buff
actions.precombat+=/variable,name=on_use_trinket,op=add,value=(trinket.2.has_use_buff)*2
actions.precombat+=/moonkin_form
actions.precombat+=/wrath
actions.precombat+=/wrath
actions.precombat+=/wrath,if=talent.dream_surge&enemies<=2
actions.precombat+=/starfire,if=hero_tree.elunes_chosen|enemies>2

# Executed every time the actor is available.
# Executed every time the actor is available.
actions=potion,if=buff.harmony_of_the_grove.up&buff.ca_inc.up&hero_tree.keeper_of_the_grove|buff.ca_inc.up&hero_tree.elunes_chosen|variable.opener&prev_gcd.1.eclipse|fight_remains<=30
actions+=/use_items,if=!trinket.1.is.wraps_of_cosmic_madness&!trinket.2.is.wraps_of_cosmic_madness&!trinket.1.is.font_of_venomous_rage&!trinket.2.is.font_of_venomous_rage&buff.ca_inc.up&(buff.harmony_of_the_grove.up|hero_tree.elunes_chosen)|fight_remains<20
actions+=/use_item,name=wraps_of_cosmic_madness,if=!buff.eclipse.up
actions+=/use_item,name=font_of_venomous_rage,if=!buff.eclipse.up
actions+=/berserking,if=buff.ca_inc.up&(buff.harmony_of_the_grove.up|!talent.dream_surge)|fight_remains<cooldown.ca_inc.remains
actions+=/invoke_external_buff,name=power_infusion,if=buff.ca_inc.up
actions+=/variable,name=eclipse_timings,value=((cooldown.eclipse.full_recharge_time<(cooldown.force_of_nature.remains<?(cooldown.fury_of_elune.remains*hero_tree.elunes_chosen*!talent.lunation)<?((buff.eclipse.duration+2)))|cooldown.ca_inc.remains<(cooldown.force_of_nature.remains<?(cooldown.fury_of_elune.remains*hero_tree.elunes_chosen*!talent.lunation)<?(buff.eclipse.duration+2)))|fight_remains<buff.eclipse.duration)&(buff.eclipse.remains<2&fight_style.dungeonroute|!fight_style.dungeonroute)
actions+=/variable,name=opener,op=set,value=0,if=buff.ca_inc.up
actions+=/variable,name=starfall_cosmos,value=(talent.starweaver&(talent.meteorites&(talent.incarnation_chosen_of_elune&talent.meteor_storm&!talent.power_of_goldrinn|buff.ca_inc.down&(talent.incarnation_chosen_of_elune|talent.stellar_amplification|!talent.power_of_goldrinn))|buff.eclipse.down&(talent.meteorites|talent.aetherial_kindling|talent.stellar_amplification&!talent.power_of_goldrinn))|buff.ca_inc.down&talent.meteorites&talent.aetherial_kindling&talent.stellar_amplification&!talent.power_of_goldrinn|buff.eclipse.down&talent.meteorites&(talent.aetherial_kindling|talent.stellar_amplification|!talent.power_of_goldrinn))&buff.touch_the_cosmos.react&!buff.starweavers_weft.react
actions+=/variable,name=cds,op=set,value=1,if=((((cooldown.force_of_nature.remains*hero_tree.keeper_of_the_grove)<?(cooldown.fury_of_elune.remains*hero_tree.elunes_chosen*!talent.lunation)<?cooldown.ca_inc.remains<?(buff.eclipse.remains-(10*(buff.bloodlust.up*buff.ascendant_stars.down)))<?buff.ca_inc.remains)<1)&(active_dot.moonfire>=active_enemies|active_dots.moonfire>=10|spell_targets=1&hero_tree.keeper_of_the_grove|hero_tree.elunes_chosen&variable.opener&spell_targets=1))&target.time_to_die>20
actions+=/variable,name=cds,op=set,value=0,if=buff.ca_inc.up
actions+=/variable,name=mini,op=set,value=1,if=(((cooldown.eclipse.remains<?cooldown.force_of_nature.remains<?cooldown.fury_of_elune.remains-15<?buff.eclipse.remains)<1)&(cooldown.ca_inc.remains+10>(cooldown.force_of_nature.duration<?cooldown.fury_of_elune.duration-15)))&hero_tree.keeper_of_the_grove
actions+=/variable,name=mini,op=set,value=0,if=prev_gcd.1.eclipse
actions+=/run_action_list,name=opener,if=variable.opener
actions+=/run_action_list,name=mini,if=variable.mini&!variable.opener
actions+=/run_action_list,name=cooldowns,if=variable.cds&!variable.opener
actions+=/run_action_list,name=ec_st,if=hero_tree.elunes_chosen&spell_targets=1
actions+=/run_action_list,name=kotg_st,if=spell_targets=1
actions+=/run_action_list,name=aoe,if=spell_targets>1

actions.aoe=celestial_alignment,if=fight_remains<20
actions.aoe+=/wrath,if=eclipse.lunar&spell_targets<=2&hero_tree.keeper_of_the_grove&buff.eclipse.down
actions.aoe+=/starfire,if=eclipse.solar&spell_targets>2&hero_tree.keeper_of_the_grove&buff.eclipse.down
actions.aoe+=/eclipse,if=!variable.opener&(cooldown.eclipse.full_recharge_time<gcd.max)
actions.aoe+=/moonfire,target_if=refreshable&(target.time_to_die-remains)>6&active_dots.moonfire<10&buff.eclipse.down
actions.aoe+=/sunfire,target_if=(remains<2|refreshable&buff.eclipse.down)&target.time_to_die>5
actions.aoe+=/fury_of_elune,if=fight_remains<10|cooldown.ca_inc.remains>10|talent.lunation
actions.aoe+=/force_of_nature,if=hero_tree.elunes_chosen&astral_power<50&cooldown.ca_inc.remains>10&buff.eclipse.up|fight_remains<15
actions.aoe+=/eclipse,if=variable.eclipse_timings
actions.aoe+=/convoke_the_spirits,if=(buff.ca_inc.up&astral_power<40|cooldown.ca_inc.remains>50&buff.harmony_of_the_grove.up&buff.ca_inc.down)&(buff.orbit_breaker.stack<10|hero_tree.keeper_of_the_grove)
actions.aoe+=/starsurge,if=(astral_power>80|buff.eclipse.up&action.starsurge.cost>1)&variable.Starfall_talents&!buff.starweavers_warp.react&!buff.touch_the_cosmos.react|buff.starweavers_weft.react
actions.aoe+=/starfall,if=((astral_power>80-79*hero_tree.elunes_chosen|buff.eclipse.up&action.starfall.cost>1)&spell_targets>=2|buff.starweavers_warp.react|buff.touch_the_cosmos.react)&target.time_to_die>5
actions.aoe+=/starfire,if=buff.ascendant_fires.up&buff.eclipse_lunar.up
actions.aoe+=/new_moon,if=astral_power.deficit>energize_amount&debuff.atmospheric_exposure.remains<execute_time+0.5
actions.aoe+=/half_moon,if=astral_power.deficit>energize_amount&debuff.atmospheric_exposure.remains<execute_time+0.5
actions.aoe+=/full_moon,if=astral_power.deficit>energize_amount&debuff.atmospheric_exposure.remains<execute_time+0.5
actions.aoe+=/wild_mushroom,if=buff.eclipse_solar.up|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains
actions.aoe+=/starfire,if=hero_tree.elunes_chosen|buff.eclipse.down&spell_targets.starfire>2|buff.eclipse_lunar.up&spell_targets.starfire>2
actions.aoe+=/wrath,if=spell_targets<=2

actions.cooldowns=moonfire,target_if=hero_tree.elunes_chosen&dot.moonfire.remains<12&spell_targets=1,line_cd=20
actions.cooldowns+=/moonfire,target_if=refreshable&(target.time_to_die-remains)>6&active_dots.moonfire<10&spell_targets>1
actions.cooldowns+=/sunfire,if=dot.sunfire.remains<15,line_cd=10
actions.cooldowns+=/fury_of_elune
actions.cooldowns+=/force_of_nature,if=hero_tree.keeper_of_the_grove
actions.cooldowns+=/celestial_alignment,add_queue_lag=1

actions.ec_st=sunfire,target_if=remains<2|refreshable&buff.eclipse.down&target.time_to_die>10
actions.ec_st+=/moonfire,target_if=(remains<2|refreshable&!buff.eclipse.up&!cooldown.force_of_nature.remains<dot.moonfire.remains)&target.time_to_die>10
actions.ec_st+=/celestial_alignment,if=fight_remains<20
actions.ec_st+=/convoke_the_spirits,if=(buff.balance_of_all_things_arcane.stack<5|buff.balance_of_all_things_nature.stack<5|astral_power<40)&buff.ca_inc.up|cooldown.ca_inc.remains>40&buff.eclipse.up
actions.ec_st+=/fury_of_elune,if=fight_remains<10|cooldown.ca_inc.remains>cooldown.fury_of_elune.duration-5|talent.lunation
actions.ec_st+=/force_of_nature,if=fight_remains<10|cooldown.force_of_nature.duration<cooldown.ca_inc.remains
actions.ec_st+=/eclipse,if=variable.eclipse_timings
actions.ec_st+=/starfall,if=buff.starweavers_warp.react
actions.ec_st+=/starfall,if=variable.starfall_cosmos
actions.ec_st+=/starsurge,if=buff.eclipse.down&astral_power.deficit<20|buff.eclipse.up&action.starsurge.cost>1|buff.touch_the_cosmos.react|buff.starweavers_weft.react
actions.ec_st+=/new_moon,if=astral_power.deficit>energize_amount
actions.ec_st+=/half_moon,if=astral_power.deficit>energize_amount
actions.ec_st+=/full_moon,if=astral_power.deficit>energize_amount
actions.ec_st+=/wild_mushroom,if=buff.eclipse.up|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains
actions.ec_st+=/starfire

actions.kotg_st=sunfire,target_if=remains<2|refreshable&buff.eclipse.down&target.time_to_die>10
actions.kotg_st+=/moonfire,target_if=buff.harmony_of_the_grove.down&(remains<2|refreshable&!buff.eclipse.up&!cooldown.force_of_nature.remains<dot.moonfire.remains)&target.time_to_die>10
actions.kotg_st+=/celestial_alignment,if=fight_remains<25
actions.kotg_st+=/fury_of_elune,if=fight_remains<10|cooldown.force_of_nature.remains>5|!talent.radiant_moonlight
actions.kotg_st+=/force_of_nature,if=fight_remains<10
actions.kotg_st+=/convoke_the_spirits,if=astral_power<40&buff.harmony_of_the_grove.up|fight_remains<10
actions.kotg_st+=/eclipse,if=variable.eclipse_timings&(astral_power>60|charges_fractional=2)
actions.kotg_st+=/starfall,if=buff.starweavers_warp.react
actions.kotg_st+=/starfall,if=variable.starfall_cosmos
actions.kotg_st+=/starsurge,if=buff.eclipse.down&astral_power.deficit<20|buff.eclipse.up&action.starsurge.cost>1&(astral_power.deficit<10|cooldown.force_of_nature.remains>5+buff.eclipse.remains|buff.ascendant_stars.up)|buff.touch_the_cosmos.react|buff.starweavers_weft.react
actions.kotg_st+=/new_moon,if=astral_power.deficit>energize_amount
actions.kotg_st+=/half_moon,if=astral_power.deficit>energize_amount
actions.kotg_st+=/full_moon,if=astral_power.deficit>energize_amount
actions.kotg_st+=/wild_mushroom,if=buff.eclipse.up|cooldown.wild_mushroom.full_recharge_time<cooldown.ca_inc.remains
actions.kotg_st+=/wrath

actions.mini=fury_of_elune
actions.mini+=/force_of_nature
actions.mini+=/eclipse

actions.opener=moonfire,if=!talent.convoke_the_spirits,line_cd=999
actions.opener+=/moonfire,target_if=refreshable&(target.time_to_die-remains)>6&active_dots.moonfire<10&spell_targets>1
actions.opener+=/sunfire,line_cd=999
actions.opener+=/eclipse,if=!talent.convoke_the_spirits,line_cd=999
actions.opener+=/starsurge,if=buff.ascendant_stars.up&!talent.convoke_the_spirits&((variable.Starfall_talents&!buff.starweavers_warp.react&!buff.touch_the_cosmos.react|buff.starweavers_weft.react)&spell_targets>1|spell_targets=1)
actions.opener+=/starfall,if=buff.ascendant_stars.up&!talent.convoke_the_spirits&((action.starfall.cost>1)|buff.starweavers_warp.react|buff.touch_the_cosmos.react)&spell_targets>=2
actions.opener+=/wrath,if=(buff.ascendant_stars.up|buff.ascendant_stars.down&astral_power<80)&!talent.convoke_the_spirits&hero_tree.keeper_of_the_grove&spell_targets.starfire<3
actions.opener+=/starfire,if=(buff.ascendant_stars.up|buff.ascendant_stars.down&astral_power<80)&!talent.convoke_the_spirits&(hero_tree.elunes_chosen|spell_targets.starfire>=3)
actions.opener+=/moonfire,if=buff.ascendant_stars.down&hero_tree.elunes_chosen,line_cd=999
actions.opener+=/sunfire,if=buff.ascendant_stars.down&!talent.convoke_the_spirits,line_cd=999
actions.opener+=/fury_of_elune
actions.opener+=/force_of_nature
actions.opener+=/celestial_alignment,add_queue_lag=1
```
