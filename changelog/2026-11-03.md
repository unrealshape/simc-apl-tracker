# APL Changelog – 2026-11-03

Generated: 2026-11-03 10:41 UTC

## Hunter

### Marksmanship
File: `apl/default/hunter/marksmanship.simc`

Changes:
  + `actions.drst+=/aimed_shot,if=buff.volley.up&talent.aspect_of_the_hydra&buff.trick_shots.remains>cast_time`
  + `actions.sentst+=/aimed_shot,target_if=max:debuff.sentinels_mark.up,if=buff.volley.up&talent.aspect_of_the_hydra&buff.trick_shots.remains>cast_time&active_enemies>2`

