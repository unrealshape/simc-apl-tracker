# Demon Hunter – Devourer

Auto-generated from SimulationCraft APL | Last updated: 2026-09-26 08:29 UTC

Source: `apl/default/demonhunter/devourer.simc`

---

## Overview

- **Action Lists:** 12
- **Total Actions:** 153
- **Lists:** `precombat`, `default`, `annihilator_melee`, `annihilator_ranged`, `cooldowns`, `reaps`, `variables`, `voidscarred_melee`, `voidscarred_ranged`, `vsm_meta`, `vsm_out`, `vsm_st`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `variable` | name=trinket_1_buffs,value=trinket.1.has_buff.intellect\|trinket.1.has_buff.mastery\|trinket.1.has_buff.versatility\|trinket.1.has_buff.haste\|trinket.1.has_buff.crit |
| 3 | `variable` | name=trinket_2_buffs,value=trinket.2.has_buff.intellect\|trinket.2.has_buff.mastery\|trinket.2.has_buff.versatility\|trinket.2.has_buff.haste\|trinket.2.has_buff.crit |
| 4 | `variable` | name=trinket_1_manual,value=trinket.1.is.font_of_venomous_rage |
| 5 | `variable` | name=trinket_2_manual,value=trinket.2.is.font_of_venomous_rage |
| 6 | `variable` | name=trinket_1_ogcd_cast,value=0 |
| 7 | `variable` | name=trinket_2_ogcd_cast,value=0 |
| 8 | `variable` | name=trinket_1_exclude,value=0 |
| 9 | `variable` | name=trinket_2_exclude,value=0 |
| 10 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs\|variable.trinket_2_buffs&((trinket.2.proc.any_dps.duration)*trinket.2.proc.any_dps.default_value)>((trinket.1.proc.any_dps.duration)*trinket.1.proc.any_dps.default_value) |
| 11 | `variable` | name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl |
| 12 | `arcane_torrent` | — |
| 13 | `soul_immolation` | — |
| 14 | `consume` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=variables |
| 2 | `call_action_list` | name=cooldowns |
| 3 | `run_action_list` | name=annihilator_melee,if=hero_tree.annihilator&talent.the_hunt |
| 4 | `run_action_list` | name=annihilator_ranged,if=hero_tree.annihilator |
| 5 | `run_action_list` | name=voidscarred_ranged,if=hero_tree.voidscarred&!talent.the_hunt |
| 6 | `run_action_list` | name=voidscarred_melee,if=hero_tree.voidscarred&talent.the_hunt |

## Action List: `annihilator_melee`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `metamorphosis` | if=(buff.eradicate.up\|!talent.eradicate\|active_enemies=1\|talent.voidfall)&(active_enemies>1\|buff.moment_of_craving.up\|cooldown.void_ray.remains>6) |
| 2 | `devour` | if=buff.soulburst.up |
| 3 | `consume` | if=buff.soulburst.up |
| 4 | `void_ray` | if=talent.eradicate&active_enemies>1&!buff.eradicate.up |
| 5 | `collapsing_star` | if=active_enemies=1&(apex.1\|buff.dark_matter.up\|talent.star_fragments) |
| 6 | `the_hunt` | if=buff.metamorphosis.up |
| 7 | `hungering_slash` | if=!buff.metamorphosis.up&soul_fragments<=8 |
| 8 | `reapers_toll` | if=!buff.metamorphosis.up&soul_fragments<=8 |
| 9 | `vengeful_retreat` | if=talent.devourers_bite&buff.voidstep.up |
| 10 | `hungering_slash` | if=active_enemies>1 |
| 11 | `reapers_toll` | if=talent.devourers_bite&(buff.voidsurge_reapers_toll.up\|active_enemies>1) |
| 12 | `voidblade` | if=buff.metamorphosis.up |
| 13 | `voidblade` | if=!buff.metamorphosis.up&(active_enemies=1\|!talent.eradicate&active_enemies<4) |
| 14 | `call_action_list` | name=reaps,if=active_enemies=1&action.reap.souls_consumed>=4 |
| 15 | `call_action_list` | name=reaps,if=!talent.eradicate&(active_enemies>1&variable.wont_overcap_cstar&set_bonus.midnight_season_2_4pc&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray\|buff.voidfall_spending.react>=3)) |
| 16 | `call_action_list` | name=reaps,if=action.reap.souls_consumed>=4&active_enemies<5&(active_enemies>1\|!buff.metamorphosis.up\|buff.moment_of_craving.up\|buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30\|void_metamorphosis_base_drain_ps>35) |
| 17 | `call_action_list` | name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1 |
| 18 | `call_action_list` | name=reaps,if=talent.eradicate&active_enemies>1&buff.eradicate.up&action.reap.souls_consumed>=1 |
| 19 | `void_ray` | if=!buff.eradicate.up\|!buff.moment_of_craving.up\|set_bonus.midnight_season_2_4pc |
| 20 | `collapsing_star` | if=active_enemies>1 |
| 21 | `call_action_list` | name=reaps,if=buff.eradicate.up&active_enemies>1&action.reap.souls_consumed>=4+6*buff.moment_of_craving.up |
| 22 | `call_action_list` | name=reaps,if=!talent.eradicate&(active_enemies>1&!buff.metamorphosis.up&buff.moment_of_craving.up&talent.voidfall&(buff.voidfall_building.react<2\|variable.ray_after_reap)) |
| 23 | `call_action_list` | name=reaps,if=!talent.eradicate&(active_enemies>1&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray\|buff.voidfall_spending.react>=3)) |
| 24 | `call_action_list` | name=reaps,if=active_enemies>1&buff.metamorphosis.up&talent.collapsing_star&(active_enemies>1\|apex.1\|buff.dark_matter.up\|talent.star_fragments)&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&variable.wont_overcap_cstar&void_metamorphosis_base_drain_ps>35 |
| 25 | `soul_immolation` | if=active_dot.soul_immolation=0&(!buff.metamorphosis.up\|fury<void_metamorphosis_base_drain_ps) |
| 26 | `devour` | — |
| 27 | `consume` | — |

## Action List: `annihilator_ranged`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.6,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1-(active_enemies>1) |
| 2 | `pick_up_fragment` | use_off_gcd=1,if=buff.metamorphosis.up&cooldown.reap.remains&soul_fragments+buff.collapsing_star_stacking.stack>=30&fury<void_metamorphosis_base_drain_ps&buff.collapsing_star_stacking.stack<30 |
| 3 | `metamorphosis` | — |
| 4 | `devour` | if=buff.soulburst.up&active_enemies=1 |
| 5 | `consume` | if=buff.soulburst.up |
| 6 | `void_ray` | if=talent.eradicate&active_enemies>1&!buff.eradicate.up |
| 7 | `collapsing_star` | if=active_enemies>1&buff.collapsing_star_stacking.stack>=30 |
| 8 | `call_action_list` | name=reaps,if=active_enemies=1&!buff.metamorphosis.up&action.reap.souls_consumed>=4&variable.wont_drop_meta |
| 9 | `collapsing_star` | if=active_enemies=1 |
| 10 | `call_action_list` | name=reaps,if=active_enemies=1&action.reap.souls_consumed>=4 |
| 11 | `call_action_list` | name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1 |
| 12 | `call_action_list` | name=reaps,if=active_enemies>1&buff.eradicate.up&action.reap.souls_consumed>=4+6*buff.moment_of_craving.up |
| 13 | `void_ray` | if=!buff.eradicate.up\|!buff.moment_of_craving.up\|!set_bonus.midnight_season_2_4pc |
| 14 | `call_action_list` | name=reaps,if=(!buff.eradicate.up\|active_enemies=1)&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray\|buff.voidfall_spending.react>=3) |
| 15 | `call_action_list` | name=reaps,if=buff.metamorphosis.up&talent.collapsing_star&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&variable.wont_overcap_cstar&void_metamorphosis_base_drain_ps>35&action.reap.souls_consumed>=4&variable.wont_drop_meta |
| 16 | `soul_immolation` | if=active_dot.soul_immolation=0&(!buff.metamorphosis.up\|fury<void_metamorphosis_base_drain_ps) |
| 17 | `devour` | — |
| 18 | `consume` | — |

## Action List: `cooldowns`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_external_buff` | name=power_infusion,if=buff.metamorphosis.up&!buff.power_infusion.up |
| 2 | `potion` | if=buff.metamorphosis.up\|fight_remains<=30 |
| 3 | `use_item` | slot=trinket1,if=buff.metamorphosis.up&(variable.void_ray_count=0\|hero_tree.annihilator)&(!trinket.2.has_cooldown\|trinket.2.cooldown.remains\|variable.trinket_priority=1\|variable.trinket_2_exclude)&!variable.trinket_1_manual\|trinket.1.proc.any_dps.duration>=fight_remains\|fight_remains<=trinket.1.buff.any_dps.duration |
| 4 | `use_item` | slot=trinket2,if=buff.metamorphosis.up&(variable.void_ray_count=0\|hero_tree.annihilator)&(!trinket.1.has_cooldown\|trinket.1.cooldown.remains\|variable.trinket_priority=2\|variable.trinket_1_exclude)&!variable.trinket_2_manual\|trinket.2.proc.any_dps.duration>=fight_remains\|fight_remains<=trinket.2.buff.any_dps.duration |
| 5 | `use_item` | use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&!variable.trinket_1_manual&(variable.damage_trinket_priority=1\|trinket.2.cooldown.remains\|trinket.2.is.spymasters_web\|trinket.2.cooldown.duration=0)&gcd.remains>0.1 |
| 6 | `use_item` | use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&!variable.trinket_2_manual&(variable.damage_trinket_priority=2\|trinket.1.cooldown.remains\|trinket.1.is.spymasters_web\|trinket.1.cooldown.duration=0)&gcd.remains>0.1 |
| 7 | `use_item` | use_off_gcd=1,slot=trinket1,if=trinket.1.is.font_of_venomous_rage&!buff.metamorphosis.up&buff.rolling_torment.up&gcd.remains>0.1 |
| 8 | `use_item` | use_off_gcd=1,slot=trinket2,if=trinket.2.is.font_of_venomous_rage&!buff.metamorphosis.up&buff.rolling_torment.up&gcd.remains>0.1 |
| 9 | `use_item` | slot=trinket1,if=!variable.trinket_1_buffs&!variable.trinket_1_manual&(variable.damage_trinket_priority=1\|trinket.2.cooldown.remains\|trinket.2.is.spymasters_web\|trinket.2.cooldown.duration=0)&!variable.trinket_1_ogcd_cast |
| 10 | `use_item` | slot=trinket2,if=!variable.trinket_2_buffs&!variable.trinket_2_manual&(variable.damage_trinket_priority=2\|trinket.1.cooldown.remains\|trinket.1.is.spymasters_web\|trinket.1.cooldown.duration=0)&!variable.trinket_2_ogcd_cast |

## Action List: `reaps`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `eradicate` | — |
| 2 | `cull` | — |
| 3 | `reap` | — |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=wont_overcap_cstar,op=set,value=!buff.metamorphosis.up\|((buff.collapsing_star_stacking.stack+action.reap.souls_consumed)<=buff.collapsing_star_stacking.max_stack\|!(talent.collapsing_star&(active_enemies>1\|apex.1\|buff.dark_matter.up\|talent.star_fragments))) |
| 2 | `variable` | name=wont_drop_meta,op=set,value=!buff.metamorphosis.up\|!buff.moment_of_craving.up\|(fury>void_metamorphosis_base_drain_ps+4*action.reap.souls_consumed+10*talent.scythes_embrace&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30\|!(talent.collapsing_star&(active_enemies>1\|apex.1\|buff.dark_matter.up\|talent.star_fragments))) |
| 3 | `variable` | name=ray_after_reap,op=set,value=fury+4*action.reap.souls_consumed+10*talent.scythes_embrace>=100 |
| 4 | `variable` | name=void_ray_count,op=reset,if=!buff.metamorphosis.up |
| 5 | `variable` | name=void_ray_count,op=add,value=1,if=buff.metamorphosis.up&action.void_ray.last_used>variable.last_ray_mark |
| 6 | `variable` | name=last_ray_mark,op=set,value=action.void_ray.last_used |

## Action List: `voidscarred_melee`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `run_action_list` | name=vsm_st,if=active_enemies=1 |
| 2 | `run_action_list` | name=vsm_meta,if=buff.metamorphosis.up |
| 3 | `run_action_list` | name=vsm_out |

## Action List: `voidscarred_ranged`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `voidblade` | if=buff.void_metamorphosis_stack.at_max_stacks&talent.devourers_bite |
| 2 | `metamorphosis` | if=buff.eradicate.up\|!talent.eradicate\|active_enemies=1 |
| 3 | `devour` | if=buff.soulburst.up&active_enemies=1 |
| 4 | `consume` | if=buff.soulburst.up |
| 5 | `collapsing_star` | if=active_enemies=1&buff.collapsing_star_stacking.stack>=35 |
| 6 | `call_action_list` | name=reaps,if=action.reap.souls_consumed>=4 |
| 7 | `call_action_list` | name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1 |
| 8 | `void_ray` | if=!buff.eradicate.up\|!buff.moment_of_craving.up\|set_bonus.midnight_season_2_4pc |
| 9 | `collapsing_star` | if=active_enemies>1 |
| 10 | `vengeful_retreat` | if=buff.voidstep.up |
| 11 | `reapers_toll` | if=buff.voidsurge_reapers_toll.up |
| 12 | `pierce_the_veil` | if=buff.voidsurge_pierce_the_veil.up |
| 13 | `soul_immolation` | if=active_dot.soul_immolation=0&(!buff.metamorphosis.up\|fury<void_metamorphosis_base_drain_ps) |
| 14 | `devour` | — |
| 15 | `consume` | — |

## Action List: `vsm_meta`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `soul_immolation` | if=variable.void_ray_count>=2&active_dot.soul_immolation=0&fury<=gcd.max*(void_metamorphosis_base_drain_ps-6)-6 |
| 2 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.35,if=variable.void_ray_count=1&cooldown.void_ray.remains<gcd.max*2&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains |
| 3 | `wait` | sec=0.05,if=variable.void_ray_count>=2 |
| 4 | `vengeful_retreat` | use_off_gcd=1,if=buff.voidstep.up |
| 5 | `void_ray` | if=variable.void_ray_count=0&!talent.eradicate |
| 6 | `eradicate` | if=(buff.moment_of_craving.remains<gcd.max\|cooldown.void_ray.remains<gcd.max)&!buff.soulburst.up |
| 7 | `void_ray` | if=talent.eradicate&!buff.eradicate.up |
| 8 | `reapers_toll` | if=buff.hungering_slash.remains<gcd.max*2 |
| 9 | `devour` | if=buff.soulburst.up |
| 10 | `reapers_toll` | if=soul_fragments<=8 |
| 11 | `pierce_the_veil` | if=!buff.hungering_slash.up |
| 12 | `predators_wake` | if=!buff.hungering_slash.up |
| 13 | `eradicate` | if=action.reap.souls_consumed>=8&!buff.soulburst.up |
| 14 | `cull` | if=action.reap.souls_consumed>=4&!buff.soulburst.up |
| 15 | `void_ray` | — |
| 16 | `soul_immolation` | if=active_dot.soul_immolation=0&fury<=gcd.max*(void_metamorphosis_base_drain_ps-6)-6&cooldown.void_ray.remains>gcd.max |
| 17 | `devour` | if=fury<void_metamorphosis_base_drain_ps*(cooldown.void_ray.remains+3) |

## Action List: `vsm_out`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.3,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-3 |
| 2 | `wait` | sec=0.05,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1&time-action.pick_up_fragment.last_used<1.5 |
| 3 | `vengeful_retreat` | use_off_gcd=1,if=buff.voidstep.up |
| 4 | `voidblade` | if=prev_gcd.1.void_ray |
| 5 | `metamorphosis` | if=buff.eradicate.up\|!talent.eradicate\|fight_remains<15 |
| 6 | `the_hunt` | — |
| 7 | `consume` | if=buff.soulburst.up&buff.soulburst.remains<gcd.max |
| 8 | `void_ray` | if=talent.eradicate&!buff.eradicate.up |
| 9 | `hungering_slash` | — |
| 10 | `soul_immolation` | if=active_dot.soul_immolation=0 |
| 11 | `reap` | if=action.reap.souls_consumed>=4&!buff.soulburst.up |
| 12 | `eradicate` | if=action.reap.souls_consumed>=4&!buff.soulburst.up |
| 13 | `void_ray` | — |
| 14 | `consume` | — |

## Action List: `vsm_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.75,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1 |
| 2 | `soul_immolation` | if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps |
| 3 | `devour` | if=buff.soulburst.up |
| 4 | `consume` | if=buff.soulburst.up |
| 5 | `voidblade` | if=buff.void_metamorphosis_stack.at_max_stacks |
| 6 | `vengeful_retreat` | if=buff.void_metamorphosis_stack.at_max_stacks&cooldown.the_hunt.ready&!buff.metamorphosis.up |
| 7 | `the_hunt` | if=buff.void_metamorphosis_stack.at_max_stacks&buff.vengeful_retreat_movement.up |
| 8 | `metamorphosis` | — |
| 9 | `the_hunt` | if=!buff.metamorphosis.up&(fight_remains<15\|buff.void_metamorphosis_stack.stack<buff.void_metamorphosis_stack.max_stack*0.25) |
| 10 | `wait` | sec=0.05,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1&soul_fragments>=1 |
| 11 | `hungering_slash` | — |
| 12 | `reapers_toll` | if=soul_fragments<=8 |
| 13 | `vengeful_retreat` | if=buff.voidstep.up |
| 14 | `pierce_the_veil` | — |
| 15 | `call_action_list` | name=reaps,if=action.reap.souls_consumed>=4 |
| 16 | `predators_wake` | — |
| 17 | `void_ray` | if=!buff.eradicate.up\|!buff.moment_of_craving.up\|set_bonus.midnight_season_2_4pc |
| 18 | `soul_immolation` | if=active_dot.soul_immolation=0&!buff.metamorphosis.up |
| 19 | `devour` | — |
| 20 | `consume` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=snapshot_stats
actions.precombat+=/variable,name=trinket_1_buffs,value=trinket.1.has_buff.intellect|trinket.1.has_buff.mastery|trinket.1.has_buff.versatility|trinket.1.has_buff.haste|trinket.1.has_buff.crit
actions.precombat+=/variable,name=trinket_2_buffs,value=trinket.2.has_buff.intellect|trinket.2.has_buff.mastery|trinket.2.has_buff.versatility|trinket.2.has_buff.haste|trinket.2.has_buff.crit
actions.precombat+=/variable,name=trinket_1_manual,value=trinket.1.is.font_of_venomous_rage
actions.precombat+=/variable,name=trinket_2_manual,value=trinket.2.is.font_of_venomous_rage
actions.precombat+=/variable,name=trinket_1_ogcd_cast,value=0
actions.precombat+=/variable,name=trinket_2_ogcd_cast,value=0
actions.precombat+=/variable,name=trinket_1_exclude,value=0
actions.precombat+=/variable,name=trinket_2_exclude,value=0
actions.precombat+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs|variable.trinket_2_buffs&((trinket.2.proc.any_dps.duration)*trinket.2.proc.any_dps.default_value)>((trinket.1.proc.any_dps.duration)*trinket.1.proc.any_dps.default_value)
actions.precombat+=/variable,name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl
actions.precombat+=/arcane_torrent
actions.precombat+=/soul_immolation
actions.precombat+=/consume

# Executed every time the actor is available.
actions=call_action_list,name=variables
actions+=/call_action_list,name=cooldowns
actions+=/run_action_list,name=annihilator_melee,if=hero_tree.annihilator&talent.the_hunt
actions+=/run_action_list,name=annihilator_ranged,if=hero_tree.annihilator
actions+=/run_action_list,name=voidscarred_ranged,if=hero_tree.voidscarred&!talent.the_hunt
actions+=/run_action_list,name=voidscarred_melee,if=hero_tree.voidscarred&talent.the_hunt

actions.annihilator_melee=metamorphosis,if=(buff.eradicate.up|!talent.eradicate|active_enemies=1|talent.voidfall)&(active_enemies>1|buff.moment_of_craving.up|cooldown.void_ray.remains>6)
actions.annihilator_melee+=/devour,if=buff.soulburst.up
actions.annihilator_melee+=/consume,if=buff.soulburst.up
actions.annihilator_melee+=/void_ray,if=talent.eradicate&active_enemies>1&!buff.eradicate.up
actions.annihilator_melee+=/collapsing_star,if=active_enemies=1&(apex.1|buff.dark_matter.up|talent.star_fragments)
actions.annihilator_melee+=/the_hunt,if=buff.metamorphosis.up
actions.annihilator_melee+=/hungering_slash,if=!buff.metamorphosis.up&soul_fragments<=8
actions.annihilator_melee+=/reapers_toll,if=!buff.metamorphosis.up&soul_fragments<=8
actions.annihilator_melee+=/vengeful_retreat,if=talent.devourers_bite&buff.voidstep.up
actions.annihilator_melee+=/hungering_slash,if=active_enemies>1
actions.annihilator_melee+=/reapers_toll,if=talent.devourers_bite&(buff.voidsurge_reapers_toll.up|active_enemies>1)
actions.annihilator_melee+=/voidblade,if=buff.metamorphosis.up
actions.annihilator_melee+=/voidblade,if=!buff.metamorphosis.up&(active_enemies=1|!talent.eradicate&active_enemies<4)
actions.annihilator_melee+=/call_action_list,name=reaps,if=active_enemies=1&action.reap.souls_consumed>=4
actions.annihilator_melee+=/call_action_list,name=reaps,if=!talent.eradicate&(active_enemies>1&variable.wont_overcap_cstar&set_bonus.midnight_season_2_4pc&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray|buff.voidfall_spending.react>=3))
actions.annihilator_melee+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4&active_enemies<5&(active_enemies>1|!buff.metamorphosis.up|buff.moment_of_craving.up|buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30|void_metamorphosis_base_drain_ps>35)
actions.annihilator_melee+=/call_action_list,name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1
actions.annihilator_melee+=/call_action_list,name=reaps,if=talent.eradicate&active_enemies>1&buff.eradicate.up&action.reap.souls_consumed>=1
actions.annihilator_melee+=/void_ray,if=!buff.eradicate.up|!buff.moment_of_craving.up|set_bonus.midnight_season_2_4pc
actions.annihilator_melee+=/collapsing_star,if=active_enemies>1
actions.annihilator_melee+=/call_action_list,name=reaps,if=buff.eradicate.up&active_enemies>1&action.reap.souls_consumed>=4+6*buff.moment_of_craving.up
actions.annihilator_melee+=/call_action_list,name=reaps,if=!talent.eradicate&(active_enemies>1&!buff.metamorphosis.up&buff.moment_of_craving.up&talent.voidfall&(buff.voidfall_building.react<2|variable.ray_after_reap))
actions.annihilator_melee+=/call_action_list,name=reaps,if=!talent.eradicate&(active_enemies>1&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray|buff.voidfall_spending.react>=3))
actions.annihilator_melee+=/call_action_list,name=reaps,if=active_enemies>1&buff.metamorphosis.up&talent.collapsing_star&(active_enemies>1|apex.1|buff.dark_matter.up|talent.star_fragments)&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&variable.wont_overcap_cstar&void_metamorphosis_base_drain_ps>35
actions.annihilator_melee+=/soul_immolation,if=active_dot.soul_immolation=0&(!buff.metamorphosis.up|fury<void_metamorphosis_base_drain_ps)
actions.annihilator_melee+=/devour
actions.annihilator_melee+=/consume

actions.annihilator_ranged=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.6,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1-(active_enemies>1)
actions.annihilator_ranged+=/pick_up_fragment,use_off_gcd=1,if=buff.metamorphosis.up&cooldown.reap.remains&soul_fragments+buff.collapsing_star_stacking.stack>=30&fury<void_metamorphosis_base_drain_ps&buff.collapsing_star_stacking.stack<30
actions.annihilator_ranged+=/metamorphosis
actions.annihilator_ranged+=/devour,if=buff.soulburst.up&active_enemies=1
actions.annihilator_ranged+=/consume,if=buff.soulburst.up
actions.annihilator_ranged+=/void_ray,if=talent.eradicate&active_enemies>1&!buff.eradicate.up
actions.annihilator_ranged+=/collapsing_star,if=active_enemies>1&buff.collapsing_star_stacking.stack>=30
actions.annihilator_ranged+=/call_action_list,name=reaps,if=active_enemies=1&!buff.metamorphosis.up&action.reap.souls_consumed>=4&variable.wont_drop_meta
actions.annihilator_ranged+=/collapsing_star,if=active_enemies=1
actions.annihilator_ranged+=/call_action_list,name=reaps,if=active_enemies=1&action.reap.souls_consumed>=4
actions.annihilator_ranged+=/call_action_list,name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1
actions.annihilator_ranged+=/call_action_list,name=reaps,if=active_enemies>1&buff.eradicate.up&action.reap.souls_consumed>=4+6*buff.moment_of_craving.up
actions.annihilator_ranged+=/void_ray,if=!buff.eradicate.up|!buff.moment_of_craving.up|!set_bonus.midnight_season_2_4pc
actions.annihilator_ranged+=/call_action_list,name=reaps,if=(!buff.eradicate.up|active_enemies=1)&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray|buff.voidfall_spending.react>=3)
actions.annihilator_ranged+=/call_action_list,name=reaps,if=buff.metamorphosis.up&talent.collapsing_star&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&variable.wont_overcap_cstar&void_metamorphosis_base_drain_ps>35&action.reap.souls_consumed>=4&variable.wont_drop_meta
actions.annihilator_ranged+=/soul_immolation,if=active_dot.soul_immolation=0&(!buff.metamorphosis.up|fury<void_metamorphosis_base_drain_ps)
actions.annihilator_ranged+=/devour
actions.annihilator_ranged+=/consume

actions.cooldowns=invoke_external_buff,name=power_infusion,if=buff.metamorphosis.up&!buff.power_infusion.up
actions.cooldowns+=/potion,if=buff.metamorphosis.up|fight_remains<=30
actions.cooldowns+=/use_item,slot=trinket1,if=buff.metamorphosis.up&(variable.void_ray_count=0|hero_tree.annihilator)&(!trinket.2.has_cooldown|trinket.2.cooldown.remains|variable.trinket_priority=1|variable.trinket_2_exclude)&!variable.trinket_1_manual|trinket.1.proc.any_dps.duration>=fight_remains|fight_remains<=trinket.1.buff.any_dps.duration
actions.cooldowns+=/use_item,slot=trinket2,if=buff.metamorphosis.up&(variable.void_ray_count=0|hero_tree.annihilator)&(!trinket.1.has_cooldown|trinket.1.cooldown.remains|variable.trinket_priority=2|variable.trinket_1_exclude)&!variable.trinket_2_manual|trinket.2.proc.any_dps.duration>=fight_remains|fight_remains<=trinket.2.buff.any_dps.duration
actions.cooldowns+=/use_item,use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&!variable.trinket_1_manual&(variable.damage_trinket_priority=1|trinket.2.cooldown.remains|trinket.2.is.spymasters_web|trinket.2.cooldown.duration=0)&gcd.remains>0.1
actions.cooldowns+=/use_item,use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&!variable.trinket_2_manual&(variable.damage_trinket_priority=2|trinket.1.cooldown.remains|trinket.1.is.spymasters_web|trinket.1.cooldown.duration=0)&gcd.remains>0.1
actions.cooldowns+=/use_item,use_off_gcd=1,slot=trinket1,if=trinket.1.is.font_of_venomous_rage&!buff.metamorphosis.up&buff.rolling_torment.up&gcd.remains>0.1
actions.cooldowns+=/use_item,use_off_gcd=1,slot=trinket2,if=trinket.2.is.font_of_venomous_rage&!buff.metamorphosis.up&buff.rolling_torment.up&gcd.remains>0.1
actions.cooldowns+=/use_item,slot=trinket1,if=!variable.trinket_1_buffs&!variable.trinket_1_manual&(variable.damage_trinket_priority=1|trinket.2.cooldown.remains|trinket.2.is.spymasters_web|trinket.2.cooldown.duration=0)&!variable.trinket_1_ogcd_cast
actions.cooldowns+=/use_item,slot=trinket2,if=!variable.trinket_2_buffs&!variable.trinket_2_manual&(variable.damage_trinket_priority=2|trinket.1.cooldown.remains|trinket.1.is.spymasters_web|trinket.1.cooldown.duration=0)&!variable.trinket_2_ogcd_cast

actions.reaps=eradicate
actions.reaps+=/cull
actions.reaps+=/reap

actions.variables=variable,name=wont_overcap_cstar,op=set,value=!buff.metamorphosis.up|((buff.collapsing_star_stacking.stack+action.reap.souls_consumed)<=buff.collapsing_star_stacking.max_stack|!(talent.collapsing_star&(active_enemies>1|apex.1|buff.dark_matter.up|talent.star_fragments)))
actions.variables+=/variable,name=wont_drop_meta,op=set,value=!buff.metamorphosis.up|!buff.moment_of_craving.up|(fury>void_metamorphosis_base_drain_ps+4*action.reap.souls_consumed+10*talent.scythes_embrace&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30|!(talent.collapsing_star&(active_enemies>1|apex.1|buff.dark_matter.up|talent.star_fragments)))
actions.variables+=/variable,name=ray_after_reap,op=set,value=fury+4*action.reap.souls_consumed+10*talent.scythes_embrace>=100
actions.variables+=/variable,name=void_ray_count,op=reset,if=!buff.metamorphosis.up
actions.variables+=/variable,name=void_ray_count,op=add,value=1,if=buff.metamorphosis.up&action.void_ray.last_used>variable.last_ray_mark
actions.variables+=/variable,name=last_ray_mark,op=set,value=action.void_ray.last_used

actions.voidscarred_melee=run_action_list,name=vsm_st,if=active_enemies=1
actions.voidscarred_melee+=/run_action_list,name=vsm_meta,if=buff.metamorphosis.up
actions.voidscarred_melee+=/run_action_list,name=vsm_out

actions.voidscarred_ranged=voidblade,if=buff.void_metamorphosis_stack.at_max_stacks&talent.devourers_bite
actions.voidscarred_ranged+=/metamorphosis,if=buff.eradicate.up|!talent.eradicate|active_enemies=1
actions.voidscarred_ranged+=/devour,if=buff.soulburst.up&active_enemies=1
actions.voidscarred_ranged+=/consume,if=buff.soulburst.up
actions.voidscarred_ranged+=/collapsing_star,if=active_enemies=1&buff.collapsing_star_stacking.stack>=35
actions.voidscarred_ranged+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4
actions.voidscarred_ranged+=/call_action_list,name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1
actions.voidscarred_ranged+=/void_ray,if=!buff.eradicate.up|!buff.moment_of_craving.up|set_bonus.midnight_season_2_4pc
actions.voidscarred_ranged+=/collapsing_star,if=active_enemies>1
actions.voidscarred_ranged+=/vengeful_retreat,if=buff.voidstep.up
actions.voidscarred_ranged+=/reapers_toll,if=buff.voidsurge_reapers_toll.up
actions.voidscarred_ranged+=/pierce_the_veil,if=buff.voidsurge_pierce_the_veil.up
actions.voidscarred_ranged+=/soul_immolation,if=active_dot.soul_immolation=0&(!buff.metamorphosis.up|fury<void_metamorphosis_base_drain_ps)
actions.voidscarred_ranged+=/devour
actions.voidscarred_ranged+=/consume

actions.vsm_meta=soul_immolation,if=variable.void_ray_count>=2&active_dot.soul_immolation=0&fury<=gcd.max*(void_metamorphosis_base_drain_ps-6)-6
actions.vsm_meta+=/pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.35,if=variable.void_ray_count=1&cooldown.void_ray.remains<gcd.max*2&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains
actions.vsm_meta+=/wait,sec=0.05,if=variable.void_ray_count>=2
actions.vsm_meta+=/vengeful_retreat,use_off_gcd=1,if=buff.voidstep.up
actions.vsm_meta+=/void_ray,if=variable.void_ray_count=0&!talent.eradicate
actions.vsm_meta+=/eradicate,if=(buff.moment_of_craving.remains<gcd.max|cooldown.void_ray.remains<gcd.max)&!buff.soulburst.up
actions.vsm_meta+=/void_ray,if=talent.eradicate&!buff.eradicate.up
actions.vsm_meta+=/reapers_toll,if=buff.hungering_slash.remains<gcd.max*2
actions.vsm_meta+=/devour,if=buff.soulburst.up
actions.vsm_meta+=/reapers_toll,if=soul_fragments<=8
actions.vsm_meta+=/pierce_the_veil,if=!buff.hungering_slash.up
actions.vsm_meta+=/predators_wake,if=!buff.hungering_slash.up
actions.vsm_meta+=/eradicate,if=action.reap.souls_consumed>=8&!buff.soulburst.up
actions.vsm_meta+=/cull,if=action.reap.souls_consumed>=4&!buff.soulburst.up
actions.vsm_meta+=/void_ray
actions.vsm_meta+=/soul_immolation,if=active_dot.soul_immolation=0&fury<=gcd.max*(void_metamorphosis_base_drain_ps-6)-6&cooldown.void_ray.remains>gcd.max
actions.vsm_meta+=/devour,if=fury<void_metamorphosis_base_drain_ps*(cooldown.void_ray.remains+3)

actions.vsm_out=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.3,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-3
actions.vsm_out+=/wait,sec=0.05,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1&time-action.pick_up_fragment.last_used<1.5
actions.vsm_out+=/vengeful_retreat,use_off_gcd=1,if=buff.voidstep.up
actions.vsm_out+=/voidblade,if=prev_gcd.1.void_ray
actions.vsm_out+=/metamorphosis,if=buff.eradicate.up|!talent.eradicate|fight_remains<15
actions.vsm_out+=/the_hunt
actions.vsm_out+=/consume,if=buff.soulburst.up&buff.soulburst.remains<gcd.max
actions.vsm_out+=/void_ray,if=talent.eradicate&!buff.eradicate.up
actions.vsm_out+=/hungering_slash
actions.vsm_out+=/soul_immolation,if=active_dot.soul_immolation=0
actions.vsm_out+=/reap,if=action.reap.souls_consumed>=4&!buff.soulburst.up
actions.vsm_out+=/eradicate,if=action.reap.souls_consumed>=4&!buff.soulburst.up
actions.vsm_out+=/void_ray
actions.vsm_out+=/consume

actions.vsm_st=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.75,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1
actions.vsm_st+=/soul_immolation,if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps
actions.vsm_st+=/devour,if=buff.soulburst.up
actions.vsm_st+=/consume,if=buff.soulburst.up
actions.vsm_st+=/voidblade,if=buff.void_metamorphosis_stack.at_max_stacks
actions.vsm_st+=/vengeful_retreat,if=buff.void_metamorphosis_stack.at_max_stacks&cooldown.the_hunt.ready&!buff.metamorphosis.up
actions.vsm_st+=/the_hunt,if=buff.void_metamorphosis_stack.at_max_stacks&buff.vengeful_retreat_movement.up
actions.vsm_st+=/metamorphosis
actions.vsm_st+=/the_hunt,if=!buff.metamorphosis.up&(fight_remains<15|buff.void_metamorphosis_stack.stack<buff.void_metamorphosis_stack.max_stack*0.25)
actions.vsm_st+=/wait,sec=0.05,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1&soul_fragments>=1
actions.vsm_st+=/hungering_slash
actions.vsm_st+=/reapers_toll,if=soul_fragments<=8
actions.vsm_st+=/vengeful_retreat,if=buff.voidstep.up
actions.vsm_st+=/pierce_the_veil
actions.vsm_st+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4
actions.vsm_st+=/predators_wake
actions.vsm_st+=/void_ray,if=!buff.eradicate.up|!buff.moment_of_craving.up|set_bonus.midnight_season_2_4pc
actions.vsm_st+=/soul_immolation,if=active_dot.soul_immolation=0&!buff.metamorphosis.up
actions.vsm_st+=/devour
actions.vsm_st+=/consume
```
