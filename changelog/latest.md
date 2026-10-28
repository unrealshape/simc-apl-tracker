# APL Changelog – 2026-10-28

Generated: 2026-10-28 09:30 UTC

## Demonhunter

### Devourer
File: `apl/default/demonhunter/devourer.simc`

Changes:
  + `actions.annihilator_meta+=/collapsing_star,if=prev_gcd.1.void_ray`
  + `actions.annihilator_meta+=/eradicate,if=buff.voidfall_spending.up`
  - `actions.annihilator_meta+=/call_action_list,name=reaps,if=(active_enemies=1|buff.eradicate.up)&action.reap.souls_consumed>=4`
  + `actions.annihilator_meta+=/devour,if=buff.eradicate.up&!buff.voidfall_spending.up&buff.moment_of_craving.remains>=4&fury.deficit<=70`
  + `actions.annihilator_meta+=/call_action_list,name=reaps,if=(active_enemies=1|buff.eradicate.up)&action.reap.souls_consumed>=4&!(talent.devourers_bite&active_enemies=1&fury<void_metamorphosis_base_drain_ps*2)`
  - `actions.annihilator_meta+=/soul_immolation,if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps&(cooldown.reap.remains|active_enemies=1)`
  + `actions.annihilator_meta+=/cull,if=talent.eradicate&buff.voidfall_spending.up`
  + `actions.annihilator_meta+=/soul_immolation,if=active_dot.soul_immolation=0&fury<void_metamorphosis_base_drain_ps&fury<40&(cooldown.reap.remains|active_enemies=1)`
  + `actions.annihilator_out+=/void_ray,if=talent.eradicate&active_enemies>1&buff.void_metamorphosis_stack.at_max_stacks&fury>=100`
  - `actions.voidscarred_meta=pick_up_fragment,mode=nearest,type=all,use_off_gcd=1,line_cd=0.35,if=cooldown.void_ray.remains<gcd.max*2&fury<void_metamorphosis_base_drain_ps*cooldown.void_ray.remains`
  - `actions.voidscarred_meta+=/vengeful_retreat,use_off_gcd=1,if=buff.voidstep.up`
  + `actions.voidscarred_meta=vengeful_retreat,use_off_gcd=1,if=buff.voidstep.up`
  - `actions.voidscarred_meta+=/void_ray,if=talent.eradicate&!buff.eradicate.up&(active_enemies>1|fury<30)`
  + `actions.voidscarred_meta+=/void_ray,if=talent.eradicate&!buff.eradicate.up&active_enemies>1`
  - `actions.voidscarred_meta+=/reapers_toll,if=soul_fragments<=8`
  + `actions.voidscarred_meta+=/pierce_the_veil,if=active_enemies>3&time-buff.metamorphosis.last_trigger<15&buff.eradicate.up`
  + `actions.voidscarred_meta+=/soul_immolation,if=active_enemies>3&!active_dot.soul_immolation&buff.collapsing_star_stacking.stack<15`
  + `actions.voidscarred_meta+=/soul_immolation,if=active_enemies=1&!active_dot.soul_immolation&fury>=void_metamorphosis_base_drain_ps*2&buff.impending_apocalypse.stack>=2`
  + `actions.voidscarred_meta+=/reapers_toll,if=soul_fragments<=8|active_enemies=1&buff.impending_apocalypse.stack>=3`
  + `actions.voidscarred_meta+=/eradicate,if=active_enemies>3&buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30`
  - `actions.voidscarred_meta+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4+4*(active_enemies>1&buff.eradicate.up)&!buff.soulburst.up`
  + `actions.voidscarred_meta+=/call_action_list,name=reaps,if=action.reap.souls_consumed>=4+4*(active_enemies>1&buff.eradicate.up)&!buff.soulburst.up&(active_enemies>1|buff.impending_apocalypse.stack<3|buff.collapsing_star_stacking.stack+action.reap.souls_consumed>=30|cooldown.void_ray.remains<action.void_ray.execute_time)`
  - `actions.voidscarred_out+=/voidblade,if=prev_gcd.1.void_ray&(active_enemies>1|!talent.the_hunt|!cooldown.the_hunt.ready)`
  + `actions.voidscarred_out+=/voidblade,if=active_enemies>1|!talent.the_hunt|!cooldown.the_hunt.ready`
  + `actions.voidscarred_out+=/the_hunt,if=talent.eradicate&active_enemies>3&cooldown.voidblade.remains`


## Hunter

### Beast Mastery
File: `apl/default/hunter/beast_mastery.simc`

Changes:
  - `actions.st+=/kill_command,if=howl_summon.ready|(cooldown.bestial_wrath.remains>full_recharge_time+gcd&buff.natures_ally.react|!apex.3)&(buff.howl_of_the_pack_leader_cooldown.remains>4|cooldown.kill_command.charges_fractional>1.8)`
  + `actions.st+=/barbed_shot,if=howl_summon.ready&!buff.natures_ally.react&cooldown.barbed_shot.charges_fractional>1.5`
  + `actions.st+=/kill_command,if=howl_summon.ready|(cooldown.bestial_wrath.remains>full_recharge_time&buff.natures_ally.react|!apex.3)&(buff.howl_of_the_pack_leader_cooldown.remains>4|cooldown.kill_command.charges_fractional>1.8)`
  - `actions.trinkets=use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(cooldown.bestial_wrath.ready|cooldown.bestial_wrath.remains<this_trinket.proc.any_dps.duration-15)|fight_remains<21`
  - `actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&!potion.liquid_luster|!equipped.font_of_venomous_rage|((buff.liquid_luster.up&buff.liquid_luster.remains<6)|(fight_remains<cooldown.potion.remains&!buff.liquid_luster.up))|fight_remains<10`
  + `actions.trinkets=use_item,name=voracious_heart_of_ulatek,if=cooldown.bestial_wrath.remains<6`
  + `actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(cooldown.bestial_wrath.ready|cooldown.bestial_wrath.remains<this_trinket.proc.any_dps.duration-15)|fight_remains<21`
  + `actions.trinkets+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&(!potion.liquid_luster|!equipped.font_of_venomous_rage|((buff.liquid_luster.up&buff.liquid_luster.remains<6)|(fight_remains<cooldown.potion.remains&!buff.liquid_luster.up)))|fight_remains<10`

### Survival
File: `apl/default/hunter/survival.simc`

Changes:
  - `actions.cds+=/use_item,name=voracious_heart_of_ulatek`
  + `actions.cds+=/use_item,name=voracious_heart_of_ulatek,if=buff.tip_of_the_spear.up`
  - `actions.sentcleave+=/wildfire_bomb,target_if=max:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up`
  + `actions.sentcleave+=/kill_command,if=buff.tip_of_the_spear.stack=1&cooldown.takedown.remains&focus<100`
  + `actions.sentcleave+=/wildfire_bomb,if=buff.tip_of_the_spear.up`
  - `actions.sentst=kill_command,if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains|!talent.twin_fangs)`
  - `actions.sentst+=/boomstick`
  + `actions.sentst=kill_command,if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains|!talent.twin_fangs|time<10&cooldown.boomstick.ready&focus<110)`
  + `actions.sentst+=/boomstick,if=buff.tip_of_the_spear.up`
  - `actions.sentst+=/takedown,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs`
  + `actions.sentst+=/takedown,if=(buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs)&!(time<10&cooldown.boomstick.ready)`

