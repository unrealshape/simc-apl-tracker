# Monk – Brewmaster

Auto-generated from SimulationCraft APL | Last updated: 2026-04-09 05:14 UTC

Source: `apl/default/monk/brewmaster.simc`

---

## Overview

- **Action Lists:** 4
- **Total Actions:** 47
- **Lists:** `precombat`, `default`, `item_actions`, `race_actions`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `potion` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `potion` | — |
| 3 | `call_action_list` | name=race_actions |
| 4 | `call_action_list` | name=item_actions |
| 5 | `black_ox_brew` | if=talent.aspect_of_harmony.enabled&cooldown.celestial_brew.charges_fractional<1 |
| 6 | `black_ox_brew` | if=!talent.aspect_of_harmony.enabled&energy<40 |
| 7 | `celestial_brew` | if=buff.aspect_of_harmony_spender.up&!buff.empty_barrel.up |
| 8 | `keg_smash` | if=buff.aspect_of_harmony_spender.up&buff.empty_barrel.up |
| 9 | `breath_of_fire` | if=talent.wisdom_of_the_wall.enabled&buff.invoke_niuzao_the_black_ox.up |
| 10 | `keg_smash` | if=talent.wisdom_of_the_wall.enabled&buff.invoke_niuzao_the_black_ox.up |
| 11 | `blackout_kick` | if=talent.blackout_combo.enabled&!buff.blackout_combo.up |
| 12 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up)&buff.aspect_of_harmony_accumulator.value>0.3*health.max&cooldown.celestial_brew.charges_fractional>1.9 |
| 13 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up)&target.time_to_die<15&buff.aspect_of_harmony_accumulator.value>0.2*health.max |
| 14 | `purifying_brew` | if=!(apex.1&buff.empty_barrel.up) |
| 15 | `fortifying_brew` | if=!(apex.3&buff.empty_barrel.up) |
| 16 | `chi_burst` | — |
| 17 | `invoke_niuzao` | — |
| 18 | `tiger_palm` | if=buff.blackout_combo.up&cooldown.blackout_kick.remains<1.3 |
| 19 | `exploding_keg` | if=cooldown.keg_smash.charges_fractional<1 |
| 20 | `empty_the_cellar` | if=talent.aspect_of_harmony.enabled&cooldown.celestial_brew.remains>15 |
| 21 | `empty_the_cellar` | if=!talent.aspect_of_harmony.enabled&buff.empty_the_cellar.remains<1.5 |
| 22 | `breath_of_fire` | if=cooldown.blackout_kick.remains>1.5&!buff.empty_barrel.up&cooldown.keg_smash.charges<1+talent.stormstouts_last_keg.enabled |
| 23 | `tiger_palm` | if=buff.blackout_combo.up |
| 24 | `celestial_brew` | if=talent.flurry_strikes.enabled&!(apex.3&buff.empty_barrel.up) |
| 25 | `breath_of_fire` | if=talent.flurry_strikes.enabled |
| 26 | `keg_smash` | if=talent.flurry_strikes.enabled |
| 27 | `keg_smash` | if=talent.scalding_brew.enabled |
| 28 | `keg_smash` | if=buff.empty_barrel.up |
| 29 | `keg_smash` | if=cooldown.keg_smash.charges=1+talent.stormstouts_last_keg.enabled |
| 30 | `breath_of_fire` | — |
| 31 | `empty_the_cellar` | — |
| 32 | `rushing_jade_wind` | — |
| 33 | `keg_smash` | — |
| 34 | `blackout_kick` | — |
| 35 | `tiger_palm` | if=talent.aspect_of_harmony.enabled&energy>50-energy.regen*2 |
| 36 | `tiger_palm` | if=energy>65-energy.regen |
| 37 | `expel_harm` | — |

## Action List: `item_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | — |

## Action List: `race_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blood_fury` | — |
| 2 | `berserking` | — |
| 3 | `arcane_torrent` | — |
| 4 | `lights_judgment` | — |
| 5 | `fireblood` | — |
| 6 | `ancestral_call` | — |
| 7 | `bag_of_tricks` | — |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
# Precombat
actions.precombat=snapshot_stats
actions.precombat+=/potion

# Executed every time the actor is available.
# Default List
actions=auto_attack
actions+=/potion
actions+=/call_action_list,name=race_actions
actions+=/call_action_list,name=item_actions
actions+=/black_ox_brew,if=talent.aspect_of_harmony.enabled&cooldown.celestial_brew.charges_fractional<1
actions+=/black_ox_brew,if=!talent.aspect_of_harmony.enabled&energy<40
actions+=/celestial_brew,if=buff.aspect_of_harmony_spender.up&!buff.empty_barrel.up
actions+=/keg_smash,if=buff.aspect_of_harmony_spender.up&buff.empty_barrel.up
actions+=/breath_of_fire,if=talent.wisdom_of_the_wall.enabled&buff.invoke_niuzao_the_black_ox.up
actions+=/keg_smash,if=talent.wisdom_of_the_wall.enabled&buff.invoke_niuzao_the_black_ox.up
actions+=/blackout_kick,if=talent.blackout_combo.enabled&!buff.blackout_combo.up
actions+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)&buff.aspect_of_harmony_accumulator.value>0.3*health.max&cooldown.celestial_brew.charges_fractional>1.9
actions+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)&target.time_to_die<15&buff.aspect_of_harmony_accumulator.value>0.2*health.max
actions+=/purifying_brew,if=!(apex.1&buff.empty_barrel.up)
actions+=/fortifying_brew,if=!(apex.3&buff.empty_barrel.up)
actions+=/chi_burst
actions+=/invoke_niuzao
actions+=/tiger_palm,if=buff.blackout_combo.up&cooldown.blackout_kick.remains<1.3
actions+=/exploding_keg,if=cooldown.keg_smash.charges_fractional<1
actions+=/empty_the_cellar,if=talent.aspect_of_harmony.enabled&cooldown.celestial_brew.remains>15
actions+=/empty_the_cellar,if=!talent.aspect_of_harmony.enabled&buff.empty_the_cellar.remains<1.5
actions+=/breath_of_fire,if=cooldown.blackout_kick.remains>1.5&!buff.empty_barrel.up&cooldown.keg_smash.charges<1+talent.stormstouts_last_keg.enabled
actions+=/tiger_palm,if=buff.blackout_combo.up
actions+=/celestial_brew,if=talent.flurry_strikes.enabled&!(apex.3&buff.empty_barrel.up)
actions+=/breath_of_fire,if=talent.flurry_strikes.enabled
actions+=/keg_smash,if=talent.flurry_strikes.enabled
actions+=/keg_smash,if=talent.scalding_brew.enabled
actions+=/keg_smash,if=buff.empty_barrel.up
actions+=/keg_smash,if=cooldown.keg_smash.charges=1+talent.stormstouts_last_keg.enabled
actions+=/breath_of_fire
actions+=/empty_the_cellar
actions+=/rushing_jade_wind
actions+=/keg_smash
actions+=/blackout_kick
actions+=/tiger_palm,if=talent.aspect_of_harmony.enabled&energy>50-energy.regen*2
actions+=/tiger_palm,if=energy>65-energy.regen
actions+=/expel_harm

# Items
actions.item_actions=use_items

# Racials
actions.race_actions=blood_fury
actions.race_actions+=/berserking
actions.race_actions+=/arcane_torrent
actions.race_actions+=/lights_judgment
actions.race_actions+=/fireblood
actions.race_actions+=/ancestral_call
actions.race_actions+=/bag_of_tricks
```
