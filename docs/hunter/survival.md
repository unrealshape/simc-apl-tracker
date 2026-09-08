# Hunter – Survival

Auto-generated from SimulationCraft APL | Last updated: 2026-09-08 07:58 UTC

Source: `apl/default/hunter/survival.simc`

---

## Overview

- **Action Lists:** 7
- **Total Actions:** 60
- **Lists:** `precombat`, `default`, `cds`, `plcleave`, `plst`, `sentcleave`, `sentst`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `summon_pet` | — |
| 2 | `snapshot_stats` | — |
| 3 | `use_item` | name=algethar_puzzle_box |
| 4 | `wildfire_bomb` | if=active_enemies=1 |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `retarget` | target_if=max:target.health,line_cd=5,if=fight_style.dungeonroute |
| 2 | `auto_attack` | — |
| 3 | `call_action_list` | name=cds |
| 4 | `call_action_list` | name=plst,if=active_enemies<3&talent.howl_of_the_pack_leader |
| 5 | `call_action_list` | name=plcleave,if=active_enemies>2&talent.howl_of_the_pack_leader |
| 6 | `call_action_list` | name=sentst,if=active_enemies<3&!talent.howl_of_the_pack_leader |
| 7 | `call_action_list` | name=sentcleave,if=active_enemies>2&!talent.howl_of_the_pack_leader |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blood_fury` | if=buff.takedown.up\|cooldown.takedown.ready |
| 2 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage |
| 3 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&talent.takedown&!other_trinket.has_use_buff&this_trinket.cooldown.duration>=cooldown.takedown.duration*2&this_trinket.has_buff.haste&(buff.takedown.up\|cooldown.takedown.remains>this_trinket.cooldown.duration*0.45) |
| 4 | `use_items` | check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(!talent.takedown\|other_trinket.has_use_buff\|this_trinket.cooldown.duration<cooldown.takedown.duration*2\|!this_trinket.has_buff.haste)&(buff.takedown.up\|cooldown.takedown.ready\|cooldown.takedown.remains>20\|!talent.takedown) |
| 5 | `use_item` | name=algethar_puzzle_box,if=cooldown.takedown.remains<5\|!talent.takedown |
| 6 | `invoke_external_buff` | name=power_infusion,if=buff.takedown.up&!buff.power_infusion.up |
| 7 | `ancestral_call` | if=buff.takedown.up\|cooldown.takedown.ready |
| 8 | `fireblood` | if=buff.takedown.up\|cooldown.takedown.ready |
| 9 | `berserking` | if=buff.takedown.up\|cooldown.takedown.ready |
| 10 | `muzzle` | — |
| 11 | `potion` | if=target.time_to_die<25\|cooldown.takedown.ready |
| 12 | `aspect_of_the_eagle` | if=target.distance>=6 |

## Action List: `plcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack<2&(buff.howl_of_the_pack_leader_wyvern.remains\|buff.howl_of_the_pack_leader_boar.remains\|buff.howl_of_the_pack_leader_bear.remains) |
| 2 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 3 | `takedown` | if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 4 | `wildfire_bomb` | if=full_recharge_time<gcd |
| 5 | `boomstick` | if=buff.tip_of_the_spear.up |
| 6 | `wildfire_bomb` | if=buff.tip_of_the_spear.up |
| 7 | `raptor_strike` | if=buff.tip_of_the_spear.up\|!buff.raptor_swipe.up |
| 8 | `kill_command` | if=cooldown.takedown.remains |
| 9 | `wildfire_bomb` | — |
| 10 | `takedown` | — |

## Action List: `plst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack<2&howl_summon.ready |
| 2 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 3 | `takedown` | if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 4 | `wildfire_bomb` | if=buff.tip_of_the_spear.up&(talent.lethal_calibration&full_recharge_time<4+gcd\|!talent.lethal_calibration) |
| 5 | `boomstick` | if=buff.tip_of_the_spear.up |
| 6 | `raptor_strike` | if=(buff.tip_of_the_spear.up\|!buff.raptor_swipe.up) |
| 7 | `wildfire_bomb` | if=buff.tip_of_the_spear.up |
| 8 | `kill_command` | if=cooldown.takedown.remains |
| 9 | `takedown` | — |

## Action List: `sentcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains\|!talent.twin_fangs) |
| 2 | `boomstick` | if=buff.tip_of_the_spear.up |
| 3 | `wildfire_bomb` | target_if=max:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up |
| 4 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 5 | `takedown` | target_if=min:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 6 | `moonlight_chakram` | target_if=min:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up |
| 7 | `raptor_strike` | target_if=min:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up&buff.raptor_swipe.up\|!buff.raptor_swipe.up |
| 8 | `kill_command` | — |

## Action List: `sentst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains\|!talent.twin_fangs) |
| 2 | `boomstick` | — |
| 3 | `wildfire_bomb` | if=buff.tip_of_the_spear.up&(debuff.sentinels_mark.remains\|full_recharge_time<4) |
| 4 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 5 | `takedown` | if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 6 | `moonlight_chakram` | — |
| 7 | `raptor_strike` | — |
| 8 | `kill_command` | if=cooldown.takedown.remains |
| 9 | `wildfire_bomb` | — |
| 10 | `takedown` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=summon_pet
# Snapshot raid buffed stats before combat begins.
actions.precombat+=/snapshot_stats
actions.precombat+=/use_item,name=algethar_puzzle_box
actions.precombat+=/wildfire_bomb,if=active_enemies=1

# Executed every time the actor is available.
actions=retarget,target_if=max:target.health,line_cd=5,if=fight_style.dungeonroute
actions+=/auto_attack
actions+=/call_action_list,name=cds
actions+=/call_action_list,name=plst,if=active_enemies<3&talent.howl_of_the_pack_leader
actions+=/call_action_list,name=plcleave,if=active_enemies>2&talent.howl_of_the_pack_leader
actions+=/call_action_list,name=sentst,if=active_enemies<3&!talent.howl_of_the_pack_leader
actions+=/call_action_list,name=sentcleave,if=active_enemies>2&!talent.howl_of_the_pack_leader

# CDS
actions.cds=blood_fury,if=buff.takedown.up|cooldown.takedown.ready
actions.cds+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage
actions.cds+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&talent.takedown&!other_trinket.has_use_buff&this_trinket.cooldown.duration>=cooldown.takedown.duration*2&this_trinket.has_buff.haste&(buff.takedown.up|cooldown.takedown.remains>this_trinket.cooldown.duration*0.45)
actions.cds+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_buff&(!talent.takedown|other_trinket.has_use_buff|this_trinket.cooldown.duration<cooldown.takedown.duration*2|!this_trinket.has_buff.haste)&(buff.takedown.up|cooldown.takedown.ready|cooldown.takedown.remains>20|!talent.takedown)
actions.cds+=/use_item,name=algethar_puzzle_box,if=cooldown.takedown.remains<5|!talent.takedown
actions.cds+=/invoke_external_buff,name=power_infusion,if=buff.takedown.up&!buff.power_infusion.up
actions.cds+=/ancestral_call,if=buff.takedown.up|cooldown.takedown.ready
actions.cds+=/fireblood,if=buff.takedown.up|cooldown.takedown.ready
actions.cds+=/berserking,if=buff.takedown.up|cooldown.takedown.ready
actions.cds+=/muzzle
actions.cds+=/potion,if=target.time_to_die<25|cooldown.takedown.ready
actions.cds+=/aspect_of_the_eagle,if=target.distance>=6

# AOE - PL
actions.plcleave=kill_command,if=buff.tip_of_the_spear.stack<2&(buff.howl_of_the_pack_leader_wyvern.remains|buff.howl_of_the_pack_leader_boar.remains|buff.howl_of_the_pack_leader_bear.remains)
actions.plcleave+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.plcleave+=/takedown,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs
actions.plcleave+=/wildfire_bomb,if=full_recharge_time<gcd
actions.plcleave+=/boomstick,if=buff.tip_of_the_spear.up
actions.plcleave+=/wildfire_bomb,if=buff.tip_of_the_spear.up
actions.plcleave+=/raptor_strike,if=buff.tip_of_the_spear.up|!buff.raptor_swipe.up
actions.plcleave+=/kill_command,if=cooldown.takedown.remains
actions.plcleave+=/wildfire_bomb
actions.plcleave+=/takedown

# ST - PL
actions.plst=kill_command,if=buff.tip_of_the_spear.stack<2&howl_summon.ready
actions.plst+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.plst+=/takedown,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs
actions.plst+=/wildfire_bomb,if=buff.tip_of_the_spear.up&(talent.lethal_calibration&full_recharge_time<4+gcd|!talent.lethal_calibration)
actions.plst+=/boomstick,if=buff.tip_of_the_spear.up
actions.plst+=/raptor_strike,if=(buff.tip_of_the_spear.up|!buff.raptor_swipe.up)
actions.plst+=/wildfire_bomb,if=buff.tip_of_the_spear.up
actions.plst+=/kill_command,if=cooldown.takedown.remains
actions.plst+=/takedown

# AOE - Sent
actions.sentcleave=kill_command,if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains|!talent.twin_fangs)
actions.sentcleave+=/boomstick,if=buff.tip_of_the_spear.up
actions.sentcleave+=/wildfire_bomb,target_if=max:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up
actions.sentcleave+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.sentcleave+=/takedown,target_if=min:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs
actions.sentcleave+=/moonlight_chakram,target_if=min:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up
actions.sentcleave+=/raptor_strike,target_if=min:debuff.sentinels_mark.remains,if=buff.tip_of_the_spear.up&buff.raptor_swipe.up|!buff.raptor_swipe.up
actions.sentcleave+=/kill_command

# ST - Sent
actions.sentst=kill_command,if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains|!talent.twin_fangs)
actions.sentst+=/boomstick
actions.sentst+=/wildfire_bomb,if=buff.tip_of_the_spear.up&(debuff.sentinels_mark.remains|full_recharge_time<4)
actions.sentst+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.sentst+=/takedown,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs
actions.sentst+=/moonlight_chakram
actions.sentst+=/raptor_strike
actions.sentst+=/kill_command,if=cooldown.takedown.remains
actions.sentst+=/wildfire_bomb
actions.sentst+=/takedown
```
