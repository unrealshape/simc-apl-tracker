# APL Changelog – 2026-10-15

Generated: 2026-10-15 08:09 UTC

## Shaman

### Enhancement
File: `apl/default/shaman/enhancement.simc`

Changes:
  - `actions.single_sb+=/lava_lash,if=!debuff.lashing_flames.up&time<5`
  - `actions.single_sb+=/voltaic_blaze,if=set_bonus.midnight_season_2_2pc`
  + `actions.single_sb+=/voltaic_blaze,if=set_bonus.midnight_season_2_2pc&buff.maelstrom_weapon.stack<9`
  + `actions.single_sb+=/lava_lash,if=!debuff.lashing_flames.up&time<5`
  - `actions.single_sb+=/ascendance,if=raid_event.adds.in>=60|fight_remains<=20`
  + `actions.single_sb+=/ascendance,if=(raid_event.adds.in>=60|fight_remains<=20)&!buff.doom_winds.up`
  + `actions.single_sb+=/tempest,if=buff.maelstrom_weapon.stack>=8&(cooldown.voltaic_blaze.remains<=gcd.max|cooldown.crash_lightning.remains<=gcd.max)`
  + `actions.single_sb+=/lightning_bolt,if=buff.maelstrom_weapon.stack>=8&(cooldown.voltaic_blaze.remains<=gcd.max|cooldown.crash_lightning.remains<=gcd.max)`

