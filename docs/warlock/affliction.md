# Warlock – Affliction

Auto-generated from SimulationCraft APL | Last updated: 2026-09-17 08:33 UTC

Source: `apl/default/warlock/affliction.simc`

---

## Overview

- **Action Lists:** 14
- **Total Actions:** 106
- **Lists:** `precombat`, `default`, `HC_aoe`, `HC_cleave`, `HC_st`, `SH_aoe`, `SH_cleave`, `SH_st`, `end_of_fight`, `hellcaller`, `items`, `ogcd`, `soul_harvester`, `variables`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `summon_pet` | — |
| 2 | `variable` | name=trinket_1_buffs,value=(trinket.1.has_buff.intellect\|trinket.1.has_buff.mastery\|trinket.1.has_buff.versatility\|trinket.1.has_buff.haste\|trinket.1.has_buff.crit\|trinket.1.is.signet_of_the_priory)&(trinket.1.cooldown.duration>=20) |
| 3 | `variable` | name=trinket_2_buffs,value=(trinket.2.has_buff.intellect\|trinket.2.has_buff.mastery\|trinket.2.has_buff.versatility\|trinket.2.has_buff.haste\|trinket.2.has_buff.crit\|trinket.2.is.signet_of_the_priory)&(trinket.2.cooldown.duration>=20) |
| 4 | `snapshot_stats` | — |
| 5 | `grimoire_of_sacrifice` | if=talent.grimoire_of_sacrifice |
| 6 | `seed_of_corruption` | if=(hero_tree.soul_harvester&active_enemies>1)\|active_enemies>2 |
| 7 | `haunt` | if=active_enemies<2\|(hero_tree.hellcaller&active_enemies<3) |
| 8 | `potion` | if=potion.liquid_luster |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=variables |
| 2 | `call_action_list` | name=end_of_fight |
| 3 | `call_action_list` | name=ogcd |
| 4 | `call_action_list` | name=items |
| 5 | `call_action_list` | name=soul_harvester,if=hero_tree.soul_harvester |
| 6 | `call_action_list` | name=hellcaller,if=hero_tree.hellcaller |
| 7 | `malefic_grasp` | chain=1,early_chain_if=buff.nightfall.react,if=pet.darkglare.active |
| 8 | `drain_soul` | chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5 |
| 9 | `shadow_bolt` | — |

## Action List: `HC_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=(!dot.wither.ticking\|dot.wither.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `dark_harvest` | — |
| 4 | `agony` | target_if=min:remains,if=active_dot.agony<14&remains<5 |
| 5 | `summon_darkglare` | — |
| 6 | `malevolence` | — |
| 7 | `seed_of_corruption` | if=talent.sow_the_seeds\|active_enemies>5 |
| 8 | `unstable_affliction` | — |
| 9 | `agony` | target_if=min:remains,if=remains<5 |
| 10 | `malefic_grasp` | if=pet.darkglare.remains<gcd |

## Action List: `HC_cleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=talent.sow_the_seeds&!dot.wither.ticking&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `wither` | target_if=min:remains,if=remains<5&!(action.seed_of_corruption.in_flight\|dot.seed_of_corruption.remains>0)&fight_remains>remains+5 |
| 4 | `agony` | target_if=refreshable |
| 5 | `dark_harvest` | — |
| 6 | `summon_darkglare` | — |
| 7 | `malevolence` | — |
| 8 | `malefic_grasp` | if=pet.darkglare.remains<gcd |
| 9 | `unstable_affliction` | — |

## Action List: `HC_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `agony` | if=refreshable |
| 3 | `wither` | if=refreshable |
| 4 | `dark_harvest` | if=execute_time<(dot.agony.remains<?dot.corruption.remains) |
| 5 | `malevolence` | — |
| 6 | `summon_darkglare` | — |
| 7 | `malefic_grasp` | if=buff.nightfall.react>1\|pet.darkglare.remains<gcd |
| 8 | `drain_soul` | if=buff.nightfall.react>1 |
| 9 | `shadow_bolt` | if=buff.nightfall.react>1 |
| 10 | `unstable_affliction` | if=pet.darkglare.remains\|buff.malevolence.remains\|soul_shard>4\|buff.shard_instability.react\|buff.cascading_calamity.remains<gcd.max |

## Action List: `SH_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=(!dot.corruption.ticking\|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `dark_harvest` | — |
| 4 | `seed_of_corruption` | target_if=!dot.unstable_affliction.ticking&buff.succulent_soul.remains,if=set_bonus.midnight_season_2_4pc&active_enemies<=5 |
| 5 | `agony` | target_if=min:remains,if=active_dot.agony<12&remains<5 |
| 6 | `summon_darkglare` | — |
| 7 | `malefic_grasp` | if=buff.nightfall.react>1&active_enemies<=6 |
| 8 | `shadow_bolt` | if=buff.nightfall.react>1&active_enemies<=7 |
| 9 | `seed_of_corruption` | if=talent.sow_the_seeds\|active_enemies>5 |
| 10 | `unstable_affliction` | — |
| 11 | `agony` | target_if=min:remains,if=remains<duration*0.5 |
| 12 | `malefic_grasp` | if=pet.darkglare.remains<gcd |

## Action List: `SH_cleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=(!dot.corruption.ticking\|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `agony` | target_if=refreshable |
| 4 | `dark_harvest` | — |
| 5 | `summon_darkglare` | — |
| 6 | `seed_of_corruption` | target_if=!dot.unstable_affliction.ticking,if=buff.succulent_soul.remains&talent.sow_the_seeds&!pet.darkglare.active |
| 7 | `seed_of_corruption` | if=talent.sow_the_seeds&!pet.darkglare.active |
| 8 | `unstable_affliction` | cycle_targets=1,if=!ticking&buff.succulent_soul.remains |
| 9 | `unstable_affliction` | — |
| 10 | `malefic_grasp` | if=buff.nightfall.react>1\|pet.darkglare.remains<gcd |
| 11 | `drain_soul` | if=buff.nightfall.react>1 |
| 12 | `shadow_bolt` | if=buff.nightfall.react>1 |

## Action List: `SH_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `agony` | if=remains<3 |
| 3 | `corruption` | if=remains<3 |
| 4 | `dark_harvest` | if=soul_shard<3&execute_time<(dot.agony.remains<?dot.corruption.remains)&(!talent.cascading_calamity\|buff.cascading_calamity.remains)&(!set_bonus.midnight_season_2_4pc\|buff.unstable_empowerment.remains) |
| 5 | `summon_darkglare` | if=cooldown.dark_harvest.remains |
| 6 | `malefic_grasp` | if=buff.nightfall.react>1\|pet.darkglare.remains<gcd |
| 7 | `drain_soul` | if=buff.nightfall.react>1 |
| 8 | `shadow_bolt` | if=buff.nightfall.react>1 |
| 9 | `seed_of_corruption` | if=set_bonus.midnight_season_2_4pc&talent.siphon_life&buff.shard_instability.react |
| 10 | `unstable_affliction` | if=soul_shard\|buff.shard_instability.react |

## Action List: `end_of_fight`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `unstable_affliction` | if=soul_shard&fight_remains<8&active_enemies<3 |
| 2 | `seed_of_corruption` | if=soul_shard&fight_remains<8&active_enemies>2 |
| 3 | `drain_soul` | if=buff.nightfall.react&fight_remains<5 |
| 4 | `shadow_bolt` | if=buff.nightfall.react&fight_remains<5 |

## Action List: `hellcaller`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=HC_st,if=active_enemies=1 |
| 2 | `call_action_list` | name=HC_cleave,if=active_enemies=2 |
| 3 | `call_action_list` | name=HC_aoe,if=active_enemies>2 |

## Action List: `items`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=stormbound_emblem_of_dazar,if=cooldown.summon_darkglare.remains<=4&dot.agony.remains&(dot.corruption.remains\|dot.wither.remains)&cooldown.dark_harvest.remains>1 |
| 2 | `use_item` | name=galactic_gladiators_badge_of_ferocity,if=(buff.malevolence.up\|pet.darkglare.active)\|fight_remains<20 |
| 3 | `use_item` | name=hex_lords_dooming_idol,if=pet.darkglare.active\|buff.hex_lords_doom.stack>19\|fight_remains<=30 |
| 4 | `use_items` | if=(buff.malevolence.up\|pet.darkglare.active)\|fight_remains<20 |
| 5 | `use_item` | use_off_gcd=1,slot=main_hand |

## Action List: `ogcd`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `potion` | use_off_gcd=1,if=variable.cds_active\|fight_remains<32 |
| 2 | `invoke_external_buff` | name=power_infusion,if=variable.cds_active\|fight_remains<16 |
| 3 | `berserking` | use_off_gcd=1,if=variable.cds_active\|fight_remains<14 |
| 4 | `blood_fury` | use_off_gcd=1,if=variable.cds_active\|fight_remains<17 |
| 5 | `fireblood` | use_off_gcd=1,if=variable.cds_active\|fight_remains<10 |
| 6 | `ancestral_call` | use_off_gcd=1,if=variable.cds_active\|fight_remains<17 |

## Action List: `soul_harvester`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=SH_st,if=active_enemies=1 |
| 2 | `call_action_list` | name=SH_cleave,if=active_enemies=2 |
| 3 | `call_action_list` | name=SH_aoe,if=active_enemies>2 |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=cds_active,op=set,value=!talent.summon_darkglare\|pet.darkglare.remains |
| 2 | `variable` | name=darkglare_active,op=set,value=pet.darkglare.active\|(cooldown.summon_darkglare.duration-cooldown.summon_darkglare.remains)<20 |
| 3 | `cycling_variable` | name=min_agony,op=min,value=dot.agony.remains+(99*!dot.agony.remains) |
| 4 | `variable` | name=malevolence_from_cast,value=0,op=set,if=buff.malevolence.up=0 |
| 5 | `variable` | name=malevolence_from_cast,value=1,op=set,if=prev_gcd.1.malevolence |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=summon_pet
actions.precombat+=/variable,name=trinket_1_buffs,value=(trinket.1.has_buff.intellect|trinket.1.has_buff.mastery|trinket.1.has_buff.versatility|trinket.1.has_buff.haste|trinket.1.has_buff.crit|trinket.1.is.signet_of_the_priory)&(trinket.1.cooldown.duration>=20)
actions.precombat+=/variable,name=trinket_2_buffs,value=(trinket.2.has_buff.intellect|trinket.2.has_buff.mastery|trinket.2.has_buff.versatility|trinket.2.has_buff.haste|trinket.2.has_buff.crit|trinket.2.is.signet_of_the_priory)&(trinket.2.cooldown.duration>=20)
actions.precombat+=/snapshot_stats
actions.precombat+=/grimoire_of_sacrifice,if=talent.grimoire_of_sacrifice
actions.precombat+=/seed_of_corruption,if=(hero_tree.soul_harvester&active_enemies>1)|active_enemies>2
actions.precombat+=/haunt,if=active_enemies<2|(hero_tree.hellcaller&active_enemies<3)
actions.precombat+=/potion,if=potion.liquid_luster

# Executed every time the actor is available.
actions=call_action_list,name=variables
actions+=/call_action_list,name=end_of_fight
actions+=/call_action_list,name=ogcd
actions+=/call_action_list,name=items
actions+=/call_action_list,name=soul_harvester,if=hero_tree.soul_harvester
actions+=/call_action_list,name=hellcaller,if=hero_tree.hellcaller
actions+=/malefic_grasp,chain=1,early_chain_if=buff.nightfall.react,if=pet.darkglare.active
actions+=/drain_soul,chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5
actions+=/shadow_bolt

actions.HC_aoe=haunt
actions.HC_aoe+=/seed_of_corruption,if=(!dot.wither.ticking|dot.wither.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
actions.HC_aoe+=/dark_harvest
actions.HC_aoe+=/agony,target_if=min:remains,if=active_dot.agony<14&remains<5
actions.HC_aoe+=/summon_darkglare
actions.HC_aoe+=/malevolence
actions.HC_aoe+=/seed_of_corruption,if=talent.sow_the_seeds|active_enemies>5
actions.HC_aoe+=/unstable_affliction
actions.HC_aoe+=/agony,target_if=min:remains,if=remains<5
actions.HC_aoe+=/malefic_grasp,if=pet.darkglare.remains<gcd

actions.HC_cleave=haunt
actions.HC_cleave+=/seed_of_corruption,if=talent.sow_the_seeds&!dot.wither.ticking&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
actions.HC_cleave+=/wither,target_if=min:remains,if=remains<5&!(action.seed_of_corruption.in_flight|dot.seed_of_corruption.remains>0)&fight_remains>remains+5
actions.HC_cleave+=/agony,target_if=refreshable
actions.HC_cleave+=/dark_harvest
actions.HC_cleave+=/summon_darkglare
actions.HC_cleave+=/malevolence
actions.HC_cleave+=/malefic_grasp,if=pet.darkglare.remains<gcd
actions.HC_cleave+=/unstable_affliction

actions.HC_st=haunt
actions.HC_st+=/agony,if=refreshable
actions.HC_st+=/wither,if=refreshable
actions.HC_st+=/dark_harvest,if=execute_time<(dot.agony.remains<?dot.corruption.remains)
actions.HC_st+=/malevolence
actions.HC_st+=/summon_darkglare
actions.HC_st+=/malefic_grasp,if=buff.nightfall.react>1|pet.darkglare.remains<gcd
actions.HC_st+=/drain_soul,if=buff.nightfall.react>1
actions.HC_st+=/shadow_bolt,if=buff.nightfall.react>1
actions.HC_st+=/unstable_affliction,if=pet.darkglare.remains|buff.malevolence.remains|soul_shard>4|buff.shard_instability.react|buff.cascading_calamity.remains<gcd.max

actions.SH_aoe=haunt
actions.SH_aoe+=/seed_of_corruption,if=(!dot.corruption.ticking|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
actions.SH_aoe+=/dark_harvest
actions.SH_aoe+=/seed_of_corruption,target_if=!dot.unstable_affliction.ticking&buff.succulent_soul.remains,if=set_bonus.midnight_season_2_4pc&active_enemies<=5
actions.SH_aoe+=/agony,target_if=min:remains,if=active_dot.agony<12&remains<5
actions.SH_aoe+=/summon_darkglare
actions.SH_aoe+=/malefic_grasp,if=buff.nightfall.react>1&active_enemies<=6
actions.SH_aoe+=/shadow_bolt,if=buff.nightfall.react>1&active_enemies<=7
actions.SH_aoe+=/seed_of_corruption,if=talent.sow_the_seeds|active_enemies>5
actions.SH_aoe+=/unstable_affliction
actions.SH_aoe+=/agony,target_if=min:remains,if=remains<duration*0.5
actions.SH_aoe+=/malefic_grasp,if=pet.darkglare.remains<gcd

actions.SH_cleave=haunt
actions.SH_cleave+=/seed_of_corruption,if=(!dot.corruption.ticking|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
actions.SH_cleave+=/agony,target_if=refreshable
actions.SH_cleave+=/dark_harvest
actions.SH_cleave+=/summon_darkglare
actions.SH_cleave+=/seed_of_corruption,target_if=!dot.unstable_affliction.ticking,if=buff.succulent_soul.remains&talent.sow_the_seeds&!pet.darkglare.active
actions.SH_cleave+=/seed_of_corruption,if=talent.sow_the_seeds&!pet.darkglare.active
actions.SH_cleave+=/unstable_affliction,cycle_targets=1,if=!ticking&buff.succulent_soul.remains
actions.SH_cleave+=/unstable_affliction
actions.SH_cleave+=/malefic_grasp,if=buff.nightfall.react>1|pet.darkglare.remains<gcd
actions.SH_cleave+=/drain_soul,if=buff.nightfall.react>1
actions.SH_cleave+=/shadow_bolt,if=buff.nightfall.react>1

actions.SH_st=haunt
actions.SH_st+=/agony,if=remains<3
actions.SH_st+=/corruption,if=remains<3
actions.SH_st+=/dark_harvest,if=soul_shard<3&execute_time<(dot.agony.remains<?dot.corruption.remains)&(!talent.cascading_calamity|buff.cascading_calamity.remains)&(!set_bonus.midnight_season_2_4pc|buff.unstable_empowerment.remains)
actions.SH_st+=/summon_darkglare,if=cooldown.dark_harvest.remains
actions.SH_st+=/malefic_grasp,if=buff.nightfall.react>1|pet.darkglare.remains<gcd
actions.SH_st+=/drain_soul,if=buff.nightfall.react>1
actions.SH_st+=/shadow_bolt,if=buff.nightfall.react>1
actions.SH_st+=/seed_of_corruption,if=set_bonus.midnight_season_2_4pc&talent.siphon_life&buff.shard_instability.react
actions.SH_st+=/unstable_affliction,if=soul_shard|buff.shard_instability.react

actions.end_of_fight=unstable_affliction,if=soul_shard&fight_remains<8&active_enemies<3
actions.end_of_fight+=/seed_of_corruption,if=soul_shard&fight_remains<8&active_enemies>2
actions.end_of_fight+=/drain_soul,if=buff.nightfall.react&fight_remains<5
actions.end_of_fight+=/shadow_bolt,if=buff.nightfall.react&fight_remains<5

actions.hellcaller=call_action_list,name=HC_st,if=active_enemies=1
actions.hellcaller+=/call_action_list,name=HC_cleave,if=active_enemies=2
actions.hellcaller+=/call_action_list,name=HC_aoe,if=active_enemies>2

actions.items=use_item,name=stormbound_emblem_of_dazar,if=cooldown.summon_darkglare.remains<=4&dot.agony.remains&(dot.corruption.remains|dot.wither.remains)&cooldown.dark_harvest.remains>1
actions.items+=/use_item,name=galactic_gladiators_badge_of_ferocity,if=(buff.malevolence.up|pet.darkglare.active)|fight_remains<20
actions.items+=/use_item,name=hex_lords_dooming_idol,if=pet.darkglare.active|buff.hex_lords_doom.stack>19|fight_remains<=30
actions.items+=/use_items,if=(buff.malevolence.up|pet.darkglare.active)|fight_remains<20
actions.items+=/use_item,use_off_gcd=1,slot=main_hand

actions.ogcd=potion,use_off_gcd=1,if=variable.cds_active|fight_remains<32
actions.ogcd+=/invoke_external_buff,name=power_infusion,if=variable.cds_active|fight_remains<16
actions.ogcd+=/berserking,use_off_gcd=1,if=variable.cds_active|fight_remains<14
actions.ogcd+=/blood_fury,use_off_gcd=1,if=variable.cds_active|fight_remains<17
actions.ogcd+=/fireblood,use_off_gcd=1,if=variable.cds_active|fight_remains<10
actions.ogcd+=/ancestral_call,use_off_gcd=1,if=variable.cds_active|fight_remains<17

actions.soul_harvester=call_action_list,name=SH_st,if=active_enemies=1
actions.soul_harvester+=/call_action_list,name=SH_cleave,if=active_enemies=2
actions.soul_harvester+=/call_action_list,name=SH_aoe,if=active_enemies>2

actions.variables=variable,name=cds_active,op=set,value=!talent.summon_darkglare|pet.darkglare.remains
actions.variables+=/variable,name=darkglare_active,op=set,value=pet.darkglare.active|(cooldown.summon_darkglare.duration-cooldown.summon_darkglare.remains)<20
actions.variables+=/cycling_variable,name=min_agony,op=min,value=dot.agony.remains+(99*!dot.agony.remains)
actions.variables+=/variable,name=malevolence_from_cast,value=0,op=set,if=buff.malevolence.up=0
actions.variables+=/variable,name=malevolence_from_cast,value=1,op=set,if=prev_gcd.1.malevolence
```
