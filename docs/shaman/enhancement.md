# Shaman – Enhancement

Auto-generated from SimulationCraft APL | Last updated: 2026-03-29 05:16 UTC

Source: `apl/default/shaman/enhancement.simc`

---

## Overview

- **Action Lists:** 6
- **Total Actions:** 106
- **Lists:** `precombat`, `default`, `aoe`, `buffs`, `single_sb`, `single_totemic`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `windfury_weapon` | — |
| 2 | `flametongue_weapon` | — |
| 3 | `lightning_shield` | — |
| 4 | `variable` | name=trinket1_is_weird,value=trinket.1.is.algethar_puzzle_box\|trinket.1.is.unyielding_netherprism |
| 5 | `variable` | name=trinket2_is_weird,value=trinket.2.is.algethar_puzzle_box\|trinket.2.is.unyielding_netherprism |
| 6 | `snapshot_stats` | — |
| 7 | `use_item` | name=algethar_puzzle_box |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=target_nature_mod,value=(1+debuff.chaos_brand.up*debuff.chaos_brand.value)*(1+(debuff.hunters_mark.up*target.health.pct>=80)*debuff.hunters_mark.value) |
| 2 | `variable` | name=expected_lb_funnel,value=action.lightning_bolt.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*(1+active_dot.flame_shock)*debuff.lightning_rod.value) |
| 3 | `variable` | name=expected_cl_funnel,value=action.chain_lightning.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*active_enemies*debuff.lightning_rod.value) |
| 4 | `variable` | name=flame_shock_saturated,value=((active_dot.flame_shock=active_enemies)\|(active_dot.flame_shock=6)) |
| 5 | `bloodlust` | line_cd=600 |
| 6 | `auto_attack` | — |
| 7 | `call_action_list` | name=single_sb,if=active_enemies=1&!talent.surging_totem.enabled |
| 8 | `call_action_list` | name=single_totemic,if=active_enemies=1&talent.surging_totem.enabled |
| 9 | `call_action_list` | name=aoe,if=active_enemies>1 |

## Action List: `aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `voltaic_blaze` | if=talent.surging_totem.enabled&dot.flame_shock.remains=0 |
| 2 | `flame_shock` | if=!ticking |
| 3 | `surging_totem` | — |
| 4 | `ascendance` | if=ti_chain_lightning |
| 5 | `call_action_list` | name=buffs |
| 6 | `sundering` | if=talent.surging_elements.enabled\|buff.whirling_earth.up |
| 7 | `lava_lash` | if=buff.whirling_fire.up |
| 8 | `doom_winds` | — |
| 9 | `crash_lightning` | if=talent.thorims_invocation.enabled&buff.whirling_air.up&(buff.doom_winds.up\|buff.ascendance.up) |
| 10 | `windstrike` | if=talent.thorims_invocation.enabled&buff.whirling_air.up |
| 11 | `stormstrike` | if=talent.thorims_invocation.enabled&buff.doom_winds.up&buff.whirling_air.up |
| 12 | `lava_lash` | if=talent.splitstream.enabled&buff.hot_hand.up |
| 13 | `tempest` | if=buff.maelstrom_weapon.stack>=10&(!buff.ascendance.up\|!buff.doom_winds.up) |
| 14 | `primordial_storm` | if=buff.maelstrom_weapon.stack>=10 |
| 15 | `crash_lightning` | if=talent.thorims_invocation.enabled&(buff.doom_winds.up\|buff.ascendance.up)&talent.splitstream.enabled&buff.hot_hand.up |
| 16 | `windstrike` | if=talent.thorims_invocation.enabled&talent.splitstream.enabled&buff.hot_hand.up |
| 17 | `stormstrike` | if=talent.thorims_invocation.enabled&buff.doom_winds.up&talent.splitstream.enabled&buff.hot_hand.up |
| 18 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=(9+1*talent.surging_totem.enabled)&talent.splitstream.enabled&buff.hot_hand.up |
| 19 | `voltaic_blaze` | if=talent.fire_nova.enabled |
| 20 | `crash_lightning` | — |
| 21 | `windstrike` | if=talent.thorims_invocation.enabled |
| 22 | `stormstrike` | if=talent.thorims_invocation.enabled&buff.doom_winds.up |
| 23 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=(9+1*talent.surging_totem.enabled) |
| 24 | `sundering` | if=talent.feral_spirit.enabled |
| 25 | `voltaic_blaze` | — |
| 26 | `lava_lash` | if=pet.searing_totem.active |
| 27 | `windstrike` | — |
| 28 | `stormstrike` | if=charges_fractional>=1.8\|buff.converging_storms.stack=buff.converging_storms.max_stack |
| 29 | `sundering` | if=cooldown.surging_totem.remains>25 |
| 30 | `stormstrike` | if=!talent.surging_totem.enabled |
| 31 | `lava_lash` | — |
| 32 | `stormstrike` | — |
| 33 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=5 |
| 34 | `flame_shock` | — |

## Action List: `buffs`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=algethar_puzzle_box,if=(talent.ascendance.enabled&(cooldown.ascendance.remains<2*gcd.max))\|(talent.doom_winds.enabled&!talent.ascendance.enabled&(cooldown.doom_winds.remains<2*gcd.max))\|(fight_remains%%120<=20) |
| 2 | `use_item` | name=unyielding_netherprism,if=(talent.ascendance.enabled&(cooldown.ascendance.remains<2*gcd.max))\|(talent.doom_winds.enabled&!talent.ascendance.enabled&(cooldown.doom_winds.remains<2*gcd.max))\|fight_remains<=20 |
| 3 | `use_item` | slot=trinket1,if=!variable.trinket1_is_weird&((buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains=20)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)))\|!trinket.1.has_use_buff |
| 4 | `use_item` | slot=trinket2,if=!variable.trinket2_is_weird&((buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains=20)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)))\|!trinket.2.has_use_buff |
| 5 | `potion` | if=(buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains%%300<=30)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)) |
| 6 | `blood_fury` | if=(buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains%%action.blood_fury.cooldown<=action.blood_fury.duration)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)) |
| 7 | `berserking` | if=(buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains%%action.berserking.cooldown<=action.berserking.duration)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)) |
| 8 | `fireblood` | if=(buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains%%action.fireblood.cooldown<=action.fireblood.duration)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)) |
| 9 | `ancestral_call` | if=(buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active\|(fight_remains%%action.ancestral_call.cooldown<=action.ancestral_call.duration)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)) |
| 10 | `invoke_external_buff` | name=power_infusion,if=((talent.deeply_rooted_elements.enabled&buff.ascendance.remains>7.5)\|(!talent.deeply_rooted_elements.enabled&(buff.ascendance.up\|buff.doom_winds.up\|pet.surging_totem.active))\|(fight_remains%%120<=20)\|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)) |

## Action List: `single_sb`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=9\|buff.primordial_storm.remains<=4&buff.maelstrom_weapon.stack>=5) |
| 2 | `voltaic_blaze` | if=dot.flame_shock.remains=0&time<5 |
| 3 | `flame_shock` | if=!ticking |
| 4 | `lava_lash` | if=!debuff.lashing_flames.up&time<5 |
| 5 | `call_action_list` | name=buffs |
| 6 | `sundering` | if=talent.surging_elements.enabled\|talent.feral_spirit.enabled |
| 7 | `doom_winds` | — |
| 8 | `crash_lightning` | if=!buff.crash_lightning.up\|talent.storm_unleashed.enabled |
| 9 | `voltaic_blaze` | if=(buff.doom_winds.up&buff.maelstrom_weapon.stack>=10-(1+2*talent.fire_nova.enabled)&!buff.maelstrom_weapon.stack=10)&talent.thorims_invocation.enabled |
| 10 | `windstrike` | if=buff.maelstrom_weapon.stack>0&talent.thorims_invocation.enabled |
| 11 | `ascendance` | — |
| 12 | `stormstrike` | if=buff.doom_winds.up&talent.thorims_invocation.enabled |
| 13 | `crash_lightning` | if=buff.doom_winds.up&talent.thorims_invocation.enabled |
| 14 | `tempest` | if=buff.maelstrom_weapon.stack=10 |
| 15 | `lightning_bolt` | if=buff.maelstrom_weapon.stack=10 |
| 16 | `stormstrike` | if=charges_fractional>=1.8 |
| 17 | `lava_lash` | — |
| 18 | `stormstrike` | — |
| 19 | `voltaic_blaze` | — |
| 20 | `sundering` | — |
| 21 | `lightning_bolt` | if=buff.maelstrom_weapon.stack>=8 |
| 22 | `crash_lightning` | — |
| 23 | `lightning_bolt` | if=buff.maelstrom_weapon.stack>=5 |
| 24 | `flame_shock` | — |

## Action List: `single_totemic`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `voltaic_blaze` | if=dot.flame_shock.remains=0 |
| 2 | `flame_shock` | if=!ticking |
| 3 | `surging_totem` | — |
| 4 | `call_action_list` | name=buffs |
| 5 | `sundering` | if=talent.surging_elements.enabled\|buff.whirling_earth.up\|talent.feral_spirit.enabled |
| 6 | `lava_lash` | if=buff.whirling_fire.up\|buff.hot_hand.up |
| 7 | `doom_winds` | — |
| 8 | `crash_lightning` | if=!buff.crash_lightning.up\|talent.storm_unleashed.enabled |
| 9 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10\|buff.primordial_storm.remains<3.5&buff.maelstrom_weapon.stack>=5) |
| 10 | `windstrike` | if=talent.thorims_invocation.enabled&buff.ascendance.up |
| 11 | `ascendance` | if=ti_lightning_bolt |
| 12 | `crash_lightning` | if=talent.thorims_invocation.enabled&buff.doom_winds.up\|buff.ascendance.up |
| 13 | `stormstrike` | if=talent.thorims_invocation.enabled&buff.doom_winds.up |
| 14 | `lightning_bolt` | if=talent.elemental_tempo.enabled&(buff.maelstrom_weapon.stack>=5&(cooldown.lava_lash.remains>gcd.max)&(cooldown.lava_lash.remains<=buff.maelstrom_weapon.stack*0.3)\|buff.maelstrom_weapon.stack>=10) |
| 15 | `crash_lightning` | if=!buff.crash_lightning.up |
| 16 | `lava_lash` | — |
| 17 | `sundering` | if=cooldown.surging_totem.remains>25 |
| 18 | `stormstrike` | — |
| 19 | `voltaic_blaze` | — |
| 20 | `crash_lightning` | — |
| 21 | `lightning_bolt` | if=buff.maelstrom_weapon.stack>=5 |
| 22 | `flame_shock` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=windfury_weapon
actions.precombat+=/flametongue_weapon
actions.precombat+=/lightning_shield
actions.precombat+=/variable,name=trinket1_is_weird,value=trinket.1.is.algethar_puzzle_box|trinket.1.is.unyielding_netherprism
actions.precombat+=/variable,name=trinket2_is_weird,value=trinket.2.is.algethar_puzzle_box|trinket.2.is.unyielding_netherprism
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat+=/snapshot_stats
actions.precombat+=/use_item,name=algethar_puzzle_box

# Executed every time the actor is available.
actions=variable,name=target_nature_mod,value=(1+debuff.chaos_brand.up*debuff.chaos_brand.value)*(1+(debuff.hunters_mark.up*target.health.pct>=80)*debuff.hunters_mark.value)
actions+=/variable,name=expected_lb_funnel,value=action.lightning_bolt.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*(1+active_dot.flame_shock)*debuff.lightning_rod.value)
actions+=/variable,name=expected_cl_funnel,value=action.chain_lightning.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*active_enemies*debuff.lightning_rod.value)
actions+=/variable,name=flame_shock_saturated,value=((active_dot.flame_shock=active_enemies)|(active_dot.flame_shock=6))
actions+=/bloodlust,line_cd=600
actions+=/auto_attack
actions+=/call_action_list,name=single_sb,if=active_enemies=1&!talent.surging_totem.enabled
actions+=/call_action_list,name=single_totemic,if=active_enemies=1&talent.surging_totem.enabled
actions+=/call_action_list,name=aoe,if=active_enemies>1

# Multi target action priority list
actions.aoe=voltaic_blaze,if=talent.surging_totem.enabled&dot.flame_shock.remains=0
actions.aoe+=/flame_shock,if=!ticking
actions.aoe+=/surging_totem
actions.aoe+=/ascendance,if=ti_chain_lightning
actions.aoe+=/call_action_list,name=buffs
actions.aoe+=/sundering,if=talent.surging_elements.enabled|buff.whirling_earth.up
actions.aoe+=/lava_lash,if=buff.whirling_fire.up
actions.aoe+=/doom_winds
actions.aoe+=/crash_lightning,if=talent.thorims_invocation.enabled&buff.whirling_air.up&(buff.doom_winds.up|buff.ascendance.up)
actions.aoe+=/windstrike,if=talent.thorims_invocation.enabled&buff.whirling_air.up
actions.aoe+=/stormstrike,if=talent.thorims_invocation.enabled&buff.doom_winds.up&buff.whirling_air.up
actions.aoe+=/lava_lash,if=talent.splitstream.enabled&buff.hot_hand.up
actions.aoe+=/tempest,if=buff.maelstrom_weapon.stack>=10&(!buff.ascendance.up|!buff.doom_winds.up)
actions.aoe+=/primordial_storm,if=buff.maelstrom_weapon.stack>=10
actions.aoe+=/crash_lightning,if=talent.thorims_invocation.enabled&(buff.doom_winds.up|buff.ascendance.up)&talent.splitstream.enabled&buff.hot_hand.up
actions.aoe+=/windstrike,if=talent.thorims_invocation.enabled&talent.splitstream.enabled&buff.hot_hand.up
actions.aoe+=/stormstrike,if=talent.thorims_invocation.enabled&buff.doom_winds.up&talent.splitstream.enabled&buff.hot_hand.up
actions.aoe+=/chain_lightning,if=buff.maelstrom_weapon.stack>=(9+1*talent.surging_totem.enabled)&talent.splitstream.enabled&buff.hot_hand.up
actions.aoe+=/voltaic_blaze,if=talent.fire_nova.enabled
actions.aoe+=/crash_lightning
actions.aoe+=/windstrike,if=talent.thorims_invocation.enabled
actions.aoe+=/stormstrike,if=talent.thorims_invocation.enabled&buff.doom_winds.up
actions.aoe+=/chain_lightning,if=buff.maelstrom_weapon.stack>=(9+1*talent.surging_totem.enabled)
actions.aoe+=/sundering,if=talent.feral_spirit.enabled
actions.aoe+=/voltaic_blaze
actions.aoe+=/lava_lash,if=pet.searing_totem.active
actions.aoe+=/windstrike
actions.aoe+=/stormstrike,if=charges_fractional>=1.8|buff.converging_storms.stack=buff.converging_storms.max_stack
actions.aoe+=/sundering,if=cooldown.surging_totem.remains>25
actions.aoe+=/stormstrike,if=!talent.surging_totem.enabled
actions.aoe+=/lava_lash
actions.aoe+=/stormstrike
actions.aoe+=/chain_lightning,if=buff.maelstrom_weapon.stack>=5
actions.aoe+=/flame_shock

# Buff action priority list
actions.buffs=use_item,name=algethar_puzzle_box,if=(talent.ascendance.enabled&(cooldown.ascendance.remains<2*gcd.max))|(talent.doom_winds.enabled&!talent.ascendance.enabled&(cooldown.doom_winds.remains<2*gcd.max))|(fight_remains%%120<=20)
actions.buffs+=/use_item,name=unyielding_netherprism,if=(talent.ascendance.enabled&(cooldown.ascendance.remains<2*gcd.max))|(talent.doom_winds.enabled&!talent.ascendance.enabled&(cooldown.doom_winds.remains<2*gcd.max))|fight_remains<=20
actions.buffs+=/use_item,slot=trinket1,if=!variable.trinket1_is_weird&((buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains=20)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)))|!trinket.1.has_use_buff
actions.buffs+=/use_item,slot=trinket2,if=!variable.trinket2_is_weird&((buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains=20)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)))|!trinket.2.has_use_buff
actions.buffs+=/potion,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%300<=30)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))
actions.buffs+=/blood_fury,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.blood_fury.cooldown<=action.blood_fury.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))
actions.buffs+=/berserking,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.berserking.cooldown<=action.berserking.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))
actions.buffs+=/fireblood,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.fireblood.cooldown<=action.fireblood.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))
actions.buffs+=/ancestral_call,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.ancestral_call.cooldown<=action.ancestral_call.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))
actions.buffs+=/invoke_external_buff,name=power_infusion,if=((talent.deeply_rooted_elements.enabled&buff.ascendance.remains>7.5)|(!talent.deeply_rooted_elements.enabled&(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active))|(fight_remains%%120<=20)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))

# Single target action priority list for the Stormbringer hero talent tree
actions.single_sb=primordial_storm,if=(buff.maelstrom_weapon.stack>=9|buff.primordial_storm.remains<=4&buff.maelstrom_weapon.stack>=5)
actions.single_sb+=/voltaic_blaze,if=dot.flame_shock.remains=0&time<5
actions.single_sb+=/flame_shock,if=!ticking
actions.single_sb+=/lava_lash,if=!debuff.lashing_flames.up&time<5
actions.single_sb+=/call_action_list,name=buffs
actions.single_sb+=/sundering,if=talent.surging_elements.enabled|talent.feral_spirit.enabled
actions.single_sb+=/doom_winds
actions.single_sb+=/crash_lightning,if=!buff.crash_lightning.up|talent.storm_unleashed.enabled
actions.single_sb+=/voltaic_blaze,if=(buff.doom_winds.up&buff.maelstrom_weapon.stack>=10-(1+2*talent.fire_nova.enabled)&!buff.maelstrom_weapon.stack=10)&talent.thorims_invocation.enabled
actions.single_sb+=/windstrike,if=buff.maelstrom_weapon.stack>0&talent.thorims_invocation.enabled
actions.single_sb+=/ascendance
actions.single_sb+=/stormstrike,if=buff.doom_winds.up&talent.thorims_invocation.enabled
actions.single_sb+=/crash_lightning,if=buff.doom_winds.up&talent.thorims_invocation.enabled
actions.single_sb+=/tempest,if=buff.maelstrom_weapon.stack=10
actions.single_sb+=/lightning_bolt,if=buff.maelstrom_weapon.stack=10
actions.single_sb+=/stormstrike,if=charges_fractional>=1.8
actions.single_sb+=/lava_lash
actions.single_sb+=/stormstrike
actions.single_sb+=/voltaic_blaze
actions.single_sb+=/sundering
actions.single_sb+=/lightning_bolt,if=buff.maelstrom_weapon.stack>=8
actions.single_sb+=/crash_lightning
actions.single_sb+=/lightning_bolt,if=buff.maelstrom_weapon.stack>=5
actions.single_sb+=/flame_shock

# Single target action priority list for the Totemic hero talent tree
actions.single_totemic=voltaic_blaze,if=dot.flame_shock.remains=0
actions.single_totemic+=/flame_shock,if=!ticking
actions.single_totemic+=/surging_totem
actions.single_totemic+=/call_action_list,name=buffs
actions.single_totemic+=/sundering,if=talent.surging_elements.enabled|buff.whirling_earth.up|talent.feral_spirit.enabled
actions.single_totemic+=/lava_lash,if=buff.whirling_fire.up|buff.hot_hand.up
actions.single_totemic+=/doom_winds
actions.single_totemic+=/crash_lightning,if=!buff.crash_lightning.up|talent.storm_unleashed.enabled
actions.single_totemic+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10|buff.primordial_storm.remains<3.5&buff.maelstrom_weapon.stack>=5)
actions.single_totemic+=/windstrike,if=talent.thorims_invocation.enabled&buff.ascendance.up
actions.single_totemic+=/ascendance,if=ti_lightning_bolt
actions.single_totemic+=/crash_lightning,if=talent.thorims_invocation.enabled&buff.doom_winds.up|buff.ascendance.up
actions.single_totemic+=/stormstrike,if=talent.thorims_invocation.enabled&buff.doom_winds.up
actions.single_totemic+=/lightning_bolt,if=talent.elemental_tempo.enabled&(buff.maelstrom_weapon.stack>=5&(cooldown.lava_lash.remains>gcd.max)&(cooldown.lava_lash.remains<=buff.maelstrom_weapon.stack*0.3)|buff.maelstrom_weapon.stack>=10)
actions.single_totemic+=/crash_lightning,if=!buff.crash_lightning.up
actions.single_totemic+=/lava_lash
actions.single_totemic+=/sundering,if=cooldown.surging_totem.remains>25
actions.single_totemic+=/stormstrike
actions.single_totemic+=/voltaic_blaze
actions.single_totemic+=/crash_lightning
actions.single_totemic+=/lightning_bolt,if=buff.maelstrom_weapon.stack>=5
actions.single_totemic+=/flame_shock
```
