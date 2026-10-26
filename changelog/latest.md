# APL Changelog – 2026-10-26

Generated: 2026-10-26 08:44 UTC

## Shaman

### Enhancement
File: `apl/default/shaman/enhancement.simc`

Changes:
  - `actions.cooldowns+=/blood_fury,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.blood_fury.cooldown<=action.blood_fury.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  - `actions.cooldowns+=/berserking,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.berserking.cooldown<=action.berserking.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  - `actions.cooldowns+=/fireblood,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.fireblood.cooldown<=action.fireblood.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  - `actions.cooldowns+=/ancestral_call,if=(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active|(fight_remains%%action.ancestral_call.cooldown<=action.ancestral_call.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  - `actions.cooldowns+=/invoke_external_buff,name=power_infusion,if=((talent.deeply_rooted_elements.enabled&buff.ascendance.remains>7.5)|(!talent.deeply_rooted_elements.enabled&(buff.ascendance.up|buff.doom_winds.up|pet.surging_totem.active))|(fight_remains%%120<=20)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)|cooldown.ascendance.remains<gcd.max)`
  + `actions.cooldowns+=/blood_fury,if=(buff.ascendance.up|buff.doom_winds.up|(fight_remains%%action.blood_fury.cooldown<=action.blood_fury.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  + `actions.cooldowns+=/berserking,if=(buff.ascendance.up|buff.doom_winds.up|(fight_remains%%action.berserking.cooldown<=action.berserking.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  + `actions.cooldowns+=/fireblood,if=(buff.ascendance.up|buff.doom_winds.up|(fight_remains%%action.fireblood.cooldown<=action.fireblood.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  + `actions.cooldowns+=/ancestral_call,if=(buff.ascendance.up|buff.doom_winds.up|(fight_remains%%action.ancestral_call.cooldown<=action.ancestral_call.duration)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled))`
  + `actions.cooldowns+=/invoke_external_buff,name=power_infusion,if=((talent.deeply_rooted_elements.enabled&buff.ascendance.remains>7.5)|(!talent.deeply_rooted_elements.enabled&(buff.ascendance.up|buff.doom_winds.up))|(fight_remains%%120<=20)|(!talent.ascendance.enabled&!talent.doom_winds.enabled&!talent.surging_totem.enabled)|cooldown.ascendance.remains<gcd.max)`
  - `actions.single_totemic=voltaic_blaze,if=dot.flame_shock.remains=0`
  + `actions.single_totemic=surging_totem,if=raid_event.adds.in>=30|fight_remains<=30`
  + `actions.single_totemic+=/crash_lightning,if=action.voltaic_blaze.ready&!dot.flame_shock.ticking`
  + `actions.single_totemic+=/voltaic_blaze,if=!dot.flame_shock.ticking`
  - `actions.single_totemic+=/surging_totem,if=raid_event.adds.in>=30|fight_remains<=30`
  + `actions.single_totemic+=/voltaic_blaze,if=set_bonus.midnight_season_2_2pc&(!buff.doom_winds.up|buff.maelstrom_weapon.stack<8)`
  + `actions.single_totemic+=/primordial_storm,if=buff.bloodlust.up&buff.maelstrom_weapon.stack>=9`
  - `actions.single_totemic+=/voltaic_blaze,if=set_bonus.midnight_season_2_2pc`
  - `actions.single_totemic+=/crash_lightning,if=!buff.crash_lightning.up|talent.storm_unleashed.enabled`
  - `actions.single_totemic+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10|buff.primordial_storm.remains<3.5&buff.maelstrom_weapon.stack>=5)`
  + `actions.single_totemic+=/crash_lightning,if=!buff.crash_lightning.up|talent.storm_unleashed.enabled|(talent.thorims_invocation.enabled&(buff.doom_winds.up|buff.ascendance.up))`
  - `actions.single_totemic+=/crash_lightning,if=talent.thorims_invocation.enabled&buff.doom_winds.up|buff.ascendance.up`
  + `actions.single_totemic+=/primordial_storm,if=(buff.maelstrom_weapon.stack>=10|buff.primordial_storm.remains<3.5&buff.maelstrom_weapon.stack>=5)`
  - `actions.single_totemic+=/lightning_bolt,if=talent.elemental_tempo.enabled&(buff.maelstrom_weapon.stack>=5&(cooldown.lava_lash.remains>gcd.max)&(cooldown.lava_lash.remains<=buff.maelstrom_weapon.stack*0.3)|buff.maelstrom_weapon.stack>=10)`
  - `actions.single_totemic+=/crash_lightning,if=!buff.crash_lightning.up`
  + `actions.single_totemic+=/lightning_bolt,if=talent.elemental_tempo.enabled&buff.hot_hand.up&buff.maelstrom_weapon.stack>=9&(cooldown.lava_lash.remains>gcd.max)&(cooldown.lava_lash.remains<=buff.maelstrom_weapon.stack*0.3)`
  - `actions.single_totemic+=/sundering,if=cooldown.surging_totem.remains>25`

