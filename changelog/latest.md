# APL Changelog – 2026-10-29

Generated: 2026-10-29 09:44 UTC

## Warrior

### Arms
File: `apl/assisted_combat/warrior/arms.simc`

Changes:
  - `actions.assisted_combat+=/cleave,if=!dot.rend.ticking&talent.rend&active_enemies>3`
  - `actions.assisted_combat+=/rend,if=!dot.rend.ticking`
  + `actions.assisted_combat+=/cleave,if=!dot.rend_dot.ticking&talent.rend&active_enemies>3`
  + `actions.assisted_combat+=/rend,if=!dot.rend_dot.ticking`

### Fury
File: `apl/assisted_combat/warrior/fury.simc`

Changes:
  - `actions.assisted_combat+=/thunder_clap,if=!dot.rend.ticking&talent.storm_of_blood&talent.crashing_thunder`
  - `actions.assisted_combat+=/whirlwind,if=!dot.rend.ticking&talent.storm_of_blood`
  + `actions.assisted_combat+=/thunder_clap,if=!dot.rend_dot.ticking&talent.storm_of_blood&talent.crashing_thunder`
  + `actions.assisted_combat+=/whirlwind,if=!dot.rend_dot.ticking&talent.storm_of_blood`

