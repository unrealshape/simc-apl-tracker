# Paladin – Retribution

Auto-generated from SimulationCraft APL | Last updated: 2026-03-31 05:14 UTC

Source: `apl/default/paladin/retribution.simc`

---

## Overview

- **Action Lists:** 5
- **Total Actions:** 41
- **Lists:** `precombat`, `default`, `cooldowns`, `finishers`, `generators`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `variable` | name=trinket_1_buffs,value=trinket.1.has_buff.strength\|trinket.1.has_buff.mastery\|trinket.1.has_buff.versatility\|trinket.1.has_buff.haste\|trinket.1.has_buff.crit |
| 3 | `variable` | name=trinket_2_buffs,value=trinket.2.has_buff.strength\|trinket.2.has_buff.mastery\|trinket.2.has_buff.versatility\|trinket.2.has_buff.haste\|trinket.2.has_buff.crit |
| 4 | `variable` | name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&(trinket.1.cooldown.duration%%cooldown.avenging_wrath.duration=0\|cooldown.avenging_wrath.duration%%trinket.1.cooldown.duration=0) |
| 5 | `variable` | name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&(trinket.2.cooldown.duration%%cooldown.avenging_wrath.duration=0\|cooldown.avenging_wrath.duration%%trinket.2.cooldown.duration=0) |
| 6 | `variable` | name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs\|variable.trinket_2_buffs&((trinket.2.cooldown.duration%trinket.2.proc.any_dps.duration)*(1.5+trinket.2.has_buff.strength)*(variable.trinket_2_sync))>((trinket.1.cooldown.duration%trinket.1.proc.any_dps.duration)*(1.5+trinket.1.has_buff.strength)*(variable.trinket_1_sync)) |
| 7 | `use_item` | name=algethar_puzzle_box,if=(trinket.1.is.algethar_puzzle_box\|trinket.2.is.algethar_puzzle_box) |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `rebuke` | — |
| 3 | `call_action_list` | name=cooldowns |
| 4 | `call_action_list` | name=generators |

## Action List: `cooldowns`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=algethar_puzzle_box,use_off_gcd=1,if=(cooldown.avenging_wrath.remains=0&!talent.radiant_glory\|(!talent.execution_sentence&cooldown.wake_of_ashes.remains=0\|cooldown.execution_sentenc.remains=0)&talent.radiant_glory) |
| 2 | `use_item` | slot=trinket1,if=((buff.avenging_wrath.up&cooldown.avenging_wrath.remains>40)&!talent.radiant_glory\|talent.radiant_glory&(!talent.execution_sentence&cooldown.wake_of_ashes.remains=0\|debuff.execution_sentence_debuff.up))&(!trinket.2.has_cooldown\|trinket.2.cooldown.remains\|variable.trinket_priority=1)\|trinket.1.proc.any_dps.duration>=fight_remains |
| 3 | `use_item` | slot=trinket2,if=((buff.avenging_wrath.up&cooldown.avenging_wrath.remains>40)&!talent.radiant_glory\|talent.radiant_glory&(!talent.execution_sentence&cooldown.wake_of_ashes.remains=0\|debuff.execution_sentence_debuff.up))&(!trinket.1.has_cooldown\|trinket.1.cooldown.remains\|variable.trinket_priority=2)\|trinket.2.proc.any_dps.duration>=fight_remains |
| 4 | `use_item` | slot=trinket1,if=!variable.trinket_1_buffs&(trinket.2.cooldown.remains\|!variable.trinket_2_buffs\|!buff.avenging_wrath.up&cooldown.avenging_wrath.remains>20) |
| 5 | `use_item` | slot=trinket2,if=!variable.trinket_2_buffs&(trinket.1.cooldown.remains\|!variable.trinket_1_buffs\|!buff.avenging_wrath.up&cooldown.avenging_wrath.remains>20) |
| 6 | `potion` | if=buff.avenging_wrath.up\|fight_remains<30\|talent.radiant_glory&cooldown.wake_of_ashes.remains=0&(!talent.holy_flames\|dot.expurgation.ticking) |
| 7 | `invoke_external_buff` | name=power_infusion,if=buff.avenging_wrath.up\|talent.radiant_glory&cooldown.wake_of_ashes.remains=0&(!talent.holy_flames\|dot.expurgation.ticking) |
| 8 | `lights_judgment` | if=!raid_event.adds.exists\|raid_event.adds.in>75\|raid_event.adds.up |
| 9 | `fireblood` | if=buff.avenging_wrath.up\|talent.radiant_glory&cooldown.wake_of_ashes.remains=0&(!talent.holy_flames\|dot.expurgation.ticking) |
| 10 | `execution_sentence` | if=(cooldown.avenging_wrath.remains>15\|talent.radiant_glory)&(target.time_to_die>10)&cooldown.wake_of_ashes.remains<gcd&(!talent.holy_flames\|dot.expurgation.ticking) |
| 11 | `avenging_wrath` | if=(!raid_event.adds.up\|target.time_to_die>10)&(!talent.holy_flames\|dot.expurgation.ticking)&(!equipped.algethar_puzzle_box\|trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>5\|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>5)&(!talent.lights_guidance\|debuff.judgment.up\|time>5) |

## Action List: `finishers`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=ds_castable,value=(active_enemies>=3\|buff.empyrean_power.up)&!buff.empyrean_legacy.up |
| 2 | `hammer_of_light` | if=!buff.hammer_of_light_free.up\|buff.hammer_of_light_free.up&(buff.undisputed_ruling.remains<gcd*1.5&(talent.radiant_glory\|cooldown.avenging_wrath.remains>4)\|buff.avenging_wrath.up&(buff.avenging_wrath.remains<gcd*2\|cooldown.wake_of_ashes.remains=0)\|buff.hammer_of_light_free.remains<gcd*2\|target.time_to_die<gcd*2) |
| 3 | `divine_storm` | if=variable.ds_castable&(!buff.hammer_of_light_ready.up\|buff.hammer_of_light_free.up) |
| 4 | `templars_verdict` | if=(!buff.hammer_of_light_ready.up\|buff.hammer_of_light_free.up) |

## Action List: `generators`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `call_action_list` | name=finishers,if=holy_power=5&cooldown.wake_of_ashes.remains\|buff.hammer_of_light_free.remains<gcd*2 |
| 2 | `blade_of_justice` | if=talent.holy_flames&!dot.expurgation.ticking&time<5 |
| 3 | `judgment` | if=talent.lights_guidance&!debuff.judgment.up&time<5 |
| 4 | `wake_of_ashes` | if=(cooldown.avenging_wrath.remains>6\|talent.radiant_glory)&(!talent.execution_sentence\|cooldown.execution_sentence.remains>4\|target.time_to_die<10)&(!raid_event.adds.exists\|raid_event.adds.in>10\|raid_event.adds.up) |
| 5 | `divine_toll` | if=(!raid_event.adds.exists\|raid_event.adds.in>10\|raid_event.adds.up)&(cooldown.avenging_wrath.remains>15\|talent.radiant_glory\|fight_remains<8) |
| 6 | `blade_of_justice` | if=(buff.art_of_war.up\|buff.righteous_cause.up)&(!talent.walk_into_light\|!buff.avenging_wrath.up) |
| 7 | `call_action_list` | name=finishers |
| 8 | `hammer_of_wrath` | if=talent.walk_into_light |
| 9 | `blade_of_justice` | — |
| 10 | `hammer_of_wrath` | — |
| 11 | `judgment` | — |
| 12 | `templar_strike` | — |
| 13 | `templar_slash` | — |
| 14 | `crusader_strike` | — |
| 15 | `arcane_torrent` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat=snapshot_stats
actions.precombat+=/variable,name=trinket_1_buffs,value=trinket.1.has_buff.strength|trinket.1.has_buff.mastery|trinket.1.has_buff.versatility|trinket.1.has_buff.haste|trinket.1.has_buff.crit
actions.precombat+=/variable,name=trinket_2_buffs,value=trinket.2.has_buff.strength|trinket.2.has_buff.mastery|trinket.2.has_buff.versatility|trinket.2.has_buff.haste|trinket.2.has_buff.crit
actions.precombat+=/variable,name=trinket_1_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_1_buffs&(trinket.1.cooldown.duration%%cooldown.avenging_wrath.duration=0|cooldown.avenging_wrath.duration%%trinket.1.cooldown.duration=0)
actions.precombat+=/variable,name=trinket_2_sync,op=setif,value=1,value_else=0.5,condition=variable.trinket_2_buffs&(trinket.2.cooldown.duration%%cooldown.avenging_wrath.duration=0|cooldown.avenging_wrath.duration%%trinket.2.cooldown.duration=0)
actions.precombat+=/variable,name=trinket_priority,op=setif,value=2,value_else=1,condition=!variable.trinket_1_buffs&variable.trinket_2_buffs|variable.trinket_2_buffs&((trinket.2.cooldown.duration%trinket.2.proc.any_dps.duration)*(1.5+trinket.2.has_buff.strength)*(variable.trinket_2_sync))>((trinket.1.cooldown.duration%trinket.1.proc.any_dps.duration)*(1.5+trinket.1.has_buff.strength)*(variable.trinket_1_sync))
actions.precombat+=/use_item,name=algethar_puzzle_box,if=(trinket.1.is.algethar_puzzle_box|trinket.2.is.algethar_puzzle_box)

# Executed every time the actor is available.
actions=auto_attack
actions+=/rebuke
actions+=/call_action_list,name=cooldowns
actions+=/call_action_list,name=generators

actions.cooldowns=use_item,name=algethar_puzzle_box,use_off_gcd=1,if=(cooldown.avenging_wrath.remains=0&!talent.radiant_glory|(!talent.execution_sentence&cooldown.wake_of_ashes.remains=0|cooldown.execution_sentenc.remains=0)&talent.radiant_glory)
actions.cooldowns+=/use_item,slot=trinket1,if=((buff.avenging_wrath.up&cooldown.avenging_wrath.remains>40)&!talent.radiant_glory|talent.radiant_glory&(!talent.execution_sentence&cooldown.wake_of_ashes.remains=0|debuff.execution_sentence_debuff.up))&(!trinket.2.has_cooldown|trinket.2.cooldown.remains|variable.trinket_priority=1)|trinket.1.proc.any_dps.duration>=fight_remains
actions.cooldowns+=/use_item,slot=trinket2,if=((buff.avenging_wrath.up&cooldown.avenging_wrath.remains>40)&!talent.radiant_glory|talent.radiant_glory&(!talent.execution_sentence&cooldown.wake_of_ashes.remains=0|debuff.execution_sentence_debuff.up))&(!trinket.1.has_cooldown|trinket.1.cooldown.remains|variable.trinket_priority=2)|trinket.2.proc.any_dps.duration>=fight_remains
actions.cooldowns+=/use_item,slot=trinket1,if=!variable.trinket_1_buffs&(trinket.2.cooldown.remains|!variable.trinket_2_buffs|!buff.avenging_wrath.up&cooldown.avenging_wrath.remains>20)
actions.cooldowns+=/use_item,slot=trinket2,if=!variable.trinket_2_buffs&(trinket.1.cooldown.remains|!variable.trinket_1_buffs|!buff.avenging_wrath.up&cooldown.avenging_wrath.remains>20)
actions.cooldowns+=/potion,if=buff.avenging_wrath.up|fight_remains<30|talent.radiant_glory&cooldown.wake_of_ashes.remains=0&(!talent.holy_flames|dot.expurgation.ticking)
actions.cooldowns+=/invoke_external_buff,name=power_infusion,if=buff.avenging_wrath.up|talent.radiant_glory&cooldown.wake_of_ashes.remains=0&(!talent.holy_flames|dot.expurgation.ticking)
actions.cooldowns+=/lights_judgment,if=!raid_event.adds.exists|raid_event.adds.in>75|raid_event.adds.up
actions.cooldowns+=/fireblood,if=buff.avenging_wrath.up|talent.radiant_glory&cooldown.wake_of_ashes.remains=0&(!talent.holy_flames|dot.expurgation.ticking)
actions.cooldowns+=/execution_sentence,if=(cooldown.avenging_wrath.remains>15|talent.radiant_glory)&(target.time_to_die>10)&cooldown.wake_of_ashes.remains<gcd&(!talent.holy_flames|dot.expurgation.ticking)
actions.cooldowns+=/avenging_wrath,if=(!raid_event.adds.up|target.time_to_die>10)&(!talent.holy_flames|dot.expurgation.ticking)&(!equipped.algethar_puzzle_box|trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>5|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>5)&(!talent.lights_guidance|debuff.judgment.up|time>5)

actions.finishers=variable,name=ds_castable,value=(active_enemies>=3|buff.empyrean_power.up)&!buff.empyrean_legacy.up
actions.finishers+=/hammer_of_light,if=!buff.hammer_of_light_free.up|buff.hammer_of_light_free.up&(buff.undisputed_ruling.remains<gcd*1.5&(talent.radiant_glory|cooldown.avenging_wrath.remains>4)|buff.avenging_wrath.up&(buff.avenging_wrath.remains<gcd*2|cooldown.wake_of_ashes.remains=0)|buff.hammer_of_light_free.remains<gcd*2|target.time_to_die<gcd*2)
actions.finishers+=/divine_storm,if=variable.ds_castable&(!buff.hammer_of_light_ready.up|buff.hammer_of_light_free.up)
actions.finishers+=/templars_verdict,if=(!buff.hammer_of_light_ready.up|buff.hammer_of_light_free.up)

actions.generators=call_action_list,name=finishers,if=holy_power=5&cooldown.wake_of_ashes.remains|buff.hammer_of_light_free.remains<gcd*2
actions.generators+=/blade_of_justice,if=talent.holy_flames&!dot.expurgation.ticking&time<5
actions.generators+=/judgment,if=talent.lights_guidance&!debuff.judgment.up&time<5
actions.generators+=/wake_of_ashes,if=(cooldown.avenging_wrath.remains>6|talent.radiant_glory)&(!talent.execution_sentence|cooldown.execution_sentence.remains>4|target.time_to_die<10)&(!raid_event.adds.exists|raid_event.adds.in>10|raid_event.adds.up)
actions.generators+=/divine_toll,if=(!raid_event.adds.exists|raid_event.adds.in>10|raid_event.adds.up)&(cooldown.avenging_wrath.remains>15|talent.radiant_glory|fight_remains<8)
actions.generators+=/blade_of_justice,if=(buff.art_of_war.up|buff.righteous_cause.up)&(!talent.walk_into_light|!buff.avenging_wrath.up)
actions.generators+=/call_action_list,name=finishers
actions.generators+=/hammer_of_wrath,if=talent.walk_into_light
actions.generators+=/blade_of_justice
actions.generators+=/hammer_of_wrath
actions.generators+=/judgment
actions.generators+=/templar_strike
actions.generators+=/templar_slash
actions.generators+=/crusader_strike
actions.generators+=/arcane_torrent
```
