# Warlock – Destruction

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:22 UTC

Source: `apl/default/warlock/destruction.simc`

---

## Overview

- **Action Lists:** 8
- **Total Actions:** 142
- **Lists:** `precombat`, `default`, `aoe`, `cleave`, `havoc`, `items`, `ogcd`, `variables`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `summon_pet` | — |
| 2 | `variable` | name=cleave_apl,default=0,op=reset |
| 3 | `variable` | name=trinket_1_buffs,value=trinket.1.has_use_buff\|trinket.1.is.funhouse_lens |
| 4 | `variable` | name=trinket_2_buffs,value=trinket.2.has_use_buff\|trinket.2.is.funhouse_lens |
| 5 | `variable` | name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&(trinket.1.cooldown.duration%%cooldown.summon_infernal.duration=0\|cooldown.summon_infernal.duration%%trinket.1.cooldown.duration=0) |
| 6 | `variable` | name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&(trinket.2.cooldown.duration%%cooldown.summon_infernal.duration=0\|cooldown.summon_infernal.duration%%trinket.2.cooldown.duration=0) |
| 7 | `variable` | name=trinket_1_manual,value=trinket.1.is.spymasters_web |
| 8 | `variable` | name=trinket_2_manual,value=trinket.2.is.spymasters_web |
| 9 | `variable` | name=trinket_1_exclude,value=trinket.1.is.whispering_incarnate_icon |
| 10 | `variable` | name=trinket_2_exclude,value=trinket.2.is.whispering_incarnate_icon |
| 11 | `variable` | name=trinket_1_buff_duration,value=trinket.1.proc.any_dps.duration+(trinket.1.is.funhouse_lens*15)+(trinket.1.is.signet_of_the_priory*20) |
| 12 | `variable` | name=trinket_2_buff_duration,value=trinket.2.proc.any_dps.duration+(trinket.2.is.funhouse_lens*15)+(trinket.2.is.signet_of_the_priory*20) |
| 13 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs\|variable.trinket_2_buffs&((trinket.2.cooldown.duration%variable.trinket_2_buff_duration)*(1+0.5*trinket.2.has_buff.intellect)*(variable.trinket_2_sync))>((trinket.1.cooldown.duration%variable.trinket_1_buff_duration)*(1+0.5*trinket.1.has_buff.intellect)*(variable.trinket_1_sync)) |
| 14 | `variable` | name=allow_rof_2t_spender,default=2,op=reset |
| 15 | `variable` | name=do_rof_2t,value=variable.allow_rof_2t_spender>1.99&!(talent.cataclysm&talent.improved_chaos_bolt),op=set |
| 16 | `variable` | name=disable_cb_2t,value=variable.do_rof_2t\|variable.allow_rof_2t_spender>0.01&variable.allow_rof_2t_spender<0.99 |
| 17 | `grimoire_of_sacrifice` | if=talent.grimoire_of_sacrifice.enabled |
| 18 | `snapshot_stats` | — |
| 19 | `cataclysm` | if=active_enemies>=2&raid_event.adds.in>15 |
| 20 | `soul_fire` | — |
| 21 | `incinerate` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=variables |
| 2 | `call_action_list` | name=aoe,if=(active_enemies>=3)&!variable.cleave_apl |
| 3 | `call_action_list` | name=cleave,if=active_enemies!=1\|variable.cleave_apl |
| 4 | `call_action_list` | name=ogcd |
| 5 | `call_action_list` | name=items |
| 6 | `malevolence` | if=cooldown.summon_infernal.remains>=55 |
| 7 | `summon_infernal` | if=demonic_art |
| 8 | `chaos_bolt` | if=talent.diabolic_ritual&(demonic_art\|((buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<(action.chaos_bolt.execute_time))) |
| 9 | `soul_fire` | if=buff.decimation.react&(soul_shard<=4\|buff.decimation.remains<=gcd.max*2)&debuff.conflagrate.remains>=execute_time |
| 10 | `wither` | if=talent.internal_combustion&(((dot.wither.remains-5*action.chaos_bolt.in_flight)<dot.wither.duration*0.4)\|dot.wither.remains<3\|(dot.wither.remains-action.chaos_bolt.execute_time)<5&action.chaos_bolt.usable)&(!talent.soul_fire\|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains-5))&target.time_to_die>8&!action.soul_fire.in_flight_to_target |
| 11 | `conflagrate` | if=talent.roaring_blaze&debuff.conflagrate.remains<1.5\|full_recharge_time<=gcd.max*2\|recharge_time<=8&(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<gcd.max)&soul_shard>=1.5 |
| 12 | `shadowburn` | if=talent.wither&((cooldown.shadowburn.full_recharge_time<=gcd.max*3\|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight&!talent.diabolic_ritual)&(talent.conflagration_of_chaos\|talent.blistering_atrophy)\|fight_remains<=8) |
| 13 | `shadowburn` | if=(cooldown.summon_infernal.remains>=90&talent.rain_of_chaos)\|buff.malevolence.up |
| 14 | `chaos_bolt` | if=(cooldown.summon_infernal.remains>=90&talent.rain_of_chaos)\|buff.malevolence.up |
| 15 | `ruination` | — |
| 16 | `cataclysm` | if=raid_event.adds.in>15&(talent.wither&dot.wither.refreshable) |
| 17 | `channel_demonfire` | if=talent.raging_demonfire&(dot.immolate.remains+dot.wither.remains-5*(action.chaos_bolt.in_flight&talent.internal_combustion))>cast_time |
| 18 | `wither` | if=!talent.internal_combustion&(((dot.wither.remains-5*(action.chaos_bolt.in_flight))<dot.wither.duration*0.3)\|dot.wither.remains<3)&(!talent.cataclysm\|cooldown.cataclysm.remains>dot.wither.remains)&(!talent.soul_fire\|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains))&target.time_to_die>8&!action.soul_fire.in_flight_to_target |
| 19 | `immolate` | if=(((dot.immolate.remains-5*(action.chaos_bolt.in_flight&talent.internal_combustion))<dot.immolate.duration*0.3)\|dot.immolate.remains<3\|(dot.immolate.remains-action.chaos_bolt.execute_time)<5&talent.internal_combustion&action.chaos_bolt.usable)&(!talent.soul_fire\|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.immolate.remains-5*talent.internal_combustion))&target.time_to_die>8&!action.soul_fire.in_flight_to_target |
| 20 | `summon_infernal` | — |
| 21 | `chaos_bolt` | if=(variable.pooling_condition_cb&(cooldown.summon_infernal.remains>=gcd.max*3\|soul_shard>4))&(talent.wither\|((buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)>(action.chaos_bolt.execute_time+2*gcd.max))) |
| 22 | `channel_demonfire` | — |
| 23 | `dimensional_rift` | — |
| 24 | `infernal_bolt` | if=soul_shard<=3 |
| 25 | `conflagrate` | if=charges>(max_charges-1)\|fight_remains<gcd.max*charges |
| 26 | `incinerate` | — |

## Action List: `aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=ogcd |
| 2 | `call_action_list` | name=items |
| 3 | `malevolence` | if=cooldown.summon_infernal.remains>=55&soul_shard<4.7&(active_enemies<=3+active_dot.wither\|time>30) |
| 4 | `chaos_bolt` | if=talent.diabolic_ritual&(((buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<(action.chaos_bolt.execute_time)&active_enemies<=9)\|(demonic_art&active_enemies<=7)) |
| 5 | `call_action_list` | name=havoc,if=havoc_active&havoc_remains>gcd.max&active_enemies<=4&talent.wither |
| 6 | `dimensional_rift` | if=soul_shard<4.7&(charges>2\|fight_remains<cooldown.dimensional_rift.duration) |
| 7 | `incinerate` | if=(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<=action.incinerate.cast_time) |
| 8 | `rain_of_fire` | if=(soul_shard>=(3.5-0.1*(active_dot.immolate+active_dot.wither))\|buff.ritual_of_ruin.up)&(talent.wither\|(talent.diabolic_ritual&active_enemies>=8)) |
| 9 | `chaos_bolt` | if=soul_shard>=((3.0-0.1*(active_dot.immolate))\|buff.ritual_of_ruin.up)&talent.diabolic_ritual&active_enemies<=7 |
| 10 | `wither` | target_if=min:dot.wither.remains+99*debuff.havoc.remains+99*!dot.wither.ticking,if=dot.wither.refreshable&(!talent.cataclysm.enabled\|cooldown.cataclysm.remains>dot.wither.remains)&(!(talent.raging_demonfire&talent.channel_demonfire)\|cooldown.channel_demonfire.remains>remains\|time<5)&(active_dot.wither<=4\|time>15)&target.time_to_die>18 |
| 11 | `channel_demonfire` | if=dot.immolate.remains+dot.wither.remains>cast_time&talent.raging_demonfire |
| 12 | `shadowburn` | if=talent.wither&(buff.malevolence.up\|active_enemies<=6\|(fight_remains>60&active_enemies<=14))&((cooldown.shadowburn.full_recharge_time<=gcd.max*3\|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight)\|fight_remains<=8) |
| 13 | `shadowburn` | target_if=min:time_to_die,if=talent.wither&(buff.malevolence.up\|active_enemies<=6\|(fight_remains>60&active_enemies<=14))&((cooldown.shadowburn.full_recharge_time<=gcd.max*3\|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight)\|fight_remains<=8) |
| 14 | `ruination` | — |
| 15 | `rain_of_fire` | if=pet.infernal.active&talent.rain_of_chaos&(talent.wither\|(talent.diabolic_ritual&active_enemies>=8)) |
| 16 | `chaos_bolt` | if=pet.infernal.active&talent.rain_of_chaos&talent.diabolic_ritual&active_enemies<=7 |
| 17 | `soul_fire` | target_if=min:dot.wither.remains+dot.immolate.remains-5*debuff.conflagrate.up+100*debuff.havoc.remains,if=(buff.decimation.up)&!talent.raging_demonfire&havoc_active |
| 18 | `soul_fire` | target_if=min:(dot.wither.remains+dot.immolate.remains-5*debuff.conflagrate.up+100*debuff.havoc.remains),if=buff.decimation.up&active_dot.immolate<=4 |
| 19 | `infernal_bolt` | if=soul_shard<2.5 |
| 20 | `chaos_bolt` | if=((soul_shard>3.0-(0.1*active_enemies))&!action.rain_of_fire.enabled) |
| 21 | `cataclysm` | if=raid_event.adds.in>15 |
| 22 | `havoc` | target_if=min:((-target.time_to_die)<?-15)+dot.immolate.remains+99*(self.target=target),if=(!cooldown.summon_infernal.up\|!talent.summon_infernal)&target.time_to_die>8&(cooldown.malevolence.remains>15\|!talent.malevolence)\|time<5 |
| 23 | `wither` | target_if=min:dot.wither.remains+99*debuff.havoc.remains,if=dot.wither.refreshable&(!talent.cataclysm.enabled\|cooldown.cataclysm.remains>dot.wither.remains)&(!(talent.raging_demonfire&talent.channel_demonfire)\|cooldown.channel_demonfire.remains>remains\|time<5)&active_dot.wither<=active_enemies&target.time_to_die>18 |
| 24 | `immolate` | target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=dot.immolate.refreshable&(!talent.cataclysm.enabled\|cooldown.cataclysm.remains>dot.immolate.remains)&(!(talent.raging_demonfire&talent.channel_demonfire)\|cooldown.channel_demonfire.remains>remains\|time<5)&active_dot.immolate<=6&target.time_to_die>18 |
| 25 | `call_action_list` | name=ogcd |
| 26 | `summon_infernal` | if=cooldown.invoke_power_infusion_0.up\|cooldown.invoke_power_infusion_0.duration=0\|fight_remains>=120 |
| 27 | `rain_of_fire` | if=debuff.pyrogenics.down&active_enemies<=4&!talent.diabolic_ritual |
| 28 | `channel_demonfire` | if=dot.immolate.remains+dot.wither.remains>cast_time |
| 29 | `immolate` | target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=((dot.immolate.refreshable&(!talent.cataclysm.enabled\|cooldown.cataclysm.remains>dot.immolate.remains))\|active_enemies>active_dot.immolate)&target.time_to_die>10&!havoc_active |
| 30 | `immolate` | target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=((dot.immolate.refreshable&variable.havoc_immo_time<5.4)\|(dot.immolate.remains<2&dot.immolate.remains<havoc_remains)\|!dot.immolate.ticking\|(variable.havoc_immo_time<2)*havoc_active)&(!talent.cataclysm.enabled\|cooldown.cataclysm.remains>dot.immolate.remains)&target.time_to_die>11 |
| 31 | `dimensional_rift` | — |
| 32 | `soul_fire` | target_if=min:(dot.wither.remains+dot.immolate.remains-5*debuff.conflagrate.up+100*debuff.havoc.remains),if=buff.decimation.up |
| 33 | `incinerate` | if=talent.fire_and_brimstone.enabled&buff.backdraft.up |
| 34 | `conflagrate` | if=buff.backdraft.stack<2\|!talent.backdraft |
| 35 | `incinerate` | — |

## Action List: `cleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=items |
| 2 | `call_action_list` | name=ogcd |
| 3 | `call_action_list` | name=havoc,if=havoc_active&havoc_remains>gcd.max |
| 4 | `variable` | name=pool_soul_shards,value=cooldown.havoc.remains<=5\|talent.mayhem |
| 5 | `malevolence` | if=(!cooldown.summon_infernal.up\|!talent.summon_infernal) |
| 6 | `havoc` | target_if=min:((-target.time_to_die)<?-15)+dot.immolate.remains+99*(self.target=target),if=(!cooldown.summon_infernal.up\|!talent.summon_infernal)&target.time_to_die>8 |
| 7 | `chaos_bolt` | if=demonic_art |
| 8 | `soul_fire` | if=buff.decimation.react&(soul_shard<=4\|buff.decimation.remains<=gcd.max*2)&debuff.conflagrate.remains>=execute_time&cooldown.havoc.remains |
| 9 | `wither` | target_if=min:dot.wither.remains+99*debuff.havoc.remains,if=talent.internal_combustion&(((dot.wither.remains-5*action.chaos_bolt.in_flight)<dot.wither.duration*0.4)\|dot.wither.remains<3\|(dot.wither.remains-action.chaos_bolt.execute_time)<5&action.chaos_bolt.usable)&(!talent.soul_fire\|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains-5))&target.time_to_die>8&!action.soul_fire.in_flight_to_target |
| 10 | `wither` | target_if=min:dot.wither.remains+99*debuff.havoc.remains,if=!talent.internal_combustion&(((dot.wither.remains-5*(action.chaos_bolt.in_flight))<dot.wither.duration*0.3)\|dot.wither.remains<3)&(!talent.soul_fire\|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains))&target.time_to_die>8&!action.soul_fire.in_flight_to_target |
| 11 | `conflagrate` | if=(talent.roaring_blaze.enabled&full_recharge_time<=gcd.max*2)\|recharge_time<=8&(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<gcd.max)&!variable.pool_soul_shards |
| 12 | `shadowburn` | if=(cooldown.shadowburn.full_recharge_time<=gcd.max*3\|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight&!talent.diabolic_ritual)&(talent.conflagration_of_chaos\|talent.blistering_atrophy)\|fight_remains<=8 |
| 13 | `shadowburn` | if=cooldown.summon_infernal.remains>=90&talent.rain_of_chaos&!talent.diabolic_ritual |
| 14 | `chaos_bolt` | if=cooldown.summon_infernal.remains>=90&talent.rain_of_chaos |
| 15 | `ruination` | if=(debuff.eradication.remains>=execute_time\|!talent.eradication\|!talent.shadowburn) |
| 16 | `cataclysm` | if=raid_event.adds.in>15 |
| 17 | `channel_demonfire` | if=talent.raging_demonfire&(dot.immolate.remains+dot.wither.remains-5*(action.chaos_bolt.in_flight&talent.internal_combustion))>cast_time |
| 18 | `soul_fire` | if=soul_shard<=3.5&(debuff.conflagrate.remains>cast_time+travel_time\|!talent.roaring_blaze&buff.backdraft.up)&!variable.pool_soul_shards |
| 19 | `immolate` | target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=(dot.immolate.refreshable&(dot.immolate.remains<cooldown.havoc.remains\|!dot.immolate.ticking))&(!talent.cataclysm\|cooldown.cataclysm.remains>remains)&(!talent.soul_fire\|cooldown.soul_fire.remains+(!talent.mayhem*action.soul_fire.cast_time)>dot.immolate.remains)&target.time_to_die>15 |
| 20 | `summon_infernal` | — |
| 21 | `incinerate` | if=talent.diabolic_ritual&(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains-2-!variable.disable_cb_2t*action.chaos_bolt.cast_time-variable.disable_cb_2t*gcd.max)<=0) |
| 22 | `soul_fire` | if=soul_shard<=4&talent.mayhem |
| 23 | `chaos_bolt` | if=(cooldown.summon_infernal.remains>=gcd.max*3\|soul_shard>4\|!talent.rain_of_chaos) |
| 24 | `channel_demonfire` | — |
| 25 | `dimensional_rift` | — |
| 26 | `infernal_bolt` | — |
| 27 | `conflagrate` | if=charges>(max_charges-1)\|fight_remains<gcd.max*charges |
| 28 | `incinerate` | — |

## Action List: `havoc`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `conflagrate` | if=talent.backdraft&buff.backdraft.down&soul_shard>=1&soul_shard<=4 |
| 2 | `soul_fire` | if=cast_time<havoc_remains&soul_shard<2.5 |
| 3 | `cataclysm` | if=raid_event.adds.in>15\|(talent.wither&dot.wither.remains<action.wither.duration*0.3) |
| 4 | `immolate` | target_if=min:dot.immolate.remains+100*debuff.havoc.remains,if=(((dot.immolate.refreshable&variable.havoc_immo_time<5.4)&target.time_to_die>5)\|((dot.immolate.remains<2&dot.immolate.remains<havoc_remains)\|!dot.immolate.ticking\|variable.havoc_immo_time<2)&target.time_to_die>11)&soul_shard<4.5 |
| 5 | `wither` | target_if=min:dot.wither.remains+100*debuff.havoc.remains,if=(((dot.wither.refreshable&variable.havoc_immo_time<5.4)&target.time_to_die>5)\|((dot.wither.remains<2&dot.wither.remains<havoc_remains)\|!dot.wither.ticking\|variable.havoc_immo_time<2)&target.time_to_die>11)&soul_shard<4.5 |
| 6 | `shadowburn` | if=(cooldown.shadowburn.full_recharge_time<=gcd.max*3\|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight)&(talent.conflagration_of_chaos\|talent.blistering_atrophy) |
| 7 | `shadowburn` | if=havoc_remains<=gcd.max*3 |
| 8 | `chaos_bolt` | if=cast_time<havoc_remains&((!talent.improved_chaos_bolt&active_enemies<=2)\|(talent.improved_chaos_bolt&active_enemies<=4)) |
| 9 | `rain_of_fire` | if=active_enemies>=3 |
| 10 | `channel_demonfire` | if=soul_shard<4.5 |
| 11 | `conflagrate` | if=!talent.backdraft |
| 12 | `dimensional_rift` | if=soul_shard<4.7&(charges>2\|fight_remains<cooldown.dimensional_rift.duration) |
| 13 | `incinerate` | if=cast_time<havoc_remains |

## Action List: `items`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=spymasters_web,if=pet.infernal.remains>=10&pet.infernal.remains<=20&buff.spymasters_report.stack>=38&(fight_remains>240\|fight_remains<=140)\|fight_remains<=30 |
| 2 | `use_item` | slot=trinket1,if=(variable.infernal_active\|!talent.summon_infernal\|variable.trinket_1_will_lose_cast)&(variable.trinket_priority=1\|variable.trinket_2_exclude\|!trinket.2.has_cooldown\|(trinket.2.cooldown.remains\|variable.trinket_priority=2&cooldown.summon_infernal.remains>20&!variable.infernal_active&trinket.2.cooldown.remains<cooldown.summon_infernal.remains))&variable.trinket_1_buffs&!variable.trinket_1_manual\|(variable.trinket_1_buff_duration+1>=fight_remains) |
| 3 | `use_item` | slot=trinket2,if=(variable.infernal_active\|!talent.summon_infernal\|variable.trinket_2_will_lose_cast)&(variable.trinket_priority=2\|variable.trinket_1_exclude\|!trinket.1.has_cooldown\|(trinket.1.cooldown.remains\|variable.trinket_priority=1&cooldown.summon_infernal.remains>20&!variable.infernal_active&trinket.1.cooldown.remains<cooldown.summon_infernal.remains))&variable.trinket_2_buffs&!variable.trinket_2_manual\|(variable.trinket_2_buff_duration+1>=fight_remains) |
| 4 | `use_item` | use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&!variable.trinket_1_manual&(!variable.trinket_1_buffs&(trinket.2.cooldown.remains\|!variable.trinket_2_buffs)\|talent.summon_infernal&cooldown.summon_infernal.remains_expected>20&!prev_gcd.1.summon_infernal\|!talent.summon_infernal) |
| 5 | `use_item` | use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&!variable.trinket_2_manual&(!variable.trinket_2_buffs&(trinket.1.cooldown.remains\|!variable.trinket_1_buffs)\|talent.summon_infernal&cooldown.summon_infernal.remains_expected>20&!prev_gcd.1.summon_infernal\|!talent.summon_infernal) |
| 6 | `use_item` | use_off_gcd=1,slot=main_hand |

## Action List: `ogcd`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `potion` | if=variable.infernal_active\|!talent.summon_infernal |
| 2 | `invoke_external_buff` | name=power_infusion,if=variable.infernal_active\|!talent.summon_infernal\|(fight_remains<cooldown.summon_infernal.remains_expected+10+cooldown.invoke_power_infusion_0.duration&fight_remains>cooldown.invoke_power_infusion_0.duration)\|fight_remains<cooldown.summon_infernal.remains_expected+15 |
| 3 | `berserking` | if=variable.infernal_active\|!talent.summon_infernal\|(fight_remains<(cooldown.summon_infernal.remains_expected+cooldown.berserking.duration)&(fight_remains>cooldown.berserking.duration))\|fight_remains<cooldown.summon_infernal.remains_expected |
| 4 | `blood_fury` | if=variable.infernal_active\|!talent.summon_infernal\|(fight_remains<cooldown.summon_infernal.remains_expected+10+cooldown.blood_fury.duration&fight_remains>cooldown.blood_fury.duration)\|fight_remains<cooldown.summon_infernal.remains |
| 5 | `fireblood` | if=variable.infernal_active\|!talent.summon_infernal\|(fight_remains<cooldown.summon_infernal.remains_expected+10+cooldown.fireblood.duration&fight_remains>cooldown.fireblood.duration)\|fight_remains<cooldown.summon_infernal.remains_expected |
| 6 | `ancestral_call` | if=variable.infernal_active\|!talent.summon_infernal\|(fight_remains<(cooldown.summon_infernal.remains_expected+cooldown.berserking.duration)&(fight_remains>cooldown.berserking.duration))\|fight_remains<cooldown.summon_infernal.remains_expected |

## Action List: `variables`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=havoc_immo_time,op=reset |
| 2 | `variable` | name=pooling_condition,value=(soul_shard>=3\|(talent.secrets_of_the_coven&buff.infernal_bolt.up\|buff.decimation.up)&soul_shard>=3),default=1,op=set |
| 3 | `variable` | name=pooling_condition_cb,value=variable.pooling_condition\|pet.infernal.active&soul_shard>=3,default=1,op=set |
| 4 | `cycling_variable` | name=havoc_immo_time,op=add,value=dot.immolate.remains*debuff.havoc.up<?dot.wither.remains*debuff.havoc.up |
| 5 | `variable` | name=infernal_active,op=set,value=pet.infernal.active\|(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains)<20 |
| 6 | `variable` | name=trinket_1_will_lose_cast,value=((floor((fight_remains%trinket.1.cooldown.duration)+1)!=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(floor((fight_remains%trinket.1.cooldown.duration)+1))!=(floor(((fight_remains-cooldown.summon_infernal.remains)%trinket.1.cooldown.duration)+1))\|((floor((fight_remains%trinket.1.cooldown.duration)+1)=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(((fight_remains-cooldown.summon_infernal.remains%%trinket.1.cooldown.duration)-cooldown.summon_infernal.remains-variable.trinket_1_buff_duration)>0)))&cooldown.summon_infernal.remains>20 |
| 7 | `variable` | name=trinket_2_will_lose_cast,value=((floor((fight_remains%trinket.2.cooldown.duration)+1)!=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(floor((fight_remains%trinket.2.cooldown.duration)+1))!=(floor(((fight_remains-cooldown.summon_infernal.remains)%trinket.2.cooldown.duration)+1))\|((floor((fight_remains%trinket.2.cooldown.duration)+1)=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(((fight_remains-cooldown.summon_infernal.remains%%trinket.2.cooldown.duration)-cooldown.summon_infernal.remains-variable.trinket_2_buff_duration)>0)))&cooldown.summon_infernal.remains>20 |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=summon_pet
actions.precombat+=/variable,name=cleave_apl,default=0,op=reset
# Automatic Logic for Buff Trinkets in Trinket Slot 1
actions.precombat+=/variable,name=trinket_1_buffs,value=trinket.1.has_use_buff|trinket.1.is.funhouse_lens
# Automatic Logic for Buff Trinkets in Trinket Slot 2
actions.precombat+=/variable,name=trinket_2_buffs,value=trinket.2.has_use_buff|trinket.2.is.funhouse_lens
actions.precombat+=/variable,name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&(trinket.1.cooldown.duration%%cooldown.summon_infernal.duration=0|cooldown.summon_infernal.duration%%trinket.1.cooldown.duration=0)
actions.precombat+=/variable,name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&(trinket.2.cooldown.duration%%cooldown.summon_infernal.duration=0|cooldown.summon_infernal.duration%%trinket.2.cooldown.duration=0)
# Sets a specific Trinkets in Slot 1 to follow an APL line and not the automatic logic
actions.precombat+=/variable,name=trinket_1_manual,value=trinket.1.is.spymasters_web
# Sets a specific Trinkets in Slot 2 to follow an APL line and not the automatic logic
actions.precombat+=/variable,name=trinket_2_manual,value=trinket.2.is.spymasters_web
# For On Use Trinkets on slot 1 with on use effects you dont want to use in combat
actions.precombat+=/variable,name=trinket_1_exclude,value=trinket.1.is.whispering_incarnate_icon
# For On Use Trinkets on slot 2 with on use effects you dont want to use in combat
actions.precombat+=/variable,name=trinket_2_exclude,value=trinket.2.is.whispering_incarnate_icon
# Sets the duration of the trinket in the automatic logic
actions.precombat+=/variable,name=trinket_1_buff_duration,value=trinket.1.proc.any_dps.duration+(trinket.1.is.funhouse_lens*15)+(trinket.1.is.signet_of_the_priory*20)
# Sets the duration of the trinket in the automatic logic
actions.precombat+=/variable,name=trinket_2_buff_duration,value=trinket.2.proc.any_dps.duration+(trinket.2.is.funhouse_lens*15)+(trinket.2.is.signet_of_the_priory*20)
# Automatic Logic in case both Trinkets are on use buffs
actions.precombat+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs|variable.trinket_2_buffs&((trinket.2.cooldown.duration%variable.trinket_2_buff_duration)*(1+0.5*trinket.2.has_buff.intellect)*(variable.trinket_2_sync))>((trinket.1.cooldown.duration%variable.trinket_1_buff_duration)*(1+0.5*trinket.1.has_buff.intellect)*(variable.trinket_1_sync))
actions.precombat+=/variable,name=allow_rof_2t_spender,default=2,op=reset
actions.precombat+=/variable,name=do_rof_2t,value=variable.allow_rof_2t_spender>1.99&!(talent.cataclysm&talent.improved_chaos_bolt),op=set
actions.precombat+=/variable,name=disable_cb_2t,value=variable.do_rof_2t|variable.allow_rof_2t_spender>0.01&variable.allow_rof_2t_spender<0.99
actions.precombat+=/grimoire_of_sacrifice,if=talent.grimoire_of_sacrifice.enabled
actions.precombat+=/snapshot_stats
actions.precombat+=/cataclysm,if=active_enemies>=2&raid_event.adds.in>15
actions.precombat+=/soul_fire
actions.precombat+=/incinerate

# Executed every time the actor is available.
actions=call_action_list,name=variables
actions+=/call_action_list,name=aoe,if=(active_enemies>=3)&!variable.cleave_apl
actions+=/call_action_list,name=cleave,if=active_enemies!=1|variable.cleave_apl
actions+=/call_action_list,name=ogcd
actions+=/call_action_list,name=items
actions+=/malevolence,if=cooldown.summon_infernal.remains>=55
actions+=/summon_infernal,if=demonic_art
actions+=/chaos_bolt,if=talent.diabolic_ritual&(demonic_art|((buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<(action.chaos_bolt.execute_time)))
actions+=/soul_fire,if=buff.decimation.react&(soul_shard<=4|buff.decimation.remains<=gcd.max*2)&debuff.conflagrate.remains>=execute_time
actions+=/wither,if=talent.internal_combustion&(((dot.wither.remains-5*action.chaos_bolt.in_flight)<dot.wither.duration*0.4)|dot.wither.remains<3|(dot.wither.remains-action.chaos_bolt.execute_time)<5&action.chaos_bolt.usable)&(!talent.soul_fire|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains-5))&target.time_to_die>8&!action.soul_fire.in_flight_to_target
actions+=/conflagrate,if=talent.roaring_blaze&debuff.conflagrate.remains<1.5|full_recharge_time<=gcd.max*2|recharge_time<=8&(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<gcd.max)&soul_shard>=1.5
actions+=/shadowburn,if=talent.wither&((cooldown.shadowburn.full_recharge_time<=gcd.max*3|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight&!talent.diabolic_ritual)&(talent.conflagration_of_chaos|talent.blistering_atrophy)|fight_remains<=8)
actions+=/shadowburn,if=(cooldown.summon_infernal.remains>=90&talent.rain_of_chaos)|buff.malevolence.up
actions+=/chaos_bolt,if=(cooldown.summon_infernal.remains>=90&talent.rain_of_chaos)|buff.malevolence.up
actions+=/ruination
actions+=/cataclysm,if=raid_event.adds.in>15&(talent.wither&dot.wither.refreshable)
actions+=/channel_demonfire,if=talent.raging_demonfire&(dot.immolate.remains+dot.wither.remains-5*(action.chaos_bolt.in_flight&talent.internal_combustion))>cast_time
actions+=/wither,if=!talent.internal_combustion&(((dot.wither.remains-5*(action.chaos_bolt.in_flight))<dot.wither.duration*0.3)|dot.wither.remains<3)&(!talent.cataclysm|cooldown.cataclysm.remains>dot.wither.remains)&(!talent.soul_fire|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains))&target.time_to_die>8&!action.soul_fire.in_flight_to_target
actions+=/immolate,if=(((dot.immolate.remains-5*(action.chaos_bolt.in_flight&talent.internal_combustion))<dot.immolate.duration*0.3)|dot.immolate.remains<3|(dot.immolate.remains-action.chaos_bolt.execute_time)<5&talent.internal_combustion&action.chaos_bolt.usable)&(!talent.soul_fire|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.immolate.remains-5*talent.internal_combustion))&target.time_to_die>8&!action.soul_fire.in_flight_to_target
actions+=/summon_infernal
actions+=/chaos_bolt,if=(variable.pooling_condition_cb&(cooldown.summon_infernal.remains>=gcd.max*3|soul_shard>4))&(talent.wither|((buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)>(action.chaos_bolt.execute_time+2*gcd.max)))
actions+=/channel_demonfire
actions+=/dimensional_rift
actions+=/infernal_bolt,if=soul_shard<=3
actions+=/conflagrate,if=charges>(max_charges-1)|fight_remains<gcd.max*charges
actions+=/incinerate

actions.aoe=call_action_list,name=ogcd
actions.aoe+=/call_action_list,name=items
actions.aoe+=/malevolence,if=cooldown.summon_infernal.remains>=55&soul_shard<4.7&(active_enemies<=3+active_dot.wither|time>30)
actions.aoe+=/chaos_bolt,if=talent.diabolic_ritual&(((buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<(action.chaos_bolt.execute_time)&active_enemies<=9)|(demonic_art&active_enemies<=7))
actions.aoe+=/call_action_list,name=havoc,if=havoc_active&havoc_remains>gcd.max&active_enemies<=4&talent.wither
actions.aoe+=/dimensional_rift,if=soul_shard<4.7&(charges>2|fight_remains<cooldown.dimensional_rift.duration)
actions.aoe+=/incinerate,if=(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<=action.incinerate.cast_time)
actions.aoe+=/rain_of_fire,if=(soul_shard>=(3.5-0.1*(active_dot.immolate+active_dot.wither))|buff.ritual_of_ruin.up)&(talent.wither|(talent.diabolic_ritual&active_enemies>=8))
actions.aoe+=/chaos_bolt,if=soul_shard>=((3.0-0.1*(active_dot.immolate))|buff.ritual_of_ruin.up)&talent.diabolic_ritual&active_enemies<=7
actions.aoe+=/wither,target_if=min:dot.wither.remains+99*debuff.havoc.remains+99*!dot.wither.ticking,if=dot.wither.refreshable&(!talent.cataclysm.enabled|cooldown.cataclysm.remains>dot.wither.remains)&(!(talent.raging_demonfire&talent.channel_demonfire)|cooldown.channel_demonfire.remains>remains|time<5)&(active_dot.wither<=4|time>15)&target.time_to_die>18
actions.aoe+=/channel_demonfire,if=dot.immolate.remains+dot.wither.remains>cast_time&talent.raging_demonfire
actions.aoe+=/shadowburn,if=talent.wither&(buff.malevolence.up|active_enemies<=6|(fight_remains>60&active_enemies<=14))&((cooldown.shadowburn.full_recharge_time<=gcd.max*3|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight)|fight_remains<=8)
actions.aoe+=/shadowburn,target_if=min:time_to_die,if=talent.wither&(buff.malevolence.up|active_enemies<=6|(fight_remains>60&active_enemies<=14))&((cooldown.shadowburn.full_recharge_time<=gcd.max*3|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight)|fight_remains<=8)
actions.aoe+=/ruination
actions.aoe+=/rain_of_fire,if=pet.infernal.active&talent.rain_of_chaos&(talent.wither|(talent.diabolic_ritual&active_enemies>=8))
actions.aoe+=/chaos_bolt,if=pet.infernal.active&talent.rain_of_chaos&talent.diabolic_ritual&active_enemies<=7
actions.aoe+=/soul_fire,target_if=min:dot.wither.remains+dot.immolate.remains-5*debuff.conflagrate.up+100*debuff.havoc.remains,if=(buff.decimation.up)&!talent.raging_demonfire&havoc_active
actions.aoe+=/soul_fire,target_if=min:(dot.wither.remains+dot.immolate.remains-5*debuff.conflagrate.up+100*debuff.havoc.remains),if=buff.decimation.up&active_dot.immolate<=4
actions.aoe+=/infernal_bolt,if=soul_shard<2.5
actions.aoe+=/chaos_bolt,if=((soul_shard>3.0-(0.1*active_enemies))&!action.rain_of_fire.enabled)
actions.aoe+=/cataclysm,if=raid_event.adds.in>15
actions.aoe+=/havoc,target_if=min:((-target.time_to_die)<?-15)+dot.immolate.remains+99*(self.target=target),if=(!cooldown.summon_infernal.up|!talent.summon_infernal)&target.time_to_die>8&(cooldown.malevolence.remains>15|!talent.malevolence)|time<5
actions.aoe+=/wither,target_if=min:dot.wither.remains+99*debuff.havoc.remains,if=dot.wither.refreshable&(!talent.cataclysm.enabled|cooldown.cataclysm.remains>dot.wither.remains)&(!(talent.raging_demonfire&talent.channel_demonfire)|cooldown.channel_demonfire.remains>remains|time<5)&active_dot.wither<=active_enemies&target.time_to_die>18
actions.aoe+=/immolate,target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=dot.immolate.refreshable&(!talent.cataclysm.enabled|cooldown.cataclysm.remains>dot.immolate.remains)&(!(talent.raging_demonfire&talent.channel_demonfire)|cooldown.channel_demonfire.remains>remains|time<5)&active_dot.immolate<=6&target.time_to_die>18
actions.aoe+=/call_action_list,name=ogcd
actions.aoe+=/summon_infernal,if=cooldown.invoke_power_infusion_0.up|cooldown.invoke_power_infusion_0.duration=0|fight_remains>=120
actions.aoe+=/rain_of_fire,if=debuff.pyrogenics.down&active_enemies<=4&!talent.diabolic_ritual
actions.aoe+=/channel_demonfire,if=dot.immolate.remains+dot.wither.remains>cast_time
actions.aoe+=/immolate,target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=((dot.immolate.refreshable&(!talent.cataclysm.enabled|cooldown.cataclysm.remains>dot.immolate.remains))|active_enemies>active_dot.immolate)&target.time_to_die>10&!havoc_active
actions.aoe+=/immolate,target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=((dot.immolate.refreshable&variable.havoc_immo_time<5.4)|(dot.immolate.remains<2&dot.immolate.remains<havoc_remains)|!dot.immolate.ticking|(variable.havoc_immo_time<2)*havoc_active)&(!talent.cataclysm.enabled|cooldown.cataclysm.remains>dot.immolate.remains)&target.time_to_die>11
actions.aoe+=/dimensional_rift
actions.aoe+=/soul_fire,target_if=min:(dot.wither.remains+dot.immolate.remains-5*debuff.conflagrate.up+100*debuff.havoc.remains),if=buff.decimation.up
actions.aoe+=/incinerate,if=talent.fire_and_brimstone.enabled&buff.backdraft.up
actions.aoe+=/conflagrate,if=buff.backdraft.stack<2|!talent.backdraft
actions.aoe+=/incinerate

actions.cleave=call_action_list,name=items
actions.cleave+=/call_action_list,name=ogcd
actions.cleave+=/call_action_list,name=havoc,if=havoc_active&havoc_remains>gcd.max
actions.cleave+=/variable,name=pool_soul_shards,value=cooldown.havoc.remains<=5|talent.mayhem
actions.cleave+=/malevolence,if=(!cooldown.summon_infernal.up|!talent.summon_infernal)
actions.cleave+=/havoc,target_if=min:((-target.time_to_die)<?-15)+dot.immolate.remains+99*(self.target=target),if=(!cooldown.summon_infernal.up|!talent.summon_infernal)&target.time_to_die>8
actions.cleave+=/chaos_bolt,if=demonic_art
actions.cleave+=/soul_fire,if=buff.decimation.react&(soul_shard<=4|buff.decimation.remains<=gcd.max*2)&debuff.conflagrate.remains>=execute_time&cooldown.havoc.remains
actions.cleave+=/wither,target_if=min:dot.wither.remains+99*debuff.havoc.remains,if=talent.internal_combustion&(((dot.wither.remains-5*action.chaos_bolt.in_flight)<dot.wither.duration*0.4)|dot.wither.remains<3|(dot.wither.remains-action.chaos_bolt.execute_time)<5&action.chaos_bolt.usable)&(!talent.soul_fire|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains-5))&target.time_to_die>8&!action.soul_fire.in_flight_to_target
actions.cleave+=/wither,target_if=min:dot.wither.remains+99*debuff.havoc.remains,if=!talent.internal_combustion&(((dot.wither.remains-5*(action.chaos_bolt.in_flight))<dot.wither.duration*0.3)|dot.wither.remains<3)&(!talent.soul_fire|cooldown.soul_fire.remains+action.soul_fire.cast_time>(dot.wither.remains))&target.time_to_die>8&!action.soul_fire.in_flight_to_target
actions.cleave+=/conflagrate,if=(talent.roaring_blaze.enabled&full_recharge_time<=gcd.max*2)|recharge_time<=8&(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains)<gcd.max)&!variable.pool_soul_shards
actions.cleave+=/shadowburn,if=(cooldown.shadowburn.full_recharge_time<=gcd.max*3|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight&!talent.diabolic_ritual)&(talent.conflagration_of_chaos|talent.blistering_atrophy)|fight_remains<=8
actions.cleave+=/shadowburn,if=cooldown.summon_infernal.remains>=90&talent.rain_of_chaos&!talent.diabolic_ritual
actions.cleave+=/chaos_bolt,if=cooldown.summon_infernal.remains>=90&talent.rain_of_chaos
actions.cleave+=/ruination,if=(debuff.eradication.remains>=execute_time|!talent.eradication|!talent.shadowburn)
actions.cleave+=/cataclysm,if=raid_event.adds.in>15
actions.cleave+=/channel_demonfire,if=talent.raging_demonfire&(dot.immolate.remains+dot.wither.remains-5*(action.chaos_bolt.in_flight&talent.internal_combustion))>cast_time
actions.cleave+=/soul_fire,if=soul_shard<=3.5&(debuff.conflagrate.remains>cast_time+travel_time|!talent.roaring_blaze&buff.backdraft.up)&!variable.pool_soul_shards
actions.cleave+=/immolate,target_if=min:dot.immolate.remains+99*debuff.havoc.remains,if=(dot.immolate.refreshable&(dot.immolate.remains<cooldown.havoc.remains|!dot.immolate.ticking))&(!talent.cataclysm|cooldown.cataclysm.remains>remains)&(!talent.soul_fire|cooldown.soul_fire.remains+(!talent.mayhem*action.soul_fire.cast_time)>dot.immolate.remains)&target.time_to_die>15
actions.cleave+=/summon_infernal
actions.cleave+=/incinerate,if=talent.diabolic_ritual&(diabolic_ritual&(buff.diabolic_ritual_mother_of_chaos.remains+buff.diabolic_ritual_overlord.remains+buff.diabolic_ritual_pit_lord.remains-2-!variable.disable_cb_2t*action.chaos_bolt.cast_time-variable.disable_cb_2t*gcd.max)<=0)
actions.cleave+=/soul_fire,if=soul_shard<=4&talent.mayhem
actions.cleave+=/chaos_bolt,if=(cooldown.summon_infernal.remains>=gcd.max*3|soul_shard>4|!talent.rain_of_chaos)
actions.cleave+=/channel_demonfire
actions.cleave+=/dimensional_rift
actions.cleave+=/infernal_bolt
actions.cleave+=/conflagrate,if=charges>(max_charges-1)|fight_remains<gcd.max*charges
actions.cleave+=/incinerate

actions.havoc=conflagrate,if=talent.backdraft&buff.backdraft.down&soul_shard>=1&soul_shard<=4
actions.havoc+=/soul_fire,if=cast_time<havoc_remains&soul_shard<2.5
actions.havoc+=/cataclysm,if=raid_event.adds.in>15|(talent.wither&dot.wither.remains<action.wither.duration*0.3)
actions.havoc+=/immolate,target_if=min:dot.immolate.remains+100*debuff.havoc.remains,if=(((dot.immolate.refreshable&variable.havoc_immo_time<5.4)&target.time_to_die>5)|((dot.immolate.remains<2&dot.immolate.remains<havoc_remains)|!dot.immolate.ticking|variable.havoc_immo_time<2)&target.time_to_die>11)&soul_shard<4.5
actions.havoc+=/wither,target_if=min:dot.wither.remains+100*debuff.havoc.remains,if=(((dot.wither.refreshable&variable.havoc_immo_time<5.4)&target.time_to_die>5)|((dot.wither.remains<2&dot.wither.remains<havoc_remains)|!dot.wither.ticking|variable.havoc_immo_time<2)&target.time_to_die>11)&soul_shard<4.5
actions.havoc+=/shadowburn,if=(cooldown.shadowburn.full_recharge_time<=gcd.max*3|debuff.eradication.remains<=gcd.max&talent.eradication&!action.chaos_bolt.in_flight)&(talent.conflagration_of_chaos|talent.blistering_atrophy)
actions.havoc+=/shadowburn,if=havoc_remains<=gcd.max*3
actions.havoc+=/chaos_bolt,if=cast_time<havoc_remains&((!talent.improved_chaos_bolt&active_enemies<=2)|(talent.improved_chaos_bolt&active_enemies<=4))
actions.havoc+=/rain_of_fire,if=active_enemies>=3
actions.havoc+=/channel_demonfire,if=soul_shard<4.5
actions.havoc+=/conflagrate,if=!talent.backdraft
actions.havoc+=/dimensional_rift,if=soul_shard<4.7&(charges>2|fight_remains<cooldown.dimensional_rift.duration)
actions.havoc+=/incinerate,if=cast_time<havoc_remains

actions.items=use_item,name=spymasters_web,if=pet.infernal.remains>=10&pet.infernal.remains<=20&buff.spymasters_report.stack>=38&(fight_remains>240|fight_remains<=140)|fight_remains<=30
actions.items+=/use_item,slot=trinket1,if=(variable.infernal_active|!talent.summon_infernal|variable.trinket_1_will_lose_cast)&(variable.trinket_priority=1|variable.trinket_2_exclude|!trinket.2.has_cooldown|(trinket.2.cooldown.remains|variable.trinket_priority=2&cooldown.summon_infernal.remains>20&!variable.infernal_active&trinket.2.cooldown.remains<cooldown.summon_infernal.remains))&variable.trinket_1_buffs&!variable.trinket_1_manual|(variable.trinket_1_buff_duration+1>=fight_remains)
actions.items+=/use_item,slot=trinket2,if=(variable.infernal_active|!talent.summon_infernal|variable.trinket_2_will_lose_cast)&(variable.trinket_priority=2|variable.trinket_1_exclude|!trinket.1.has_cooldown|(trinket.1.cooldown.remains|variable.trinket_priority=1&cooldown.summon_infernal.remains>20&!variable.infernal_active&trinket.1.cooldown.remains<cooldown.summon_infernal.remains))&variable.trinket_2_buffs&!variable.trinket_2_manual|(variable.trinket_2_buff_duration+1>=fight_remains)
actions.items+=/use_item,use_off_gcd=1,slot=trinket1,if=!variable.trinket_1_buffs&!variable.trinket_1_manual&(!variable.trinket_1_buffs&(trinket.2.cooldown.remains|!variable.trinket_2_buffs)|talent.summon_infernal&cooldown.summon_infernal.remains_expected>20&!prev_gcd.1.summon_infernal|!talent.summon_infernal)
actions.items+=/use_item,use_off_gcd=1,slot=trinket2,if=!variable.trinket_2_buffs&!variable.trinket_2_manual&(!variable.trinket_2_buffs&(trinket.1.cooldown.remains|!variable.trinket_1_buffs)|talent.summon_infernal&cooldown.summon_infernal.remains_expected>20&!prev_gcd.1.summon_infernal|!talent.summon_infernal)
actions.items+=/use_item,use_off_gcd=1,slot=main_hand

actions.ogcd=potion,if=variable.infernal_active|!talent.summon_infernal
actions.ogcd+=/invoke_external_buff,name=power_infusion,if=variable.infernal_active|!talent.summon_infernal|(fight_remains<cooldown.summon_infernal.remains_expected+10+cooldown.invoke_power_infusion_0.duration&fight_remains>cooldown.invoke_power_infusion_0.duration)|fight_remains<cooldown.summon_infernal.remains_expected+15
actions.ogcd+=/berserking,if=variable.infernal_active|!talent.summon_infernal|(fight_remains<(cooldown.summon_infernal.remains_expected+cooldown.berserking.duration)&(fight_remains>cooldown.berserking.duration))|fight_remains<cooldown.summon_infernal.remains_expected
actions.ogcd+=/blood_fury,if=variable.infernal_active|!talent.summon_infernal|(fight_remains<cooldown.summon_infernal.remains_expected+10+cooldown.blood_fury.duration&fight_remains>cooldown.blood_fury.duration)|fight_remains<cooldown.summon_infernal.remains
actions.ogcd+=/fireblood,if=variable.infernal_active|!talent.summon_infernal|(fight_remains<cooldown.summon_infernal.remains_expected+10+cooldown.fireblood.duration&fight_remains>cooldown.fireblood.duration)|fight_remains<cooldown.summon_infernal.remains_expected
actions.ogcd+=/ancestral_call,if=variable.infernal_active|!talent.summon_infernal|(fight_remains<(cooldown.summon_infernal.remains_expected+cooldown.berserking.duration)&(fight_remains>cooldown.berserking.duration))|fight_remains<cooldown.summon_infernal.remains_expected

actions.variables=variable,name=havoc_immo_time,op=reset
actions.variables+=/variable,name=pooling_condition,value=(soul_shard>=3|(talent.secrets_of_the_coven&buff.infernal_bolt.up|buff.decimation.up)&soul_shard>=3),default=1,op=set
actions.variables+=/variable,name=pooling_condition_cb,value=variable.pooling_condition|pet.infernal.active&soul_shard>=3,default=1,op=set
actions.variables+=/cycling_variable,name=havoc_immo_time,op=add,value=dot.immolate.remains*debuff.havoc.up<?dot.wither.remains*debuff.havoc.up
actions.variables+=/variable,name=infernal_active,op=set,value=pet.infernal.active|(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains)<20
actions.variables+=/variable,name=trinket_1_will_lose_cast,value=((floor((fight_remains%trinket.1.cooldown.duration)+1)!=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(floor((fight_remains%trinket.1.cooldown.duration)+1))!=(floor(((fight_remains-cooldown.summon_infernal.remains)%trinket.1.cooldown.duration)+1))|((floor((fight_remains%trinket.1.cooldown.duration)+1)=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(((fight_remains-cooldown.summon_infernal.remains%%trinket.1.cooldown.duration)-cooldown.summon_infernal.remains-variable.trinket_1_buff_duration)>0)))&cooldown.summon_infernal.remains>20
actions.variables+=/variable,name=trinket_2_will_lose_cast,value=((floor((fight_remains%trinket.2.cooldown.duration)+1)!=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(floor((fight_remains%trinket.2.cooldown.duration)+1))!=(floor(((fight_remains-cooldown.summon_infernal.remains)%trinket.2.cooldown.duration)+1))|((floor((fight_remains%trinket.2.cooldown.duration)+1)=floor((fight_remains+(cooldown.summon_infernal.duration-cooldown.summon_infernal.remains))%cooldown.summon_infernal.duration))&(((fight_remains-cooldown.summon_infernal.remains%%trinket.2.cooldown.duration)-cooldown.summon_infernal.remains-variable.trinket_2_buff_duration)>0)))&cooldown.summon_infernal.remains>20
```
