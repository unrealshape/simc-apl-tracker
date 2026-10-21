# APL Changelog – 2026-10-21

Generated: 2026-10-21 08:27 UTC

## Rogue

### Outlaw
File: `apl/default/rogue/outlaw.simc`

Changes:
  - `actions.build+=/blade_flurry,if=talent.deft_maneuvers&spell_targets>=3`
  + `actions.build+=/blade_flurry,if=talent.deft_maneuvers&spell_targets>=3-(combo_points.deficit=2)`
  - `actions.cds+=/roll_the_bones,if=!buff.roll_the_bones.up|rtb_buffs=1+(buff.loaded_dice.up&cooldown.between_the_eyes.ready)`
  - `actions.cds+=/blade_rush,if=set_bonus.mid1_2pc|spell_targets=1&energy.base_time_to_max>2|spell_targets>=2`
  + `actions.cds+=/roll_the_bones,if=!buff.roll_the_bones.up|rtb_buffs=1+buff.loaded_dice.up&talent.keep_it_rolling`
  + `actions.cds+=/blade_rush,if=set_bonus.mid1_2pc|spell_targets>=3|!buff.adrenaline_rush.up&talent.menacing_rush`

