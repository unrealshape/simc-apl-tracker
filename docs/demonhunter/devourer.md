# Demon Hunter – Devourer

Auto-generated from SimulationCraft APL | Last updated: 2026-10-15 08:09 UTC

Source: `apl/default/demonhunter/devourer.simc`

---

## Overview

- **Action Lists:** 12
- **Total Actions:** 93
- **Lists:** `precombat`, `default`, `annihilator`, `annihilator_meta`, `annihilator_out`, `cooldowns`, `reaps`, `variables`, `voidscarred`, `voidscarred_hunt_entry`, `voidscarred_meta`, `voidscarred_out`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `variable` | name=trinket_1_buffs,value=trinket.1.has_buff.intellect\|trinket.1.has_buff.mastery\|trinket.1.has_buff.versatility\|trinket.1.has_buff.haste\|trinket.1.has_buff.crit |
| 3 | `variable` | name=trinket_2_buffs,value=trinket.2.has_buff.intellect\|trinket.2.has_buff.mastery\|trinket.2.has_buff.versatility\|trinket.2.has_buff.haste\|trinket.2.has_buff.crit |
| 4 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs\|variable.trinket_2_buffs&((trinket.2.proc.any_dps.duration)*trinket.2.proc.any_dps.default_value)>((trinket.1.proc.any_dps.duration)*trinket.1.proc.any_dps.default_value) |
| 5 | `variable` | name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl |
| 6 | `arcane_torrent` | — |
| 7 | `soul_immolation` | — |
| 8 | `consume` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `retarget` | target_if=max:target.time_to_die,line_cd=0.25 |
| 2 | `call_action_list` | name=variables |
| 3 | `call_action_list` | name=cooldowns |
| 4 | `call_action_list` | name=reaps,if=target.time_to_die<=4&action.reap.souls_consumed>=1&!buff.soulburst.up |
| 5 | `run_action_list` | name=annihilator,if=hero_tree.annihilator |
| 6 | `run_action_list` | name=voidscarred,if=hero_tree.voidscarred |

## Action List: `annihilator`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `run_action_list` | name=annihilator_meta,if=buff.metamorphosis.up |
| 2 | `run_action_list` | name=annihilator_out |

## Action List: `annihilator_meta`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | use_off_gcd=1,if=cooldown.reap.remains&(talent.eradicate&target.time_to_die<15\|soul_fragments+buff.collapsing_star_stacking.stack>=30&buff.collapsing_star_stacking.stack<30) |
| 2 | `devour` | if=buff.soulburst.up&active_enemies=1 |
| 3 | `the_hunt` | if=talent.devourers_bite |
| 4 | `voidblade` | if=talent.devourers_bite&active_enemies<=3 |
| 5 | `collapsing_star` | if=fight_remains<10 |
| 6 | `void_ray` | if=talent.eradicate&active_enemies>1&!buff.eradicate.up |
| 7 | `collapsing_star` | if=active_enemies>1\|cooldown.void_ray.remains |
| 8 | `call_action_list` | name=reaps,if=(active_enemies=1\|buff.eradicate.up)&action.reap.souls_consumed>=4 |
| 9 | `call_action_list` | name=reaps,if=!talent.eradicate&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&action.reap.souls_consumed>=4 |
| 10 | `void_ray` | if=active_enemies>1\|talent.eradicate\|fury>=100\|fury<55 |
| 11 | `call_action_list` | name=reaps,if=variable.voidfall_dump |
| 12 | `call_action_list` | name=reaps,if=buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&action.reap.souls_consumed>=4&fight_remains<45 |
| 13 | `soul_immolation` | if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps&(cooldown.reap.remains\|active_enemies=1) |
| 14 | `devour` | — |

## Action List: `annihilator_out`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.6,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-2 |
| 2 | `voidblade` | if=talent.devourers_bite&active_enemies<=3&buff.void_metamorphosis_stack.at_max_stacks |
| 3 | `metamorphosis` | — |
| 4 | `consume` | if=buff.soulburst.up |
| 5 | `call_action_list` | name=reaps,if=(active_enemies=1\|buff.eradicate.up)&action.reap.souls_consumed>=4 |
| 6 | `call_action_list` | name=reaps,if=!talent.eradicate&action.reap.souls_consumed>=8 |
| 7 | `void_ray` | — |
| 8 | `call_action_list` | name=reaps,if=variable.voidfall_dump |
| 9 | `soul_immolation` | if=active_dot.soul_immolation=0&(active_enemies>1\|talent.eradicate) |
| 10 | `consume` | — |

## Action List: `cooldowns`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_external_buff` | name=power_infusion,if=buff.metamorphosis.up&!buff.power_infusion.up |
| 2 | `potion` | if=buff.metamorphosis.up\|fight_remains<=30 |
| 3 | `use_item` | slot=trinket1,if=buff.metamorphosis.up&(variable.no_ray_this_window\|hero_tree.annihilator)&(!trinket.2.has_cooldown\|trinket.2.cooldown.remains\|variable.trinket_priority=1)\|trinket.1.proc.any_dps.duration>=fight_remains\|fight_remains<=trinket.1.buff.any_dps.duration |
| 4 | `use_item` | slot=trinket2,if=buff.metamorphosis.up&(variable.no_ray_this_window\|hero_tree.annihilator)&(!trinket.1.has_cooldown\|trinket.1.cooldown.remains\|variable.trinket_priority=2)\|trinket.2.proc.any_dps.duration>=fight_remains\|fight_remains<=trinket.2.buff.any_dps.duration |
| 5 | `use_item` | use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1\|trinket.2.cooldown.remains\|trinket.2.cooldown.duration=0)&gcd.remains>0.1 |
| 6 | `use_item` | use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2\|trinket.1.cooldown.remains\|trinket.1.cooldown.duration=0)&gcd.remains>0.1 |
| 7 | `use_item` | slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1\|trinket.2.cooldown.remains\|trinket.2.cooldown.duration=0) |
| 8 | `use_item` | slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2\|trinket.1.cooldown.remains\|trinket.1.cooldown.duration=0) |

## Action List: `reaps`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `eradicate` | — |
| 2 | `cull` | — |
| 3 | `reap` | — |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=voidfall_dump,op=set,value=!buff.eradicate.up&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray\|buff.voidfall_spending.react>=3) |
| 2 | `variable` | name=no_ray_this_window,op=set,value=action.void_ray.last_used<buff.metamorphosis.last_trigger |

## Action List: `voidscarred`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `run_action_list` | name=voidscarred_meta,if=buff.metamorphosis.up |
| 2 | `run_action_list` | name=voidscarred_out |

## Action List: `voidscarred_hunt_entry`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `voidblade` | if=cooldown.the_hunt.ready |
| 2 | `vengeful_retreat` | if=cooldown.the_hunt.ready |
| 3 | `the_hunt` | if=buff.vengeful_retreat_movement.up |

## Action List: `voidscarred_meta`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.35,if=cooldown.void_ray.remains<gcd.max*2&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains |
| 2 | `vengeful_retreat` | use_off_gcd=1,if=buff.voidstep.up |
| 3 | `void_ray` | if=variable.no_ray_this_window&(!talent.eradicate\|active_enemies=1) |
| 4 | `eradicate` | if=cooldown.void_ray.remains<gcd.max&!buff.soulburst.up |
| 5 | `void_ray` | if=talent.eradicate&!buff.eradicate.up&(active_enemies>1\|fury<30) |
| 6 | `reapers_toll` | if=active_enemies>1&buff.hungering_slash.remains<gcd.max*2 |
| 7 | `predators_wake` | if=buff.collapsing_star.up |
| 8 | `reapers_toll` | if=talent.voidrush&buff.collapsing_star.up&cooldown.voidblade.remains<gcd.max |
| 9 | `pierce_the_veil` | if=talent.voidrush&buff.collapsing_star.up |
| 10 | `collapsing_star` | — |
| 11 | `devour` | if=buff.soulburst.up |
| 12 | `reapers_toll` | if=active_enemies>3&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains |
| 13 | `reapers_toll` | if=soul_fragments<=8 |
| 14 | `pierce_the_veil` | if=active_enemies<4 |
| 15 | `predators_wake` | if=!buff.hungering_slash.up |
| 16 | `pierce_the_veil` | — |
| 17 | `call_action_list` | name=reaps,if=action.reap.souls_consumed>=4+4*(active_enemies>1&buff.eradicate.up)&!buff.soulburst.up |
| 18 | `void_ray` | — |
| 19 | `soul_immolation` | if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps |
| 20 | `devour` | — |

## Action List: `voidscarred_out`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `pick_up_fragment` | mode=nearest,type=all,use_off_gcd=1,line_cd=0.3,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-3 |
| 2 | `wait` | sec=0.05,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1&(active_enemies=1&soul_fragments>=1\|active_enemies>1&time-action.pick_up_fragment.last_used<1.5) |
| 3 | `vengeful_retreat` | use_off_gcd=1,if=buff.voidstep.up |
| 4 | `consume` | if=buff.soulburst.up&(active_enemies=1\|talent.eradicate\|buff.soulburst.remains<gcd.max) |
| 5 | `call_action_list` | name=voidscarred_hunt_entry,if=talent.the_hunt&active_enemies=1&buff.void_metamorphosis_stack.at_max_stacks |
| 6 | `voidblade` | if=prev_gcd.1.void_ray&(active_enemies>1\|!talent.the_hunt\|!cooldown.the_hunt.ready) |
| 7 | `metamorphosis` | if=buff.eradicate.up\|!talent.eradicate\|active_enemies=1\|fight_remains<15 |
| 8 | `void_ray` | if=talent.eradicate&active_enemies>1&!buff.eradicate.up |
| 9 | `call_action_list` | name=reaps,if=fury<100&fury+4*action.reap.souls_consumed+10*talent.scythes_embrace>=100&action.reap.souls_consumed>=1&!buff.soulburst.up |
| 10 | `hungering_slash` | — |
| 11 | `soul_immolation` | if=active_enemies>1&active_dot.soul_immolation=0 |
| 12 | `call_action_list` | name=reaps,if=action.reap.souls_consumed>=4+4*(active_enemies>1&buff.eradicate.up)&!buff.soulburst.up |
| 13 | `void_ray` | — |
| 14 | `soul_immolation` | if=active_enemies=1&active_dot.soul_immolation=0 |
| 15 | `consume` | — |

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
actions.precombat+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs|variable.trinket_2_buffs&((trinket.2.proc.any_dps.duration)*trinket.2.proc.any_dps.default_value)>((trinket.1.proc.any_dps.duration)*trinket.1.proc.any_dps.default_value)
actions.precombat+=/variable,name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl
actions.precombat+=/arcane_torrent
actions.precombat+=/soul_immolation
actions.precombat+=/consume

# Executed every time the actor is available.
actions=retarget,target_if=max:target.time_to_die,line_cd=0.25
actions+=/call_action_list,name=variables
actions+=/call_action_list,name=cooldowns
actions+=/call_action_list,name=reaps,if=target.time_to_die<=4&action.reap.souls_consumed>=1&!buff.soulburst.up
actions+=/run_action_list,name=annihilator,if=hero_tree.annihilator
actions+=/run_action_list,name=voidscarred,if=hero_tree.voidscarred

actions.annihilator=run_action_list,name=annihilator_meta,if=buff.metamorphosis.up
actions.annihilator+=/run_action_list,name=annihilator_out

actions.annihilator_meta=pick_up_fragment,use_off_gcd=1,if=cooldown.reap.remains&(talent.eradicate&target.time_to_die<15|soul_fragments+buff.collapsing_star_stacking.stack>=30&buff.collapsing_star_stacking.stack<30)
actions.annihilator_meta+=/devour,if=buff.soulburst.up&active_enemies=1
actions.annihilator_meta+=/the_hunt,if=talent.devourers_bite
actions.annihilator_meta+=/voidblade,if=talent.devourers_bite&active_enemies<=3
actions.annihilator_meta+=/collapsing_star,if=fight_remains<10
actions.annihilator_meta+=/void_ray,if=talent.eradicate&active_enemies>1&!buff.eradicate.up
actions.annihilator_meta+=/collapsing_star,if=active_enemies>1|cooldown.void_ray.remains
actions.annihilator_meta+=/call_action_list,name=reaps,if=(active_enemies=1|buff.eradicate.up)&action.reap.souls_consumed>=4
actions.annihilator_meta+=/call_action_list,name=reaps,if=!talent.eradicate&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&action.reap.souls_consumed>=4
actions.annihilator_meta+=/void_ray,if=active_enemies>1|talent.eradicate|fury>=100|fury<55
actions.annihilator_meta+=/call_action_list,name=reaps,if=variable.voidfall_dump
actions.annihilator_meta+=/call_action_list,name=reaps,if=buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&action.reap.souls_consumed>=4&fight_remains<45
actions.annihilator_meta+=/soul_immolation,if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps&(cooldown.reap.remains|active_enemies=1)
actions.annihilator_meta+=/devour

actions.annihilator_out=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.6,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-2
actions.annihilator_out+=/voidblade,if=talent.devourers_bite&active_enemies<=3&buff.void_metamorphosis_stack.at_max_stacks
actions.annihilator_out+=/metamorphosis
actions.annihilator_out+=/consume,if=buff.soulburst.up
actions.annihilator_out+=/call_action_list,name=reaps,if=(active_enemies=1|buff.eradicate.up)&action.reap.souls_consumed>=4
actions.annihilator_out+=/call_action_list,name=reaps,if=!talent.eradicate&action.reap.souls_consumed>=8
actions.annihilator_out+=/void_ray
actions.annihilator_out+=/call_action_list,name=reaps,if=variable.voidfall_dump
actions.annihilator_out+=/soul_immolation,if=active_dot.soul_immolation=0&(active_enemies>1|talent.eradicate)
actions.annihilator_out+=/consume

actions.cooldowns=invoke_external_buff,name=power_infusion,if=buff.metamorphosis.up&!buff.power_infusion.up
actions.cooldowns+=/potion,if=buff.metamorphosis.up|fight_remains<=30
actions.cooldowns+=/use_item,slot=trinket1,if=buff.metamorphosis.up&(variable.no_ray_this_window|hero_tree.annihilator)&(!trinket.2.has_cooldown|trinket.2.cooldown.remains|variable.trinket_priority=1)|trinket.1.proc.any_dps.duration>=fight_remains|fight_remains<=trinket.1.buff.any_dps.duration
actions.cooldowns+=/use_item,slot=trinket2,if=buff.metamorphosis.up&(variable.no_ray_this_window|hero_tree.annihilator)&(!trinket.1.has_cooldown|trinket.1.cooldown.remains|variable.trinket_priority=2)|trinket.2.proc.any_dps.duration>=fight_remains|fight_remains<=trinket.2.buff.any_dps.duration
actions.cooldowns+=/use_item,use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1|trinket.2.cooldown.remains|trinket.2.cooldown.duration=0)&gcd.remains>0.1
actions.cooldowns+=/use_item,use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2|trinket.1.cooldown.remains|trinket.1.cooldown.duration=0)&gcd.remains>0.1
actions.cooldowns+=/use_item,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1|trinket.2.cooldown.remains|trinket.2.cooldown.duration=0)
actions.cooldowns+=/use_item,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2|trinket.1.cooldown.remains|trinket.1.cooldown.duration=0)

actions.reaps=eradicate
actions.reaps+=/cull
actions.reaps+=/reap

actions.variables=variable,name=voidfall_dump,op=set,value=!buff.eradicate.up&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray|buff.voidfall_spending.react>=3)
actions.variables+=/variable,name=no_ray_this_window,op=set,value=action.void_ray.last_used<buff.metamorphosis.last_trigger

actions.voidscarred=run_action_list,name=voidscarred_meta,if=buff.metamorphosis.up
actions.voidscarred+=/run_action_list,name=voidscarred_out

actions.voidscarred_hunt_entry=voidblade,if=cooldown.the_hunt.ready
actions.voidscarred_hunt_entry+=/vengeful_retreat,if=cooldown.the_hunt.ready
actions.voidscarred_hunt_entry+=/the_hunt,if=buff.vengeful_retreat_movement.up

actions.voidscarred_meta=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.35,if=cooldown.void_ray.remains<gcd.max*2&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains
actions.voidscarred_meta+=/vengeful_retreat,use_off_gcd=1,if=buff.voidstep.up
actions.voidscarred_meta+=/void_ray,if=variable.no_ray_this_window&(!talent.eradicate|active_enemies=1)
actions.voidscarred_meta+=/eradicate,if=cooldown.void_ray.remains<gcd.max&!buff.soulburst.up
actions.voidscarred_meta+=/void_ray,if=talent.eradicate&!buff.eradicate.up&(active_enemies>1|fury<30)
actions.voidscarred_meta+=/reapers_toll,if=active_enemies>1&buff.hungering_slash.remains<gcd.max*2
actions.voidscarred_meta+=/predators_wake,if=buff.collapsing_star.up
actions.voidscarred_meta+=/reapers_toll,if=talent.voidrush&buff.collapsing_star.up&cooldown.voidblade.remains<gcd.max
actions.voidscarred_meta+=/pierce_the_veil,if=talent.voidrush&buff.collapsing_star.up
actions.voidscarred_meta+=/collapsing_star
actions.voidscarred_meta+=/devour,if=buff.soulburst.up
actions.voidscarred_meta+=/reapers_toll,if=active_enemies>3&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains
actions.voidscarred_meta+=/reapers_toll,if=soul_fragments<=8
actions.voidscarred_meta+=/pierce_the_veil,if=active_enemies<4
actions.voidscarred_meta+=/predators_wake,if=!buff.hungering_slash.up
actions.voidscarred_meta+=/pierce_the_veil
actions.voidscarred_meta+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4+4*(active_enemies>1&buff.eradicate.up)&!buff.soulburst.up
actions.voidscarred_meta+=/void_ray
actions.voidscarred_meta+=/soul_immolation,if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps
actions.voidscarred_meta+=/devour

actions.voidscarred_out=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.3,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-3
actions.voidscarred_out+=/wait,sec=0.05,if=!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1&(active_enemies=1&soul_fragments>=1|active_enemies>1&time-action.pick_up_fragment.last_used<1.5)
actions.voidscarred_out+=/vengeful_retreat,use_off_gcd=1,if=buff.voidstep.up
actions.voidscarred_out+=/consume,if=buff.soulburst.up&(active_enemies=1|talent.eradicate|buff.soulburst.remains<gcd.max)
actions.voidscarred_out+=/call_action_list,name=voidscarred_hunt_entry,if=talent.the_hunt&active_enemies=1&buff.void_metamorphosis_stack.at_max_stacks
actions.voidscarred_out+=/voidblade,if=prev_gcd.1.void_ray&(active_enemies>1|!talent.the_hunt|!cooldown.the_hunt.ready)
actions.voidscarred_out+=/metamorphosis,if=buff.eradicate.up|!talent.eradicate|active_enemies=1|fight_remains<15
actions.voidscarred_out+=/void_ray,if=talent.eradicate&active_enemies>1&!buff.eradicate.up
actions.voidscarred_out+=/call_action_list,name=reaps,if=fury<100&fury+4*action.reap.souls_consumed+10*talent.scythes_embrace>=100&action.reap.souls_consumed>=1&!buff.soulburst.up
actions.voidscarred_out+=/hungering_slash
actions.voidscarred_out+=/soul_immolation,if=active_enemies>1&active_dot.soul_immolation=0
actions.voidscarred_out+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4+4*(active_enemies>1&buff.eradicate.up)&!buff.soulburst.up
actions.voidscarred_out+=/void_ray
actions.voidscarred_out+=/soul_immolation,if=active_enemies=1&active_dot.soul_immolation=0
actions.voidscarred_out+=/consume
```
