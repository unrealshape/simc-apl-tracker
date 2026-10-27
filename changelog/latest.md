# APL Changelog – 2026-10-27

Generated: 2026-10-27 08:50 UTC

## Hunter

### Marksmanship
File: `apl/default/hunter/marksmanship.simc`

Changes:
  - `actions=variable,name=trueshot_ready,value=!talent.bullseye|(fight_remains>cooldown.trueshot.duration+10|buff.bullseye.stack=buff.bullseye.max_stack)&(cooldown.explosive_shot.remains>=15|cooldown.explosive_shot.ready)|fight_remains<25|time<10`
  + `actions=variable,name=trueshot_ready,value=!talent.bullseye|(fight_remains>cooldown.trueshot.duration+10|buff.bullseye.stack=buff.bullseye.max_stack|target.time_to_pct_20>60)&(cooldown.explosive_shot.remains>=15|cooldown.explosive_shot.ready)|fight_remains<25|time<10`

