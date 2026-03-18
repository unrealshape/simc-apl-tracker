# Monk – Brewmaster

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:22 UTC

Source: `apl/default/monk/brewmaster.simc`

---

## Overview

- **Action Lists:** 4
- **Total Actions:** 48
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
| 5 | `black_ox_brew` | if=energy<40&(!talent.aspect_of_harmony.enabled\|cooldown.celestial_brew.charges_fractional<1) |
| 6 | `celestial_brew` | if=(buff.aspect_of_harmony_accumulator.value>0.3*health.max&buff.weapons_of_order.up&!dot.aspect_of_harmony_damage.ticking) |
| 7 | `celestial_brew` | if=(buff.aspect_of_harmony_accumulator.value>0.3*health.max&!talent.weapons_of_order.enabled&!dot.aspect_of_harmony_damage.ticking) |
| 8 | `celestial_brew` | if=(target.time_to_die<20&target.time_to_die>14&buff.aspect_of_harmony_accumulator.value>0.2*health.max) |
| 9 | `celestial_brew` | if=(buff.aspect_of_harmony_accumulator.value>0.3*health.max&cooldown.weapons_of_order.remains>20&!dot.aspect_of_harmony_damage.ticking) |
| 10 | `celestial_brew` | if=!buff.blackout_combo.up&(cooldown.celestial_brew.charges_fractional>1.8\|(cooldown.celestial_brew.charges_fractional>1.2&cooldown.black_ox_brew.up)) |
| 11 | `blackout_kick` | — |
| 12 | `chi_burst` | if=!talent.aspect_of_harmony.enabled\|buff.balanced_stratagem_magic.stack>3 |
| 13 | `weapons_of_order` | — |
| 14 | `invoke_niuzao` | if=!talent.call_to_arms.enabled |
| 15 | `invoke_niuzao` | if=talent.call_to_arms.enabled&buff.call_to_arms_invoke_niuzao.down&buff.weapons_of_order.remains<16 |
| 16 | `rising_sun_kick` | if=!talent.fluidity_of_motion.enabled |
| 17 | `keg_smash` | if=buff.weapons_of_order.up&(debuff.weapons_of_order_debuff.remains<1.8\|debuff.weapons_of_order_debuff.stack<3-buff.blackout_combo.up\|(buff.weapons_of_order.remains<3-buff.blackout_combo.up&buff.weapons_of_order.remains<1+cooldown.rising_sun_kick.remains)) |
| 18 | `tiger_palm` | if=buff.blackout_combo.up |
| 19 | `keg_smash` | if=talent.scalding_brew.enabled |
| 20 | `spinning_crane_kick` | if=talent.charred_passions.enabled&talent.scalding_brew.enabled&buff.charred_passions.up&buff.charred_passions.remains<3&dot.breath_of_fire.remains<9&active_enemies>4 |
| 21 | `rising_sun_kick` | if=talent.fluidity_of_motion.enabled |
| 22 | `purifying_brew` | if=buff.blackout_combo.down&!(talent.call_to_arms.enabled\|talent.invoke_niuzao_the_black_ox.enabled) |
| 23 | `purifying_brew` | if=buff.blackout_combo.down&(talent.call_to_arms.enabled\|talent.invoke_niuzao_the_black_ox.enabled)&(buff.invoke_niuzao_the_black_ox.up\|buff.call_to_arms_invoke_niuzao.up) |
| 24 | `purifying_brew` | if=buff.blackout_combo.down&(talent.call_to_arms.enabled\|talent.invoke_niuzao_the_black_ox.enabled)&cooldown.weapons_of_order.remains>10&cooldown.invoke_niuzao_the_black_ox.remains>10 |
| 25 | `breath_of_fire` | if=(buff.charred_passions.down&(!talent.scalding_brew.enabled\|active_enemies<5))\|!talent.charred_passions.enabled\|(dot.breath_of_fire.remains<3&talent.scalding_brew.enabled) |
| 26 | `exploding_keg` | if=!talent.rushing_jade_wind.enabled\|buff.rushing_jade_wind.up |
| 27 | `rushing_jade_wind` | if=talent.aspect_of_harmony.enabled&((buff.rushing_jade_wind.remains<2.5&buff.rushing_jade_wind.up)\|!buff.rushing_jade_wind.up) |
| 28 | `keg_smash` | — |
| 29 | `rushing_jade_wind` | if=!talent.aspect_of_harmony.enabled&((buff.rushing_jade_wind.remains<2.5&buff.rushing_jade_wind.up)\|!buff.rushing_jade_wind.up) |
| 30 | `tiger_palm` | if=energy>40-cooldown.keg_smash.remains*energy.regen |
| 31 | `spinning_crane_kick` | if=energy>40-cooldown.keg_smash.remains*energy.regen |

## Action List: `item_actions`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=tome_of_lights_devotion,if=buff.inner_resilience.up |
| 2 | `use_item` | name=unyielding_netherprism,if=buff.weapons_of_order.up&debuff.weapons_of_order_debuff.stack=4 |
| 3 | `use_item` | name=unyielding_netherprism,if=!talent.weapons_of_order.enabled |
| 4 | `use_item` | name=lily_of_the_eternal_weave,if=buff.weapons_of_order.up&debuff.weapons_of_order_debuff.stack=4 |
| 5 | `use_item` | name=lily_of_the_eternal_weave,if=!talent.weapons_of_order.enabled |
| 6 | `use_item` | name=signet_of_the_priory,if=buff.weapons_of_order.up&debuff.weapons_of_order_debuff.stack=4 |
| 7 | `use_item` | name=signet_of_the_priory,if=!talent.weapons_of_order.enabled |
| 8 | `use_items` | — |

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
actions.precombat=snapshot_stats
actions.precombat+=/potion

# Executed every time the actor is available.
actions=auto_attack
actions+=/potion
actions+=/call_action_list,name=race_actions
actions+=/call_action_list,name=item_actions
actions+=/black_ox_brew,if=energy<40&(!talent.aspect_of_harmony.enabled|cooldown.celestial_brew.charges_fractional<1)
actions+=/celestial_brew,if=(buff.aspect_of_harmony_accumulator.value>0.3*health.max&buff.weapons_of_order.up&!dot.aspect_of_harmony_damage.ticking)
actions+=/celestial_brew,if=(buff.aspect_of_harmony_accumulator.value>0.3*health.max&!talent.weapons_of_order.enabled&!dot.aspect_of_harmony_damage.ticking)
actions+=/celestial_brew,if=(target.time_to_die<20&target.time_to_die>14&buff.aspect_of_harmony_accumulator.value>0.2*health.max)
actions+=/celestial_brew,if=(buff.aspect_of_harmony_accumulator.value>0.3*health.max&cooldown.weapons_of_order.remains>20&!dot.aspect_of_harmony_damage.ticking)
actions+=/celestial_brew,if=!buff.blackout_combo.up&(cooldown.celestial_brew.charges_fractional>1.8|(cooldown.celestial_brew.charges_fractional>1.2&cooldown.black_ox_brew.up))
actions+=/blackout_kick
actions+=/chi_burst,if=!talent.aspect_of_harmony.enabled|buff.balanced_stratagem_magic.stack>3
actions+=/weapons_of_order
actions+=/invoke_niuzao,if=!talent.call_to_arms.enabled
actions+=/invoke_niuzao,if=talent.call_to_arms.enabled&buff.call_to_arms_invoke_niuzao.down&buff.weapons_of_order.remains<16
actions+=/rising_sun_kick,if=!talent.fluidity_of_motion.enabled
actions+=/keg_smash,if=buff.weapons_of_order.up&(debuff.weapons_of_order_debuff.remains<1.8|debuff.weapons_of_order_debuff.stack<3-buff.blackout_combo.up|(buff.weapons_of_order.remains<3-buff.blackout_combo.up&buff.weapons_of_order.remains<1+cooldown.rising_sun_kick.remains))
actions+=/tiger_palm,if=buff.blackout_combo.up
actions+=/keg_smash,if=talent.scalding_brew.enabled
actions+=/spinning_crane_kick,if=talent.charred_passions.enabled&talent.scalding_brew.enabled&buff.charred_passions.up&buff.charred_passions.remains<3&dot.breath_of_fire.remains<9&active_enemies>4
actions+=/rising_sun_kick,if=talent.fluidity_of_motion.enabled
actions+=/purifying_brew,if=buff.blackout_combo.down&!(talent.call_to_arms.enabled|talent.invoke_niuzao_the_black_ox.enabled)
actions+=/purifying_brew,if=buff.blackout_combo.down&(talent.call_to_arms.enabled|talent.invoke_niuzao_the_black_ox.enabled)&(buff.invoke_niuzao_the_black_ox.up|buff.call_to_arms_invoke_niuzao.up)
actions+=/purifying_brew,if=buff.blackout_combo.down&(talent.call_to_arms.enabled|talent.invoke_niuzao_the_black_ox.enabled)&cooldown.weapons_of_order.remains>10&cooldown.invoke_niuzao_the_black_ox.remains>10
actions+=/breath_of_fire,if=(buff.charred_passions.down&(!talent.scalding_brew.enabled|active_enemies<5))|!talent.charred_passions.enabled|(dot.breath_of_fire.remains<3&talent.scalding_brew.enabled)
actions+=/exploding_keg,if=!talent.rushing_jade_wind.enabled|buff.rushing_jade_wind.up
actions+=/rushing_jade_wind,if=talent.aspect_of_harmony.enabled&((buff.rushing_jade_wind.remains<2.5&buff.rushing_jade_wind.up)|!buff.rushing_jade_wind.up)
actions+=/keg_smash
actions+=/rushing_jade_wind,if=!talent.aspect_of_harmony.enabled&((buff.rushing_jade_wind.remains<2.5&buff.rushing_jade_wind.up)|!buff.rushing_jade_wind.up)
actions+=/tiger_palm,if=energy>40-cooldown.keg_smash.remains*energy.regen
actions+=/spinning_crane_kick,if=energy>40-cooldown.keg_smash.remains*energy.regen

actions.item_actions=use_item,name=tome_of_lights_devotion,if=buff.inner_resilience.up
actions.item_actions+=/use_item,name=unyielding_netherprism,if=buff.weapons_of_order.up&debuff.weapons_of_order_debuff.stack=4
actions.item_actions+=/use_item,name=unyielding_netherprism,if=!talent.weapons_of_order.enabled
actions.item_actions+=/use_item,name=lily_of_the_eternal_weave,if=buff.weapons_of_order.up&debuff.weapons_of_order_debuff.stack=4
actions.item_actions+=/use_item,name=lily_of_the_eternal_weave,if=!talent.weapons_of_order.enabled
actions.item_actions+=/use_item,name=signet_of_the_priory,if=buff.weapons_of_order.up&debuff.weapons_of_order_debuff.stack=4
actions.item_actions+=/use_item,name=signet_of_the_priory,if=!talent.weapons_of_order.enabled
actions.item_actions+=/use_items

actions.race_actions=blood_fury
actions.race_actions+=/berserking
actions.race_actions+=/arcane_torrent
actions.race_actions+=/lights_judgment
actions.race_actions+=/fireblood
actions.race_actions+=/ancestral_call
actions.race_actions+=/bag_of_tricks
```
