# Monk – Brewmaster

Auto-generated from SimulationCraft APL | Last updated: 2026-09-10 08:01 UTC

Source: `apl/default/monk/brewmaster.simc`

---

## Overview

- **Action Lists:** 6
- **Total Actions:** 62
- **Lists:** `precombat`, `default`, `item_actions`, `master_of_harmony`, `race_actions`, `shado_pan`

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
| 5 | `run_action_list` | name=master_of_harmony,if=hero_tree.master_of_harmony |
| 6 | `run_action_list` | name=shado_pan,if=hero_tree.shadopan |

## Action List: `item_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | — |

## Action List: `master_of_harmony`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `black_ox_brew` | if=cooldown.celestial_brew.charges_fractional<1 |
| 2 | `celestial_brew` | if=buff.aspect_of_harmony_spender.up&!buff.empty_barrel.up |
| 3 | `keg_smash` | if=buff.aspect_of_harmony_spender.up&buff.empty_barrel.up |
| 4 | `blackout_kick` | if=talent.blackout_combo.enabled&!buff.blackout_combo.up |
| 5 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up)&buff.aspect_of_harmony_accumulator.value>0.95*health.max&cooldown.celestial_brew.charges_fractional>1.9 |
| 6 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up)&target.time_to_die<15&buff.aspect_of_harmony_accumulator.value>0.2*health.max |
| 7 | `purifying_brew` | if=!(apex.1&buff.empty_barrel.up) |
| 8 | `fortifying_brew` | if=!(apex.3&buff.empty_barrel.up) |
| 9 | `chi_burst` | — |
| 10 | `invoke_niuzao` | — |
| 11 | `tiger_palm` | if=buff.blackout_combo.up&cooldown.blackout_kick.remains<1.3 |
| 12 | `exploding_keg` | if=cooldown.keg_smash.charges_fractional<1 |
| 13 | `empty_the_cellar` | if=cooldown.celestial_brew.remains>15 |
| 14 | `breath_of_fire` | if=cooldown.blackout_kick.remains>1.5&buff.blackout_combo.up |
| 15 | `tiger_palm` | if=buff.blackout_combo.up |
| 16 | `breath_of_fire` | — |
| 17 | `keg_smash` | — |
| 18 | `empty_the_cellar` | — |
| 19 | `rushing_jade_wind` | — |
| 20 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up) |
| 21 | `blackout_kick` | — |
| 22 | `tiger_palm` | if=energy>50-energy.regen*2 |
| 23 | `expel_harm` | — |

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

## Action List: `shado_pan`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `breath_of_fire` | if=talent.salsalabims_strength.enabled&buff.invoke_niuzao_the_black_ox.up |
| 2 | `keg_smash` | if=talent.salsalabims_strength.enabled&buff.invoke_niuzao_the_black_ox.up |
| 3 | `purifying_brew` | if=!(apex.1&buff.empty_barrel.up)&buff.invoke_niuzao_the_black_ox.up |
| 4 | `black_ox_brew` | if=!(apex.1&buff.empty_barrel.up)&cooldown.celestial_brew.charges_fractional<0.25&buff.invoke_niuzao_the_black_ox.up |
| 5 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up)&buff.invoke_niuzao_the_black_ox.up |
| 6 | `exploding_keg` | if=buff.invoke_niuzao_the_black_ox.up |
| 7 | `fortifying_brew` | if=!(apex.3&buff.empty_barrel.up)&buff.invoke_niuzao_the_black_ox.up |
| 8 | `blackout_kick` | if=talent.blackout_combo.enabled&!buff.blackout_combo.up |
| 9 | `purifying_brew` | if=!(apex.1&buff.empty_barrel.up) |
| 10 | `invoke_niuzao` | — |
| 11 | `tiger_palm` | if=buff.blackout_combo.up&cooldown.blackout_kick.remains<1.3 |
| 12 | `empty_the_cellar` | if=buff.empty_the_cellar.remains<1.5 |
| 13 | `tiger_palm` | if=buff.blackout_combo.up |
| 14 | `breath_of_fire` | — |
| 15 | `keg_smash` | — |
| 16 | `exploding_keg` | — |
| 17 | `celestial_brew` | if=!(apex.3&buff.empty_barrel.up) |
| 18 | `empty_the_cellar` | — |
| 19 | `chi_burst` | — |
| 20 | `rushing_jade_wind` | — |
| 21 | `blackout_kick` | — |
| 22 | `tiger_palm` | if=energy>65-energy.regen |
| 23 | `expel_harm` | — |

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
actions+=/run_action_list,name=master_of_harmony,if=hero_tree.master_of_harmony
actions+=/run_action_list,name=shado_pan,if=hero_tree.shadopan

# Items
actions.item_actions=use_items

actions.master_of_harmony=black_ox_brew,if=cooldown.celestial_brew.charges_fractional<1
actions.master_of_harmony+=/celestial_brew,if=buff.aspect_of_harmony_spender.up&!buff.empty_barrel.up
actions.master_of_harmony+=/keg_smash,if=buff.aspect_of_harmony_spender.up&buff.empty_barrel.up
actions.master_of_harmony+=/blackout_kick,if=talent.blackout_combo.enabled&!buff.blackout_combo.up
actions.master_of_harmony+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)&buff.aspect_of_harmony_accumulator.value>0.95*health.max&cooldown.celestial_brew.charges_fractional>1.9
actions.master_of_harmony+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)&target.time_to_die<15&buff.aspect_of_harmony_accumulator.value>0.2*health.max
actions.master_of_harmony+=/purifying_brew,if=!(apex.1&buff.empty_barrel.up)
actions.master_of_harmony+=/fortifying_brew,if=!(apex.3&buff.empty_barrel.up)
actions.master_of_harmony+=/chi_burst
actions.master_of_harmony+=/invoke_niuzao
actions.master_of_harmony+=/tiger_palm,if=buff.blackout_combo.up&cooldown.blackout_kick.remains<1.3
actions.master_of_harmony+=/exploding_keg,if=cooldown.keg_smash.charges_fractional<1
actions.master_of_harmony+=/empty_the_cellar,if=cooldown.celestial_brew.remains>15
actions.master_of_harmony+=/breath_of_fire,if=cooldown.blackout_kick.remains>1.5&buff.blackout_combo.up
actions.master_of_harmony+=/tiger_palm,if=buff.blackout_combo.up
actions.master_of_harmony+=/breath_of_fire
actions.master_of_harmony+=/keg_smash
actions.master_of_harmony+=/empty_the_cellar
actions.master_of_harmony+=/rushing_jade_wind
actions.master_of_harmony+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)
actions.master_of_harmony+=/blackout_kick
actions.master_of_harmony+=/tiger_palm,if=energy>50-energy.regen*2
actions.master_of_harmony+=/expel_harm

# Racials
actions.race_actions=blood_fury
actions.race_actions+=/berserking
actions.race_actions+=/arcane_torrent
actions.race_actions+=/lights_judgment
actions.race_actions+=/fireblood
actions.race_actions+=/ancestral_call
actions.race_actions+=/bag_of_tricks

actions.shado_pan=breath_of_fire,if=talent.salsalabims_strength.enabled&buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/keg_smash,if=talent.salsalabims_strength.enabled&buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/purifying_brew,if=!(apex.1&buff.empty_barrel.up)&buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/black_ox_brew,if=!(apex.1&buff.empty_barrel.up)&cooldown.celestial_brew.charges_fractional<0.25&buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)&buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/exploding_keg,if=buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/fortifying_brew,if=!(apex.3&buff.empty_barrel.up)&buff.invoke_niuzao_the_black_ox.up
actions.shado_pan+=/blackout_kick,if=talent.blackout_combo.enabled&!buff.blackout_combo.up
actions.shado_pan+=/purifying_brew,if=!(apex.1&buff.empty_barrel.up)
actions.shado_pan+=/invoke_niuzao
actions.shado_pan+=/tiger_palm,if=buff.blackout_combo.up&cooldown.blackout_kick.remains<1.3
actions.shado_pan+=/empty_the_cellar,if=buff.empty_the_cellar.remains<1.5
actions.shado_pan+=/tiger_palm,if=buff.blackout_combo.up
actions.shado_pan+=/breath_of_fire
actions.shado_pan+=/keg_smash
actions.shado_pan+=/exploding_keg
actions.shado_pan+=/celestial_brew,if=!(apex.3&buff.empty_barrel.up)
actions.shado_pan+=/empty_the_cellar
actions.shado_pan+=/chi_burst
actions.shado_pan+=/rushing_jade_wind
actions.shado_pan+=/blackout_kick
actions.shado_pan+=/tiger_palm,if=energy>65-energy.regen
actions.shado_pan+=/expel_harm
```
