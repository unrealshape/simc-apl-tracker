# APL Changelog – 2026-10-23

Generated: 2026-10-23 08:25 UTC

## Mage

### Fire
File: `apl/default/mage/fire.simc`

Changes:
  + `actions.precombat+=/use_item,name=stormbound_emblem_of_dazar,if=!equipped.vile_vial_of_volatile_venom|active_enemies<3`
  - `actions.sf_filler+=/scorch,if=talent.scald&scorch_execute.active|buff.heat_shimmer.react&(firestarter.active|prev_gcd.1.pyroblast|prev_gcd.1.flamestrike)`
  + `actions.sf_filler+=/scorch,if=talent.scald&scorch_execute.active|buff.heat_shimmer.react&(firestarter.active|prev_gcd.1.pyroblast|prev_gcd.1.flamestrike|active_enemies<variable.sf_filler_flamestrike)`

