# Death Knight – Blood

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:18 UTC

Source: `apl/default/deathknight/blood.simc`

---

## Overview

- **Action Lists:** 6
- **Total Actions:** 70
- **Lists:** `precombat`, `default`, `deathbringer`, `high_prio_actions`, `san_drw`, `sanlayn`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `deaths_caress` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `use_item` | name=tome_of_lights_devotion,if=buff.inner_resilience.up,use_off_gcd=1 |
| 3 | `use_item` | name=unyielding_netherprism,if=cooldown.dancing_rune_weapon.remains<1\|target.time_to_die<=20,use_off_gcd=1 |
| 4 | `use_items` | — |
| 5 | `use_item` | name=bestinslots,use_off_gcd=1 |
| 6 | `blood_fury` | if=buff.dancing_rune_weapon.up |
| 7 | `berserking` | if=buff.dancing_rune_weapon.up |
| 8 | `ancestral_call` | if=buff.dancing_rune_weapon.up |
| 9 | `fireblood` | if=buff.dancing_rune_weapon.up |
| 10 | `potion` | if=buff.dancing_rune_weapon.up |
| 11 | `vampiric_blood` | if=!buff.vampiric_blood.up |
| 12 | `call_action_list` | name=high_prio_actions |
| 13 | `run_action_list` | name=deathbringer,if=hero_tree.deathbringer |
| 14 | `run_action_list` | name=san_drw,if=hero_tree.sanlayn&buff.dancing_rune_weapon.up |
| 15 | `run_action_list` | name=sanlayn,if=hero_tree.sanlayn |

## Action List: `deathbringer`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `rune_tap` | if=rune>4 |
| 2 | `bonestorm` | if=buff.bone_shield.stack>=5&buff.death_and_decay.remains |
| 3 | `death_strike` | if=(runic_power.deficit<20\|(runic_power.deficit<26&buff.dancing_rune_weapon.up)) |
| 4 | `soul_reaper` | if=active_enemies<=2&buff.reaper_of_souls.up&target.time_to_die>(dot.soul_reaper.remains+5) |
| 5 | `soul_reaper` | if=active_enemies<=2&target.time_to_pct_35<5&target.time_to_die>(dot.soul_reaper.remains+5) |
| 6 | `reapers_mark` | — |
| 7 | `blood_boil` | if=buff.dancing_rune_weapon.up&!drw.bp_ticking |
| 8 | `death_and_decay` | if=!buff.death_and_decay.up |
| 9 | `marrowrend` | if=buff.exterminate.up\|(buff.bone_shield.stack<5&!dot.bonestorm.ticking) |
| 10 | `death_strike` | — |
| 11 | `tombstone` | if=buff.bone_shield.stack>=8&buff.death_and_decay.remains&cooldown.dancing_rune_weapon.remains>=25 |
| 12 | `blooddrinker` | if=!buff.dancing_rune_weapon.up&active_enemies<=2&buff.coagulopathy.remains>3 |
| 13 | `consumption` | — |
| 14 | `blood_boil` | — |
| 15 | `heart_strike` | if=buff.coagulopathy.stack<5 |
| 16 | `heart_strike` | — |
| 17 | `soul_reaper` | if=buff.reaper_of_souls.up |
| 18 | `arcane_torrent` | if=runic_power.deficit>20 |

## Action List: `high_prio_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `raise_dead` | use_off_gcd=1 |
| 2 | `blood_tap` | if=(rune<=2&rune.time_to_3>gcd&charges_fractional>=1.8) |
| 3 | `blood_tap` | if=(rune<=1&rune.time_to_3>gcd) |
| 4 | `death_strike` | if=buff.coagulopathy.up&buff.coagulopathy.remains<=gcd |
| 5 | `dancing_rune_weapon` | — |

## Action List: `san_drw`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `heart_strike` | if=buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains |
| 2 | `bonestorm` | if=buff.bone_shield.stack>=5 |
| 3 | `death_strike` | if=runic_power.deficit<36 |
| 4 | `blood_boil` | if=!drw.bp_ticking |
| 5 | `any_dnd` | if=(active_enemies<=3&buff.crimson_scourge.remains)\|(active_enemies>3&!buff.death_and_decay.remains) |
| 6 | `heart_strike` | — |
| 7 | `death_strike` | — |
| 8 | `consumption` | — |
| 9 | `blood_boil` | — |

## Action List: `sanlayn`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blood_boil` | if=(!buff.bone_shield.up\|buff.bone_shield.remains<1.5\|buff.bone_shield.stack<=1)&active_enemies>=2 |
| 2 | `deaths_caress` | if=!buff.bone_shield.up\|buff.bone_shield.remains<1.5\|buff.bone_shield.stack<=1 |
| 3 | `blood_boil` | if=dot.blood_plague.remains<3 |
| 4 | `heart_strike` | if=(buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains&buff.vampiric_strike.remains) |
| 5 | `bonestorm` | if=buff.bone_shield.stack>=5&(buff.death_and_decay.remains\|active_enemies<=3) |
| 6 | `death_strike` | if=runic_power.deficit<20 |
| 7 | `consumption` | if=buff.infliction_of_sorrow.up&buff.death_and_decay.up |
| 8 | `heart_strike` | if=(buff.infliction_of_sorrow.up\|buff.vampiric_strike.up)&buff.death_and_decay.up |
| 9 | `soul_reaper` | if=active_enemies<=2&target.time_to_pct_35<5&target.time_to_die>(dot.soul_reaper.remains+5) |
| 10 | `blood_boil` | if=buff.bone_shield.stack<6&!dot.bonestorm.ticking&active_enemies>=2 |
| 11 | `deaths_caress` | if=buff.bone_shield.stack<6&!dot.bonestorm.ticking |
| 12 | `marrowrend` | if=buff.bone_shield.stack<6&!dot.bonestorm.ticking |
| 13 | `tombstone` | if=buff.bone_shield.stack>=6&(buff.death_and_decay.remains\|active_enemies<=3)&cooldown.dancing_rune_weapon.remains>=25 |
| 14 | `any_dnd` | if=(active_enemies<=3&buff.crimson_scourge.remains)\|(active_enemies>3&!buff.death_and_decay.remains) |
| 15 | `blooddrinker` | if=active_enemies<=2&buff.coagulopathy.remains>3 |
| 16 | `heart_strike` | if=buff.vampiric_strike.up |
| 17 | `death_strike` | — |
| 18 | `heart_strike` | if=rune>=2 |
| 19 | `consumption` | — |
| 20 | `blood_boil` | — |
| 21 | `heart_strike` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
# Default consumables otion=tempered_potion_ lask=flask_of_alchemical_chaos_ ood=beledars_bount ugmentation=crystallize emporary_enchant=main_hand:algari_mana_oil_
actions.precombat=snapshot_stats
actions.precombat+=/deaths_caress

# Executed every time the actor is available.
actions=auto_attack
actions+=/use_item,name=tome_of_lights_devotion,if=buff.inner_resilience.up,use_off_gcd=1
actions+=/use_item,name=unyielding_netherprism,if=cooldown.dancing_rune_weapon.remains<1|target.time_to_die<=20,use_off_gcd=1
actions+=/use_items
actions+=/use_item,name=bestinslots,use_off_gcd=1
actions+=/blood_fury,if=buff.dancing_rune_weapon.up
actions+=/berserking,if=buff.dancing_rune_weapon.up
actions+=/ancestral_call,if=buff.dancing_rune_weapon.up
actions+=/fireblood,if=buff.dancing_rune_weapon.up
actions+=/potion,if=buff.dancing_rune_weapon.up
actions+=/vampiric_blood,if=!buff.vampiric_blood.up
actions+=/call_action_list,name=high_prio_actions
actions+=/run_action_list,name=deathbringer,if=hero_tree.deathbringer
actions+=/run_action_list,name=san_drw,if=hero_tree.sanlayn&buff.dancing_rune_weapon.up
actions+=/run_action_list,name=sanlayn,if=hero_tree.sanlayn

actions.deathbringer=rune_tap,if=rune>4
actions.deathbringer+=/bonestorm,if=buff.bone_shield.stack>=5&buff.death_and_decay.remains
actions.deathbringer+=/death_strike,if=(runic_power.deficit<20|(runic_power.deficit<26&buff.dancing_rune_weapon.up))
actions.deathbringer+=/soul_reaper,if=active_enemies<=2&buff.reaper_of_souls.up&target.time_to_die>(dot.soul_reaper.remains+5)
actions.deathbringer+=/soul_reaper,if=active_enemies<=2&target.time_to_pct_35<5&target.time_to_die>(dot.soul_reaper.remains+5)
actions.deathbringer+=/reapers_mark
actions.deathbringer+=/blood_boil,if=buff.dancing_rune_weapon.up&!drw.bp_ticking
actions.deathbringer+=/death_and_decay,if=!buff.death_and_decay.up
actions.deathbringer+=/marrowrend,if=buff.exterminate.up|(buff.bone_shield.stack<5&!dot.bonestorm.ticking)
actions.deathbringer+=/death_strike
actions.deathbringer+=/tombstone,if=buff.bone_shield.stack>=8&buff.death_and_decay.remains&cooldown.dancing_rune_weapon.remains>=25
actions.deathbringer+=/blooddrinker,if=!buff.dancing_rune_weapon.up&active_enemies<=2&buff.coagulopathy.remains>3
actions.deathbringer+=/consumption
actions.deathbringer+=/blood_boil
actions.deathbringer+=/heart_strike,if=buff.coagulopathy.stack<5
actions.deathbringer+=/heart_strike
actions.deathbringer+=/soul_reaper,if=buff.reaper_of_souls.up
actions.deathbringer+=/arcane_torrent,if=runic_power.deficit>20

actions.high_prio_actions=raise_dead,use_off_gcd=1
actions.high_prio_actions+=/blood_tap,if=(rune<=2&rune.time_to_3>gcd&charges_fractional>=1.8)
actions.high_prio_actions+=/blood_tap,if=(rune<=1&rune.time_to_3>gcd)
actions.high_prio_actions+=/death_strike,if=buff.coagulopathy.up&buff.coagulopathy.remains<=gcd
actions.high_prio_actions+=/dancing_rune_weapon

actions.san_drw=heart_strike,if=buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains
actions.san_drw+=/bonestorm,if=buff.bone_shield.stack>=5
actions.san_drw+=/death_strike,if=runic_power.deficit<36
actions.san_drw+=/blood_boil,if=!drw.bp_ticking
actions.san_drw+=/any_dnd,if=(active_enemies<=3&buff.crimson_scourge.remains)|(active_enemies>3&!buff.death_and_decay.remains)
actions.san_drw+=/heart_strike
actions.san_drw+=/death_strike
actions.san_drw+=/consumption
actions.san_drw+=/blood_boil

actions.sanlayn=blood_boil,if=(!buff.bone_shield.up|buff.bone_shield.remains<1.5|buff.bone_shield.stack<=1)&active_enemies>=2
actions.sanlayn+=/deaths_caress,if=!buff.bone_shield.up|buff.bone_shield.remains<1.5|buff.bone_shield.stack<=1
actions.sanlayn+=/blood_boil,if=dot.blood_plague.remains<3
actions.sanlayn+=/heart_strike,if=(buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains&buff.vampiric_strike.remains)
actions.sanlayn+=/bonestorm,if=buff.bone_shield.stack>=5&(buff.death_and_decay.remains|active_enemies<=3)
actions.sanlayn+=/death_strike,if=runic_power.deficit<20
actions.sanlayn+=/consumption,if=buff.infliction_of_sorrow.up&buff.death_and_decay.up
actions.sanlayn+=/heart_strike,if=(buff.infliction_of_sorrow.up|buff.vampiric_strike.up)&buff.death_and_decay.up
actions.sanlayn+=/soul_reaper,if=active_enemies<=2&target.time_to_pct_35<5&target.time_to_die>(dot.soul_reaper.remains+5)
actions.sanlayn+=/blood_boil,if=buff.bone_shield.stack<6&!dot.bonestorm.ticking&active_enemies>=2
actions.sanlayn+=/deaths_caress,if=buff.bone_shield.stack<6&!dot.bonestorm.ticking
actions.sanlayn+=/marrowrend,if=buff.bone_shield.stack<6&!dot.bonestorm.ticking
actions.sanlayn+=/tombstone,if=buff.bone_shield.stack>=6&(buff.death_and_decay.remains|active_enemies<=3)&cooldown.dancing_rune_weapon.remains>=25
actions.sanlayn+=/any_dnd,if=(active_enemies<=3&buff.crimson_scourge.remains)|(active_enemies>3&!buff.death_and_decay.remains)
actions.sanlayn+=/blooddrinker,if=active_enemies<=2&buff.coagulopathy.remains>3
actions.sanlayn+=/heart_strike,if=buff.vampiric_strike.up
actions.sanlayn+=/death_strike
actions.sanlayn+=/heart_strike,if=rune>=2
actions.sanlayn+=/consumption
actions.sanlayn+=/blood_boil
actions.sanlayn+=/heart_strike
```
