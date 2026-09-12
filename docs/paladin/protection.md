# Paladin – Protection

Auto-generated from SimulationCraft APL | Last updated: 2026-09-12 07:50 UTC

Source: `apl/default/paladin/protection.simc`

---

## Overview

- **Action Lists:** 2
- **Total Actions:** 36
- **Lists:** `precombat`, `default`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `rite_of_sanctification` | — |
| 2 | `rite_of_adjuration` | — |
| 3 | `snapshot_stats` | — |
| 4 | `devotion_aura` | — |
| 5 | `lights_judgment` | — |
| 6 | `consecration` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `use_item` | name=algethar_puzzle_box |
| 3 | `use_items` | — |
| 4 | `potion` | if=buff.avenging_wrath.up |
| 5 | `avenging_wrath` | if=cooldown.divine_toll.remains<=10 |
| 6 | `fireblood` | if=buff.avenging_wrath.up |
| 7 | `divine_toll` | if=buff.avenging_wrath.up\|(!talent.righteous_protector.enabled&cooldown.avenging_wrath.remains>30) |
| 8 | `hammer_of_light` | if=(!buff.undisputed_ruling.up\|buff.hammer_of_light_ready.remains<5)&debuff.judgment.up |
| 9 | `shield_of_the_righteous` | if=!buff.hammer_of_light_ready.up\|(!buff.hammer_of_light_ready.remains<5&buff.undisputed_ruling.up)\|buff.hammer_of_light_free.up\|prev_gcd.1.divine_toll |
| 10 | `holy_armaments` | if=next_armament=sacred_weapon&(buff.sacred_weapon.remains<6\|!buff.sacred_weapon.up) |
| 11 | `hammer_of_wrath` | if=buff.hammer_of_light_ready.up&!debuff.judgment.up |
| 12 | `hammer_of_wrath` | if=hero_tree.lightsmith |
| 13 | `judgment` | if=buff.hammer_of_light_ready.up&!debuff.judgment.up |
| 14 | `avengers_shield` | if=buff.vanguard.up\|(buff.avenging_wrath.up&apex.3) |
| 15 | `holy_armaments` | if=next_armament=holy_bulwark&cooldown.avenging_wrath.remains<5 |
| 16 | `consecration` | if=buff.divine_guidance.stack>=5 |
| 17 | `hammer_of_wrath` | — |
| 18 | `judgment` | if=full_recharge_time<=gcd*2 |
| 19 | `avengers_shield` | — |
| 20 | `consecration` | if=!consecration.up |
| 21 | `hammer_of_the_righteous` | if=buff.blessed_assurance.up |
| 22 | `blessed_hammer` | if=buff.blessed_assurance.up |
| 23 | `judgment` | — |
| 24 | `holy_armaments` | if=next_armament=holy_bulwark&charges=2 |
| 25 | `consecration` | if=!consecration.up |
| 26 | `blessed_hammer` | — |
| 27 | `hammer_of_the_righteous` | — |
| 28 | `arcane_torrent` | — |
| 29 | `word_of_glory` | if=buff.shining_light_free.up |
| 30 | `consecration` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=rite_of_sanctification
actions.precombat+=/rite_of_adjuration
actions.precombat+=/snapshot_stats
actions.precombat+=/devotion_aura
actions.precombat+=/lights_judgment
actions.precombat+=/consecration

# Executed every time the actor is available.
actions=auto_attack
actions+=/use_item,name=algethar_puzzle_box
actions+=/use_items
actions+=/potion,if=buff.avenging_wrath.up
actions+=/avenging_wrath,if=cooldown.divine_toll.remains<=10
actions+=/fireblood,if=buff.avenging_wrath.up
actions+=/divine_toll,if=buff.avenging_wrath.up|(!talent.righteous_protector.enabled&cooldown.avenging_wrath.remains>30)
actions+=/hammer_of_light,if=(!buff.undisputed_ruling.up|buff.hammer_of_light_ready.remains<5)&debuff.judgment.up
actions+=/shield_of_the_righteous,if=!buff.hammer_of_light_ready.up|(!buff.hammer_of_light_ready.remains<5&buff.undisputed_ruling.up)|buff.hammer_of_light_free.up|prev_gcd.1.divine_toll
actions+=/holy_armaments,if=next_armament=sacred_weapon&(buff.sacred_weapon.remains<6|!buff.sacred_weapon.up)
actions+=/hammer_of_wrath,if=buff.hammer_of_light_ready.up&!debuff.judgment.up
actions+=/hammer_of_wrath,if=hero_tree.lightsmith
actions+=/judgment,if=buff.hammer_of_light_ready.up&!debuff.judgment.up
actions+=/avengers_shield,if=buff.vanguard.up|(buff.avenging_wrath.up&apex.3)
actions+=/holy_armaments,if=next_armament=holy_bulwark&cooldown.avenging_wrath.remains<5
actions+=/consecration,if=buff.divine_guidance.stack>=5
actions+=/hammer_of_wrath
actions+=/judgment,if=full_recharge_time<=gcd*2
actions+=/avengers_shield
actions+=/consecration,if=!consecration.up
actions+=/hammer_of_the_righteous,if=buff.blessed_assurance.up
actions+=/blessed_hammer,if=buff.blessed_assurance.up
actions+=/judgment
actions+=/holy_armaments,if=next_armament=holy_bulwark&charges=2
actions+=/consecration,if=!consecration.up
actions+=/blessed_hammer
actions+=/hammer_of_the_righteous
actions+=/arcane_torrent
actions+=/word_of_glory,if=buff.shining_light_free.up
actions+=/consecration
```
