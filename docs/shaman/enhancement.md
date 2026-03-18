# Shaman – Enhancement

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:22 UTC

Source: `apl/default/shaman/enhancement.simc`

---

## Overview

- **Action Lists:** 11
- **Total Actions:** 327
- **Lists:** `precombat`, `default`, `aoe`, `aoe_open`, `aoe_totemic`, `aoe_totemic_open`, `funnel`, `single`, `single_open`, `single_totemic`, `single_totemic_open`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `windfury_weapon` | — |
| 2 | `flametongue_weapon` | — |
| 3 | `lightning_shield` | — |
| 4 | `variable` | name=trinket1_is_weird,value=trinket.1.is.algethar_puzzle_box\|trinket.1.is.manic_grieftorch\|trinket.1.is.elementium_pocket_anvil\|trinket.1.is.beacon_to_the_beyond\|trinket.1.is.unyielding_netherprism |
| 5 | `variable` | name=trinket2_is_weird,value=trinket.2.is.algethar_puzzle_box\|trinket.2.is.manic_grieftorch\|trinket.2.is.elementium_pocket_anvil\|trinket.2.is.beacon_to_the_beyond\|trinket.2.is.unyielding_netherprism |
| 6 | `snapshot_stats` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `variable` | name=min_talented_cd_remains,value=((cooldown.feral_spirit.remains%(4*talent.witch_doctors_ancestry.enabled))+1000*!talent.feral_spirit.enabled)>?(cooldown.doom_winds.remains+1000*!talent.doom_winds.enabled)>?(cooldown.ascendance.remains+1000*!talent.ascendance.enabled) |
| 2 | `variable` | name=target_nature_mod,value=(1+debuff.chaos_brand.up*debuff.chaos_brand.value)*(1+(debuff.hunters_mark.up*target.health.pct>=80)*debuff.hunters_mark.value) |
| 3 | `variable` | name=expected_lb_funnel,value=action.lightning_bolt.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*(1+buff.primordial_wave.up*active_dot.flame_shock*buff.primordial_wave.value)*debuff.lightning_rod.value) |
| 4 | `variable` | name=expected_cl_funnel,value=action.chain_lightning.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*(active_enemies>?(3+2*talent.crashing_storms.enabled))*debuff.lightning_rod.value) |
| 5 | `variable` | name=flame_shock_saturated,value=((active_dot.flame_shock=active_enemies)\|(active_dot.flame_shock=6)) |
| 6 | `bloodlust` | line_cd=600 |
| 7 | `potion` | if=(buff.ascendance.up\|buff.feral_spirit.up\|buff.doom_winds.up\|(fight_remains%%300<=30)\|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled)) |
| 8 | `auto_attack` | — |
| 9 | `use_item` | name=elementium_pocket_anvil,use_off_gcd=1 |
| 10 | `use_item` | name=algethar_puzzle_box,use_off_gcd=1,if=(!buff.ascendance.up&!buff.feral_spirit.up&!buff.doom_winds.up)\|(talent.ascendance.enabled&(cooldown.ascendance.remains<2*action.stormstrike.gcd))\|(fight_remains%%180<=30) |
| 11 | `use_item` | slot=trinket1,if=!variable.trinket1_is_weird&((talent.ascendance.enabled&(buff.ascendance.remains>12.5\|cooldown.ascendance.remains>fight_remains))\|(talent.deeply_rooted_elements.enabled&(buff.ascendance.up\|trinket.1.has_use_buff&fight_remains=20))) |
| 12 | `use_item` | slot=trinket2,if=!variable.trinket2_is_weird&((talent.ascendance.enabled&(buff.ascendance.remains>12.5\|cooldown.ascendance.remains>fight_remains))\|(talent.deeply_rooted_elements.enabled&(buff.ascendance.up\|trinket.2.has_use_buff&fight_remains=20))) |
| 13 | `use_item` | slot=trinket1,if=!variable.trinket1_is_weird&(!talent.ascendance.enabled&!talent.deeply_rooted_elements.enabled)&((trinket.1.has_use_buff&fight_remains<=20)\|(buff.splintered_elements.up\|buff.doom_winds.up\|buff.feral_spirit.up\|(!talent.splintered_elements.enabled&!talent.doom_winds.enabled&!talent.feral_spirit.enabled))\|(variable.min_talented_cd_remains>=trinket.1.cooldown.duration)) |
| 14 | `use_item` | slot=trinket2,if=!variable.trinket2_is_weird&(!talent.ascendance.enabled&!talent.deeply_rooted_elements.enabled)&((trinket.2.has_use_buff&fight_remains<=20)\|(buff.splintered_elements.up\|buff.doom_winds.up\|buff.feral_spirit.up\|(!talent.splintered_elements.enabled&!talent.doom_winds.enabled&!talent.feral_spirit.enabled))\|(variable.min_talented_cd_remains>=trinket.2.cooldown.duration)) |
| 15 | `use_item` | name=beacon_to_the_beyond,use_off_gcd=1,if=(!buff.ascendance.up&!buff.feral_spirit.up&!buff.doom_winds.up)\|(fight_remains%%150<=5) |
| 16 | `use_item` | name=manic_grieftorch,use_off_gcd=1,if=(!buff.ascendance.up&!buff.feral_spirit.up&!buff.doom_winds.up)\|(fight_remains%%120<=5) |
| 17 | `use_item` | name=unyielding_netherprism,use_off_gcd=1,if=(buff.ascendance.remains>7.5)\|(fight_remains<=20) |
| 18 | `use_item` | slot=trinket1,if=!variable.trinket1_is_weird&!trinket.1.has_use_buff |
| 19 | `use_item` | slot=trinket2,if=!variable.trinket2_is_weird&!trinket.2.has_use_buff |
| 20 | `blood_fury` | if=(buff.ascendance.up\|buff.feral_spirit.up\|buff.doom_winds.up\|(fight_remains%%action.blood_fury.cooldown<=action.blood_fury.duration)\|(variable.min_talented_cd_remains>=action.blood_fury.cooldown)\|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled)) |
| 21 | `berserking` | if=(buff.ascendance.up\|buff.feral_spirit.up\|buff.doom_winds.up\|(fight_remains%%action.berserking.cooldown<=action.berserking.duration)\|(variable.min_talented_cd_remains>=action.berserking.cooldown)\|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled)) |
| 22 | `fireblood` | if=(buff.ascendance.up\|buff.feral_spirit.up\|buff.doom_winds.up\|(fight_remains%%action.fireblood.cooldown<=action.fireblood.duration)\|(variable.min_talented_cd_remains>=action.fireblood.cooldown)\|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled)) |
| 23 | `ancestral_call` | if=(buff.ascendance.up\|buff.feral_spirit.up\|buff.doom_winds.up\|(fight_remains%%action.ancestral_call.cooldown<=action.ancestral_call.duration)\|(variable.min_talented_cd_remains>=action.ancestral_call.cooldown)\|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled)) |
| 24 | `invoke_external_buff` | name=power_infusion,if=((talent.deeply_rooted_elements.enabled&buff.ascendance.remains>7.5)\|(!talent.deeply_rooted_elements.enabled&(buff.ascendance.up\|buff.feral_spirit.up\|buff.doom_winds.up))\|(fight_remains%%120<=20)\|(variable.min_talented_cd_remains>=120)\|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled)) |
| 25 | `call_action_list` | name=single,if=active_enemies=1&!talent.surging_totem.enabled |
| 26 | `call_action_list` | name=single_totemic,if=active_enemies=1&talent.surging_totem.enabled |
| 27 | `call_action_list` | name=aoe,if=active_enemies>1&(rotation.standard\|rotation.simple)&!talent.surging_totem.enabled |
| 28 | `call_action_list` | name=aoe_totemic,if=active_enemies>1&(rotation.standard\|rotation.simple)&talent.surging_totem.enabled |
| 29 | `call_action_list` | name=funnel,if=active_enemies>1&rotation.funnel |

## Action List: `aoe`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `feral_spirit` | if=talent.elemental_spirits.enabled\|talent.alpha_wolf.enabled |
| 2 | `run_action_list` | name=aoe_open,if=time<15 |
| 3 | `flame_shock` | if=talent.molten_assault.enabled&!ticking |
| 4 | `primordial_wave` | if=dot.flame_shock.ticking&variable.flame_shock_saturated&(buff.tempest.up\|tempest_mael_count<=35) |
| 5 | `ascendance` | if=(dot.flame_shock.ticking\|!talent.molten_assault.enabled)&ti_chain_lightning |
| 6 | `tempest` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=9&!buff.ascendance.up&(cooldown.primordial_wave.remains>15\|buff.tempest.max_stack) |
| 7 | `windstrike` | target_if=min:debuff.lightning_rod.remains,if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>=10&ti_chain_lightning&buff.tempest.up |
| 8 | `feral_spirit` | if=(cooldown.doom_winds.remains>30\|cooldown.doom_winds.remains<7) |
| 9 | `doom_winds` | — |
| 10 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10)&(buff.doom_winds.up\|!talent.doom_winds.enabled\|(cooldown.doom_winds.remains>buff.primordial_storm.remains)\|(buff.primordial_storm.remains<2*gcd)) |
| 11 | `crash_lightning` | if=talent.converging_storms.enabled&buff.electrostatic_wager.stack>6\|!buff.crash_lightning.up\|(buff.maelstrom_weapon.stack<2&buff.ascendance.up&buff.tempest.up) |
| 12 | `voltaic_blaze` | if=(buff.maelstrom_weapon.stack<6&buff.ascendance.up&(buff.ascendance.remains>=gcd*2)&buff.tempest.up) |
| 13 | `sundering` | if=(buff.maelstrom_weapon.stack<6&buff.ascendance.up&(buff.ascendance.remains>=gcd*2)&buff.tempest.up) |
| 14 | `chain_lightning` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=10&buff.ascendance.up&!buff.tempest.up |
| 15 | `windstrike` | target_if=min:debuff.lightning_rod.remains,if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0&ti_chain_lightning |
| 16 | `tempest` | if=buff.maelstrom_weapon.stack>=5&((buff.tempest.up&tww3_procs_to_asc<=1)\|(buff.tempest.max_stack&cooldown.ascendance.remains<=2&talent.ascendance.enabled)) |
| 17 | `crash_lightning` | if=talent.converging_storms.enabled&talent.alpha_wolf.enabled |
| 18 | `stormstrike` | if=buff.converging_storms.stack=6&buff.stormblast.stack>0&buff.legacy_of_the_frost_witch.up&buff.maelstrom_weapon.stack<=8 |
| 19 | `crash_lightning` | if=buff.maelstrom_weapon.stack<=8 |
| 20 | `voltaic_blaze` | if=buff.maelstrom_weapon.stack<=8 |
| 21 | `chain_lightning` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=7&!buff.primordial_storm.up |
| 22 | `fire_nova` | if=variable.flame_shock_saturated&active_enemies>=4 |
| 23 | `sundering` | — |
| 24 | `stormstrike` | if=talent.stormblast.enabled&talent.stormflurry.enabled |
| 25 | `voltaic_blaze` | — |
| 26 | `lava_lash` | target_if=min:debuff.lashing_flames.remains,if=talent.lashing_flames.enabled\|talent.molten_assault.enabled&dot.flame_shock.ticking |
| 27 | `ice_strike` | if=talent.hailstorm.enabled&!buff.ice_strike.up |
| 28 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up |
| 29 | `sundering` | — |
| 30 | `flame_shock` | if=talent.molten_assault.enabled&!ticking |
| 31 | `flame_shock` | target_if=min:dot.flame_shock.remains,if=(talent.fire_nova.enabled\|talent.primordial_wave.enabled)&!variable.flame_shock_saturated |
| 32 | `fire_nova` | if=active_dot.flame_shock>=3 |
| 33 | `stormstrike` | if=buff.crash_lightning.up&(talent.deeply_rooted_elements.enabled\|buff.converging_storms.stack=buff.converging_storms.max_stack) |
| 34 | `crash_lightning` | if=talent.crashing_storms.enabled&buff.cl_crash_lightning.up |
| 35 | `windstrike` | — |
| 36 | `stormstrike` | — |
| 37 | `ice_strike` | — |
| 38 | `lava_lash` | — |
| 39 | `crash_lightning` | — |
| 40 | `fire_nova` | if=active_dot.flame_shock>=2 |
| 41 | `chain_lightning` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up |
| 42 | `flame_shock` | if=!ticking |
| 43 | `frost_shock` | if=!talent.hailstorm.enabled |

## Action List: `aoe_open`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `flame_shock` | if=!ticking |
| 2 | `crash_lightning` | if=(buff.electrostatic_wager.stack>9&buff.doom_winds.up)\|!buff.crash_lightning.up |
| 3 | `voltaic_blaze` | if=active_dot.flame_shock<3 |
| 4 | `lava_lash` | if=talent.molten_assault.enabled&(talent.primordial_wave.enabled\|talent.fire_nova.enabled)&dot.flame_shock.ticking&!variable.flame_shock_saturated&active_dot.flame_shock<3 |
| 5 | `primordial_wave` | if=(buff.maelstrom_weapon.stack>=4)&dot.flame_shock.ticking&variable.flame_shock_saturated |
| 6 | `feral_spirit` | if=buff.maelstrom_weapon.stack>=9 |
| 7 | `doom_winds` | if=buff.legacy_of_the_frost_witch.up |
| 8 | `ascendance` | if=(dot.flame_shock.ticking\|!talent.molten_assault.enabled)&ti_chain_lightning&(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled) |
| 9 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10)&(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled) |
| 10 | `tempest` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=9&!buff.ascendance.up |
| 11 | `crash_lightning` | if=(buff.electrostatic_wager.stack>4)\|!buff.crash_lightning.up\|(buff.maelstrom_weapon.stack<2&buff.ascendance.up&buff.tempest.up) |
| 12 | `voltaic_blaze` | if=(buff.maelstrom_weapon.stack<6&buff.ascendance.up&(buff.ascendance.remains>=gcd*2)&buff.tempest.up) |
| 13 | `windstrike` | target_if=min:debuff.lightning_rod.remains,if=talent.thorims_invocation.enabled&ti_chain_lightning |
| 14 | `chain_lightning` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=5&(!buff.primordial_storm.up\|!buff.legacy_of_the_frost_witch.up)&buff.doom_winds.up |
| 15 | `chain_lightning` | target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=9&(!buff.primordial_storm.up\|!buff.legacy_of_the_frost_witch.up) |
| 16 | `stormstrike` | if=buff.converging_storms.stack=6&buff.stormblast.stack>1 |
| 17 | `fire_nova` | if=variable.flame_shock_saturated&active_enemies>=4 |
| 18 | `crash_lightning` | — |
| 19 | `sundering` | if=buff.doom_winds.up |
| 20 | `voltaic_blaze` | — |
| 21 | `stormstrike` | — |

## Action List: `aoe_totemic`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `run_action_list` | name=aoe_totemic_open,if=(time<=16) |
| 2 | `surging_totem` | — |
| 3 | `ascendance` | if=ti_chain_lightning |
| 4 | `crash_lightning` | if=talent.crashing_storms.enabled&(active_enemies>=15-5*talent.unruly_winds.enabled) |
| 5 | `feral_spirit` | if=(cooldown.doom_winds.remains>15\|cooldown.doom_winds.remains<=7)\|buff.earthen_weapon.stack>=2 |
| 6 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10)&(buff.doom_winds.remains<=gcd*3\|!buff.doom_winds.up&cooldown.doom_winds.remains>buff.primordial_storm.remains\|buff.earthen_weapon.stack>=4\|buff.earthen_weapon.remains<=gcd*3) |
| 7 | `flame_shock` | if=!ticking&(talent.ashen_catalyst.enabled\|talent.primordial_wave.enabled)&!variable.flame_shock_saturated |
| 8 | `doom_winds` | — |
| 9 | `primordial_wave` | if=dot.flame_shock.ticking&variable.flame_shock_saturated |
| 10 | `windstrike` | — |
| 11 | `lava_lash` | if=buff.hot_hand.up |
| 12 | `totemic_recall` | if=(!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up)&pet.surging_totem.remains>=10 |
| 13 | `crash_lightning` | if=buff.electrostatic_wager.stack>8 |
| 14 | `sundering` | if=buff.doom_winds.up\|talent.earthsurge.enabled&(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled)&pet.surging_totem.active |
| 15 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=10&buff.electrostatic_wager.stack>4&!buff.cl_crash_lightning.up&buff.doom_winds.up |
| 16 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=10 |
| 17 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=10&((buff.doom_winds.remains>=gcd*3&buff.primordial_storm.up)\|!buff.primordial_storm.up) |
| 18 | `crash_lightning` | if=buff.doom_winds.up\|!buff.crash_lightning.up\|(talent.alpha_wolf.enabled&feral_spirit.active&alpha_wolf_min_remains=0) |
| 19 | `voltaic_blaze` | — |
| 20 | `fire_nova` | if=(dot.flame_shock.ticking&variable.flame_shock_saturated)&pet.searing_totem.active |
| 21 | `lava_lash` | if=talent.molten_assault.enabled&dot.flame_shock.ticking |
| 22 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up&pet.searing_totem.active |
| 23 | `crash_lightning` | if=talent.crashing_storms.enabled |
| 24 | `fire_nova` | if=dot.flame_shock.ticking&variable.flame_shock_saturated |
| 25 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up |
| 26 | `crash_lightning` | — |
| 27 | `ice_strike` | if=talent.hailstorm.enabled&!buff.ice_strike.up |
| 28 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up&((buff.doom_winds.remains>=gcd*3&buff.primordial_storm.up)\|!buff.primordial_storm.up) |
| 29 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up&((buff.doom_winds.remains>=gcd*3&buff.primordial_storm.up)\|!buff.primordial_storm.up) |
| 30 | `stormstrike` | — |
| 31 | `sundering` | if=buff.doom_winds.up\|talent.earthsurge.enabled&(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled)&pet.surging_totem.active |
| 32 | `fire_nova` | if=variable.flame_shock_saturated&active_enemies>=4 |
| 33 | `voltaic_blaze` | — |
| 34 | `ice_strike` | if=talent.hailstorm.enabled&!buff.ice_strike.up |
| 35 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up |
| 36 | `sundering` | if=(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled)&pet.surging_totem.active |
| 37 | `flame_shock` | if=talent.molten_assault.enabled&!ticking |
| 38 | `fire_nova` | if=active_dot.flame_shock>=3 |
| 39 | `ice_strike` | — |
| 40 | `lava_lash` | — |
| 41 | `crash_lightning` | — |
| 42 | `flame_shock` | if=!ticking |

## Action List: `aoe_totemic_open`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `flame_shock` | if=!ticking&!variable.flame_shock_saturated |
| 2 | `lava_lash` | if=!pet.surging_totem.active&!variable.flame_shock_saturated |
| 3 | `surging_totem` | if=!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up |
| 4 | `totemic_recall` | — |
| 5 | `flame_shock` | if=!ticking |
| 6 | `fire_nova` | if=talent.swirling_maelstrom.enabled&dot.flame_shock.ticking&variable.flame_shock_saturated |
| 7 | `primordial_wave` | if=dot.flame_shock.ticking&variable.flame_shock_saturated |
| 8 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=10&!buff.legacy_of_the_frost_witch.up&cooldown.doom_winds.remains=0 |
| 9 | `doom_winds` | if=buff.legacy_of_the_frost_witch.up |
| 10 | `crash_lightning` | if=(buff.electrostatic_wager.stack>9&buff.doom_winds.up)\|!buff.crash_lightning.up |
| 11 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10)&(buff.doom_winds.remains<=gcd.max\|!buff.doom_winds.up&cooldown.doom_winds.remains>buff.primordial_storm.remains) |
| 12 | `lava_lash` | if=buff.hot_hand.up |
| 13 | `sundering` | if=buff.legacy_of_the_frost_witch.up\|(buff.earthen_weapon.stack>=2&buff.primordial_storm.up) |
| 14 | `lava_lash` | if=(buff.legacy_of_the_frost_witch.up&buff.whirling_fire.up) |
| 15 | `crash_lightning` | if=(buff.earthen_weapon.stack>=2&buff.primordial_storm.up&buff.doom_winds.up) |
| 16 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=10 |
| 17 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=10 |
| 18 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up&pet.searing_totem.active |
| 19 | `fire_nova` | if=pet.searing_totem.active&dot.flame_shock.ticking&variable.flame_shock_saturated |
| 20 | `ice_strike` | — |
| 21 | `stormstrike` | if=buff.maelstrom_weapon.stack<10&!buff.legacy_of_the_frost_witch.up |
| 22 | `lava_lash` | — |
| 23 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up&pet.searing_totem.active |
| 24 | `crash_lightning` | if=talent.crashing_storms.enabled |
| 25 | `fire_nova` | if=dot.flame_shock.ticking&variable.flame_shock_saturated |
| 26 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up |
| 27 | `crash_lightning` | — |
| 28 | `ice_strike` | if=talent.hailstorm.enabled&!buff.ice_strike.up |
| 29 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up |
| 30 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up |
| 31 | `stormstrike` | — |

## Action List: `funnel`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `feral_spirit` | if=talent.elemental_spirits.enabled |
| 2 | `surging_totem` | — |
| 3 | `ascendance` | — |
| 4 | `windstrike` | if=(talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0)\|buff.converging_storms.stack=buff.converging_storms.max_stack |
| 5 | `tempest` | if=buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack\|(buff.maelstrom_weapon.stack>=5&(tempest_mael_count>30\|buff.awakening_storms.stack=2)) |
| 6 | `lightning_bolt` | if=variable.flame_shock_saturated&buff.primordial_wave.up&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack&(!buff.splintered_elements.up\|fight_remains<=12\|raid_event.adds.remains<=gcd) |
| 7 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=5&talent.elemental_spirits.enabled&feral_spirit.active>=4 |
| 8 | `lightning_bolt` | if=talent.supercharge.enabled&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack&(variable.expected_lb_funnel>variable.expected_cl_funnel) |
| 9 | `chain_lightning` | if=(talent.supercharge.enabled&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack)\|buff.arc_discharge.up&buff.maelstrom_weapon.stack>=5 |
| 10 | `lava_lash` | if=(talent.molten_assault.enabled&dot.flame_shock.ticking&!variable.flame_shock_saturated)\|(talent.ashen_catalyst.enabled&buff.ashen_catalyst.stack=buff.ashen_catalyst.max_stack) |
| 11 | `primordial_wave` | target_if=min:dot.flame_shock.remains,if=!buff.primordial_wave.up |
| 12 | `elemental_blast` | if=(!talent.elemental_spirits.enabled\|(talent.elemental_spirits.enabled&(charges=max_charges\|buff.feral_spirit.up)))&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack |
| 13 | `feral_spirit` | — |
| 14 | `doom_winds` | — |
| 15 | `stormstrike` | if=buff.converging_storms.stack=buff.converging_storms.max_stack |
| 16 | `lava_burst` | if=(buff.molten_weapon.stack>buff.crackling_surge.stack)&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack |
| 17 | `lightning_bolt` | if=buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack&(variable.expected_lb_funnel>variable.expected_cl_funnel) |
| 18 | `chain_lightning` | if=buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack |
| 19 | `crash_lightning` | if=buff.doom_winds.up\|!buff.crash_lightning.up\|(talent.alpha_wolf.enabled&feral_spirit.active&alpha_wolf_min_remains=0)\|(talent.converging_storms.enabled&buff.converging_storms.stack<buff.converging_storms.max_stack) |
| 20 | `sundering` | if=buff.doom_winds.up\|talent.earthsurge.enabled |
| 21 | `fire_nova` | if=variable.flame_shock_saturated&active_enemies>=4 |
| 22 | `ice_strike` | if=talent.hailstorm.enabled&!buff.ice_strike.up |
| 23 | `frost_shock` | if=talent.hailstorm.enabled&buff.hailstorm.up |
| 24 | `sundering` | — |
| 25 | `flame_shock` | if=talent.molten_assault.enabled&!ticking |
| 26 | `flame_shock` | target_if=min:dot.flame_shock.remains,if=(talent.fire_nova.enabled\|talent.primordial_wave.enabled)&(active_dot.flame_shock<active_enemies)&active_dot.flame_shock<6 |
| 27 | `fire_nova` | if=active_dot.flame_shock>=3 |
| 28 | `stormstrike` | if=buff.crash_lightning.up&talent.deeply_rooted_elements.enabled |
| 29 | `crash_lightning` | if=talent.crashing_storms.enabled&buff.cl_crash_lightning.up&active_enemies>=4 |
| 30 | `windstrike` | — |
| 31 | `stormstrike` | — |
| 32 | `ice_strike` | — |
| 33 | `lava_lash` | — |
| 34 | `crash_lightning` | — |
| 35 | `fire_nova` | if=active_dot.flame_shock>=2 |
| 36 | `elemental_blast` | if=(!talent.elemental_spirits.enabled\|(talent.elemental_spirits.enabled&(charges=max_charges\|buff.feral_spirit.up)))&buff.maelstrom_weapon.stack>=5 |
| 37 | `lava_burst` | if=(buff.molten_weapon.stack>buff.crackling_surge.stack)&buff.maelstrom_weapon.stack>=5 |
| 38 | `lightning_bolt` | if=buff.maelstrom_weapon.stack>=5&(variable.expected_lb_funnel>variable.expected_cl_funnel) |
| 39 | `chain_lightning` | if=buff.maelstrom_weapon.stack>=5 |
| 40 | `flame_shock` | if=!ticking |
| 41 | `frost_shock` | if=!talent.hailstorm.enabled |

## Action List: `single`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `run_action_list` | name=single_open,if=time<15 |
| 2 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10\|buff.primordial_storm.remains<=4&buff.maelstrom_weapon.stack>=5) |
| 3 | `feral_spirit` | if=(cooldown.doom_winds.remains>25\|cooldown.doom_winds.remains<=5) |
| 4 | `doom_winds` | if=(!buff.ascendance.up\|(buff.tempest.up&buff.ascendance.remains>1*gcd&buff.maelstrom_weapon.stack<=9))&set_bonus.tww3_4pc |
| 5 | `ice_strike` | if=buff.tempest.up&buff.ascendance.remains>5*gcd&buff.maelstrom_weapon.stack<=1 |
| 6 | `lava_lash` | if=(buff.hot_hand.up&buff.ashen_catalyst.stack=buff.ashen_catalyst.max_stack)&(buff.tempest.up&buff.ascendance.remains>5*gcd&buff.maelstrom_weapon.stack<=1) |
| 7 | `flame_shock` | if=!ticking&(talent.ashen_catalyst.enabled\|talent.primordial_wave.enabled\|talent.lashing_flames.enabled)&!buff.ascendance.up&!talent.voltaic_blaze.enabled |
| 8 | `windstrike` | if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0&ti_lightning_bolt |
| 9 | `doom_winds` | — |
| 10 | `primordial_wave` | if=dot.flame_shock.ticking&(raid_event.adds.in>action.primordial_wave.cooldown\|raid_event.adds.in<6) |
| 11 | `ice_strike` | if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=8 |
| 12 | `voltaic_blaze` | if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=6 |
| 13 | `frost_shock` | if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=6&buff.hailstorm.stack=10&buff.ice_strike.up&talent.swirling_maelstrom.enabled |
| 14 | `natures_swiftness` | if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=4 |
| 15 | `tempest` | if=(buff.maelstrom_weapon.stack>=5\|buff.natures_swiftness.up)&(buff.tempest.up&tww3_procs_to_asc=1\|buff.tempest.max_stack&cooldown.ascendance.remains<=2&talent.ascendance.enabled)&set_bonus.tww3_4pc |
| 16 | `ascendance` | if=(dot.flame_shock.ticking\|!talent.primordial_wave.enabled\|!talent.ashen_catalyst.enabled) |
| 17 | `tempest` | if=((buff.maelstrom_weapon.stack>=5)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=5))&(buff.tempest.stack=buff.tempest.max_stack&(tempest_mael_count>30\|buff.awakening_storms.stack=3)) |
| 18 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=5&tww3_procs_to_asc=1&((tempest_mael_count+buff.maelstrom_weapon.stack)>=40)&!buff.tempest.up |
| 19 | `elemental_blast` | if=((!talent.overflowing_maelstrom.enabled&buff.maelstrom_weapon.stack>=5)\|(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8))&(charges_fractional>=1.6\|set_bonus.tww2_4pc) |
| 20 | `stormstrike` | if=charges_fractional>=2&(buff.maelstrom_weapon.stack<=6)&!buff.tempest.up&tww3_procs_to_asc=1 |
| 21 | `tempest` | if=(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8) |
| 22 | `elemental_blast` | if=((!talent.overflowing_maelstrom.enabled&buff.maelstrom_weapon.stack>=5)\|(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8))&!buff.arc_discharge.up |
| 23 | `lightning_bolt` | if=(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8) |
| 24 | `windstrike` | if=!talent.thorims_invocation.enabled |
| 25 | `stormstrike` | if=!buff.tempest.up&tww3_procs_to_asc=1 |
| 26 | `crash_lightning` | if=(buff.doom_winds.up&buff.electrostatic_wager.stack>1)\|buff.electrostatic_wager.stack>8 |
| 27 | `ice_strike` | if=(buff.tempest.up\|(tempest_mael_count>=30&buff.tempest.up))&tww3_procs_to_asc=1 |
| 28 | `voltaic_blaze` | if=tempest_mael_count>=30&tww3_procs_to_asc=1 |
| 29 | `stormstrike` | if=buff.doom_winds.up\|buff.stormblast.stack>0 |
| 30 | `crash_lightning` | if=(talent.unrelenting_storms.enabled&talent.alpha_wolf.enabled&alpha_wolf_min_remains=0)\|set_bonus.tww2_4pc |
| 31 | `voltaic_blaze` | if=dot.flame_shock.remains<=4 |
| 32 | `ice_strike` | — |
| 33 | `stormstrike` | if=charges_fractional>=1.8 |
| 34 | `lava_lash` | if=(talent.lashing_flames.enabled&(debuff.lashing_flames.remains<2)) |
| 35 | `voltaic_blaze` | — |
| 36 | `stormstrike` | — |
| 37 | `crash_lightning` | if=talent.unrelenting_storms.enabled |
| 38 | `elemental_blast` | if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up |
| 39 | `lightning_bolt` | if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up |
| 40 | `lava_lash` | if=talent.elemental_assault.enabled&talent.molten_assault.enabled&dot.flame_shock.ticking |
| 41 | `sundering` | — |
| 42 | `lava_lash` | — |
| 43 | `frost_shock` | if=buff.hailstorm.up |
| 44 | `flame_shock` | if=!ticking |
| 45 | `sundering` | if=raid_event.adds.in>=action.sundering.cooldown |
| 46 | `crash_lightning` | — |
| 47 | `frost_shock` | — |
| 48 | `fire_nova` | if=active_dot.flame_shock |
| 49 | `earth_elemental` | — |
| 50 | `flame_shock` | — |

## Action List: `single_open`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `flame_shock` | if=!ticking |
| 2 | `voltaic_blaze` | if=active_dot.flame_shock<3&!buff.ascendance.up |
| 3 | `primordial_wave` | if=(buff.maelstrom_weapon.stack>=4)&dot.flame_shock.ticking |
| 4 | `feral_spirit` | if=buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled |
| 5 | `doom_winds` | if=buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled |
| 6 | `ascendance` | if=(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled)&(buff.maelstrom_weapon.stack>=6\|!set_bonus.tww3_4pc) |
| 7 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10)&(buff.legacy_of_the_frost_witch.up\|!talent.legacy_of_the_frost_witch.enabled) |
| 8 | `windstrike` | — |
| 9 | `elemental_blast` | if=((buff.maelstrom_weapon.stack>=5&!talent.deeply_rooted_elements.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=7))&(!buff.legacy_of_the_frost_witch.up\|buff.ascendance.up\|talent.deeply_rooted_elements.enabled) |
| 10 | `tempest` | if=((buff.maelstrom_weapon.stack>=5&!talent.deeply_rooted_elements.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=7))&(!buff.legacy_of_the_frost_witch.up\|buff.ascendance.up\|talent.deeply_rooted_elements.enabled) |
| 11 | `lightning_bolt` | if=((buff.maelstrom_weapon.stack>=5&!talent.deeply_rooted_elements.enabled)\|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=7))&(!buff.legacy_of_the_frost_witch.up\|buff.ascendance.up\|talent.deeply_rooted_elements.enabled) |
| 12 | `ice_strike` | — |
| 13 | `stormstrike` | — |
| 14 | `crash_lightning` | if=set_bonus.tww2_4pc |
| 15 | `voltaic_blaze` | — |
| 16 | `lava_lash` | — |

## Action List: `single_totemic`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `run_action_list` | name=single_totemic_open,if=time<20 |
| 2 | `surging_totem` | — |
| 3 | `ascendance` | if=ti_lightning_bolt&pet.surging_totem.remains>4&(buff.totemic_rebound.stack>=3\|buff.maelstrom_weapon.stack>0) |
| 4 | `flame_shock` | if=!ticking&(talent.ashen_catalyst.enabled\|talent.primordial_wave.enabled) |
| 5 | `lava_lash` | if=buff.hot_hand.up |
| 6 | `totemic_recall` | if=(!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up)&pet.surging_totem.remains>=10 |
| 7 | `feral_spirit` | if=((cooldown.doom_winds.remains>23\|cooldown.doom_winds.remains<7)&(cooldown.primordial_wave.remains<20\|buff.primordial_storm.up\|!talent.primordial_storm.enabled)) |
| 8 | `primordial_wave` | if=dot.flame_shock.ticking&(raid_event.adds.in>action.primordial_wave.cooldown)\|raid_event.adds.in<6 |
| 9 | `doom_winds` | if=buff.legacy_of_the_frost_witch.up |
| 10 | `primordial_storm` | if=(buff.maelstrom_weapon.stack>=10)&((cooldown.doom_winds.remains>=buff.primordial_storm.remains)\|buff.doom_winds.up\|!talent.doom_winds.enabled\|(buff.primordial_storm.remains<2*gcd)) |
| 11 | `sundering` | if=buff.ascendance.up&pet.surging_totem.active&talent.earthsurge.enabled&buff.legacy_of_the_frost_witch.up&buff.totemic_rebound.stack>=5&buff.earthen_weapon.stack>=2 |
| 12 | `windstrike` | if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0&ti_lightning_bolt |
| 13 | `sundering` | if=buff.legacy_of_the_frost_witch.up&((cooldown.ascendance.remains>=10&talent.ascendance.enabled)\|!talent.ascendance.enabled)&pet.surging_totem.active&buff.totemic_rebound.stack>=3&!buff.ascendance.up |
| 14 | `crash_lightning` | if=talent.unrelenting_storms.enabled&talent.alpha_wolf.enabled&alpha_wolf_min_remains=0 |
| 15 | `lava_burst` | if=!talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>=10&buff.whirling_air.down |
| 16 | `elemental_blast` | if=(buff.maelstrom_weapon.stack>=10)&(buff.primordial_storm.down\|buff.primordial_storm.remains>4) |
| 17 | `stormstrike` | if=buff.doom_winds.up&buff.legacy_of_the_frost_witch.up |
| 18 | `lightning_bolt` | if=(buff.maelstrom_weapon.stack>=10)&(buff.primordial_storm.down\|buff.primordial_storm.remains>4) |
| 19 | `crash_lightning` | if=buff.electrostatic_wager.stack>4 |
| 20 | `stormstrike` | if=buff.doom_winds.up\|buff.stormblast.stack>1 |
| 21 | `lava_lash` | if=buff.whirling_fire.up\|buff.ashen_catalyst.stack>=8 |
| 22 | `windstrike` | — |
| 23 | `stormstrike` | — |
| 24 | `lava_lash` | — |
| 25 | `crash_lightning` | if=set_bonus.tww2_4pc |
| 26 | `voltaic_blaze` | — |
| 27 | `crash_lightning` | if=talent.unrelenting_storms.enabled |
| 28 | `ice_strike` | if=!buff.ice_strike.up |
| 29 | `crash_lightning` | — |
| 30 | `frost_shock` | — |
| 31 | `fire_nova` | if=active_dot.flame_shock |
| 32 | `earth_elemental` | — |
| 33 | `flame_shock` | if=!talent.voltaic_blaze.enabled |

## Action List: `single_totemic_open`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `flame_shock` | if=!ticking |
| 2 | `lava_lash` | if=!pet.surging_totem.active&talent.lashing_flames.enabled&debuff.lashing_flames.down |
| 3 | `surging_totem` | if=!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up |
| 4 | `totemic_recall` | — |
| 5 | `primordial_wave` | — |
| 6 | `feral_spirit` | if=buff.legacy_of_the_frost_witch.up |
| 7 | `lava_lash` | if=buff.hot_hand.up\|(buff.whirling_fire.up&cooldown.surging_totem.up&!buff.doom_winds.remains<=2) |
| 8 | `primordial_storm` | if=buff.doom_winds.up&buff.maelstrom_weapon.max_stack&buff.legacy_of_the_frost_witch.up\|(buff.primordial_storm.remains<=3&buff.maelstrom_weapon.max_stack) |
| 9 | `doom_winds` | if=buff.legacy_of_the_frost_witch.up |
| 10 | `stormstrike` | if=buff.doom_winds.up&buff.legacy_of_the_frost_witch.up |
| 11 | `sundering` | if=buff.legacy_of_the_frost_witch.up |
| 12 | `elemental_blast` | if=buff.maelstrom_weapon.stack=10 |
| 13 | `lightning_bolt` | if=buff.maelstrom_weapon.stack=10 |
| 14 | `stormstrike` | — |
| 15 | `lava_lash` | — |

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
actions.precombat+=/variable,name=trinket1_is_weird,value=trinket.1.is.algethar_puzzle_box|trinket.1.is.manic_grieftorch|trinket.1.is.elementium_pocket_anvil|trinket.1.is.beacon_to_the_beyond|trinket.1.is.unyielding_netherprism
actions.precombat+=/variable,name=trinket2_is_weird,value=trinket.2.is.algethar_puzzle_box|trinket.2.is.manic_grieftorch|trinket.2.is.elementium_pocket_anvil|trinket.2.is.beacon_to_the_beyond|trinket.2.is.unyielding_netherprism
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat+=/snapshot_stats

# Executed every time the actor is available.
actions=variable,name=min_talented_cd_remains,value=((cooldown.feral_spirit.remains%(4*talent.witch_doctors_ancestry.enabled))+1000*!talent.feral_spirit.enabled)>?(cooldown.doom_winds.remains+1000*!talent.doom_winds.enabled)>?(cooldown.ascendance.remains+1000*!talent.ascendance.enabled)
actions+=/variable,name=target_nature_mod,value=(1+debuff.chaos_brand.up*debuff.chaos_brand.value)*(1+(debuff.hunters_mark.up*target.health.pct>=80)*debuff.hunters_mark.value)
actions+=/variable,name=expected_lb_funnel,value=action.lightning_bolt.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*(1+buff.primordial_wave.up*active_dot.flame_shock*buff.primordial_wave.value)*debuff.lightning_rod.value)
actions+=/variable,name=expected_cl_funnel,value=action.chain_lightning.damage*(1+debuff.lightning_rod.up*variable.target_nature_mod*(active_enemies>?(3+2*talent.crashing_storms.enabled))*debuff.lightning_rod.value)
actions+=/variable,name=flame_shock_saturated,value=((active_dot.flame_shock=active_enemies)|(active_dot.flame_shock=6))
actions+=/bloodlust,line_cd=600
actions+=/potion,if=(buff.ascendance.up|buff.feral_spirit.up|buff.doom_winds.up|(fight_remains%%300<=30)|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled))
actions+=/auto_attack
actions+=/use_item,name=elementium_pocket_anvil,use_off_gcd=1
actions+=/use_item,name=algethar_puzzle_box,use_off_gcd=1,if=(!buff.ascendance.up&!buff.feral_spirit.up&!buff.doom_winds.up)|(talent.ascendance.enabled&(cooldown.ascendance.remains<2*action.stormstrike.gcd))|(fight_remains%%180<=30)
actions+=/use_item,slot=trinket1,if=!variable.trinket1_is_weird&((talent.ascendance.enabled&(buff.ascendance.remains>12.5|cooldown.ascendance.remains>fight_remains))|(talent.deeply_rooted_elements.enabled&(buff.ascendance.up|trinket.1.has_use_buff&fight_remains=20)))
actions+=/use_item,slot=trinket2,if=!variable.trinket2_is_weird&((talent.ascendance.enabled&(buff.ascendance.remains>12.5|cooldown.ascendance.remains>fight_remains))|(talent.deeply_rooted_elements.enabled&(buff.ascendance.up|trinket.2.has_use_buff&fight_remains=20)))
actions+=/use_item,slot=trinket1,if=!variable.trinket1_is_weird&(!talent.ascendance.enabled&!talent.deeply_rooted_elements.enabled)&((trinket.1.has_use_buff&fight_remains<=20)|(buff.splintered_elements.up|buff.doom_winds.up|buff.feral_spirit.up|(!talent.splintered_elements.enabled&!talent.doom_winds.enabled&!talent.feral_spirit.enabled))|(variable.min_talented_cd_remains>=trinket.1.cooldown.duration))
actions+=/use_item,slot=trinket2,if=!variable.trinket2_is_weird&(!talent.ascendance.enabled&!talent.deeply_rooted_elements.enabled)&((trinket.2.has_use_buff&fight_remains<=20)|(buff.splintered_elements.up|buff.doom_winds.up|buff.feral_spirit.up|(!talent.splintered_elements.enabled&!talent.doom_winds.enabled&!talent.feral_spirit.enabled))|(variable.min_talented_cd_remains>=trinket.2.cooldown.duration))
actions+=/use_item,name=beacon_to_the_beyond,use_off_gcd=1,if=(!buff.ascendance.up&!buff.feral_spirit.up&!buff.doom_winds.up)|(fight_remains%%150<=5)
actions+=/use_item,name=manic_grieftorch,use_off_gcd=1,if=(!buff.ascendance.up&!buff.feral_spirit.up&!buff.doom_winds.up)|(fight_remains%%120<=5)
actions+=/use_item,name=unyielding_netherprism,use_off_gcd=1,if=(buff.ascendance.remains>7.5)|(fight_remains<=20)
actions+=/use_item,slot=trinket1,if=!variable.trinket1_is_weird&!trinket.1.has_use_buff
actions+=/use_item,slot=trinket2,if=!variable.trinket2_is_weird&!trinket.2.has_use_buff
actions+=/blood_fury,if=(buff.ascendance.up|buff.feral_spirit.up|buff.doom_winds.up|(fight_remains%%action.blood_fury.cooldown<=action.blood_fury.duration)|(variable.min_talented_cd_remains>=action.blood_fury.cooldown)|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled))
actions+=/berserking,if=(buff.ascendance.up|buff.feral_spirit.up|buff.doom_winds.up|(fight_remains%%action.berserking.cooldown<=action.berserking.duration)|(variable.min_talented_cd_remains>=action.berserking.cooldown)|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled))
actions+=/fireblood,if=(buff.ascendance.up|buff.feral_spirit.up|buff.doom_winds.up|(fight_remains%%action.fireblood.cooldown<=action.fireblood.duration)|(variable.min_talented_cd_remains>=action.fireblood.cooldown)|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled))
actions+=/ancestral_call,if=(buff.ascendance.up|buff.feral_spirit.up|buff.doom_winds.up|(fight_remains%%action.ancestral_call.cooldown<=action.ancestral_call.duration)|(variable.min_talented_cd_remains>=action.ancestral_call.cooldown)|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled))
actions+=/invoke_external_buff,name=power_infusion,if=((talent.deeply_rooted_elements.enabled&buff.ascendance.remains>7.5)|(!talent.deeply_rooted_elements.enabled&(buff.ascendance.up|buff.feral_spirit.up|buff.doom_winds.up))|(fight_remains%%120<=20)|(variable.min_talented_cd_remains>=120)|(!talent.ascendance.enabled&!talent.feral_spirit.enabled&!talent.doom_winds.enabled))
actions+=/call_action_list,name=single,if=active_enemies=1&!talent.surging_totem.enabled
actions+=/call_action_list,name=single_totemic,if=active_enemies=1&talent.surging_totem.enabled
actions+=/call_action_list,name=aoe,if=active_enemies>1&(rotation.standard|rotation.simple)&!talent.surging_totem.enabled
actions+=/call_action_list,name=aoe_totemic,if=active_enemies>1&(rotation.standard|rotation.simple)&talent.surging_totem.enabled
actions+=/call_action_list,name=funnel,if=active_enemies>1&rotation.funnel

# Multi target action priority list
actions.aoe=feral_spirit,if=talent.elemental_spirits.enabled|talent.alpha_wolf.enabled
actions.aoe+=/run_action_list,name=aoe_open,if=time<15
actions.aoe+=/flame_shock,if=talent.molten_assault.enabled&!ticking
actions.aoe+=/primordial_wave,if=dot.flame_shock.ticking&variable.flame_shock_saturated&(buff.tempest.up|tempest_mael_count<=35)
actions.aoe+=/ascendance,if=(dot.flame_shock.ticking|!talent.molten_assault.enabled)&ti_chain_lightning
actions.aoe+=/tempest,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=9&!buff.ascendance.up&(cooldown.primordial_wave.remains>15|buff.tempest.max_stack)
actions.aoe+=/windstrike,target_if=min:debuff.lightning_rod.remains,if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>=10&ti_chain_lightning&buff.tempest.up
actions.aoe+=/feral_spirit,if=(cooldown.doom_winds.remains>30|cooldown.doom_winds.remains<7)
actions.aoe+=/doom_winds
actions.aoe+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10)&(buff.doom_winds.up|!talent.doom_winds.enabled|(cooldown.doom_winds.remains>buff.primordial_storm.remains)|(buff.primordial_storm.remains<2*gcd))
actions.aoe+=/crash_lightning,if=talent.converging_storms.enabled&buff.electrostatic_wager.stack>6|!buff.crash_lightning.up|(buff.maelstrom_weapon.stack<2&buff.ascendance.up&buff.tempest.up)
actions.aoe+=/voltaic_blaze,if=(buff.maelstrom_weapon.stack<6&buff.ascendance.up&(buff.ascendance.remains>=gcd*2)&buff.tempest.up)
actions.aoe+=/sundering,if=(buff.maelstrom_weapon.stack<6&buff.ascendance.up&(buff.ascendance.remains>=gcd*2)&buff.tempest.up)
actions.aoe+=/chain_lightning,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=10&buff.ascendance.up&!buff.tempest.up
actions.aoe+=/windstrike,target_if=min:debuff.lightning_rod.remains,if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0&ti_chain_lightning
actions.aoe+=/tempest,if=buff.maelstrom_weapon.stack>=5&((buff.tempest.up&tww3_procs_to_asc<=1)|(buff.tempest.max_stack&cooldown.ascendance.remains<=2&talent.ascendance.enabled))
actions.aoe+=/crash_lightning,if=talent.converging_storms.enabled&talent.alpha_wolf.enabled
actions.aoe+=/stormstrike,if=buff.converging_storms.stack=6&buff.stormblast.stack>0&buff.legacy_of_the_frost_witch.up&buff.maelstrom_weapon.stack<=8
actions.aoe+=/crash_lightning,if=buff.maelstrom_weapon.stack<=8
actions.aoe+=/voltaic_blaze,if=buff.maelstrom_weapon.stack<=8
actions.aoe+=/chain_lightning,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=7&!buff.primordial_storm.up
actions.aoe+=/fire_nova,if=variable.flame_shock_saturated&active_enemies>=4
actions.aoe+=/sundering
actions.aoe+=/stormstrike,if=talent.stormblast.enabled&talent.stormflurry.enabled
actions.aoe+=/voltaic_blaze
actions.aoe+=/lava_lash,target_if=min:debuff.lashing_flames.remains,if=talent.lashing_flames.enabled|talent.molten_assault.enabled&dot.flame_shock.ticking
actions.aoe+=/ice_strike,if=talent.hailstorm.enabled&!buff.ice_strike.up
actions.aoe+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up
actions.aoe+=/sundering
actions.aoe+=/flame_shock,if=talent.molten_assault.enabled&!ticking
actions.aoe+=/flame_shock,target_if=min:dot.flame_shock.remains,if=(talent.fire_nova.enabled|talent.primordial_wave.enabled)&!variable.flame_shock_saturated
actions.aoe+=/fire_nova,if=active_dot.flame_shock>=3
actions.aoe+=/stormstrike,if=buff.crash_lightning.up&(talent.deeply_rooted_elements.enabled|buff.converging_storms.stack=buff.converging_storms.max_stack)
actions.aoe+=/crash_lightning,if=talent.crashing_storms.enabled&buff.cl_crash_lightning.up
actions.aoe+=/windstrike
actions.aoe+=/stormstrike
actions.aoe+=/ice_strike
actions.aoe+=/lava_lash
actions.aoe+=/crash_lightning
actions.aoe+=/fire_nova,if=active_dot.flame_shock>=2
actions.aoe+=/chain_lightning,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up
actions.aoe+=/flame_shock,if=!ticking
actions.aoe+=/frost_shock,if=!talent.hailstorm.enabled

# Multi target opener priority list
actions.aoe_open=flame_shock,if=!ticking
actions.aoe_open+=/crash_lightning,if=(buff.electrostatic_wager.stack>9&buff.doom_winds.up)|!buff.crash_lightning.up
actions.aoe_open+=/voltaic_blaze,if=active_dot.flame_shock<3
actions.aoe_open+=/lava_lash,if=talent.molten_assault.enabled&(talent.primordial_wave.enabled|talent.fire_nova.enabled)&dot.flame_shock.ticking&!variable.flame_shock_saturated&active_dot.flame_shock<3
actions.aoe_open+=/primordial_wave,if=(buff.maelstrom_weapon.stack>=4)&dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_open+=/feral_spirit,if=buff.maelstrom_weapon.stack>=9
actions.aoe_open+=/doom_winds,if=buff.legacy_of_the_frost_witch.up
actions.aoe_open+=/ascendance,if=(dot.flame_shock.ticking|!talent.molten_assault.enabled)&ti_chain_lightning&(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)
actions.aoe_open+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10)&(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)
actions.aoe_open+=/tempest,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=9&!buff.ascendance.up
actions.aoe_open+=/crash_lightning,if=(buff.electrostatic_wager.stack>4)|!buff.crash_lightning.up|(buff.maelstrom_weapon.stack<2&buff.ascendance.up&buff.tempest.up)
actions.aoe_open+=/voltaic_blaze,if=(buff.maelstrom_weapon.stack<6&buff.ascendance.up&(buff.ascendance.remains>=gcd*2)&buff.tempest.up)
actions.aoe_open+=/windstrike,target_if=min:debuff.lightning_rod.remains,if=talent.thorims_invocation.enabled&ti_chain_lightning
actions.aoe_open+=/chain_lightning,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=5&(!buff.primordial_storm.up|!buff.legacy_of_the_frost_witch.up)&buff.doom_winds.up
actions.aoe_open+=/chain_lightning,target_if=min:debuff.lightning_rod.remains,if=buff.maelstrom_weapon.stack>=9&(!buff.primordial_storm.up|!buff.legacy_of_the_frost_witch.up)
actions.aoe_open+=/stormstrike,if=buff.converging_storms.stack=6&buff.stormblast.stack>1
actions.aoe_open+=/fire_nova,if=variable.flame_shock_saturated&active_enemies>=4
actions.aoe_open+=/crash_lightning
actions.aoe_open+=/sundering,if=buff.doom_winds.up
actions.aoe_open+=/voltaic_blaze
actions.aoe_open+=/stormstrike

# Multi target action priority list for the Totemic hero talent tree
actions.aoe_totemic=run_action_list,name=aoe_totemic_open,if=(time<=16)
actions.aoe_totemic+=/surging_totem
actions.aoe_totemic+=/ascendance,if=ti_chain_lightning
actions.aoe_totemic+=/crash_lightning,if=talent.crashing_storms.enabled&(active_enemies>=15-5*talent.unruly_winds.enabled)
actions.aoe_totemic+=/feral_spirit,if=(cooldown.doom_winds.remains>15|cooldown.doom_winds.remains<=7)|buff.earthen_weapon.stack>=2
actions.aoe_totemic+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10)&(buff.doom_winds.remains<=gcd*3|!buff.doom_winds.up&cooldown.doom_winds.remains>buff.primordial_storm.remains|buff.earthen_weapon.stack>=4|buff.earthen_weapon.remains<=gcd*3)
actions.aoe_totemic+=/flame_shock,if=!ticking&(talent.ashen_catalyst.enabled|talent.primordial_wave.enabled)&!variable.flame_shock_saturated
actions.aoe_totemic+=/doom_winds
actions.aoe_totemic+=/primordial_wave,if=dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_totemic+=/windstrike
actions.aoe_totemic+=/lava_lash,if=buff.hot_hand.up
actions.aoe_totemic+=/totemic_recall,if=(!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up)&pet.surging_totem.remains>=10
actions.aoe_totemic+=/crash_lightning,if=buff.electrostatic_wager.stack>8
actions.aoe_totemic+=/sundering,if=buff.doom_winds.up|talent.earthsurge.enabled&(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)&pet.surging_totem.active
actions.aoe_totemic+=/chain_lightning,if=buff.maelstrom_weapon.stack>=10&buff.electrostatic_wager.stack>4&!buff.cl_crash_lightning.up&buff.doom_winds.up
actions.aoe_totemic+=/elemental_blast,if=buff.maelstrom_weapon.stack>=10
actions.aoe_totemic+=/chain_lightning,if=buff.maelstrom_weapon.stack>=10&((buff.doom_winds.remains>=gcd*3&buff.primordial_storm.up)|!buff.primordial_storm.up)
actions.aoe_totemic+=/crash_lightning,if=buff.doom_winds.up|!buff.crash_lightning.up|(talent.alpha_wolf.enabled&feral_spirit.active&alpha_wolf_min_remains=0)
actions.aoe_totemic+=/voltaic_blaze
actions.aoe_totemic+=/fire_nova,if=(dot.flame_shock.ticking&variable.flame_shock_saturated)&pet.searing_totem.active
actions.aoe_totemic+=/lava_lash,if=talent.molten_assault.enabled&dot.flame_shock.ticking
actions.aoe_totemic+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up&pet.searing_totem.active
actions.aoe_totemic+=/crash_lightning,if=talent.crashing_storms.enabled
actions.aoe_totemic+=/fire_nova,if=dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_totemic+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up
actions.aoe_totemic+=/crash_lightning
actions.aoe_totemic+=/ice_strike,if=talent.hailstorm.enabled&!buff.ice_strike.up
actions.aoe_totemic+=/elemental_blast,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up&((buff.doom_winds.remains>=gcd*3&buff.primordial_storm.up)|!buff.primordial_storm.up)
actions.aoe_totemic+=/chain_lightning,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up&((buff.doom_winds.remains>=gcd*3&buff.primordial_storm.up)|!buff.primordial_storm.up)
actions.aoe_totemic+=/stormstrike
actions.aoe_totemic+=/sundering,if=buff.doom_winds.up|talent.earthsurge.enabled&(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)&pet.surging_totem.active
actions.aoe_totemic+=/fire_nova,if=variable.flame_shock_saturated&active_enemies>=4
actions.aoe_totemic+=/voltaic_blaze
actions.aoe_totemic+=/ice_strike,if=talent.hailstorm.enabled&!buff.ice_strike.up
actions.aoe_totemic+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up
actions.aoe_totemic+=/sundering,if=(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)&pet.surging_totem.active
actions.aoe_totemic+=/flame_shock,if=talent.molten_assault.enabled&!ticking
actions.aoe_totemic+=/fire_nova,if=active_dot.flame_shock>=3
actions.aoe_totemic+=/ice_strike
actions.aoe_totemic+=/lava_lash
actions.aoe_totemic+=/crash_lightning
actions.aoe_totemic+=/flame_shock,if=!ticking

# Multi target opener priority list for the Totemic hero talent tree
actions.aoe_totemic_open=flame_shock,if=!ticking&!variable.flame_shock_saturated
actions.aoe_totemic_open+=/lava_lash,if=!pet.surging_totem.active&!variable.flame_shock_saturated
actions.aoe_totemic_open+=/surging_totem,if=!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up
actions.aoe_totemic_open+=/totemic_recall
actions.aoe_totemic_open+=/flame_shock,if=!ticking
actions.aoe_totemic_open+=/fire_nova,if=talent.swirling_maelstrom.enabled&dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_totemic_open+=/primordial_wave,if=dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_totemic_open+=/elemental_blast,if=buff.maelstrom_weapon.stack>=10&!buff.legacy_of_the_frost_witch.up&cooldown.doom_winds.remains=0
actions.aoe_totemic_open+=/doom_winds,if=buff.legacy_of_the_frost_witch.up
actions.aoe_totemic_open+=/crash_lightning,if=(buff.electrostatic_wager.stack>9&buff.doom_winds.up)|!buff.crash_lightning.up
actions.aoe_totemic_open+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10)&(buff.doom_winds.remains<=gcd.max|!buff.doom_winds.up&cooldown.doom_winds.remains>buff.primordial_storm.remains)
actions.aoe_totemic_open+=/lava_lash,if=buff.hot_hand.up
actions.aoe_totemic_open+=/sundering,if=buff.legacy_of_the_frost_witch.up|(buff.earthen_weapon.stack>=2&buff.primordial_storm.up)
actions.aoe_totemic_open+=/lava_lash,if=(buff.legacy_of_the_frost_witch.up&buff.whirling_fire.up)
actions.aoe_totemic_open+=/crash_lightning,if=(buff.earthen_weapon.stack>=2&buff.primordial_storm.up&buff.doom_winds.up)
actions.aoe_totemic_open+=/elemental_blast,if=buff.maelstrom_weapon.stack>=10
actions.aoe_totemic_open+=/chain_lightning,if=buff.maelstrom_weapon.stack>=10
actions.aoe_totemic_open+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up&pet.searing_totem.active
actions.aoe_totemic_open+=/fire_nova,if=pet.searing_totem.active&dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_totemic_open+=/ice_strike
actions.aoe_totemic_open+=/stormstrike,if=buff.maelstrom_weapon.stack<10&!buff.legacy_of_the_frost_witch.up
actions.aoe_totemic_open+=/lava_lash
actions.aoe_totemic_open+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up&pet.searing_totem.active
actions.aoe_totemic_open+=/crash_lightning,if=talent.crashing_storms.enabled
actions.aoe_totemic_open+=/fire_nova,if=dot.flame_shock.ticking&variable.flame_shock_saturated
actions.aoe_totemic_open+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up
actions.aoe_totemic_open+=/crash_lightning
actions.aoe_totemic_open+=/ice_strike,if=talent.hailstorm.enabled&!buff.ice_strike.up
actions.aoe_totemic_open+=/elemental_blast,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up
actions.aoe_totemic_open+=/chain_lightning,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up
actions.aoe_totemic_open+=/stormstrike

# Funnel action priority list
actions.funnel=feral_spirit,if=talent.elemental_spirits.enabled
actions.funnel+=/surging_totem
actions.funnel+=/ascendance
actions.funnel+=/windstrike,if=(talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0)|buff.converging_storms.stack=buff.converging_storms.max_stack
actions.funnel+=/tempest,if=buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack|(buff.maelstrom_weapon.stack>=5&(tempest_mael_count>30|buff.awakening_storms.stack=2))
actions.funnel+=/lightning_bolt,if=variable.flame_shock_saturated&buff.primordial_wave.up&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack&(!buff.splintered_elements.up|fight_remains<=12|raid_event.adds.remains<=gcd)
actions.funnel+=/elemental_blast,if=buff.maelstrom_weapon.stack>=5&talent.elemental_spirits.enabled&feral_spirit.active>=4
actions.funnel+=/lightning_bolt,if=talent.supercharge.enabled&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack&(variable.expected_lb_funnel>variable.expected_cl_funnel)
actions.funnel+=/chain_lightning,if=(talent.supercharge.enabled&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack)|buff.arc_discharge.up&buff.maelstrom_weapon.stack>=5
actions.funnel+=/lava_lash,if=(talent.molten_assault.enabled&dot.flame_shock.ticking&!variable.flame_shock_saturated)|(talent.ashen_catalyst.enabled&buff.ashen_catalyst.stack=buff.ashen_catalyst.max_stack)
actions.funnel+=/primordial_wave,target_if=min:dot.flame_shock.remains,if=!buff.primordial_wave.up
actions.funnel+=/elemental_blast,if=(!talent.elemental_spirits.enabled|(talent.elemental_spirits.enabled&(charges=max_charges|buff.feral_spirit.up)))&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack
actions.funnel+=/feral_spirit
actions.funnel+=/doom_winds
actions.funnel+=/stormstrike,if=buff.converging_storms.stack=buff.converging_storms.max_stack
actions.funnel+=/lava_burst,if=(buff.molten_weapon.stack>buff.crackling_surge.stack)&buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack
actions.funnel+=/lightning_bolt,if=buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack&(variable.expected_lb_funnel>variable.expected_cl_funnel)
actions.funnel+=/chain_lightning,if=buff.maelstrom_weapon.stack=buff.maelstrom_weapon.max_stack
actions.funnel+=/crash_lightning,if=buff.doom_winds.up|!buff.crash_lightning.up|(talent.alpha_wolf.enabled&feral_spirit.active&alpha_wolf_min_remains=0)|(talent.converging_storms.enabled&buff.converging_storms.stack<buff.converging_storms.max_stack)
actions.funnel+=/sundering,if=buff.doom_winds.up|talent.earthsurge.enabled
actions.funnel+=/fire_nova,if=variable.flame_shock_saturated&active_enemies>=4
actions.funnel+=/ice_strike,if=talent.hailstorm.enabled&!buff.ice_strike.up
actions.funnel+=/frost_shock,if=talent.hailstorm.enabled&buff.hailstorm.up
actions.funnel+=/sundering
actions.funnel+=/flame_shock,if=talent.molten_assault.enabled&!ticking
actions.funnel+=/flame_shock,target_if=min:dot.flame_shock.remains,if=(talent.fire_nova.enabled|talent.primordial_wave.enabled)&(active_dot.flame_shock<active_enemies)&active_dot.flame_shock<6
actions.funnel+=/fire_nova,if=active_dot.flame_shock>=3
actions.funnel+=/stormstrike,if=buff.crash_lightning.up&talent.deeply_rooted_elements.enabled
actions.funnel+=/crash_lightning,if=talent.crashing_storms.enabled&buff.cl_crash_lightning.up&active_enemies>=4
actions.funnel+=/windstrike
actions.funnel+=/stormstrike
actions.funnel+=/ice_strike
actions.funnel+=/lava_lash
actions.funnel+=/crash_lightning
actions.funnel+=/fire_nova,if=active_dot.flame_shock>=2
actions.funnel+=/elemental_blast,if=(!talent.elemental_spirits.enabled|(talent.elemental_spirits.enabled&(charges=max_charges|buff.feral_spirit.up)))&buff.maelstrom_weapon.stack>=5
actions.funnel+=/lava_burst,if=(buff.molten_weapon.stack>buff.crackling_surge.stack)&buff.maelstrom_weapon.stack>=5
actions.funnel+=/lightning_bolt,if=buff.maelstrom_weapon.stack>=5&(variable.expected_lb_funnel>variable.expected_cl_funnel)
actions.funnel+=/chain_lightning,if=buff.maelstrom_weapon.stack>=5
actions.funnel+=/flame_shock,if=!ticking
actions.funnel+=/frost_shock,if=!talent.hailstorm.enabled

# Single target action priority list
actions.single=run_action_list,name=single_open,if=time<15
actions.single+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10|buff.primordial_storm.remains<=4&buff.maelstrom_weapon.stack>=5)
actions.single+=/feral_spirit,if=(cooldown.doom_winds.remains>25|cooldown.doom_winds.remains<=5)
actions.single+=/doom_winds,if=(!buff.ascendance.up|(buff.tempest.up&buff.ascendance.remains>1*gcd&buff.maelstrom_weapon.stack<=9))&set_bonus.tww3_4pc
actions.single+=/ice_strike,if=buff.tempest.up&buff.ascendance.remains>5*gcd&buff.maelstrom_weapon.stack<=1
actions.single+=/lava_lash,if=(buff.hot_hand.up&buff.ashen_catalyst.stack=buff.ashen_catalyst.max_stack)&(buff.tempest.up&buff.ascendance.remains>5*gcd&buff.maelstrom_weapon.stack<=1)
actions.single+=/flame_shock,if=!ticking&(talent.ashen_catalyst.enabled|talent.primordial_wave.enabled|talent.lashing_flames.enabled)&!buff.ascendance.up&!talent.voltaic_blaze.enabled
actions.single+=/windstrike,if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0&ti_lightning_bolt
actions.single+=/doom_winds
actions.single+=/primordial_wave,if=dot.flame_shock.ticking&(raid_event.adds.in>action.primordial_wave.cooldown|raid_event.adds.in<6)
actions.single+=/ice_strike,if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=8
actions.single+=/voltaic_blaze,if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=6
actions.single+=/frost_shock,if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=6&buff.hailstorm.stack=10&buff.ice_strike.up&talent.swirling_maelstrom.enabled
actions.single+=/natures_swiftness,if=buff.tempest.up&tww3_procs_to_asc=1&buff.maelstrom_weapon.stack<=4
actions.single+=/tempest,if=(buff.maelstrom_weapon.stack>=5|buff.natures_swiftness.up)&(buff.tempest.up&tww3_procs_to_asc=1|buff.tempest.max_stack&cooldown.ascendance.remains<=2&talent.ascendance.enabled)&set_bonus.tww3_4pc
actions.single+=/ascendance,if=(dot.flame_shock.ticking|!talent.primordial_wave.enabled|!talent.ashen_catalyst.enabled)
actions.single+=/tempest,if=((buff.maelstrom_weapon.stack>=5)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=5))&(buff.tempest.stack=buff.tempest.max_stack&(tempest_mael_count>30|buff.awakening_storms.stack=3))
actions.single+=/elemental_blast,if=buff.maelstrom_weapon.stack>=5&tww3_procs_to_asc=1&((tempest_mael_count+buff.maelstrom_weapon.stack)>=40)&!buff.tempest.up
actions.single+=/elemental_blast,if=((!talent.overflowing_maelstrom.enabled&buff.maelstrom_weapon.stack>=5)|(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8))&(charges_fractional>=1.6|set_bonus.tww2_4pc)
actions.single+=/stormstrike,if=charges_fractional>=2&(buff.maelstrom_weapon.stack<=6)&!buff.tempest.up&tww3_procs_to_asc=1
actions.single+=/tempest,if=(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8)
actions.single+=/elemental_blast,if=((!talent.overflowing_maelstrom.enabled&buff.maelstrom_weapon.stack>=5)|(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8))&!buff.arc_discharge.up
actions.single+=/lightning_bolt,if=(buff.maelstrom_weapon.stack>=9&talent.ascendance.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=8)
actions.single+=/windstrike,if=!talent.thorims_invocation.enabled
actions.single+=/stormstrike,if=!buff.tempest.up&tww3_procs_to_asc=1
actions.single+=/crash_lightning,if=(buff.doom_winds.up&buff.electrostatic_wager.stack>1)|buff.electrostatic_wager.stack>8
actions.single+=/ice_strike,if=(buff.tempest.up|(tempest_mael_count>=30&buff.tempest.up))&tww3_procs_to_asc=1
actions.single+=/voltaic_blaze,if=tempest_mael_count>=30&tww3_procs_to_asc=1
actions.single+=/stormstrike,if=buff.doom_winds.up|buff.stormblast.stack>0
actions.single+=/crash_lightning,if=(talent.unrelenting_storms.enabled&talent.alpha_wolf.enabled&alpha_wolf_min_remains=0)|set_bonus.tww2_4pc
actions.single+=/voltaic_blaze,if=dot.flame_shock.remains<=4
actions.single+=/ice_strike
actions.single+=/stormstrike,if=charges_fractional>=1.8
actions.single+=/lava_lash,if=(talent.lashing_flames.enabled&(debuff.lashing_flames.remains<2))
actions.single+=/voltaic_blaze
actions.single+=/stormstrike
actions.single+=/crash_lightning,if=talent.unrelenting_storms.enabled
actions.single+=/elemental_blast,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up
actions.single+=/lightning_bolt,if=buff.maelstrom_weapon.stack>=5&!buff.primordial_storm.up
actions.single+=/lava_lash,if=talent.elemental_assault.enabled&talent.molten_assault.enabled&dot.flame_shock.ticking
actions.single+=/sundering
actions.single+=/lava_lash
actions.single+=/frost_shock,if=buff.hailstorm.up
actions.single+=/flame_shock,if=!ticking
actions.single+=/sundering,if=raid_event.adds.in>=action.sundering.cooldown
actions.single+=/crash_lightning
actions.single+=/frost_shock
actions.single+=/fire_nova,if=active_dot.flame_shock
actions.single+=/earth_elemental
actions.single+=/flame_shock

# Single target opener priority list
actions.single_open=flame_shock,if=!ticking
actions.single_open+=/voltaic_blaze,if=active_dot.flame_shock<3&!buff.ascendance.up
actions.single_open+=/primordial_wave,if=(buff.maelstrom_weapon.stack>=4)&dot.flame_shock.ticking
actions.single_open+=/feral_spirit,if=buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled
actions.single_open+=/doom_winds,if=buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled
actions.single_open+=/ascendance,if=(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)&(buff.maelstrom_weapon.stack>=6|!set_bonus.tww3_4pc)
actions.single_open+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10)&(buff.legacy_of_the_frost_witch.up|!talent.legacy_of_the_frost_witch.enabled)
actions.single_open+=/windstrike
actions.single_open+=/elemental_blast,if=((buff.maelstrom_weapon.stack>=5&!talent.deeply_rooted_elements.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=7))&(!buff.legacy_of_the_frost_witch.up|buff.ascendance.up|talent.deeply_rooted_elements.enabled)
actions.single_open+=/tempest,if=((buff.maelstrom_weapon.stack>=5&!talent.deeply_rooted_elements.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=7))&(!buff.legacy_of_the_frost_witch.up|buff.ascendance.up|talent.deeply_rooted_elements.enabled)
actions.single_open+=/lightning_bolt,if=((buff.maelstrom_weapon.stack>=5&!talent.deeply_rooted_elements.enabled)|(talent.deeply_rooted_elements.enabled&buff.maelstrom_weapon.stack>=7))&(!buff.legacy_of_the_frost_witch.up|buff.ascendance.up|talent.deeply_rooted_elements.enabled)
actions.single_open+=/ice_strike
actions.single_open+=/stormstrike
actions.single_open+=/crash_lightning,if=set_bonus.tww2_4pc
actions.single_open+=/voltaic_blaze
actions.single_open+=/lava_lash

# Single target action priority list for the Totemic hero talent tree
actions.single_totemic=run_action_list,name=single_totemic_open,if=time<20
actions.single_totemic+=/surging_totem
actions.single_totemic+=/ascendance,if=ti_lightning_bolt&pet.surging_totem.remains>4&(buff.totemic_rebound.stack>=3|buff.maelstrom_weapon.stack>0)
actions.single_totemic+=/flame_shock,if=!ticking&(talent.ashen_catalyst.enabled|talent.primordial_wave.enabled)
actions.single_totemic+=/lava_lash,if=buff.hot_hand.up
actions.single_totemic+=/totemic_recall,if=(!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up)&pet.surging_totem.remains>=10
actions.single_totemic+=/feral_spirit,if=((cooldown.doom_winds.remains>23|cooldown.doom_winds.remains<7)&(cooldown.primordial_wave.remains<20|buff.primordial_storm.up|!talent.primordial_storm.enabled))
actions.single_totemic+=/primordial_wave,if=dot.flame_shock.ticking&(raid_event.adds.in>action.primordial_wave.cooldown)|raid_event.adds.in<6
actions.single_totemic+=/doom_winds,if=buff.legacy_of_the_frost_witch.up
actions.single_totemic+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10)&((cooldown.doom_winds.remains>=buff.primordial_storm.remains)|buff.doom_winds.up|!talent.doom_winds.enabled|(buff.primordial_storm.remains<2*gcd))
actions.single_totemic+=/sundering,if=buff.ascendance.up&pet.surging_totem.active&talent.earthsurge.enabled&buff.legacy_of_the_frost_witch.up&buff.totemic_rebound.stack>=5&buff.earthen_weapon.stack>=2
actions.single_totemic+=/windstrike,if=talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>0&ti_lightning_bolt
actions.single_totemic+=/sundering,if=buff.legacy_of_the_frost_witch.up&((cooldown.ascendance.remains>=10&talent.ascendance.enabled)|!talent.ascendance.enabled)&pet.surging_totem.active&buff.totemic_rebound.stack>=3&!buff.ascendance.up
actions.single_totemic+=/crash_lightning,if=talent.unrelenting_storms.enabled&talent.alpha_wolf.enabled&alpha_wolf_min_remains=0
actions.single_totemic+=/lava_burst,if=!talent.thorims_invocation.enabled&buff.maelstrom_weapon.stack>=10&buff.whirling_air.down
actions.single_totemic+=/elemental_blast,if=(buff.maelstrom_weapon.stack>=10)&(buff.primordial_storm.down|buff.primordial_storm.remains>4)
actions.single_totemic+=/stormstrike,if=buff.doom_winds.up&buff.legacy_of_the_frost_witch.up
actions.single_totemic+=/lightning_bolt,if=(buff.maelstrom_weapon.stack>=10)&(buff.primordial_storm.down|buff.primordial_storm.remains>4)
actions.single_totemic+=/crash_lightning,if=buff.electrostatic_wager.stack>4
actions.single_totemic+=/stormstrike,if=buff.doom_winds.up|buff.stormblast.stack>1
actions.single_totemic+=/lava_lash,if=buff.whirling_fire.up|buff.ashen_catalyst.stack>=8
actions.single_totemic+=/windstrike
actions.single_totemic+=/stormstrike
actions.single_totemic+=/lava_lash
actions.single_totemic+=/crash_lightning,if=set_bonus.tww2_4pc
actions.single_totemic+=/voltaic_blaze
actions.single_totemic+=/crash_lightning,if=talent.unrelenting_storms.enabled
actions.single_totemic+=/ice_strike,if=!buff.ice_strike.up
actions.single_totemic+=/crash_lightning
actions.single_totemic+=/frost_shock
actions.single_totemic+=/fire_nova,if=active_dot.flame_shock
actions.single_totemic+=/earth_elemental
actions.single_totemic+=/flame_shock,if=!talent.voltaic_blaze.enabled

# Single target opener priority list for the Totemic hero talent tree
actions.single_totemic_open=flame_shock,if=!ticking
actions.single_totemic_open+=/lava_lash,if=!pet.surging_totem.active&talent.lashing_flames.enabled&debuff.lashing_flames.down
actions.single_totemic_open+=/surging_totem,if=!buff.whirling_air.up&!buff.whirling_fire.up&!buff.whirling_earth.up
actions.single_totemic_open+=/totemic_recall
actions.single_totemic_open+=/primordial_wave
actions.single_totemic_open+=/feral_spirit,if=buff.legacy_of_the_frost_witch.up
actions.single_totemic_open+=/lava_lash,if=buff.hot_hand.up|(buff.whirling_fire.up&cooldown.surging_totem.up&!buff.doom_winds.remains<=2)
actions.single_totemic_open+=/primordial_storm,if=buff.doom_winds.up&buff.maelstrom_weapon.max_stack&buff.legacy_of_the_frost_witch.up|(buff.primordial_storm.remains<=3&buff.maelstrom_weapon.max_stack)
actions.single_totemic_open+=/doom_winds,if=buff.legacy_of_the_frost_witch.up
actions.single_totemic_open+=/stormstrike,if=buff.doom_winds.up&buff.legacy_of_the_frost_witch.up
actions.single_totemic_open+=/sundering,if=buff.legacy_of_the_frost_witch.up
actions.single_totemic_open+=/elemental_blast,if=buff.maelstrom_weapon.stack=10
actions.single_totemic_open+=/lightning_bolt,if=buff.maelstrom_weapon.stack=10
actions.single_totemic_open+=/stormstrike
actions.single_totemic_open+=/lava_lash
```
