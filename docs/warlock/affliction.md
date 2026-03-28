# Warlock – Affliction

Auto-generated from SimulationCraft APL | Last updated: 2026-03-28 04:58 UTC

Source: `apl/default/warlock/affliction.simc`

---

## Overview

- **Action Lists:** 14
- **Total Actions:** 93
- **Lists:** `precombat`, `default`, `HC_aoe`, `HC_cleave`, `HC_st`, `SH_aoe`, `SH_cleave`, `SH_st`, `end_of_fight`, `hellcaller`, `items`, `ogcd`, `soul_harvester`, `variables`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `summon_pet` | — |
| 2 | `grimoire_of_sacrifice` | if=talent.grimoire_of_sacrifice |
| 3 | `snapshot_stats` | — |
| 4 | `seed_of_corruption` | if=(hero_tree.soul_harvester&active_enemies>1)\|active_enemies>2 |
| 5 | `haunt` | if=active_enemies<2\|(hero_tree.hellcaller&active_enemies<3) |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=variables |
| 2 | `call_action_list` | name=end_of_fight |
| 3 | `call_action_list` | name=ogcd |
| 4 | `call_action_list` | name=items |
| 5 | `call_action_list` | name=soul_harvester,if=hero_tree.soul_harvester |
| 6 | `call_action_list` | name=hellcaller,if=hero_tree.hellcaller |
| 7 | `seed_of_corruption` | if=talent.nocturnal_yield&active_enemies>1&buff.nightfall.react&(buff.nightfall.react=buff.nightfall.max_stack\|buff.nightfall.remains<execute_time*buff.nightfall.max_stack) |
| 8 | `malefic_grasp` | chain=1,early_chain_if=buff.nightfall.react,if=pet.darkglare.active |
| 9 | `drain_soul` | chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5 |
| 10 | `shadow_bolt` | — |

## Action List: `HC_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=(!dot.wither.ticking\|dot.wither.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `dark_harvest` | — |
| 4 | `agony` | target_if=min:remains,if=active_dot.agony<active_enemies&remains<5 |
| 5 | `summon_darkglare` | — |
| 6 | `malevolence` | — |
| 7 | `seed_of_corruption` | — |
| 8 | `unstable_affliction` | if=buff.shard_instability.react |
| 9 | `agony` | target_if=min:remains,if=remains<duration*0.5 |
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
| 9 | `unstable_affliction` | if=!talent.sow_the_seeds&!talent.patient_zero&(pet.darkglare.remains\|buff.malevolence.remains\|soul_shard>4\|buff.shard_instability.react\|buff.cascading_calamity.remains<gcd.max) |
| 10 | `seed_of_corruption` | if=talent.patient_zero&talent.sow_the_seeds |

## Action List: `HC_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `agony` | if=refreshable |
| 3 | `wither` | if=refreshable |
| 4 | `dark_harvest` | if=execute_time<(dot.agony.remains<?dot.corruption.remains) |
| 5 | `agony` | if=dot.agony.remains<20&cooldown.summon_darkglare.remains<gcd |
| 6 | `summon_darkglare` | — |
| 7 | `malevolence` | — |
| 8 | `malefic_grasp` | if=buff.nightfall.react>1\|pet.darkglare.remains<gcd |
| 9 | `drain_soul` | if=buff.nightfall.react>1 |
| 10 | `shadow_bolt` | if=buff.nightfall.react>1 |
| 11 | `unstable_affliction` | if=pet.darkglare.remains\|buff.malevolence.remains\|soul_shard>4\|buff.shard_instability.react\|buff.cascading_calamity.remains<gcd.max |

## Action List: `SH_aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=(!dot.corruption.ticking\|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `dark_harvest` | — |
| 4 | `agony` | target_if=min:remains,if=active_dot.agony<5&remains<5 |
| 5 | `summon_darkglare` | — |
| 6 | `seed_of_corruption` | if=talent.sow_the_seeds |
| 7 | `unstable_affliction` | if=!talent.sow_the_seeds |
| 8 | `agony` | target_if=min:remains,if=remains<duration*0.5 |
| 9 | `malefic_grasp` | if=pet.darkglare.remains<gcd |

## Action List: `SH_cleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `seed_of_corruption` | if=(!dot.corruption.ticking\|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight |
| 3 | `dark_harvest` | — |
| 4 | `agony` | target_if=refreshable |
| 5 | `summon_darkglare` | — |
| 6 | `malefic_grasp` | if=buff.nightfall.react>1\|pet.darkglare.remains<gcd |
| 7 | `drain_soul` | if=buff.nightfall.react>1 |
| 8 | `shadow_bolt` | if=buff.nightfall.react>1 |
| 9 | `unstable_affliction` | if=!talent.patient_zero&!talent.sow_the_seeds&(soul_shard\|buff.shard_instability.react) |
| 10 | `seed_of_corruption` | if=talent.patient_zero&talent.sow_the_seeds |

## Action List: `SH_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `haunt` | — |
| 2 | `agony` | if=refreshable |
| 3 | `corruption` | if=refreshable |
| 4 | `dark_harvest` | if=soul_shard<3&execute_time<(dot.agony.remains<?dot.corruption.remains) |
| 5 | `summon_darkglare` | if=cooldown.dark_harvest.remains |
| 6 | `malefic_grasp` | if=buff.nightfall.react>1\|pet.darkglare.remains<gcd |
| 7 | `drain_soul` | if=buff.nightfall.react>1 |
| 8 | `shadow_bolt` | if=buff.nightfall.react>1 |
| 9 | `unstable_affliction` | if=soul_shard\|buff.shard_instability.react |

## Action List: `end_of_fight`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `unstable_affliction` | if=soul_shard&fight_remains<8&(!talent.patient_zero&!talent.sow_the_seeds) |
| 2 | `seed_of_corruption` | if=soul_shard&fight_remains<8&(talent.patient_zero&talent.sow_the_seeds) |
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
| 1 | `use_item` | use_off_gcd=1,slot=trinket1,if=variable.cds_active |
| 2 | `use_item` | use_off_gcd=1,slot=trinket2,if=variable.cds_active |

## Action List: `ogcd`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `potion` | use_off_gcd=1,if=variable.cds_active\|fight_remains<32 |
| 2 | `berserking` | use_off_gcd=1,if=variable.cds_active\|fight_remains<14 |
| 3 | `blood_fury` | use_off_gcd=1,if=variable.cds_active\|fight_remains<17 |
| 4 | `fireblood` | use_off_gcd=1,if=variable.cds_active\|fight_remains<10 |
| 5 | `ancestral_call` | use_off_gcd=1,if=variable.cds_active\|fight_remains<17 |

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
| 2 | `cycling_variable` | name=min_agony,op=min,value=dot.agony.remains+(99*!dot.agony.remains) |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=summon_pet
actions.precombat+=/grimoire_of_sacrifice,if=talent.grimoire_of_sacrifice
actions.precombat+=/snapshot_stats
actions.precombat+=/seed_of_corruption,if=(hero_tree.soul_harvester&active_enemies>1)|active_enemies>2
actions.precombat+=/haunt,if=active_enemies<2|(hero_tree.hellcaller&active_enemies<3)

# Executed every time the actor is available.
actions=call_action_list,name=variables
actions+=/call_action_list,name=end_of_fight
actions+=/call_action_list,name=ogcd
actions+=/call_action_list,name=items
actions+=/call_action_list,name=soul_harvester,if=hero_tree.soul_harvester
actions+=/call_action_list,name=hellcaller,if=hero_tree.hellcaller
actions+=/seed_of_corruption,if=talent.nocturnal_yield&active_enemies>1&buff.nightfall.react&(buff.nightfall.react=buff.nightfall.max_stack|buff.nightfall.remains<execute_time*buff.nightfall.max_stack)
actions+=/malefic_grasp,chain=1,early_chain_if=buff.nightfall.react,if=pet.darkglare.active
actions+=/drain_soul,chain=1,early_chain_if=buff.nightfall.react,interrupt_if=tick_time>0.5
actions+=/shadow_bolt

actions.HC_aoe=haunt
actions.HC_aoe+=/seed_of_corruption,if=(!dot.wither.ticking|dot.wither.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
actions.HC_aoe+=/dark_harvest
actions.HC_aoe+=/agony,target_if=min:remains,if=active_dot.agony<active_enemies&remains<5
actions.HC_aoe+=/summon_darkglare
actions.HC_aoe+=/malevolence
actions.HC_aoe+=/seed_of_corruption
actions.HC_aoe+=/unstable_affliction,if=buff.shard_instability.react
actions.HC_aoe+=/agony,target_if=min:remains,if=remains<duration*0.5
actions.HC_aoe+=/malefic_grasp,if=pet.darkglare.remains<gcd

actions.HC_cleave=haunt
actions.HC_cleave+=/seed_of_corruption,if=talent.sow_the_seeds&!dot.wither.ticking&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
actions.HC_cleave+=/wither,target_if=min:remains,if=remains<5&!(action.seed_of_corruption.in_flight|dot.seed_of_corruption.remains>0)&fight_remains>remains+5
actions.HC_cleave+=/agony,target_if=refreshable
actions.HC_cleave+=/dark_harvest
actions.HC_cleave+=/summon_darkglare
actions.HC_cleave+=/malevolence
actions.HC_cleave+=/malefic_grasp,if=pet.darkglare.remains<gcd
actions.HC_cleave+=/unstable_affliction,if=!talent.sow_the_seeds&!talent.patient_zero&(pet.darkglare.remains|buff.malevolence.remains|soul_shard>4|buff.shard_instability.react|buff.cascading_calamity.remains<gcd.max)
actions.HC_cleave+=/seed_of_corruption,if=talent.patient_zero&talent.sow_the_seeds

# Haunt on CD for apex
actions.HC_st=haunt
actions.HC_st+=/agony,if=refreshable
actions.HC_st+=/wither,if=refreshable
# Dark Harvest on CD regardless of Darkglare
actions.HC_st+=/dark_harvest,if=execute_time<(dot.agony.remains<?dot.corruption.remains)
# Refresh agony right before Darkglare so it lasts the entire duration
actions.HC_st+=/agony,if=dot.agony.remains<20&cooldown.summon_darkglare.remains<gcd
actions.HC_st+=/summon_darkglare
actions.HC_st+=/malevolence
actions.HC_st+=/malefic_grasp,if=buff.nightfall.react>1|pet.darkglare.remains<gcd
actions.HC_st+=/drain_soul,if=buff.nightfall.react>1
actions.HC_st+=/shadow_bolt,if=buff.nightfall.react>1
# Always maintain Cascading Calamity, only dump inside Malevolence
actions.HC_st+=/unstable_affliction,if=pet.darkglare.remains|buff.malevolence.remains|soul_shard>4|buff.shard_instability.react|buff.cascading_calamity.remains<gcd.max

actions.SH_aoe=haunt
actions.SH_aoe+=/seed_of_corruption,if=(!dot.corruption.ticking|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
# Do not care about losing shards in 2+ targets
actions.SH_aoe+=/dark_harvest
# Maintain ~5 agonies (will be 6 with Shared Agony)
actions.SH_aoe+=/agony,target_if=min:remains,if=active_dot.agony<5&remains<5
actions.SH_aoe+=/summon_darkglare
actions.SH_aoe+=/seed_of_corruption,if=talent.sow_the_seeds
actions.SH_aoe+=/unstable_affliction,if=!talent.sow_the_seeds
actions.SH_aoe+=/agony,target_if=min:remains,if=remains<duration*0.5
actions.SH_aoe+=/malefic_grasp,if=pet.darkglare.remains<gcd

actions.SH_cleave=haunt
actions.SH_cleave+=/seed_of_corruption,if=(!dot.corruption.ticking|dot.corruption.refreshable)&!dot.seed_of_corruption.ticking&!prev.seed_of_corruption&!action.seed_of_corruption.in_flight
# Do not care about losing shards in 2+ targets
actions.SH_cleave+=/dark_harvest
actions.SH_cleave+=/agony,target_if=refreshable
actions.SH_cleave+=/summon_darkglare
actions.SH_cleave+=/malefic_grasp,if=buff.nightfall.react>1|pet.darkglare.remains<gcd
actions.SH_cleave+=/drain_soul,if=buff.nightfall.react>1
actions.SH_cleave+=/shadow_bolt,if=buff.nightfall.react>1
actions.SH_cleave+=/unstable_affliction,if=!talent.patient_zero&!talent.sow_the_seeds&(soul_shard|buff.shard_instability.react)
actions.SH_cleave+=/seed_of_corruption,if=talent.patient_zero&talent.sow_the_seeds

# Haunt on CD for apex, regardless of Nightfall stacks
actions.SH_st=haunt
actions.SH_st+=/agony,if=refreshable
actions.SH_st+=/corruption,if=refreshable
# Do not overcap shards
actions.SH_st+=/dark_harvest,if=soul_shard<3&execute_time<(dot.agony.remains<?dot.corruption.remains)
# use Dark Harvest only outside Darkglare
actions.SH_st+=/summon_darkglare,if=cooldown.dark_harvest.remains
actions.SH_st+=/malefic_grasp,if=buff.nightfall.react>1|pet.darkglare.remains<gcd
actions.SH_st+=/drain_soul,if=buff.nightfall.react>1
actions.SH_st+=/shadow_bolt,if=buff.nightfall.react>1
# SH does not care about saving shards in pure patchwerk. In reality it's good to save 1 shard for cascading calamity
actions.SH_st+=/unstable_affliction,if=soul_shard|buff.shard_instability.react

actions.end_of_fight=unstable_affliction,if=soul_shard&fight_remains<8&(!talent.patient_zero&!talent.sow_the_seeds)
actions.end_of_fight+=/seed_of_corruption,if=soul_shard&fight_remains<8&(talent.patient_zero&talent.sow_the_seeds)
actions.end_of_fight+=/drain_soul,if=buff.nightfall.react&fight_remains<5
actions.end_of_fight+=/shadow_bolt,if=buff.nightfall.react&fight_remains<5

actions.hellcaller=call_action_list,name=HC_st,if=active_enemies=1
actions.hellcaller+=/call_action_list,name=HC_cleave,if=active_enemies=2
actions.hellcaller+=/call_action_list,name=HC_aoe,if=active_enemies>2

actions.items=use_item,use_off_gcd=1,slot=trinket1,if=variable.cds_active
actions.items+=/use_item,use_off_gcd=1,slot=trinket2,if=variable.cds_active

actions.ogcd=potion,use_off_gcd=1,if=variable.cds_active|fight_remains<32
actions.ogcd+=/berserking,use_off_gcd=1,if=variable.cds_active|fight_remains<14
actions.ogcd+=/blood_fury,use_off_gcd=1,if=variable.cds_active|fight_remains<17
actions.ogcd+=/fireblood,use_off_gcd=1,if=variable.cds_active|fight_remains<10
actions.ogcd+=/ancestral_call,use_off_gcd=1,if=variable.cds_active|fight_remains<17

actions.soul_harvester=call_action_list,name=SH_st,if=active_enemies=1
actions.soul_harvester+=/call_action_list,name=SH_cleave,if=active_enemies=2
actions.soul_harvester+=/call_action_list,name=SH_aoe,if=active_enemies>2

actions.variables=variable,name=cds_active,op=set,value=!talent.summon_darkglare|pet.darkglare.remains
actions.variables+=/cycling_variable,name=min_agony,op=min,value=dot.agony.remains+(99*!dot.agony.remains)
```
