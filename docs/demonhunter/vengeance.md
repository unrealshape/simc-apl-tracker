# Demon Hunter – Vengeance

Auto-generated from SimulationCraft APL | Last updated: 2026-04-17 05:32 UTC

Source: `apl/default/demonhunter/vengeance.simc`

---

## Overview

- **Action Lists:** 16
- **Total Actions:** 203
- **Lists:** `precombat`, `default`, `anni`, `anni_cooldowns`, `anni_filler_no_spend`, `anni_generate_fury`, `anni_meta_entry`, `anni_pre_meta_spb`, `anni_voidfall_fishing`, `anni_voidfall_spending`, `ar`, `ar_fillers`, `ar_glaive_cycle`, `ar_glaive_cycle_filler`, `ar_quick_consume`, `trinkets`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `sigil_of_flame` | — |
| 3 | `sigil_of_spite` | if=hero_tree.aldrachi_reaver\|talent.soul_carver |
| 4 | `immolation_aura` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=single_target,value=spell_targets.spirit_bomb=1 |
| 2 | `variable` | name=aoe,value=spell_targets.spirit_bomb>=3 |
| 3 | `variable` | name=execute,value=fight_remains<20 |
| 4 | `variable` | name=is_dungeon,value=fight_style.dungeonroute\|fight_style.dungeonslice |
| 5 | `cycling_variable` | name=dung_pull_ttd,op=reset |
| 6 | `cycling_variable` | name=dung_pull_ttd,op=max,value=target.time_to_die |
| 7 | `variable` | name=dung_next_pull,value=variable.is_dungeon&raid_event.adds.exists&raid_event.pull.remains<12&(raid_event.adds.has_boss\|raid_event.adds.count>=3) |
| 8 | `variable` | name=dung_cd_ok,value=variable.execute\|!variable.is_dungeon\|(variable.dung_pull_ttd>12&!variable.dung_next_pull) |
| 9 | `variable` | name=dung_meta_ok,value=variable.execute\|!variable.is_dungeon\|(variable.dung_pull_ttd>(15-5*hero_tree.annihilator)&!variable.dung_next_pull) |
| 10 | `variable` | name=trinket_1_buffs,value=trinket.1.has_use_buff\|(trinket.1.has_buff.agility\|trinket.1.has_buff.mastery\|trinket.1.has_buff.versatility\|trinket.1.has_buff.haste\|trinket.1.has_buff.crit\|trinket.1.has_buff.attack_power) |
| 11 | `variable` | name=trinket_2_buffs,value=trinket.2.has_use_buff\|(trinket.2.has_buff.agility\|trinket.2.has_buff.mastery\|trinket.2.has_buff.versatility\|trinket.2.has_buff.haste\|trinket.2.has_buff.crit\|trinket.2.has_buff.attack_power) |
| 12 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs\|variable.trinket_2_buffs&((trinket.2.proc.any_dps.duration)*trinket.2.proc.any_dps.default_value)>((trinket.1.proc.any_dps.duration)*trinket.1.proc.any_dps.default_value) |
| 13 | `variable` | name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl |
| 14 | `variable` | name=fiery_demise_active,value=talent.fiery_demise&dot.fiery_brand.ticking |
| 15 | `variable` | name=fire_cd_soon,value=cooldown.soul_carver.remains>?cooldown.fel_devastation.remains>?cooldown.sigil_of_spite.remains<(8+talent.charred_flesh.rank) |
| 16 | `variable` | name=fragment_target,op=setif,value=5+apex.2,value_else=variable.fiery_demise_active*3+!variable.fiery_demise_active*(5-buff.metamorphosis.up),condition=hero_tree.aldrachi_reaver |
| 17 | `auto_attack` | — |
| 18 | `retarget_auto_attack` | target_if=min:debuff.reavers_mark.remains,if=hero_tree.aldrachi_reaver |
| 19 | `disrupt` | if=target.debuff.casting.react |
| 20 | `infernal_strike` | use_off_gcd=1 |
| 21 | `demon_spikes` | use_off_gcd=1,if=!buff.demon_spikes.up&in_combat |
| 22 | `run_action_list` | name=ar,if=hero_tree.aldrachi_reaver |
| 23 | `run_action_list` | name=anni,if=hero_tree.annihilator |

## Action List: `anni`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=anni_meta_entry_time,value=3*gcd.max |
| 2 | `potion` | use_off_gcd=1,if=variable.execute&(!variable.is_dungeon\|in_boss_encounter) |
| 3 | `invoke_external_buff` | name=power_infusion,if=buff.voidfall_spending.stack=3\|variable.execute |
| 4 | `call_action_list` | name=anni_voidfall_spending,if=buff.voidfall_spending.up |
| 5 | `call_action_list` | name=anni_voidfall_fishing,if=buff.voidfall_building.stack>=2&!buff.voidfall_spending.up |
| 6 | `call_action_list` | name=anni_meta_entry,if=buff.untethered_rage.up\|(variable.dung_meta_ok&cooldown.metamorphosis.remains<variable.anni_meta_entry_time) |
| 7 | `call_action_list` | name=anni_cooldowns,if=variable.dung_cd_ok&(!talent.fiery_demise\|variable.fiery_demise_active\|cooldown.fiery_brand.remains>20\|variable.execute) |
| 8 | `fiery_brand` | if=charges>=2\|(!variable.fiery_demise_active&(!talent.fiery_demise\|variable.fire_cd_soon\|variable.execute)) |
| 9 | `fracture` | if=full_recharge_time<gcd.max |
| 10 | `immolation_aura` | if=(talent.fallout&variable.aoe)\|(talent.charred_flesh&variable.fiery_demise_active) |
| 11 | `spirit_bomb` | if=soul_fragments>=variable.fragment_target |
| 12 | `immolation_aura` | — |
| 13 | `sigil_of_flame` | — |
| 14 | `fracture` | if=soul_fragments.total<=4\|fury<40 |
| 15 | `soul_cleave` | if=soul_fragments<=1\|fury.deficit<=15 |
| 16 | `soul_cleave` | if=!(apex.3&!buff.untethered_rage.up&buff.seething_anger.stack>=10)&!cooldown.metamorphosis.up |
| 17 | `fracture` | — |
| 18 | `felblade` | — |
| 19 | `throw_glaive` | — |

## Action List: `anni_cooldowns`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `spirit_bomb` | if=soul_fragments>=variable.fragment_target |
| 2 | `soul_carver` | if=soul_fragments<=3 |
| 3 | `sigil_of_spite` | if=soul_fragments<=2+talent.soul_sigils |
| 4 | `fel_devastation` | — |
| 5 | `call_action_list` | name=anni_generate_fury,if=cooldown.fel_devastation.up&fury<50 |

## Action List: `anni_filler_no_spend`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `soul_cleave` | if=soul_fragments=0&!action.sigil_of_flame.placed&(!talent.sigil_of_spite\|(talent.sigil_of_spite&!action.sigil_of_spite.placed))&!prev_gcd.2.soul_carver |
| 2 | `immolation_aura` | — |
| 3 | `sigil_of_flame` | — |
| 4 | `felblade` | — |
| 5 | `fracture` | if=!buff.voidfall_spending.up |
| 6 | `soul_carver` | if=(!talent.sigil_of_spite\|(talent.sigil_of_spite&!action.sigil_of_spite.placed)) |
| 7 | `fel_devastation` | if=(!talent.sigil_of_spite\|(talent.sigil_of_spite&!action.sigil_of_spite.placed)) |
| 8 | `sigil_of_spite` | — |
| 9 | `fracture` | — |
| 10 | `throw_glaive` | — |

## Action List: `anni_generate_fury`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `immolation_aura` | — |
| 2 | `sigil_of_flame` | — |
| 3 | `felblade` | — |
| 4 | `fracture` | — |

## Action List: `anni_meta_entry`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `potion` | use_off_gcd=1,if=(variable.fiery_demise_active\|variable.execute)&(!variable.is_dungeon\|in_boss_encounter) |
| 2 | `call_action_list` | name=trinkets |
| 3 | `invoke_external_buff` | name=power_infusion |
| 4 | `metamorphosis` | use_off_gcd=1,if=gcd.remains=0&buff.untethered_rage.up&!buff.voidfall_spending.up |
| 5 | `call_action_list` | name=anni_pre_meta_spb,if=cooldown.spirit_bomb.remains<variable.anni_meta_entry_time&soul_fragments.total<variable.fragment_target |
| 6 | `fiery_brand` | if=charges>=2\|!variable.fiery_demise_active |
| 7 | `sigil_of_spite` | if=soul_fragments>=variable.fragment_target&cooldown.spirit_bomb.up&cooldown.metamorphosis.up |
| 8 | `spirit_bomb` | if=soul_fragments>=variable.fragment_target&fury>=60 |
| 9 | `sigil_of_spite` | if=soul_fragments.total<variable.fragment_target |
| 10 | `call_action_list` | name=anni_generate_fury,if=fury<75&cooldown.metamorphosis.up&cooldown.spirit_bomb.remains>gcd.max*3 |
| 11 | `metamorphosis` | use_off_gcd=1,if=variable.dung_meta_ok&gcd.remains=0&cooldown.spirit_bomb.remains>gcd.max*3&(soul_fragments.total>=variable.fragment_target\|(talent.sigil_of_spite&action.sigil_of_spite.placed)) |
| 12 | `call_action_list` | name=anni_filler_no_spend |

## Action List: `anni_pre_meta_spb`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `fracture` | — |
| 2 | `immolation_aura` | if=variable.aoe |
| 3 | `fiery_brand` | if=charges>=2\|!variable.fiery_demise_active |
| 4 | `soul_carver` | if=(cooldown.soul_carver.up+cooldown.sigil_of_spite.up+cooldown.fel_devastation.up)>=2 |
| 5 | `fel_devastation` | if=(cooldown.soul_carver.up+cooldown.sigil_of_spite.up+cooldown.fel_devastation.up)>=2 |
| 6 | `felblade` | — |
| 7 | `call_action_list` | name=anni_filler_no_spend |

## Action List: `anni_voidfall_fishing`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `fracture` | — |
| 2 | `call_action_list` | name=anni_generate_fury,if=cooldown.fracture.charges_fractional>=0.75 |

## Action List: `anni_voidfall_spending`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `fiery_brand` | if=charges>=2\|!variable.fiery_demise_active |
| 2 | `felblade` | if=buff.voidfall_spending.stack=buff.voidfall_spending.max_stack&cooldown.spirit_bomb.ready&soul_fragments.total>=variable.fragment_target&fury>=30&fury<45&cooldown.fracture.charges>=1 |
| 3 | `fracture` | if=buff.voidfall_spending.stack=buff.voidfall_spending.max_stack&cooldown.spirit_bomb.ready&soul_fragments.total>=variable.fragment_target&fury>=45&fury<75 |
| 4 | `soul_cleave` | if=cooldown.spirit_bomb.remains>gcd.max*4 |
| 5 | `spirit_bomb` | if=soul_fragments>=variable.fragment_target |
| 6 | `felblade` | if=(fury<40&cooldown.spirit_bomb.remains<=gcd.max)\|(fury<25&cooldown.spirit_bomb.remains>gcd.max) |
| 7 | `immolation_aura` | if=(fury<40&cooldown.spirit_bomb.remains<=gcd.max)\|(fury<25&cooldown.spirit_bomb.remains>gcd.max) |
| 8 | `soul_carver` | if=(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target&(!talent.sigil_of_spite\|!action.sigil_of_spite.placed) |
| 9 | `fel_devastation` | if=(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target&(!talent.sigil_of_spite\|!action.sigil_of_spite.placed) |
| 10 | `immolation_aura` | if=variable.aoe&(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target&(!talent.sigil_of_spite\|!action.sigil_of_spite.placed) |
| 11 | `sigil_of_spite` | if=(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target |
| 12 | `call_action_list` | name=anni_filler_no_spend |

## Action List: `ar`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=frac_souls,value=2+buff.metamorphosis.up |
| 2 | `variable` | name=base_deficit,value=(20-buff.art_of_the_glaive.stack-soul_fragments.total)<?0 |
| 3 | `variable` | name=eff_recharge,value=cooldown.fracture.remains+(cooldown.fracture.charges>=2)*cooldown.fracture.duration |
| 4 | `variable` | name=passive_per_sec,value=0.30+(talent.fallout&buff.immolation_aura.up)*0.30*spell_targets.spirit_bomb |
| 5 | `variable` | name=fracs_base,value=variable.base_deficit%variable.frac_souls |
| 6 | `variable` | name=fracs_base,op=ceil |
| 7 | `variable` | name=base_gen_time,value=(variable.fracs_base>0)*((variable.fracs_base<=cooldown.fracture.charges)*variable.fracs_base*(1+apex.3)*gcd.max+(variable.fracs_base>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_base-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max)) |
| 8 | `variable` | name=sc1,value=talent.soul_carver&cooldown.soul_carver.remains<variable.base_gen_time |
| 9 | `variable` | name=net1,value=(variable.base_deficit-variable.sc1*6)<?0 |
| 10 | `variable` | name=fracs1,value=variable.net1%variable.frac_souls |
| 11 | `variable` | name=fracs1,op=ceil |
| 12 | `variable` | name=gt1,value=(variable.fracs1>0)*((variable.fracs1<=cooldown.fracture.charges)*variable.fracs1*(1+apex.3)*gcd.max+(variable.fracs1>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs1-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max)) |
| 13 | `variable` | name=sos1,value=talent.sigil_of_spite&cooldown.sigil_of_spite.remains<variable.gt1 |
| 14 | `variable` | name=N1,value=(variable.net1-variable.sos1*3)<?0 |
| 15 | `variable` | name=fracs_np,value=variable.N1%variable.frac_souls |
| 16 | `variable` | name=fracs_np,op=ceil |
| 17 | `variable` | name=gt_np,value=(variable.fracs_np>0)*((variable.fracs_np<=cooldown.fracture.charges)*variable.fracs_np*(1+apex.3)*gcd.max+(variable.fracs_np>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_np-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max)) |
| 18 | `variable` | name=T1,value=gcd.max+variable.gt_np+variable.sc1*gcd.max+variable.sos1*gcd.max |
| 19 | `variable` | name=sc_prop,value=(talent.soul_carver&cooldown.soul_carver.remains<variable.T1)*((1-cooldown.soul_carver.remains%variable.T1)<?0) |
| 20 | `variable` | name=net_p,value=(variable.base_deficit-6*variable.sc_prop)<?0 |
| 21 | `variable` | name=fracs_p,value=variable.net_p%variable.frac_souls |
| 22 | `variable` | name=fracs_p,op=ceil |
| 23 | `variable` | name=gt_p,value=(variable.fracs_p>0)*((variable.fracs_p<=cooldown.fracture.charges)*variable.fracs_p*(1+apex.3)*gcd.max+(variable.fracs_p>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_p-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max)) |
| 24 | `variable` | name=sos_p,value=talent.sigil_of_spite&cooldown.sigil_of_spite.remains<variable.gt_p |
| 25 | `variable` | name=N_p,value=(variable.net_p-variable.sos_p*3)<?0 |
| 26 | `variable` | name=adj2,value=(variable.N_p-variable.passive_per_sec*variable.T1)<?0 |
| 27 | `variable` | name=fracs_p2,value=variable.adj2%variable.frac_souls |
| 28 | `variable` | name=fracs_p2,op=ceil |
| 29 | `variable` | name=gt_p2,value=(variable.fracs_p2>0)*((variable.fracs_p2<=cooldown.fracture.charges)*variable.fracs_p2*(1+apex.3)*gcd.max+(variable.fracs_p2>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_p2-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max)) |
| 30 | `variable` | name=T2,value=gcd.max+variable.gt_p2+(variable.sc_prop>0)*gcd.max+variable.sos_p*gcd.max |
| 31 | `variable` | name=T_avg,value=(variable.T1+variable.T2)%2 |
| 32 | `variable` | name=adj_f,value=(variable.N_p-variable.passive_per_sec*variable.T_avg)<?0 |
| 33 | `variable` | name=fracs_f,value=variable.adj_f%variable.frac_souls |
| 34 | `variable` | name=fracs_f,op=ceil |
| 35 | `variable` | name=gt_f,value=(variable.fracs_f>0)*((variable.fracs_f<=cooldown.fracture.charges)*variable.fracs_f*(1+apex.3)*gcd.max+(variable.fracs_f>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_f-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max)) |
| 36 | `variable` | name=time_to_next_glaive,value=gcd.max+variable.gt_f+(variable.sc_prop>0)*gcd.max+variable.sos_p*gcd.max |
| 37 | `variable` | name=passive_floor,value=variable.N_p%(variable.passive_per_sec*gcd.max) |
| 38 | `variable` | name=passive_floor,op=ceil |
| 39 | `variable` | name=passive_floor,value=variable.passive_floor*gcd.max |
| 40 | `variable` | name=time_to_next_glaive,value=variable.time_to_next_glaive<?(variable.fracs_f=0&variable.N_p>0)*variable.passive_floor |
| 41 | `variable` | name=time_to_next_rm_application,value=variable.time_to_next_glaive+2*gcd.max |
| 42 | `variable` | name=rm_remains,value=(variable.last_rm_applied>0)*(20-(time-variable.last_rm_applied))<?0 |
| 43 | `variable` | name=prio_slashes,value=variable.aoe\|variable.execute\|(variable.rm_remains>0&variable.last_refresh_at>variable.last_slash_at) |
| 44 | `variable` | name=last_slash_at,op=setif,value=time,value_else=variable.last_slash_at,condition=buff.reavers_glaive.up&!variable.cycle_recorded&variable.prio_slashes |
| 45 | `variable` | name=last_refresh_at,op=setif,value=time,value_else=variable.last_refresh_at,condition=buff.reavers_glaive.up&!variable.cycle_recorded&!variable.prio_slashes |
| 46 | `variable` | name=cycle_recorded,value=buff.reavers_glaive.up |
| 47 | `variable` | name=rg_imminent,value=(buff.reavers_glaive.up&(variable.execute\|variable.rm_remains<=variable.time_to_next_rm_application\|buff.art_of_the_glaive.stack+soul_fragments>=(20-variable.frac_souls)))\|(buff.art_of_the_glaive.stack+soul_fragments>=20)\|(soul_fragments>=6&buff.art_of_the_glaive.stack>=(20-variable.frac_souls)&cooldown.fracture.charges>=1) |
| 48 | `felblade` | if=prev_gcd.1.vengeful_retreat\|prev_off_gcd.vengeful_retreat |
| 49 | `metamorphosis` | use_off_gcd=1,if=buff.untethered_rage.up\|(!buff.metamorphosis.up&variable.dung_meta_ok) |
| 50 | `call_action_list` | name=trinkets |
| 51 | `reavers_glaive` | if=buff.reavers_glaive.up&!buff.rending_strike.up&!buff.glaive_flurry.up&(variable.execute\|variable.prio_slashes\|variable.rm_remains<=0\|variable.rm_remains<10\|buff.art_of_the_glaive.stack+soul_fragments>=(20-variable.frac_souls)) |
| 52 | `call_action_list` | name=ar_glaive_cycle,if=buff.rending_strike.up\|buff.glaive_flurry.up\|prev_gcd.1.reavers_glaive |
| 53 | `fiery_brand` | if=charges>=2\|!variable.fiery_demise_active\|variable.execute |
| 54 | `sigil_of_spite` | if=variable.dung_cd_ok&!buff.reavers_glaive.up&!buff.rending_strike.up&!buff.glaive_flurry.up |
| 55 | `call_action_list` | name=ar_quick_consume,if=!buff.reavers_glaive.up&!buff.rending_strike.up&!buff.glaive_flurry.up&(buff.art_of_the_glaive.stack+soul_fragments>=20\|(variable.aoe&soul_fragments>=6)) |
| 56 | `immolation_aura` | if=in_combat |
| 57 | `fel_devastation` | if=variable.dung_cd_ok&fury>85&(soul_fragments.inactive>1\|variable.aoe)&(!variable.rg_imminent\|variable.aoe) |
| 58 | `sigil_of_flame` | — |
| 59 | `soul_carver` | if=variable.dung_cd_ok&(variable.fiery_demise_active\|(variable.rm_remains<7&buff.art_of_the_glaive.stack+soul_fragments<20)\|variable.execute) |
| 60 | `call_action_list` | name=ar_fillers |

## Action List: `ar_fillers`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `spirit_bomb` | if=soul_fragments>=(variable.fragment_target-variable.aoe) |
| 2 | `immolation_aura` | if=variable.time_to_next_glaive>3*gcd.max |
| 3 | `felblade` | if=cooldown.spirit_bomb.remains<gcd.max&soul_fragments.total>=variable.fragment_target&fury<40 |
| 4 | `vengeful_retreat` | use_off_gcd=1,if=!cooldown.felblade.up&talent.unhindered_assault&cooldown.spirit_bomb.remains<gcd.max&soul_fragments.total>=variable.fragment_target&fury<40 |
| 5 | `soul_cleave` | if=((soul_fragments>=5&!variable.aoe)\|soul_fragments<=1\|fury.deficit<30)&(fury>=2*action.soul_cleave.cost\|cooldown.fracture.charges>=1\|cooldown.fracture.remains<=gcd.max)&(!buff.rending_strike.up\|!buff.glaive_flurry.up\|!variable.prio_slashes) |
| 6 | `sigil_of_flame` | if=variable.aoe |
| 7 | `fracture` | if=buff.metamorphosis.up\|full_recharge_time<gcd.max\|buff.warblades_hunger.stack>=4 |
| 8 | `immolation_aura` | if=!variable.is_dungeon\|in_combat |
| 9 | `sigil_of_flame` | — |
| 10 | `soul_cleave` | if=(fury>=2*action.soul_cleave.cost\|cooldown.fracture.charges>=1\|cooldown.fracture.remains<=gcd.max)&(!buff.rending_strike.up\|!buff.glaive_flurry.up\|!variable.prio_slashes) |
| 11 | `fracture` | — |
| 12 | `felblade` | — |
| 13 | `vengeful_retreat` | use_off_gcd=1,if=talent.unhindered_assault&!cooldown.felblade.up |
| 14 | `soul_carver` | — |
| 15 | `fel_devastation` | — |
| 16 | `throw_glaive` | — |

## Action List: `ar_glaive_cycle`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1\|trinket.2.cooldown.remains\|trinket.2.cooldown.duration=0)&gcd.remains>0.1 |
| 2 | `use_item` | use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2\|trinket.1.cooldown.remains\|trinket.1.cooldown.duration=0)&gcd.remains>0.1 |
| 3 | `call_action_list` | name=ar_glaive_cycle_filler,if=(variable.prio_slashes&((cooldown.fracture.charges<1&buff.rending_strike.up&buff.glaive_flurry.up)\|fury<10))\|(!variable.prio_slashes&((buff.rending_strike.up&buff.glaive_flurry.up&fury<35)\|(buff.rending_strike.up&!buff.glaive_flurry.up&cooldown.fracture.charges<1))) |
| 4 | `potion` | use_off_gcd=1 |
| 5 | `invoke_external_buff` | name=power_infusion |
| 6 | `variable` | name=last_rm_applied,value=time,if=buff.rending_strike.up |
| 7 | `fracture` | if=buff.rending_strike.up&buff.glaive_flurry.up&variable.prio_slashes |
| 8 | `soul_cleave` | if=buff.rending_strike.up&buff.glaive_flurry.up&!variable.prio_slashes |
| 9 | `fracture` | if=buff.rending_strike.up&!buff.glaive_flurry.up |
| 10 | `soul_cleave` | if=buff.glaive_flurry.up&!buff.rending_strike.up |
| 11 | `call_action_list` | name=ar_glaive_cycle_filler |

## Action List: `ar_glaive_cycle_filler`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `spirit_bomb` | if=fury>75&soul_fragments>=variable.fragment_target |
| 2 | `immolation_aura` | — |
| 3 | `fel_devastation` | if=fury>=85 |
| 4 | `sigil_of_flame` | — |
| 5 | `felblade` | — |
| 6 | `soul_carver` | — |
| 7 | `vengeful_retreat` | use_off_gcd=1,if=talent.unhindered_assault&!cooldown.felblade.up |
| 8 | `soul_cleave` | if=!buff.glaive_flurry.up |
| 9 | `throw_glaive` | — |

## Action List: `ar_quick_consume`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `soul_cleave` | if=soul_fragments<(3-variable.aoe) |
| 2 | `spirit_bomb` | if=soul_fragments>=(3-variable.aoe) |
| 3 | `soul_cleave` | if=!variable.aoe |

## Action List: `trinkets`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | slot=trinket1,if=variable.trinket_1_buffs&variable.dung_cd_ok&(!trinket.2.has_cooldown\|trinket.2.cooldown.remains\|variable.trinket_priority=1) |
| 2 | `use_item` | slot=trinket2,if=variable.trinket_2_buffs&variable.dung_cd_ok&(!trinket.1.has_cooldown\|trinket.1.cooldown.remains\|variable.trinket_priority=2) |
| 3 | `use_item` | use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1\|trinket.2.cooldown.remains\|trinket.2.cooldown.duration=0)&gcd.remains>0.1 |
| 4 | `use_item` | use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2\|trinket.1.cooldown.remains\|trinket.1.cooldown.duration=0)&gcd.remains>0.1 |
| 5 | `use_item` | slot=trinket1,if=variable.execute |
| 6 | `use_item` | slot=trinket2,if=variable.execute |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=snapshot_stats
actions.precombat+=/sigil_of_flame
# AR always. Anni only with Soul Carver (non-SC builds lose DPS from pre-pull frag misalignment)
actions.precombat+=/sigil_of_spite,if=hero_tree.aldrachi_reaver|talent.soul_carver
actions.precombat+=/immolation_aura

# Executed every time the actor is available.
actions=variable,name=single_target,value=spell_targets.spirit_bomb=1
actions+=/variable,name=aoe,value=spell_targets.spirit_bomb>=3
actions+=/variable,name=execute,value=fight_remains<20
# Dungeon Route
actions+=/variable,name=is_dungeon,value=fight_style.dungeonroute|fight_style.dungeonslice
actions+=/cycling_variable,name=dung_pull_ttd,op=reset
actions+=/cycling_variable,name=dung_pull_ttd,op=max,value=target.time_to_die
actions+=/variable,name=dung_next_pull,value=variable.is_dungeon&raid_event.adds.exists&raid_event.pull.remains<12&(raid_event.adds.has_boss|raid_event.adds.count>=3)
# Safe to use 40-60s CDs (SC, SoS, FD, buff trinkets)
actions+=/variable,name=dung_cd_ok,value=variable.execute|!variable.is_dungeon|(variable.dung_pull_ttd>12&!variable.dung_next_pull)
# Stricter guard for Meta (2min CD) - Anni gets lower bar for UR proc windows
actions+=/variable,name=dung_meta_ok,value=variable.execute|!variable.is_dungeon|(variable.dung_pull_ttd>(15-5*hero_tree.annihilator)&!variable.dung_next_pull)
actions+=/variable,name=trinket_1_buffs,value=trinket.1.has_use_buff|(trinket.1.has_buff.agility|trinket.1.has_buff.mastery|trinket.1.has_buff.versatility|trinket.1.has_buff.haste|trinket.1.has_buff.crit|trinket.1.has_buff.attack_power)
actions+=/variable,name=trinket_2_buffs,value=trinket.2.has_use_buff|(trinket.2.has_buff.agility|trinket.2.has_buff.mastery|trinket.2.has_buff.versatility|trinket.2.has_buff.haste|trinket.2.has_buff.crit|trinket.2.has_buff.attack_power)
# Rank buff trinkets by total stat value (duration * proc value)
actions+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs|variable.trinket_2_buffs&((trinket.2.proc.any_dps.duration)*trinket.2.proc.any_dps.default_value)>((trinket.1.proc.any_dps.duration)*trinket.1.proc.any_dps.default_value)
# Non-buff damage trinkets: which slot has higher ilvl
actions+=/variable,name=damage_trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&!variable.trinket_2_buffs&trinket.2.ilvl>=trinket.1.ilvl
actions+=/variable,name=fiery_demise_active,value=talent.fiery_demise&dot.fiery_brand.ticking
actions+=/variable,name=fire_cd_soon,value=cooldown.soul_carver.remains>?cooldown.fel_devastation.remains>?cooldown.sigil_of_spite.remains<(8+talent.charred_flesh.rank)
# Fragment target: AR uses AotG scaling; Anni uses 3 during Brand, 4 in Meta, 5 baseline
actions+=/variable,name=fragment_target,op=setif,value=5+apex.2,value_else=variable.fiery_demise_active*3+!variable.fiery_demise_active*(5-buff.metamorphosis.up),condition=hero_tree.aldrachi_reaver
actions+=/auto_attack
actions+=/retarget_auto_attack,target_if=min:debuff.reavers_mark.remains,if=hero_tree.aldrachi_reaver
actions+=/disrupt,if=target.debuff.casting.react
actions+=/infernal_strike,use_off_gcd=1
actions+=/demon_spikes,use_off_gcd=1,if=!buff.demon_spikes.up&in_combat
actions+=/run_action_list,name=ar,if=hero_tree.aldrachi_reaver
actions+=/run_action_list,name=anni,if=hero_tree.annihilator

# Pre-meta setup window, typically ~3 GCDs
actions.anni=variable,name=anni_meta_entry_time,value=3*gcd.max
actions.anni+=/potion,use_off_gcd=1,if=variable.execute&(!variable.is_dungeon|in_boss_encounter)
actions.anni+=/invoke_external_buff,name=power_infusion,if=buff.voidfall_spending.stack=3|variable.execute
actions.anni+=/call_action_list,name=anni_voidfall_spending,if=buff.voidfall_spending.up
actions.anni+=/call_action_list,name=anni_voidfall_fishing,if=buff.voidfall_building.stack>=2&!buff.voidfall_spending.up
# Prepare to enter hardcast meta (UR procs enter unconditionally)
actions.anni+=/call_action_list,name=anni_meta_entry,if=buff.untethered_rage.up|(variable.dung_meta_ok&cooldown.metamorphosis.remains<variable.anni_meta_entry_time)
# Use cooldowns, reserving at least one for the next meta
actions.anni+=/call_action_list,name=anni_cooldowns,if=variable.dung_cd_ok&(!talent.fiery_demise|variable.fiery_demise_active|cooldown.fiery_brand.remains>20|variable.execute)
actions.anni+=/fiery_brand,if=charges>=2|(!variable.fiery_demise_active&(!talent.fiery_demise|variable.fire_cd_soon|variable.execute))
actions.anni+=/fracture,if=full_recharge_time<gcd.max
# Priority IA: Fallout generates frags in aoe, Charred Flesh extends brand
actions.anni+=/immolation_aura,if=(talent.fallout&variable.aoe)|(talent.charred_flesh&variable.fiery_demise_active)
actions.anni+=/spirit_bomb,if=soul_fragments>=variable.fragment_target
actions.anni+=/immolation_aura
actions.anni+=/sigil_of_flame
actions.anni+=/fracture,if=soul_fragments.total<=4|fury<40
actions.anni+=/soul_cleave,if=soul_fragments<=1|fury.deficit<=15
actions.anni+=/soul_cleave,if=!(apex.3&!buff.untethered_rage.up&buff.seething_anger.stack>=10)&!cooldown.metamorphosis.up
actions.anni+=/fracture
actions.anni+=/felblade
actions.anni+=/throw_glaive

actions.anni_cooldowns=spirit_bomb,if=soul_fragments>=variable.fragment_target
actions.anni_cooldowns+=/soul_carver,if=soul_fragments<=3
actions.anni_cooldowns+=/sigil_of_spite,if=soul_fragments<=2+talent.soul_sigils
actions.anni_cooldowns+=/fel_devastation
actions.anni_cooldowns+=/call_action_list,name=anni_generate_fury,if=cooldown.fel_devastation.up&fury<50

actions.anni_filler_no_spend=soul_cleave,if=soul_fragments=0&!action.sigil_of_flame.placed&(!talent.sigil_of_spite|(talent.sigil_of_spite&!action.sigil_of_spite.placed))&!prev_gcd.2.soul_carver
actions.anni_filler_no_spend+=/immolation_aura
actions.anni_filler_no_spend+=/sigil_of_flame
actions.anni_filler_no_spend+=/felblade
actions.anni_filler_no_spend+=/fracture,if=!buff.voidfall_spending.up
actions.anni_filler_no_spend+=/soul_carver,if=(!talent.sigil_of_spite|(talent.sigil_of_spite&!action.sigil_of_spite.placed))
actions.anni_filler_no_spend+=/fel_devastation,if=(!talent.sigil_of_spite|(talent.sigil_of_spite&!action.sigil_of_spite.placed))
actions.anni_filler_no_spend+=/sigil_of_spite
actions.anni_filler_no_spend+=/fracture
actions.anni_filler_no_spend+=/throw_glaive

actions.anni_generate_fury=immolation_aura
actions.anni_generate_fury+=/sigil_of_flame
actions.anni_generate_fury+=/felblade
actions.anni_generate_fury+=/fracture

actions.anni_meta_entry=potion,use_off_gcd=1,if=(variable.fiery_demise_active|variable.execute)&(!variable.is_dungeon|in_boss_encounter)
actions.anni_meta_entry+=/call_action_list,name=trinkets
actions.anni_meta_entry+=/invoke_external_buff,name=power_infusion
actions.anni_meta_entry+=/metamorphosis,use_off_gcd=1,if=gcd.remains=0&buff.untethered_rage.up&!buff.voidfall_spending.up
actions.anni_meta_entry+=/call_action_list,name=anni_pre_meta_spb,if=cooldown.spirit_bomb.remains<variable.anni_meta_entry_time&soul_fragments.total<variable.fragment_target
actions.anni_meta_entry+=/fiery_brand,if=charges>=2|!variable.fiery_demise_active
actions.anni_meta_entry+=/sigil_of_spite,if=soul_fragments>=variable.fragment_target&cooldown.spirit_bomb.up&cooldown.metamorphosis.up
actions.anni_meta_entry+=/spirit_bomb,if=soul_fragments>=variable.fragment_target&fury>=60
actions.anni_meta_entry+=/sigil_of_spite,if=soul_fragments.total<variable.fragment_target
# Pool to 75 fury for SB+SC voidfall combo after meta entry
actions.anni_meta_entry+=/call_action_list,name=anni_generate_fury,if=fury<75&cooldown.metamorphosis.up&cooldown.spirit_bomb.remains>gcd.max*3
actions.anni_meta_entry+=/metamorphosis,use_off_gcd=1,if=variable.dung_meta_ok&gcd.remains=0&cooldown.spirit_bomb.remains>gcd.max*3&(soul_fragments.total>=variable.fragment_target|(talent.sigil_of_spite&action.sigil_of_spite.placed))
actions.anni_meta_entry+=/call_action_list,name=anni_filler_no_spend

actions.anni_pre_meta_spb=fracture
actions.anni_pre_meta_spb+=/immolation_aura,if=variable.aoe
actions.anni_pre_meta_spb+=/fiery_brand,if=charges>=2|!variable.fiery_demise_active
actions.anni_pre_meta_spb+=/soul_carver,if=(cooldown.soul_carver.up+cooldown.sigil_of_spite.up+cooldown.fel_devastation.up)>=2
actions.anni_pre_meta_spb+=/fel_devastation,if=(cooldown.soul_carver.up+cooldown.sigil_of_spite.up+cooldown.fel_devastation.up)>=2
actions.anni_pre_meta_spb+=/felblade
actions.anni_pre_meta_spb+=/call_action_list,name=anni_filler_no_spend

actions.anni_voidfall_fishing=fracture
actions.anni_voidfall_fishing+=/call_action_list,name=anni_generate_fury,if=cooldown.fracture.charges_fractional>=0.75

actions.anni_voidfall_spending=fiery_brand,if=charges>=2|!variable.fiery_demise_active
# Felblade to bridge fury into fracture bridge range (30+15=45)
actions.anni_voidfall_spending+=/felblade,if=buff.voidfall_spending.stack=buff.voidfall_spending.max_stack&cooldown.spirit_bomb.ready&soul_fragments.total>=variable.fragment_target&fury>=30&fury<45&cooldown.fracture.charges>=1
# Fracture to bridge fury for SB+SC combo when 1 fracture away (45+30=75)
actions.anni_voidfall_spending+=/fracture,if=buff.voidfall_spending.stack=buff.voidfall_spending.max_stack&cooldown.spirit_bomb.ready&soul_fragments.total>=variable.fragment_target&fury>=45&fury<75
actions.anni_voidfall_spending+=/soul_cleave,if=cooldown.spirit_bomb.remains>gcd.max*4
actions.anni_voidfall_spending+=/spirit_bomb,if=soul_fragments>=variable.fragment_target
actions.anni_voidfall_spending+=/felblade,if=(fury<40&cooldown.spirit_bomb.remains<=gcd.max)|(fury<25&cooldown.spirit_bomb.remains>gcd.max)
actions.anni_voidfall_spending+=/immolation_aura,if=(fury<40&cooldown.spirit_bomb.remains<=gcd.max)|(fury<25&cooldown.spirit_bomb.remains>gcd.max)
actions.anni_voidfall_spending+=/soul_carver,if=(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target&(!talent.sigil_of_spite|!action.sigil_of_spite.placed)
actions.anni_voidfall_spending+=/fel_devastation,if=(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target&(!talent.sigil_of_spite|!action.sigil_of_spite.placed)
actions.anni_voidfall_spending+=/immolation_aura,if=variable.aoe&(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target&(!talent.sigil_of_spite|!action.sigil_of_spite.placed)
actions.anni_voidfall_spending+=/sigil_of_spite,if=(cooldown.spirit_bomb.remains<=gcd.max)&soul_fragments.total<variable.fragment_target
actions.anni_voidfall_spending+=/call_action_list,name=anni_filler_no_spend

# TTNG MODEL: GCDs until next glaive, accounting for SC, SoS, and passive frags
actions.ar=variable,name=frac_souls,value=2+buff.metamorphosis.up
actions.ar+=/variable,name=base_deficit,value=(20-buff.art_of_the_glaive.stack-soul_fragments.total)<?0
actions.ar+=/variable,name=eff_recharge,value=cooldown.fracture.remains+(cooldown.fracture.charges>=2)*cooldown.fracture.duration
actions.ar+=/variable,name=passive_per_sec,value=0.30+(talent.fallout&buff.immolation_aura.up)*0.30*spell_targets.spirit_bomb
actions.ar+=/variable,name=fracs_base,value=variable.base_deficit%variable.frac_souls
actions.ar+=/variable,name=fracs_base,op=ceil
actions.ar+=/variable,name=base_gen_time,value=(variable.fracs_base>0)*((variable.fracs_base<=cooldown.fracture.charges)*variable.fracs_base*(1+apex.3)*gcd.max+(variable.fracs_base>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_base-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max))
# Pass 1: subtract SC (6 frags) and SoS (3 frags) if they arrive within the gen window
actions.ar+=/variable,name=sc1,value=talent.soul_carver&cooldown.soul_carver.remains<variable.base_gen_time
actions.ar+=/variable,name=net1,value=(variable.base_deficit-variable.sc1*6)<?0
actions.ar+=/variable,name=fracs1,value=variable.net1%variable.frac_souls
actions.ar+=/variable,name=fracs1,op=ceil
actions.ar+=/variable,name=gt1,value=(variable.fracs1>0)*((variable.fracs1<=cooldown.fracture.charges)*variable.fracs1*(1+apex.3)*gcd.max+(variable.fracs1>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs1-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max))
actions.ar+=/variable,name=sos1,value=talent.sigil_of_spite&cooldown.sigil_of_spite.remains<variable.gt1
actions.ar+=/variable,name=N1,value=(variable.net1-variable.sos1*3)<?0
actions.ar+=/variable,name=fracs_np,value=variable.N1%variable.frac_souls
actions.ar+=/variable,name=fracs_np,op=ceil
actions.ar+=/variable,name=gt_np,value=(variable.fracs_np>0)*((variable.fracs_np<=cooldown.fracture.charges)*variable.fracs_np*(1+apex.3)*gcd.max+(variable.fracs_np>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_np-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max))
# T1: no-passive reference time (overhead GCD + fracture gen + SC/SoS cast GCDs)
actions.ar+=/variable,name=T1,value=gcd.max+variable.gt_np+variable.sc1*gcd.max+variable.sos1*gcd.max
# Pass 2: proportional SC credit (scales by how early SC arrives relative to T1)
actions.ar+=/variable,name=sc_prop,value=(talent.soul_carver&cooldown.soul_carver.remains<variable.T1)*((1-cooldown.soul_carver.remains%variable.T1)<?0)
actions.ar+=/variable,name=net_p,value=(variable.base_deficit-6*variable.sc_prop)<?0
actions.ar+=/variable,name=fracs_p,value=variable.net_p%variable.frac_souls
actions.ar+=/variable,name=fracs_p,op=ceil
actions.ar+=/variable,name=gt_p,value=(variable.fracs_p>0)*((variable.fracs_p<=cooldown.fracture.charges)*variable.fracs_p*(1+apex.3)*gcd.max+(variable.fracs_p>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_p-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max))
actions.ar+=/variable,name=sos_p,value=talent.sigil_of_spite&cooldown.sigil_of_spite.remains<variable.gt_p
actions.ar+=/variable,name=N_p,value=(variable.net_p-variable.sos_p*3)<?0
actions.ar+=/variable,name=adj2,value=(variable.N_p-variable.passive_per_sec*variable.T1)<?0
actions.ar+=/variable,name=fracs_p2,value=variable.adj2%variable.frac_souls
actions.ar+=/variable,name=fracs_p2,op=ceil
actions.ar+=/variable,name=gt_p2,value=(variable.fracs_p2>0)*((variable.fracs_p2<=cooldown.fracture.charges)*variable.fracs_p2*(1+apex.3)*gcd.max+(variable.fracs_p2>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_p2-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max))
# T2: passive-adjusted estimate, averaged with T1 to tame oscillation
actions.ar+=/variable,name=T2,value=gcd.max+variable.gt_p2+(variable.sc_prop>0)*gcd.max+variable.sos_p*gcd.max
actions.ar+=/variable,name=T_avg,value=(variable.T1+variable.T2)%2
# Final pass: use T_avg as the passive window for the definitive fracture count
actions.ar+=/variable,name=adj_f,value=(variable.N_p-variable.passive_per_sec*variable.T_avg)<?0
actions.ar+=/variable,name=fracs_f,value=variable.adj_f%variable.frac_souls
actions.ar+=/variable,name=fracs_f,op=ceil
actions.ar+=/variable,name=gt_f,value=(variable.fracs_f>0)*((variable.fracs_f<=cooldown.fracture.charges)*variable.fracs_f*(1+apex.3)*gcd.max+(variable.fracs_f>cooldown.fracture.charges)*((cooldown.fracture.charges*(1+apex.3)*gcd.max<?variable.eff_recharge)+((variable.fracs_f-cooldown.fracture.charges-1)<?0)*cooldown.fracture.duration+gcd.max))
actions.ar+=/variable,name=time_to_next_glaive,value=gcd.max+variable.gt_f+(variable.sc_prop>0)*gcd.max+variable.sos_p*gcd.max
# When passives alone cover the deficit, round up to GCD boundaries
actions.ar+=/variable,name=passive_floor,value=variable.N_p%(variable.passive_per_sec*gcd.max)
actions.ar+=/variable,name=passive_floor,op=ceil
actions.ar+=/variable,name=passive_floor,value=variable.passive_floor*gcd.max
actions.ar+=/variable,name=time_to_next_glaive,value=variable.time_to_next_glaive<?(variable.fracs_f=0&variable.N_p>0)*variable.passive_floor
# RM application happens 2 GCDs into the cycle (RG -> SC -> Frac applies mark)
actions.ar+=/variable,name=time_to_next_rm_application,value=variable.time_to_next_glaive+2*gcd.max
# Manual RM tracking (debuff.remains unreliable with async stacks)
actions.ar+=/variable,name=rm_remains,value=(variable.last_rm_applied>0)*(20-(time-variable.last_rm_applied))<?0
# Alternate slash and refresh cycles
actions.ar+=/variable,name=prio_slashes,value=variable.aoe|variable.execute|(variable.rm_remains>0&variable.last_refresh_at>variable.last_slash_at)
# Record cycle type once when RG first stored (resets when RG buff drops)
actions.ar+=/variable,name=last_slash_at,op=setif,value=time,value_else=variable.last_slash_at,condition=buff.reavers_glaive.up&!variable.cycle_recorded&variable.prio_slashes
actions.ar+=/variable,name=last_refresh_at,op=setif,value=time,value_else=variable.last_refresh_at,condition=buff.reavers_glaive.up&!variable.cycle_recorded&!variable.prio_slashes
actions.ar+=/variable,name=cycle_recorded,value=buff.reavers_glaive.up
# RG imminent: stored and ready to fire, at AotG cap, or one consume from overflow
actions.ar+=/variable,name=rg_imminent,value=(buff.reavers_glaive.up&(variable.execute|variable.rm_remains<=variable.time_to_next_rm_application|buff.art_of_the_glaive.stack+soul_fragments>=(20-variable.frac_souls)))|(buff.art_of_the_glaive.stack+soul_fragments>=20)|(soul_fragments>=6&buff.art_of_the_glaive.stack>=(20-variable.frac_souls)&cooldown.fracture.charges>=1)
actions.ar+=/felblade,if=prev_gcd.1.vengeful_retreat|prev_off_gcd.vengeful_retreat
# UR proc meta fires unconditionally; hardcast gates on dungeon TTD
actions.ar+=/metamorphosis,use_off_gcd=1,if=buff.untethered_rage.up|(!buff.metamorphosis.up&variable.dung_meta_ok)
# Stat buff trinkets before RG so the buff covers the glaive cycle
actions.ar+=/call_action_list,name=trinkets
# Fire stored RG: execute, mark expired or aging, or about to overflow AotG
actions.ar+=/reavers_glaive,if=buff.reavers_glaive.up&!buff.rending_strike.up&!buff.glaive_flurry.up&(variable.execute|variable.prio_slashes|variable.rm_remains<=0|variable.rm_remains<10|buff.art_of_the_glaive.stack+soul_fragments>=(20-variable.frac_souls))
actions.ar+=/call_action_list,name=ar_glaive_cycle,if=buff.rending_strike.up|buff.glaive_flurry.up|prev_gcd.1.reavers_glaive
# Fiery brand: overcapped charges, or setup for fiery demise window
actions.ar+=/fiery_brand,if=charges>=2|!variable.fiery_demise_active|variable.execute
# SoS for frags, skip during glaive cycle
actions.ar+=/sigil_of_spite,if=variable.dung_cd_ok&!buff.reavers_glaive.up&!buff.rending_strike.up&!buff.glaive_flurry.up
# Emergency consume: AotG overflow or frag cap in aoe
actions.ar+=/call_action_list,name=ar_quick_consume,if=!buff.reavers_glaive.up&!buff.rending_strike.up&!buff.glaive_flurry.up&(buff.art_of_the_glaive.stack+soul_fragments>=20|(variable.aoe&soul_fragments>=6))
actions.ar+=/immolation_aura,if=in_combat
# FD: high fury, in-flight frags, not near RG. aoe skips the RG check
actions.ar+=/fel_devastation,if=variable.dung_cd_ok&fury>85&(soul_fragments.inactive>1|variable.aoe)&(!variable.rg_imminent|variable.aoe)
actions.ar+=/sigil_of_flame
# SC: 6 frags, prefer fiery demise. OK when mark is aging or in execute
actions.ar+=/soul_carver,if=variable.dung_cd_ok&(variable.fiery_demise_active|(variable.rm_remains<7&buff.art_of_the_glaive.stack+soul_fragments<20)|variable.execute)
actions.ar+=/call_action_list,name=ar_fillers

# Fillers outside glaive cycles. aoe lowers SpB threshold by 1
actions.ar_fillers=spirit_bomb,if=soul_fragments>=(variable.fragment_target-variable.aoe)
actions.ar_fillers+=/immolation_aura,if=variable.time_to_next_glaive>3*gcd.max
actions.ar_fillers+=/felblade,if=cooldown.spirit_bomb.remains<gcd.max&soul_fragments.total>=variable.fragment_target&fury<40
actions.ar_fillers+=/vengeful_retreat,use_off_gcd=1,if=!cooldown.felblade.up&talent.unhindered_assault&cooldown.spirit_bomb.remains<gcd.max&soul_fragments.total>=variable.fragment_target&fury<40
# SC: aoe skips frag>=5 trigger to save frags for SpB
actions.ar_fillers+=/soul_cleave,if=((soul_fragments>=5&!variable.aoe)|soul_fragments<=1|fury.deficit<30)&(fury>=2*action.soul_cleave.cost|cooldown.fracture.charges>=1|cooldown.fracture.remains<=gcd.max)&(!buff.rending_strike.up|!buff.glaive_flurry.up|!variable.prio_slashes)
actions.ar_fillers+=/sigil_of_flame,if=variable.aoe
actions.ar_fillers+=/fracture,if=buff.metamorphosis.up|full_recharge_time<gcd.max|buff.warblades_hunger.stack>=4
actions.ar_fillers+=/immolation_aura,if=!variable.is_dungeon|in_combat
actions.ar_fillers+=/sigil_of_flame
# Unconditional SC fallback with same guards
actions.ar_fillers+=/soul_cleave,if=(fury>=2*action.soul_cleave.cost|cooldown.fracture.charges>=1|cooldown.fracture.remains<=gcd.max)&(!buff.rending_strike.up|!buff.glaive_flurry.up|!variable.prio_slashes)
actions.ar_fillers+=/fracture
actions.ar_fillers+=/felblade
actions.ar_fillers+=/vengeful_retreat,use_off_gcd=1,if=talent.unhindered_assault&!cooldown.felblade.up
actions.ar_fillers+=/soul_carver
actions.ar_fillers+=/fel_devastation
actions.ar_fillers+=/throw_glaive

# GLAIVE CYCLE: alternate RS+GF buffs after RG. Slash = frac first, refresh = SC first
actions.ar_glaive_cycle=use_item,use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1|trinket.2.cooldown.remains|trinket.2.cooldown.duration=0)&gcd.remains>0.1
actions.ar_glaive_cycle+=/use_item,use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2|trinket.1.cooldown.remains|trinket.1.cooldown.duration=0)&gcd.remains>0.1
# Fill GCD when waiting for fracture charge (slash) or fury (refresh)
actions.ar_glaive_cycle+=/call_action_list,name=ar_glaive_cycle_filler,if=(variable.prio_slashes&((cooldown.fracture.charges<1&buff.rending_strike.up&buff.glaive_flurry.up)|fury<10))|(!variable.prio_slashes&((buff.rending_strike.up&buff.glaive_flurry.up&fury<35)|(buff.rending_strike.up&!buff.glaive_flurry.up&cooldown.fracture.charges<1)))
actions.ar_glaive_cycle+=/potion,use_off_gcd=1
actions.ar_glaive_cycle+=/invoke_external_buff,name=power_infusion
# Record RM application time when fracture is about to consume RS
actions.ar_glaive_cycle+=/variable,name=last_rm_applied,value=time,if=buff.rending_strike.up
# Slash: fracture first when both buffs up (applies 1-stack RM + triggers slash damage)
actions.ar_glaive_cycle+=/fracture,if=buff.rending_strike.up&buff.glaive_flurry.up&variable.prio_slashes
# Refresh: SC first when both buffs up (subsequent fracture gets 3-stack RM)
actions.ar_glaive_cycle+=/soul_cleave,if=buff.rending_strike.up&buff.glaive_flurry.up&!variable.prio_slashes
# Single-buff continuation
actions.ar_glaive_cycle+=/fracture,if=buff.rending_strike.up&!buff.glaive_flurry.up
actions.ar_glaive_cycle+=/soul_cleave,if=buff.glaive_flurry.up&!buff.rending_strike.up
actions.ar_glaive_cycle+=/call_action_list,name=ar_glaive_cycle_filler

# Glaive cycle filler: non-consuming actions while waiting for resources
actions.ar_glaive_cycle_filler=spirit_bomb,if=fury>75&soul_fragments>=variable.fragment_target
actions.ar_glaive_cycle_filler+=/immolation_aura
actions.ar_glaive_cycle_filler+=/fel_devastation,if=fury>=85
actions.ar_glaive_cycle_filler+=/sigil_of_flame
actions.ar_glaive_cycle_filler+=/felblade
actions.ar_glaive_cycle_filler+=/soul_carver
actions.ar_glaive_cycle_filler+=/vengeful_retreat,use_off_gcd=1,if=talent.unhindered_assault&!cooldown.felblade.up
# SC only when GF already consumed (safe during slash cycles)
actions.ar_glaive_cycle_filler+=/soul_cleave,if=!buff.glaive_flurry.up
actions.ar_glaive_cycle_filler+=/throw_glaive

# Quick consume: rush to AotG 20. aoe uses lower SpB threshold
actions.ar_quick_consume=soul_cleave,if=soul_fragments<(3-variable.aoe)
actions.ar_quick_consume+=/spirit_bomb,if=soul_fragments>=(3-variable.aoe)
actions.ar_quick_consume+=/soul_cleave,if=!variable.aoe

actions.trinkets=use_item,slot=trinket1,if=variable.trinket_1_buffs&variable.dung_cd_ok&(!trinket.2.has_cooldown|trinket.2.cooldown.remains|variable.trinket_priority=1)
actions.trinkets+=/use_item,slot=trinket2,if=variable.trinket_2_buffs&variable.dung_cd_ok&(!trinket.1.has_cooldown|trinket.1.cooldown.remains|variable.trinket_priority=2)
# Non-buff on-use trinkets (direct damage): fire on cooldown, off-GCD
actions.trinkets+=/use_item,use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&(variable.damage_trinket_priority=1|trinket.2.cooldown.remains|trinket.2.cooldown.duration=0)&gcd.remains>0.1
actions.trinkets+=/use_item,use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&(variable.damage_trinket_priority=2|trinket.1.cooldown.remains|trinket.1.cooldown.duration=0)&gcd.remains>0.1
# End of fight: dump everything
actions.trinkets+=/use_item,slot=trinket1,if=variable.execute
actions.trinkets+=/use_item,slot=trinket2,if=variable.execute
```
