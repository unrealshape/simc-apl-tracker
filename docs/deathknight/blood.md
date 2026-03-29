# Death Knight – Blood

Auto-generated from SimulationCraft APL | Last updated: 2026-03-29 05:16 UTC

Source: `apl/default/deathknight/blood.simc`

---

## Overview

- **Action Lists:** 6
- **Total Actions:** 54
- **Lists:** `precombat`, `default`, `deathbringer`, `high_prio_actions`, `san_gift`, `sanlayn`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `deaths_caress` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `use_items` | — |
| 3 | `use_item` | name=light_company_guidon,use_off_gcd=1,if=cooldown.dancing_rune_weapon.remains>78\|fight_remains<15 |
| 4 | `use_item` | name=algethar_puzzle_box,if=fight_remains>122\|cooldown.dancing_rune_weapon.remains>78\|fight_remains<25 |
| 5 | `fireblood` | if=fight_remains>120\|cooldown.dancing_rune_weapon.remains>78\|fight_remains<8 |
| 6 | `blood_fury` | if=fight_remains>120\|cooldown.dancing_rune_weapon.remains>78\|fight_remains<12 |
| 7 | `berserking` | if=cooldown.dancing_rune_weapon.remains>78\|fight_remains<=15 |
| 8 | `ancestral_call` | if=fight_remains>120\|cooldown.dancing_rune_weapon.remains>78\|fight_remains<15 |
| 9 | `potion` | if=cooldown.dancing_rune_weapon.remains>78\|fight_remains<=30 |
| 10 | `vampiric_blood` | if=!buff.vampiric_blood.up |
| 11 | `call_action_list` | name=high_prio_actions |
| 12 | `run_action_list` | name=deathbringer,if=hero_tree.deathbringer |
| 13 | `run_action_list` | name=san_gift,if=hero_tree.sanlayn&buff.gift_of_the_sanlayn.up |
| 14 | `run_action_list` | name=sanlayn,if=hero_tree.sanlayn |

## Action List: `deathbringer`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `death_strike` | if=(runic_power.deficit<20\|(runic_power.deficit<26&buff.dancing_rune_weapon.up)) |
| 2 | `death_and_decay` | if=!buff.death_and_decay.up |
| 3 | `reapers_mark` | — |
| 4 | `marrowrend` | if=buff.exterminate.up |
| 5 | `deaths_caress` | if=(!buff.bone_shield.up\|buff.bone_shield.remains<3\|buff.bone_shield.stack<6)&rune<4 |
| 6 | `marrowrend` | if=!buff.bone_shield.up\|buff.bone_shield.remains<3\|buff.bone_shield.stack<6 |
| 7 | `death_strike` | — |
| 8 | `blood_boil` | — |
| 9 | `consumption` | empower_to=1,if=!buff.dancing_rune_weapon.up |
| 10 | `heart_strike` | — |
| 11 | `consumption` | empower_to=1 |
| 12 | `arcane_torrent` | if=runic_power.deficit>20 |

## Action List: `high_prio_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `raise_dead` | use_off_gcd=1 |
| 2 | `death_strike` | if=buff.coagulopathy.up&buff.coagulopathy.remains<=gcd |
| 3 | `dancing_rune_weapon` | if=!buff.exterminate.up&!debuff.reapers_mark_debuff.up&!buff.dancing_rune_weapon.up&(fight_remains>95\|fight_remains<25\|time>300) |

## Action List: `san_gift`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `heart_strike` | if=buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains |
| 2 | `death_strike` | if=runic_power.deficit<36 |
| 3 | `blood_boil` | if=!drw.bp_ticking |
| 4 | `any_dnd` | if=buff.crimson_scourge.remains |
| 5 | `heart_strike` | if=buff.essence_of_the_blood_queen.stack<7 |
| 6 | `death_strike` | — |
| 7 | `blood_boil` | if=buff.boiling_point.up&!buff.boiling_point_echo.up |
| 8 | `heart_strike` | — |
| 9 | `blood_boil` | — |

## Action List: `sanlayn`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `deaths_caress` | if=!buff.bone_shield.up\|buff.bone_shield.remains<1.5\|buff.bone_shield.stack<=1 |
| 2 | `blood_boil` | if=dot.blood_plague.remains<3 |
| 3 | `heart_strike` | if=(buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains&buff.vampiric_strike.remains) |
| 4 | `death_strike` | if=runic_power.deficit<20 |
| 5 | `deaths_caress` | if=buff.bone_shield.stack<6 |
| 6 | `marrowrend` | if=buff.bone_shield.stack<6 |
| 7 | `any_dnd` | if=buff.crimson_scourge.remains |
| 8 | `heart_strike` | if=buff.vampiric_strike.up |
| 9 | `death_strike` | — |
| 10 | `blood_boil` | if=buff.boiling_point.up&!buff.boiling_point_echo.up |
| 11 | `consumption` | empower_to=1 |
| 12 | `heart_strike` | if=rune>=2 |
| 13 | `blood_boil` | — |
| 14 | `heart_strike` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=snapshot_stats
actions.precombat+=/deaths_caress

# Executed every time the actor is available.
actions=auto_attack
actions+=/use_items
actions+=/use_item,name=light_company_guidon,use_off_gcd=1,if=cooldown.dancing_rune_weapon.remains>78|fight_remains<15
actions+=/use_item,name=algethar_puzzle_box,if=fight_remains>122|cooldown.dancing_rune_weapon.remains>78|fight_remains<25
actions+=/fireblood,if=fight_remains>120|cooldown.dancing_rune_weapon.remains>78|fight_remains<8
actions+=/blood_fury,if=fight_remains>120|cooldown.dancing_rune_weapon.remains>78|fight_remains<12
actions+=/berserking,if=cooldown.dancing_rune_weapon.remains>78|fight_remains<=15
actions+=/ancestral_call,if=fight_remains>120|cooldown.dancing_rune_weapon.remains>78|fight_remains<15
actions+=/potion,if=cooldown.dancing_rune_weapon.remains>78|fight_remains<=30
actions+=/vampiric_blood,if=!buff.vampiric_blood.up
actions+=/call_action_list,name=high_prio_actions
actions+=/run_action_list,name=deathbringer,if=hero_tree.deathbringer
actions+=/run_action_list,name=san_gift,if=hero_tree.sanlayn&buff.gift_of_the_sanlayn.up
actions+=/run_action_list,name=sanlayn,if=hero_tree.sanlayn

actions.deathbringer=death_strike,if=(runic_power.deficit<20|(runic_power.deficit<26&buff.dancing_rune_weapon.up))
actions.deathbringer+=/death_and_decay,if=!buff.death_and_decay.up
actions.deathbringer+=/reapers_mark
actions.deathbringer+=/marrowrend,if=buff.exterminate.up
actions.deathbringer+=/deaths_caress,if=(!buff.bone_shield.up|buff.bone_shield.remains<3|buff.bone_shield.stack<6)&rune<4
actions.deathbringer+=/marrowrend,if=!buff.bone_shield.up|buff.bone_shield.remains<3|buff.bone_shield.stack<6
actions.deathbringer+=/death_strike
actions.deathbringer+=/blood_boil
actions.deathbringer+=/consumption,empower_to=1,if=!buff.dancing_rune_weapon.up
actions.deathbringer+=/heart_strike
actions.deathbringer+=/consumption,empower_to=1
actions.deathbringer+=/arcane_torrent,if=runic_power.deficit>20

actions.high_prio_actions=raise_dead,use_off_gcd=1
actions.high_prio_actions+=/death_strike,if=buff.coagulopathy.up&buff.coagulopathy.remains<=gcd
actions.high_prio_actions+=/dancing_rune_weapon,if=!buff.exterminate.up&!debuff.reapers_mark_debuff.up&!buff.dancing_rune_weapon.up&(fight_remains>95|fight_remains<25|time>300)

actions.san_gift=heart_strike,if=buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains
actions.san_gift+=/death_strike,if=runic_power.deficit<36
actions.san_gift+=/blood_boil,if=!drw.bp_ticking
actions.san_gift+=/any_dnd,if=buff.crimson_scourge.remains
actions.san_gift+=/heart_strike,if=buff.essence_of_the_blood_queen.stack<7
actions.san_gift+=/death_strike
actions.san_gift+=/blood_boil,if=buff.boiling_point.up&!buff.boiling_point_echo.up
actions.san_gift+=/heart_strike
actions.san_gift+=/blood_boil

actions.sanlayn=deaths_caress,if=!buff.bone_shield.up|buff.bone_shield.remains<1.5|buff.bone_shield.stack<=1
actions.sanlayn+=/blood_boil,if=dot.blood_plague.remains<3
actions.sanlayn+=/heart_strike,if=(buff.essence_of_the_blood_queen.remains<1.5&buff.essence_of_the_blood_queen.remains&buff.vampiric_strike.remains)
actions.sanlayn+=/death_strike,if=runic_power.deficit<20
actions.sanlayn+=/deaths_caress,if=buff.bone_shield.stack<6
actions.sanlayn+=/marrowrend,if=buff.bone_shield.stack<6
actions.sanlayn+=/any_dnd,if=buff.crimson_scourge.remains
actions.sanlayn+=/heart_strike,if=buff.vampiric_strike.up
actions.sanlayn+=/death_strike
actions.sanlayn+=/blood_boil,if=buff.boiling_point.up&!buff.boiling_point_echo.up
actions.sanlayn+=/consumption,empower_to=1
actions.sanlayn+=/heart_strike,if=rune>=2
actions.sanlayn+=/blood_boil
actions.sanlayn+=/heart_strike
```
