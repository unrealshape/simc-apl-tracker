# Rogue – Subtlety

Auto-generated from SimulationCraft APL | Last updated: 2026-03-18 10:18 UTC

Source: `apl/default/rogue/subtlety.simc`

---

## Overview

- **Action Lists:** 9
- **Total Actions:** 67
- **Lists:** `precombat`, `default`, `build`, `cds`, `fill`, `finish`, `item`, `race`, `stealth_cds`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `apply_poison` | — |
| 2 | `snapshot_stats` | — |
| 3 | `variable` | name=priority_rotation,value=priority_rotation |
| 4 | `variable` | name=trinket_sync_slot,value=1,if=trinket.1.has_use_buff&(!trinket.2.has_use_buff\|trinket.1.is.treacherous_transmitter\|trinket.1.cooldown.duration>=trinket.2.cooldown.duration) |
| 5 | `variable` | name=trinket_sync_slot,value=2,if=trinket.2.has_use_buff&(!trinket.1.has_use_buff\|trinket.2.cooldown.duration>trinket.1.cooldown.duration) |
| 6 | `stealth` | — |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `stealth` | — |
| 2 | `variable` | name=stealth,value=buff.shadow_dance.up\|buff.stealth.up\|buff.vanish.up |
| 3 | `variable` | name=targets,value=spell_targets.shuriken_storm |
| 4 | `variable` | name=skip_rupture,value=buff.shadow_dance.up\|buff.darkest_night.up\|variable.targets>=4&(!talent.replicating_shadows&talent.unseen_blade\|raid_event.adds.up\|buff.flagellation_buff.up&(fight_remains%%90<30\|!talent.shuriken_tornado)) |
| 5 | `variable` | name=maintenance,value=(dot.rupture.ticking\|variable.skip_rupture)&(buff.slice_and_dice.up\|variable.targets<=2) |
| 6 | `variable` | name=secret,value=buff.shadow_dance.up&!buff.darkest_night.up\|(cooldown.flagellation.remains<60&cooldown.flagellation.remains>30&talent.death_perception&talent.unseen_blade) |
| 7 | `variable` | name=racial_sync,value=(buff.shadow_blades.up&buff.shadow_dance.up)\|!talent.shadow_blades&buff.symbols_of_death.up\|fight_remains<20 |
| 8 | `variable` | name=shd_cp,value=combo_points<=1\|buff.darkest_night.up&combo_points>=7\|effective_combo_points>=6&talent.unseen_blade |
| 9 | `call_action_list` | name=cds |
| 10 | `call_action_list` | name=race |
| 11 | `call_action_list` | name=item |
| 12 | `call_action_list` | name=stealth_cds,if=!variable.stealth |
| 13 | `call_action_list` | name=finish,if=!buff.darkest_night.up&effective_combo_points>=6\|buff.darkest_night.up&combo_points==cp_max_spend\|action.coup_de_grace.ready&cooldown.secret_technique.remains>0 |
| 14 | `call_action_list` | name=build |
| 15 | `call_action_list` | name=fill,if=!variable.stealth |

## Action List: `build`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `shuriken_tornado` | if=(buff.tww3_trickster_4pc.up\|buff.escalating_blade.stack=4)&(variable.targets>=4\|!buff.shadow_blades.up) |
| 2 | `shuriken_storm` | if=(buff.tww3_trickster_4pc.up\|buff.escalating_blade.stack=4)&!used_for_danse&(buff.shadow_blades.up\|variable.targets>=4) |
| 3 | `backstab` | if=(talent.unseen_blade\|variable.targets<=2)&(buff.shadow_dance.remains>7&(buff.premeditation.up\|buff.shadow_blades.up)&!used_for_danse\|!variable.stealth&buff.shadow_blades.up) |
| 4 | `gloomblade` | if=(talent.unseen_blade\|variable.targets<=2)&(buff.shadow_dance.remains>7&(buff.premeditation.up\|buff.shadow_blades.up)&!used_for_danse\|!variable.stealth&buff.shadow_blades.up) |
| 5 | `shuriken_tornado` | if=buff.lingering_darkness.up\|talent.deathstalkers_mark&cooldown.shadow_blades.remains>=32&variable.targets>=3 |
| 6 | `shuriken_storm` | if=buff.clear_the_witnesses.up&(variable.targets>=2\|!buff.symbols_of_death.up) |
| 7 | `shadowstrike` | cycle_targets=1,if=debuff.find_weakness.remains<=2&variable.targets>=2&talent.unseen_blade&!variable.priority_rotation |
| 8 | `shadowstrike` | cycle_targets=1,if=talent.deathstalkers_mark&!debuff.deathstalkers_mark.up&variable.targets>=3&(buff.shadow_blades.up\|buff.premeditation.up\|talent.the_rotten) |
| 9 | `shuriken_storm` | if=talent.deathstalkers_mark&variable.targets>=(2+3*buff.shadow_dance.up) |
| 10 | `shuriken_storm` | if=talent.unseen_blade&buff.flawless_form.up&variable.targets>=3&!variable.stealth |
| 11 | `shadowstrike` | — |
| 12 | `goremaws_bite` | if=combo_points.deficit>=3 |
| 13 | `gloomblade` | — |
| 14 | `backstab` | — |

## Action List: `cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `cold_blood` | if=cooldown.secret_technique.up&buff.shadow_dance.up&combo_points>=6&variable.secret&(buff.flagellation_persist.up\|buff.flagellation_buff.remains<=3\|!talent.flagellation) |
| 2 | `potion` | if=buff.bloodlust.react\|fight_remains<30\|buff.shadow_blades.up |
| 3 | `symbols_of_death` | if=(buff.symbols_of_death.remains<=3.5&variable.maintenance&(variable.targets>1\|raid_event.adds.up\|!buff.flagellation_buff.up\|dot.rupture.remains>=30)&(!talent.flagellation\|cooldown.flagellation.remains>=30-15*!talent.death_perception&cooldown.secret_technique.remains<8\|!talent.death_perception)\|fight_remains<=15) |
| 4 | `shadow_blades` | if=variable.maintenance&variable.shd_cp&buff.shadow_dance.up&!buff.premeditation.up |
| 5 | `thistle_tea` | if=buff.shadow_dance.remains>4&!buff.thistle_tea.up |
| 6 | `flagellation` | if=combo_points>=5&cooldown.shadow_blades.remains<=3\|fight_remains<=25 |

## Action List: `fill`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `arcane_torrent` | if=energy.deficit>=15+energy.regen |
| 2 | `arcane_pulse` | — |
| 3 | `lights_judgment` | — |
| 4 | `bag_of_tricks` | — |

## Action List: `finish`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `secret_technique` | if=variable.secret |
| 2 | `rupture` | if=!variable.skip_rupture&(!dot.rupture.ticking\|refreshable&cooldown.shadow_blades.remains>=12\|buff.flagellation_buff.up&!buff.symbols_of_death.up&variable.targets<=2)&target.time_to_die-remains>6 |
| 3 | `rupture` | cycle_targets=1,if=!variable.skip_rupture&!variable.priority_rotation&target.time_to_die>=(2*combo_points)&refreshable&variable.targets>=2 |
| 4 | `coup_de_grace` | if=debuff.fazed.up&(cooldown.flagellation.remains>=20\|!talent.flagellation)\|fight_remains<=10 |
| 5 | `black_powder` | if=!variable.priority_rotation&variable.maintenance&(((variable.targets>=2&talent.deathstalkers_mark&(!buff.darkest_night.up\|buff.shadow_dance.up&variable.targets>=5))\|talent.unseen_blade&variable.targets>=4)\|action.coup_de_grace.ready&variable.targets>=3) |
| 6 | `eviscerate` | if=cooldown.flagellation.remains>=10\|!talent.flagellation\|variable.targets>=3 |

## Action List: `item`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | name=treacherous_transmitter,if=cooldown.flagellation.remains<=2\|fight_remains<=15 |
| 2 | `do_treacherous_transmitter_task` | if=buff.shadow_dance.up\|fight_remains<=15 |
| 3 | `use_item` | name=imperfect_ascendancy_serum,use_off_gcd=1,if=dot.rupture.ticking&buff.flagellation_buff.up |
| 4 | `use_item` | name=mad_queens_mandate,if=(!talent.lingering_darkness\|buff.lingering_darkness.up\|equipped.treacherous_transmitter)&(!equipped.treacherous_transmitter\|trinket.treacherous_transmitter.cooldown.remains>20)\|fight_remains<=15 |
| 5 | `use_item` | name=cursed_stone_idol,use_off_gcd=1,if=dot.rupture.remains>=30&(buff.flagellation_buff.up\|!talent.flagellation)&buff.latent_energy.stack<=16\|fight_remains<=20 |
| 6 | `use_item` | name=unyielding_netherprism,use_off_gcd=1,if=buff.shadow_blades.up&(buff.latent_energy.stack>=8+8*(trinket.arazs_ritual_forge.cooldown.ready\|!equipped.arazs_ritual_forge)\|!equipped.arazs_ritual_forge&fight_remains<=90)\|fight_remains<=20 |
| 7 | `use_items` | slots=trinket1,if=(variable.trinket_sync_slot=1&(buff.shadow_blades.up\|fight_remains<=20+equipped.unyielding_netherprism*20)\|(variable.trinket_sync_slot=2&(!trinket.2.cooldown.ready&cooldown.shadow_blades.remains>20))\|!variable.trinket_sync_slot) |
| 8 | `use_items` | slots=trinket2,if=(variable.trinket_sync_slot=2&(buff.shadow_blades.up\|fight_remains<=20+equipped.unyielding_netherprism*20)\|(variable.trinket_sync_slot=1&(!trinket.1.cooldown.ready&cooldown.shadow_blades.remains>20))\|!variable.trinket_sync_slot) |

## Action List: `race`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blood_fury` | if=variable.racial_sync |
| 2 | `berserking` | if=variable.racial_sync |
| 3 | `fireblood` | if=variable.racial_sync&buff.shadow_dance.up |
| 4 | `ancestral_call` | if=variable.racial_sync |
| 5 | `invoke_external_buff` | name=power_infusion,if=buff.shadow_dance.up |

## Action List: `stealth_cds`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `shadow_dance` | if=(variable.shd_cp\|!talent.premeditation)&variable.maintenance&(cooldown.secret_technique.remains<=24\|talent.the_first_dance&buff.shadow_blades.up)&(buff.symbols_of_death.remains>=6\|buff.shadow_blades.remains>=6)\|fight_remains<=10 |
| 2 | `vanish` | if=energy>=40&!buff.subterfuge.up&effective_combo_points<=3 |
| 3 | `shadowmeld` | if=energy>=40&combo_points.deficit>=3 |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
# Consumables
actions.precombat=apply_poison
actions.precombat+=/snapshot_stats
actions.precombat+=/variable,name=priority_rotation,value=priority_rotation
actions.precombat+=/variable,name=trinket_sync_slot,value=1,if=trinket.1.has_use_buff&(!trinket.2.has_use_buff|trinket.1.is.treacherous_transmitter|trinket.1.cooldown.duration>=trinket.2.cooldown.duration)
actions.precombat+=/variable,name=trinket_sync_slot,value=2,if=trinket.2.has_use_buff&(!trinket.1.has_use_buff|trinket.2.cooldown.duration>trinket.1.cooldown.duration)
actions.precombat+=/stealth

# Executed every time the actor is available.
actions=stealth
# Variables
actions+=/variable,name=stealth,value=buff.shadow_dance.up|buff.stealth.up|buff.vanish.up
actions+=/variable,name=targets,value=spell_targets.shuriken_storm
actions+=/variable,name=skip_rupture,value=buff.shadow_dance.up|buff.darkest_night.up|variable.targets>=4&(!talent.replicating_shadows&talent.unseen_blade|raid_event.adds.up|buff.flagellation_buff.up&(fight_remains%%90<30|!talent.shuriken_tornado))
actions+=/variable,name=maintenance,value=(dot.rupture.ticking|variable.skip_rupture)&(buff.slice_and_dice.up|variable.targets<=2)
actions+=/variable,name=secret,value=buff.shadow_dance.up&!buff.darkest_night.up|(cooldown.flagellation.remains<60&cooldown.flagellation.remains>30&talent.death_perception&talent.unseen_blade)
actions+=/variable,name=racial_sync,value=(buff.shadow_blades.up&buff.shadow_dance.up)|!talent.shadow_blades&buff.symbols_of_death.up|fight_remains<20
actions+=/variable,name=shd_cp,value=combo_points<=1|buff.darkest_night.up&combo_points>=7|effective_combo_points>=6&talent.unseen_blade
# Cooldowns
actions+=/call_action_list,name=cds
# Racials
actions+=/call_action_list,name=race
# Items (Trinkets)
actions+=/call_action_list,name=item
# Cooldowns for Stealth
actions+=/call_action_list,name=stealth_cds,if=!variable.stealth
# Finishing Rules
actions+=/call_action_list,name=finish,if=!buff.darkest_night.up&effective_combo_points>=6|buff.darkest_night.up&combo_points==cp_max_spend|action.coup_de_grace.ready&cooldown.secret_technique.remains>0
# Combo Point Builder
actions+=/call_action_list,name=build
# Filler, Spells used if you can use nothing else.
actions+=/call_action_list,name=fill,if=!variable.stealth

actions.build=shuriken_tornado,if=(buff.tww3_trickster_4pc.up|buff.escalating_blade.stack=4)&(variable.targets>=4|!buff.shadow_blades.up)
actions.build+=/shuriken_storm,if=(buff.tww3_trickster_4pc.up|buff.escalating_blade.stack=4)&!used_for_danse&(buff.shadow_blades.up|variable.targets>=4)
actions.build+=/backstab,if=(talent.unseen_blade|variable.targets<=2)&(buff.shadow_dance.remains>7&(buff.premeditation.up|buff.shadow_blades.up)&!used_for_danse|!variable.stealth&buff.shadow_blades.up)
actions.build+=/gloomblade,if=(talent.unseen_blade|variable.targets<=2)&(buff.shadow_dance.remains>7&(buff.premeditation.up|buff.shadow_blades.up)&!used_for_danse|!variable.stealth&buff.shadow_blades.up)
actions.build+=/shuriken_tornado,if=buff.lingering_darkness.up|talent.deathstalkers_mark&cooldown.shadow_blades.remains>=32&variable.targets>=3
actions.build+=/shuriken_storm,if=buff.clear_the_witnesses.up&(variable.targets>=2|!buff.symbols_of_death.up)
actions.build+=/shadowstrike,cycle_targets=1,if=debuff.find_weakness.remains<=2&variable.targets>=2&talent.unseen_blade&!variable.priority_rotation
actions.build+=/shadowstrike,cycle_targets=1,if=talent.deathstalkers_mark&!debuff.deathstalkers_mark.up&variable.targets>=3&(buff.shadow_blades.up|buff.premeditation.up|talent.the_rotten)
actions.build+=/shuriken_storm,if=talent.deathstalkers_mark&variable.targets>=(2+3*buff.shadow_dance.up)
actions.build+=/shuriken_storm,if=talent.unseen_blade&buff.flawless_form.up&variable.targets>=3&!variable.stealth
actions.build+=/shadowstrike
actions.build+=/goremaws_bite,if=combo_points.deficit>=3
actions.build+=/gloomblade
actions.build+=/backstab

# Cooldowns
actions.cds=cold_blood,if=cooldown.secret_technique.up&buff.shadow_dance.up&combo_points>=6&variable.secret&(buff.flagellation_persist.up|buff.flagellation_buff.remains<=3|!talent.flagellation)
actions.cds+=/potion,if=buff.bloodlust.react|fight_remains<30|buff.shadow_blades.up
actions.cds+=/symbols_of_death,if=(buff.symbols_of_death.remains<=3.5&variable.maintenance&(variable.targets>1|raid_event.adds.up|!buff.flagellation_buff.up|dot.rupture.remains>=30)&(!talent.flagellation|cooldown.flagellation.remains>=30-15*!talent.death_perception&cooldown.secret_technique.remains<8|!talent.death_perception)|fight_remains<=15)
actions.cds+=/shadow_blades,if=variable.maintenance&variable.shd_cp&buff.shadow_dance.up&!buff.premeditation.up
actions.cds+=/thistle_tea,if=buff.shadow_dance.remains>4&!buff.thistle_tea.up
actions.cds+=/flagellation,if=combo_points>=5&cooldown.shadow_blades.remains<=3|fight_remains<=25

# This list usually contains Cooldowns with neglectable impact that causes global cooldowns
actions.fill=arcane_torrent,if=energy.deficit>=15+energy.regen
actions.fill+=/arcane_pulse
actions.fill+=/lights_judgment
actions.fill+=/bag_of_tricks

actions.finish=secret_technique,if=variable.secret
# Maintenance Finisher
actions.finish+=/rupture,if=!variable.skip_rupture&(!dot.rupture.ticking|refreshable&cooldown.shadow_blades.remains>=12|buff.flagellation_buff.up&!buff.symbols_of_death.up&variable.targets<=2)&target.time_to_die-remains>6
actions.finish+=/rupture,cycle_targets=1,if=!variable.skip_rupture&!variable.priority_rotation&target.time_to_die>=(2*combo_points)&refreshable&variable.targets>=2
# Direct Damage Finisher
actions.finish+=/coup_de_grace,if=debuff.fazed.up&(cooldown.flagellation.remains>=20|!talent.flagellation)|fight_remains<=10
actions.finish+=/black_powder,if=!variable.priority_rotation&variable.maintenance&(((variable.targets>=2&talent.deathstalkers_mark&(!buff.darkest_night.up|buff.shadow_dance.up&variable.targets>=5))|talent.unseen_blade&variable.targets>=4)|action.coup_de_grace.ready&variable.targets>=3)
actions.finish+=/eviscerate,if=cooldown.flagellation.remains>=10|!talent.flagellation|variable.targets>=3

# Trinket and Items
actions.item=use_item,name=treacherous_transmitter,if=cooldown.flagellation.remains<=2|fight_remains<=15
actions.item+=/do_treacherous_transmitter_task,if=buff.shadow_dance.up|fight_remains<=15
actions.item+=/use_item,name=imperfect_ascendancy_serum,use_off_gcd=1,if=dot.rupture.ticking&buff.flagellation_buff.up
actions.item+=/use_item,name=mad_queens_mandate,if=(!talent.lingering_darkness|buff.lingering_darkness.up|equipped.treacherous_transmitter)&(!equipped.treacherous_transmitter|trinket.treacherous_transmitter.cooldown.remains>20)|fight_remains<=15
actions.item+=/use_item,name=cursed_stone_idol,use_off_gcd=1,if=dot.rupture.remains>=30&(buff.flagellation_buff.up|!talent.flagellation)&buff.latent_energy.stack<=16|fight_remains<=20
actions.item+=/use_item,name=unyielding_netherprism,use_off_gcd=1,if=buff.shadow_blades.up&(buff.latent_energy.stack>=8+8*(trinket.arazs_ritual_forge.cooldown.ready|!equipped.arazs_ritual_forge)|!equipped.arazs_ritual_forge&fight_remains<=90)|fight_remains<=20
actions.item+=/use_items,slots=trinket1,if=(variable.trinket_sync_slot=1&(buff.shadow_blades.up|fight_remains<=20+equipped.unyielding_netherprism*20)|(variable.trinket_sync_slot=2&(!trinket.2.cooldown.ready&cooldown.shadow_blades.remains>20))|!variable.trinket_sync_slot)
actions.item+=/use_items,slots=trinket2,if=(variable.trinket_sync_slot=2&(buff.shadow_blades.up|fight_remains<=20+equipped.unyielding_netherprism*20)|(variable.trinket_sync_slot=1&(!trinket.1.cooldown.ready&cooldown.shadow_blades.remains>20))|!variable.trinket_sync_slot)

# Race Cooldowns
actions.race=blood_fury,if=variable.racial_sync
actions.race+=/berserking,if=variable.racial_sync
actions.race+=/fireblood,if=variable.racial_sync&buff.shadow_dance.up
actions.race+=/ancestral_call,if=variable.racial_sync
actions.race+=/invoke_external_buff,name=power_infusion,if=buff.shadow_dance.up

# Shadow Dance, Vanish, Shadowmeld
actions.stealth_cds=shadow_dance,if=(variable.shd_cp|!talent.premeditation)&variable.maintenance&(cooldown.secret_technique.remains<=24|talent.the_first_dance&buff.shadow_blades.up)&(buff.symbols_of_death.remains>=6|buff.shadow_blades.remains>=6)|fight_remains<=10
actions.stealth_cds+=/vanish,if=energy>=40&!buff.subterfuge.up&effective_combo_points<=3
actions.stealth_cds+=/shadowmeld,if=energy>=40&combo_points.deficit>=3
```
