# APL Changelog – 2026-10-24

Generated: 2026-10-24 08:01 UTC

## Hunter

### Survival
File: `apl/default/hunter/survival.simc`

Changes:
  + `actions.cds+=/use_item,name=voracious_heart_of_ulatek`
  - `actions.cds+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&!equipped.font_of_venomous_rage`
  + `actions.cds+=/use_items,check_existing=0,slots=trinket1:trinket2,if=this_trinket.has_use_damage&!this_trinket.is.font_of_venomous_rage`

