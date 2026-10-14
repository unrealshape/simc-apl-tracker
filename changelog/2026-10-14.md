# APL Changelog – 2026-10-14

Generated: 2026-10-14 08:35 UTC

## Demonhunter

### Devourer
File: `apl/default/demonhunter/devourer.simc`

Changes:
  - `actions.precombat+=/variable,name=trinket_1_manual,value=trinket.1.is.font_of_venomous_rage`
  - `actions.precombat+=/variable,name=trinket_2_manual,value=trinket.2.is.font_of_venomous_rage`
  - `actions.precombat+=/variable,name=trinket_1_ogcd_cast,value=0`
  - `actions.precombat+=/variable,name=trinket_2_ogcd_cast,value=0`
  - `actions.precombat+=/variable,name=trinket_1_exclude,value=0`
  - `actions.precombat+=/variable,name=trinket_2_exclude,value=0`
  - `actions=call_action_list,name=variables`
  + `actions=retarget,target_if=max:target.time_to_die,line_cd=0.25`
  + `actions+=/call_action_list,name=variables`
  - `actions+=/run_action_list,name=annihilator_melee,if=hero_tree.annihilator&talent.the_hunt`
  - `actions+=/run_action_list,name=annihilator_ranged,if=hero_tree.annihilator`
  - `actions+=/run_action_list,name=voidscarred_ranged,if=hero_tree.voidscarred&!talent.the_hunt`
  - `actions+=/run_action_list,name=voidscarred_melee,if=hero_tree.voidscarred&talent.the_hunt`
  + `actions+=/call_action_list,name=reaps,if=target.time_to_die<=4&action.reap.souls_consumed>=1&!buff.soulburst.up`
  + `actions+=/run_action_list,name=annihilator,if=hero_tree.annihilator`
  + `actions+=/run_action_list,name=voidscarred,if=hero_tree.voidscarred`
  - `actions.annihilator_melee=metamorphosis,if=(buff.eradicate.up|!talent.eradicate|active_enemies=1|talent.voidfall)&(active_enemies>1|buff.moment_of_craving.up|cooldown.void_ray.remains>6)`
  - `actions.annihilator_melee+=/devour,if=buff.soulburst.up`
  - `actions.annihilator_melee+=/consume,if=buff.soulburst.up`
  - `actions.annihilator_melee+=/void_ray,if=talent.eradicate&active_enemies>1&!buff.eradicate.up`
  - `actions.annihilator_melee+=/collapsing_star,if=active_enemies=1&(apex.1|buff.dark_matter.up|talent.star_fragments)`
  - `actions.annihilator_melee+=/the_hunt,if=buff.metamorphosis.up`
  - `actions.annihilator_melee+=/hungering_slash,if=!buff.metamorphosis.up&soul_fragments<=8`
  - `actions.annihilator_melee+=/reapers_toll,if=!buff.metamorphosis.up&soul_fragments<=8`
  - `actions.annihilator_melee+=/vengeful_retreat,if=talent.devourers_bite&buff.voidstep.up`
  - `actions.annihilator_melee+=/hungering_slash,if=active_enemies>1`
  - `actions.annihilator_melee+=/reapers_toll,if=talent.devourers_bite&(buff.voidsurge_reapers_toll.up|active_enemies>1)`
  - `actions.annihilator_melee+=/voidblade,if=buff.metamorphosis.up`
  - `actions.annihilator_melee+=/voidblade,if=!buff.metamorphosis.up&(active_enemies=1|!talent.eradicate&active_enemies<4)`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=active_enemies=1&action.reap.souls_consumed>=4`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=!talent.eradicate&(active_enemies>1&variable.wont_overcap_cstar&set_bonus.midnight_season_2_4pc&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray|buff.voidfall_spending.react>=3))`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4&active_enemies<5&(active_enemies>1|!buff.metamorphosis.up|buff.moment_of_craving.up|buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30|void_metamorphosis_base_drain_ps>35)`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=fight_remains<=6&action.reap.souls_consumed>=1`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=talent.eradicate&active_enemies>1&buff.eradicate.up&action.reap.souls_consumed>=1`
  - `actions.annihilator_melee+=/void_ray,if=!buff.eradicate.up|!buff.moment_of_craving.up|set_bonus.midnight_season_2_4pc`
  - `actions.annihilator_melee+=/collapsing_star,if=active_enemies>1`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=buff.eradicate.up&active_enemies>1&action.reap.souls_consumed>=4+6*buff.moment_of_craving.up`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=!talent.eradicate&(active_enemies>1&!buff.metamorphosis.up&buff.moment_of_craving.up&talent.voidfall&(buff.voidfall_building.react<2|variable.ray_after_reap))`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=!talent.eradicate&(active_enemies>1&(buff.voidfall_spending.stack>=3&prev_gcd.1.void_ray|buff.voidfall_spending.react>=3))`
  - `actions.annihilator_melee+=/call_action_list,name=reaps,if=active_enemies>1&buff.metamorphosis.up&talent.collapsing_star&(active_enemies>1|apex.1|buff.dark_matter.up|talent.star_fragments)&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30&variable.wont_overcap_cstar&void_metamorphosis_base_drain_ps>35`
  - `actions.annihilator_melee+=/soul_immolation,if=active_dot.soul_immolation=0&(!buff.metamorphosis.up|fury<void_metamorphosis_base_drain_ps)`
  - `actions.annihilator_melee+=/devour`
  - `actions.annihilator_melee+=/consume`
  + `actions.annihilator=run_action_list,name=annihilator_meta,if=buff.metamorphosis.up`
  + `actions.annihilator+=/run_action_list,name=annihilator_out`
  - `actions.annihilator_ranged=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.6,if=!buff.metamorphosis.up&!buff.void_metamorphosis_stack.at_max_stacks&buff.void_metamorphosis_stack.stack>=buff.void_metamorphosis_stack.max_stack-1-(active_enemies>1)`
  - `actions.annihilator_ranged+=/pick_up_fragment,use_off_gcd=1,if=buff.metamorphosis.up&cooldown.reap.remains&soul_fragments+buff.collapsing_star_stacking.stack>=30&fury<void_metamorphosis_base_drain_ps&buff.collapsing_star_stacking.stack<30`
  - `actions.annihilator_ranged+=/metamorphosis`
  - `actions.annihilator_ranged+=/devour,if=buff.soulburst.up&active_enemies=1`
  - `actions.annihilator_ranged+=/consume,if=buff.soulburst.up`
  ... and 168 more changes

### Havoc
File: `apl/default/demonhunter/havoc.simc`

Changes:
  + `actions+=/abyssal_gaze,if=!action.death_sweep.demonsurge_available&!action.annihilation.demonsurge_available`


## Hunter

### Marksmanship
File: `apl/default/hunter/marksmanship.simc`

Changes:
  - `actions+=/variable,name=trueshot_ready,op=setif,condition=fight_style.dungeonroute,value_else=variable.trueshot_ready,value=raid_event.pull.remains>30|raid_event.pull.in>60|talent.calling_the_shots`
  + `actions+=/variable,name=trueshot_ready,op=setif,condition=fight_style.dungeonroute,value_else=variable.trueshot_ready,value=raid_event.pull.remains>20|raid_event.pull.in>45|talent.calling_the_shots`
  - `actions.cds+=/potion,name=liquid_luster_2,if=potion.potion_of_recklessness&buff.bullseye.up&cooldown.trueshot.remains<10&(fight_style.dungeonroute|cooldown.explosive_shot.remains>=25|cooldown.explosive_shot.remains<10)|fight_remains<31`
  + `actions.cds+=/potion,name=liquid_luster_2,if=potion.potion_of_recklessness&buff.bullseye.up&cooldown.trueshot.remains<7&(fight_style.dungeonroute|cooldown.explosive_shot.remains>=25|cooldown.explosive_shot.remains<10)|fight_remains<31`
  - `actions.draoe=explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&(!max_prio_damage|!fight_style.dungeonroute)&(!talent.tactical_reload|!buff.lock_and_load.up)`
  - `actions.draoe+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|buff.unstable_trigger.up|!fight_style.dungeonroute)`
  + `actions.draoe=explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&!fight_style.dungeonroute&(!talent.tactical_reload|!buff.lock_and_load.up)`
  + `actions.draoe+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|!fight_style.dungeonroute)`
  - `actions.draoe+=/aimed_shot,target_if=max:debuff.spotters_mark.up|max_prio_damage,if=buff.trick_shots.remains>cast_time&full_recharge_time<gcd+cast_time`
  - `actions.draoe+=/black_arrow,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up`
  - `actions.draoe+=/multishot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.trick_shots.down`
  + `actions.draoe+=/aimed_shot,if=buff.trick_shots.remains>cast_time&full_recharge_time<gcd+cast_time`
  + `actions.draoe+=/black_arrow,if=buff.precise_shots.up`
  + `actions.draoe+=/multishot,if=buff.trick_shots.down`
  - `actions.draoe+=/multishot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up`
  - `actions.draoe+=/aimed_shot,target_if=max:debuff.spotters_mark.up|max_prio_damage,if=buff.trick_shots.remains>cast_time`
  + `actions.draoe+=/multishot,if=buff.precise_shots.up`
  + `actions.draoe+=/aimed_shot,if=buff.trick_shots.remains>cast_time`
  - `actions.draoe+=/multishot,if=focus>cost+action.aimed_shot.cost&!max_prio_damage`
  + `actions.draoe+=/multishot,if=focus>cost+action.aimed_shot.cost`
  - `actions.drst=black_arrow,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up`
  - `actions.drst+=/explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&active_enemies>1&(!max_prio_damage|!fight_style.dungeonroute)&(!talent.tactical_reload|!buff.lock_and_load.up)`
  - `actions.drst+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|buff.unstable_trigger.up|!fight_style.dungeonroute)`
  + `actions.drst=black_arrow,if=buff.precise_shots.up`
  + `actions.drst+=/explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&active_enemies>1&!fight_style.dungeonroute&(!talent.tactical_reload|!buff.lock_and_load.up)`
  + `actions.drst+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|!fight_style.dungeonroute)`
  - `actions.drst+=/arcane_shot,target_if=max:debuff.spotters_mark.down|action.aimed_shot.in_flight_to_target|max_prio_damage,if=buff.precise_shots.up`
  - `actions.drst+=/aimed_shot,target_if=max:debuff.spotters_mark.up|max_prio_damage`
  + `actions.drst+=/arcane_shot,if=buff.precise_shots.up`
  + `actions.drst+=/aimed_shot`
  - `actions.sentaoe=explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&(!max_prio_damage|!fight_style.dungeonroute)&(!talent.tactical_reload|!buff.lock_and_load.up)`
  - `actions.sentaoe+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|buff.unstable_trigger.up|!fight_style.dungeonroute)`
  + `actions.sentaoe=explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&!fight_style.dungeonroute&(!talent.tactical_reload|!buff.lock_and_load.up)`
  + `actions.sentaoe+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|!fight_style.dungeonroute)`
  - `actions.sentaoe+=/rapid_fire,target_if=max:debuff.sentinels_mark.down,if=talent.unload,interrupt_if=talent.unload&ticks_remain<2&buff.precise_shots.up&!gcd.remains,interrupt_immediate=1,interrupt_global=1`
  - `actions.sentaoe+=/rapid_fire,interrupt_if=talent.unload&ticks_remain<2&buff.precise_shots.up&!gcd.remains,interrupt_immediate=1,interrupt_global=1`
  + `actions.sentaoe+=/rapid_fire`
  - `actions.sentaoe+=/multishot,if=focus>cost+action.aimed_shot.cost&!max_prio_damage`
  + `actions.sentaoe+=/multishot,if=focus>cost+action.aimed_shot.cost`
  - `actions.sentst=explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&active_enemies>1&(!max_prio_damage|!fight_style.dungeonroute)&(!talent.tactical_reload|!buff.lock_and_load.up)`
  - `actions.sentst+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|buff.unstable_trigger.up|!fight_style.dungeonroute)`
  + `actions.sentst=explosive_shot,target_if=min:dot.explosive_shot.remains,if=set_bonus.mid2_4pc&active_enemies>1&!fight_style.dungeonroute&(!talent.tactical_reload|!buff.lock_and_load.up)`
  + `actions.sentst+=/explosive_shot,if=(!talent.tactical_reload|!buff.lock_and_load.up)&(!cooldown.rapid_fire.ready|!fight_style.dungeonroute)`
  - `actions.sentst+=/rapid_fire,target_if=max:debuff.sentinels_mark.down,if=!fight_style.dungeonroute`
  - `actions.sentst+=/rapid_fire`
  - `actions.sentst+=/kill_shot,target_if=max:debuff.sentinels_mark.down|max_prio_damage,if=buff.precise_shots.up`
  + `actions.sentst+=/aimed_shot,if=buff.trueshot.up&buff.precise_shots.down&active_enemies=1`
  + `actions.sentst+=/rapid_fire,if=buff.precise_shots.down|buff.trueshot.up|active_enemies>1&talent.aspect_of_the_hydra|!talent.no_scope`
  + `actions.sentst+=/kill_shot,if=buff.precise_shots.up`
  - `actions.sentst+=/multishot,target_if=max:debuff.sentinels_mark.down,if=buff.precise_shots.up&active_enemies>1&talent.aspect_of_the_hydra&(!fight_style.dungeonroute|!max_prio_damage|active_enemies>2)`
  ... and 3 more changes

