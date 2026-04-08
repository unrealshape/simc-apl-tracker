# Hunter – Survival

Auto-generated from SimulationCraft APL | Last updated: 2026-04-08 05:17 UTC

Source: `apl/default/hunter/survival.simc`

---

## Overview

- **Action Lists:** 7
- **Total Actions:** 63
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
| 1 | `auto_attack` | — |
| 2 | `call_action_list` | name=cds |
| 3 | `call_action_list` | name=plst,if=active_enemies<3&talent.howl_of_the_pack_leader |
| 4 | `call_action_list` | name=plcleave,if=active_enemies>2&talent.howl_of_the_pack_leader |
| 5 | `call_action_list` | name=sentst,if=active_enemies<3&!talent.howl_of_the_pack_leader |
| 6 | `call_action_list` | name=sentcleave,if=active_enemies>2&!talent.howl_of_the_pack_leader |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blood_fury` | if=buff.takedown.up\|cooldown.takedown.ready |
| 2 | `use_items` | if=buff.takedown.up\|cooldown.takedown.ready\|!talent.takedown |
| 3 | `invoke_external_buff` | name=power_infusion,if=buff.takedown.up&!buff.power_infusion.up\|fight_remains<16 |
| 4 | `ancestral_call` | if=buff.takedown.up\|cooldown.takedown.ready |
| 5 | `fireblood` | if=buff.takedown.up\|cooldown.takedown.ready |
| 6 | `berserking` | if=buff.takedown.up\|cooldown.takedown.ready |
| 7 | `muzzle` | — |
| 8 | `potion` | if=target.time_to_die<25\|cooldown.takedown.ready |
| 9 | `aspect_of_the_eagle` | if=target.distance>=6 |

## Action List: `plcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack<2&(buff.howl_of_the_pack_leader_wyvern.remains\|buff.howl_of_the_pack_leader_boar.remains\|buff.howl_of_the_pack_leader_bear.remains) |
| 2 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 3 | `takedown` | if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 4 | `flamefang_pitch` | — |
| 5 | `wildfire_bomb` | if=full_recharge_time<gcd |
| 6 | `boomstick` | if=buff.tip_of_the_spear.up |
| 7 | `wildfire_bomb` | if=buff.tip_of_the_spear.up |
| 8 | `raptor_strike` | if=buff.tip_of_the_spear.up\|!buff.raptor_swipe.up |
| 9 | `kill_command` | if=cooldown.takedown.remains |
| 10 | `wildfire_bomb` | — |
| 11 | `takedown` | — |

## Action List: `plst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack<2&(buff.howl_of_the_pack_leader_wyvern.remains\|buff.howl_of_the_pack_leader_boar.remains\|buff.howl_of_the_pack_leader_bear.remains) |
| 2 | `wildfire_bomb` | if=fury_of_the_wyvern_extendable&buff.wyverns_cry.remains<gcd |
| 3 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 4 | `raptor_strike` | if=!buff.raptor_swipe.up&cooldown.takedown.remains<gcd |
| 5 | `boomstick` | if=buff.tip_of_the_spear.up\|cooldown.takedown.remains<gcd&talent.twin_fangs |
| 6 | `takedown` | if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 7 | `flamefang_pitch` | — |
| 8 | `wildfire_bomb` | if=fury_of_the_wyvern_extendable&buff.tip_of_the_spear.up&!buff.takedown.remains |
| 9 | `raptor_strike` | if=(buff.tip_of_the_spear.up\|!buff.raptor_swipe.up) |
| 10 | `kill_command` | if=cooldown.takedown.remains |
| 11 | `wildfire_bomb` | — |
| 12 | `takedown` | — |

## Action List: `sentcleave`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack=0 |
| 2 | `wildfire_bomb` | if=talent.wildfire_shells&(buff.tip_of_the_spear.up&!debuff.sentinels_mark.remains&cooldown.boomstick.remains<11&cooldown.boomstick.remains>1) |
| 3 | `boomstick` | if=buff.tip_of_the_spear.up |
| 4 | `wildfire_bomb` | if=buff.tip_of_the_spear.up&(debuff.sentinels_mark.remains\|full_recharge_time<4+gcd) |
| 5 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 6 | `takedown` | if=buff.tip_of_the_spear.up |
| 7 | `moonlight_chakram` | if=buff.tip_of_the_spear.up |
| 8 | `flamefang_pitch` | if=talent.flamefang_pitch&buff.tip_of_the_spear.up |
| 9 | `raptor_strike` | if=buff.tip_of_the_spear.up&buff.raptor_swipe.up\|!buff.raptor_swipe.up |
| 10 | `kill_command` | — |

## Action List: `sentst`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `kill_command` | if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains\|!talent.twin_fangs) |
| 2 | `boomstick` | if=buff.tip_of_the_spear.up&!cooldown.takedown.ready&!debuff.sentinels_mark.remains |
| 3 | `wildfire_bomb` | if=buff.tip_of_the_spear.up&(debuff.sentinels_mark.remains\|full_recharge_time<4+gcd) |
| 4 | `kill_command` | if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs |
| 5 | `takedown` | if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs\|buff.tip_of_the_spear.stack=0&talent.twin_fangs |
| 6 | `boomstick` | if=buff.tip_of_the_spear.up |
| 7 | `moonlight_chakram` | if=buff.tip_of_the_spear.up |
| 8 | `flamefang_pitch` | — |
| 9 | `raptor_strike` | if=buff.tip_of_the_spear.up\|!buff.raptor_swipe.up |
| 10 | `kill_command` | if=cooldown.takedown.remains |
| 11 | `takedown` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=summon_pet
actions.precombat+=/snapshot_stats
actions.precombat+=/use_item,name=algethar_puzzle_box
actions.precombat+=/wildfire_bomb,if=active_enemies=1

# Executed every time the actor is available.
actions=auto_attack
actions+=/call_action_list,name=cds
actions+=/call_action_list,name=plst,if=active_enemies<3&talent.howl_of_the_pack_leader
actions+=/call_action_list,name=plcleave,if=active_enemies>2&talent.howl_of_the_pack_leader
actions+=/call_action_list,name=sentst,if=active_enemies<3&!talent.howl_of_the_pack_leader
actions+=/call_action_list,name=sentcleave,if=active_enemies>2&!talent.howl_of_the_pack_leader

# CDS
actions.cds=blood_fury,if=buff.takedown.up|cooldown.takedown.ready
actions.cds+=/use_items,if=buff.takedown.up|cooldown.takedown.ready|!talent.takedown
actions.cds+=/invoke_external_buff,name=power_infusion,if=buff.takedown.up&!buff.power_infusion.up|fight_remains<16
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
actions.plcleave+=/flamefang_pitch
actions.plcleave+=/wildfire_bomb,if=full_recharge_time<gcd
actions.plcleave+=/boomstick,if=buff.tip_of_the_spear.up
actions.plcleave+=/wildfire_bomb,if=buff.tip_of_the_spear.up
actions.plcleave+=/raptor_strike,if=buff.tip_of_the_spear.up|!buff.raptor_swipe.up
actions.plcleave+=/kill_command,if=cooldown.takedown.remains
actions.plcleave+=/wildfire_bomb
actions.plcleave+=/takedown

# ST - PL
actions.plst=kill_command,if=buff.tip_of_the_spear.stack<2&(buff.howl_of_the_pack_leader_wyvern.remains|buff.howl_of_the_pack_leader_boar.remains|buff.howl_of_the_pack_leader_bear.remains)
actions.plst+=/wildfire_bomb,if=fury_of_the_wyvern_extendable&buff.wyverns_cry.remains<gcd
actions.plst+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.plst+=/raptor_strike,if=!buff.raptor_swipe.up&cooldown.takedown.remains<gcd
actions.plst+=/boomstick,if=buff.tip_of_the_spear.up|cooldown.takedown.remains<gcd&talent.twin_fangs
actions.plst+=/takedown,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs
actions.plst+=/flamefang_pitch
actions.plst+=/wildfire_bomb,if=fury_of_the_wyvern_extendable&buff.tip_of_the_spear.up&!buff.takedown.remains
actions.plst+=/raptor_strike,if=(buff.tip_of_the_spear.up|!buff.raptor_swipe.up)
actions.plst+=/kill_command,if=cooldown.takedown.remains
actions.plst+=/wildfire_bomb
actions.plst+=/takedown

# AOE - Sent
actions.sentcleave=kill_command,if=buff.tip_of_the_spear.stack=0
actions.sentcleave+=/wildfire_bomb,if=talent.wildfire_shells&(buff.tip_of_the_spear.up&!debuff.sentinels_mark.remains&cooldown.boomstick.remains<11&cooldown.boomstick.remains>1)
actions.sentcleave+=/boomstick,if=buff.tip_of_the_spear.up
actions.sentcleave+=/wildfire_bomb,if=buff.tip_of_the_spear.up&(debuff.sentinels_mark.remains|full_recharge_time<4+gcd)
actions.sentcleave+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.sentcleave+=/takedown,if=buff.tip_of_the_spear.up
actions.sentcleave+=/moonlight_chakram,if=buff.tip_of_the_spear.up
actions.sentcleave+=/flamefang_pitch,if=talent.flamefang_pitch&buff.tip_of_the_spear.up
actions.sentcleave+=/raptor_strike,if=buff.tip_of_the_spear.up&buff.raptor_swipe.up|!buff.raptor_swipe.up
actions.sentcleave+=/kill_command

# ST - Sent
actions.sentst=kill_command,if=buff.tip_of_the_spear.stack=0&(cooldown.takedown.remains|!talent.twin_fangs)
actions.sentst+=/boomstick,if=buff.tip_of_the_spear.up&!cooldown.takedown.ready&!debuff.sentinels_mark.remains
actions.sentst+=/wildfire_bomb,if=buff.tip_of_the_spear.up&(debuff.sentinels_mark.remains|full_recharge_time<4+gcd)
actions.sentst+=/kill_command,if=cooldown.takedown.remains<gcd&buff.tip_of_the_spear.stack<2&!talent.twin_fangs
actions.sentst+=/takedown,if=buff.tip_of_the_spear.stack>0&!talent.twin_fangs|buff.tip_of_the_spear.stack=0&talent.twin_fangs
actions.sentst+=/boomstick,if=buff.tip_of_the_spear.up
actions.sentst+=/moonlight_chakram,if=buff.tip_of_the_spear.up
actions.sentst+=/flamefang_pitch
actions.sentst+=/raptor_strike,if=buff.tip_of_the_spear.up|!buff.raptor_swipe.up
actions.sentst+=/kill_command,if=cooldown.takedown.remains
actions.sentst+=/takedown
```
