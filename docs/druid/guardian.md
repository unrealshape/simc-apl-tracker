# Druid – Guardian

Auto-generated from SimulationCraft APL | Last updated: 2026-09-12 07:50 UTC

Source: `apl/default/druid/guardian.simc`

---

## Overview

- **Action Lists:** 4
- **Total Actions:** 56
- **Lists:** `precombat`, `default`, `bear`, `cooldowns`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `bear_form` | if=buff.bear_form.down&!talent.heart_of_the_wild.enabled |
| 3 | `cat_form` | if=buff.bear_form.down&talent.heart_of_the_wild.enabled |
| 4 | `variable` | name=algethar_puzzle_box_precombat_cast,value=3,if=equipped.algethar_puzzle_box |
| 5 | `use_item` | name=algethar_puzzle_box |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | — |
| 2 | `call_action_list` | name=cooldowns |
| 3 | `call_action_list` | name=bear |

## Action List: `bear`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `bear_form` | if=!buff.bear_form.up&!buff.feline_potential.up&!talent.fluid_form.enabled |
| 2 | `mangle` | if=buff.cat_form.up |
| 3 | `ironfur` | use_off_gcd=1,if=buff.gory_fur_ironfur.up |
| 4 | `ironfur` | use_off_gcd=1,if=rage>=40&!talent.killing_blow.enabled&!buff.answered_calling.up&!buff.dream_conduit.up |
| 5 | `ironfur` | use_off_gcd=1,if=rage>=80&!talent.killing_blow.enabled&buff.answered_calling.up |
| 6 | `ironfur` | use_off_gcd=1,if=(!buff.ironfur.up\|(buff.incarnation_guardian_of_ursoc.up\|buff.berserk.up))&!buff.answered_calling.up&talent.killing_blow.enabled&!buff.ravage.up&!buff.dream_conduit.up |
| 7 | `ironfur` | use_off_gcd=1,if=(!buff.ironfur.up\|(buff.incarnation_guardian_of_ursoc.up\|buff.berserk.up))&rage>=80&buff.answered_calling.up&talent.killing_blow.enabled&!buff.ravage.up&!buff.dream_conduit.up |
| 8 | `thrash` | target_if=refreshable\|(dot.thrash.stack<5&talent.flashing_claws.rank=2\|dot.thrash.stack<4&talent.flashing_claws.rank=1\|dot.thrash.stack<3&!talent.flashing_claws.enabled) |
| 9 | `mangle` | if=buff.answered_calling.up&active_enemies=1&talent.fount_of_strength.enabled |
| 10 | `thrash` | if=talent.lunar_calling.enabled\|set_bonus.midnight_season_2_4pc&(active_enemies>1\|buff.answered_calling.up) |
| 11 | `maul` | if=buff.dream_conduit.up&!talent.fount_of_strength.enabled&!buff.answered_calling.up |
| 12 | `maul` | if=rage>=55&talent.killing_blow.enabled&!buff.answered_calling.up |
| 13 | `maul` | if=rage>=80&talent.killing_blow.enabled&buff.answered_calling.up |
| 14 | `maul` | if=buff.gory_fur_maul.up&talent.raze.enabled |
| 15 | `maul` | if=buff.gory_fur_maul.up&!talent.raze.enabled&active_enemies<3 |
| 16 | `thrash` | if=active_enemies>=3&talent.fount_of_strength.enabled |
| 17 | `mangle` | if=dot.red_moon.ticking\|(buff.gorestained_claws.up\|buff.answered_calling.up)&talent.fount_of_strength.enabled |
| 18 | `rake` | if=!buff.cat_form.up&talent.fluid_form.enabled&cooldown.heart_of_the_wild.up&talent.heart_of_the_wild.enabled&(active_enemies<=5&talent.moonkin_form.enabled\|!talent.moonkin_form.enabled) |
| 19 | `cat_form` | if=!buff.cat_form.up&!talent.fluid_form.enabled&cooldown.heart_of_the_wild.up&talent.heart_of_the_wild.enabled&(active_enemies<=5&talent.moonkin_form.enabled\|!talent.moonkin_form.enabled)&(rage<30&!talent.fount_of_strength.enabled\|talent.fount_of_strength.enabled) |
| 20 | `moonkin_form` | if=!buff.moonkin_form.up&cooldown.heart_of_the_wild.up&active_enemies>=6&talent.moonkin_form.enabled |
| 21 | `thrash` | target_if=refreshable\|(dot.thrash.stack<5&talent.flashing_claws.rank=2\|dot.thrash.stack<4&talent.flashing_claws.rank=1\|dot.thrash.stack<3&!talent.flashing_claws.enabled) |
| 22 | `ferocious_bite` | if=(buff.cat_form.up&buff.feline_potential.up&(buff.incarnation_guardian_of_ursoc.up\|buff.berserk.up)&!dot.rip.refreshable) |
| 23 | `rake` | if=!buff.cat_form.up&talent.fluid_form.enabled&buff.feline_potential_counter.stack=6&talent.wildpower_surge.enabled&active_enemies<=2 |
| 24 | `rip` | if=(buff.cat_form.up&buff.feline_potential.up)&active_enemies<=2 |
| 25 | `red_moon` | if=cooldown.mangle.up&!dot.red_moon.ticking&(!talent.convoke_the_spirits.enabled\|talent.convoke_the_spirits.enabled&cooldown.convoke_the_spirits.remains>=5) |
| 26 | `mangle` | if=(((buff.incarnation_guardian_of_ursoc.up\|buff.berserk.up)&buff.feline_potential_counter.stack<6&talent.wildpower_surge.enabled)) |
| 27 | `shred` | if=(buff.feline_potential_counter.stack=6&!buff.cat_form.up&!dot.rake.refreshable&talent.fluid_form.enabled) |
| 28 | `rake` | if=(buff.feline_potential_counter.stack=6&!buff.cat_form.up&talent.fluid_form.enabled) |
| 29 | `maul` | if=!buff.ravage.up&rage>=90&talent.fount_of_strength.enabled&!talent.raze.enabled |
| 30 | `mangle` | if=(buff.incarnation_guardian_of_ursoc.up\|buff.berserk.up)\|talent.red_moon.enabled&(cooldown.red_moon.remains>3&(((rage<88)&!talent.fount_of_strength.enabled)\|((rage<83)&!talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled)\|((rage<108)&talent.fount_of_strength.enabled)\|((rage<103)&talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled))) |
| 31 | `mangle` | if=!talent.red_moon.enabled&(((rage<88)&!talent.fount_of_strength.enabled)\|((rage<83)&!talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled)\|((rage<108)&talent.fount_of_strength.enabled)\|((rage<103)&talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled)) |
| 32 | `thrash` | — |
| 33 | `moonfire` | if=talent.lunation.enabled&buff.bear_form.up&!talent.red_moon.enabled&(buff.galactic_guardian.up\|active_enemies<3\|refreshable) |
| 34 | `swipe_bear` | if=!talent.lunation.enabled\|(talent.lunation.enabled&talent.red_moon.enabled)\|talent.lunation.enabled&active_enemies>3 |

## Action List: `cooldowns`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_items` | — |
| 2 | `potion` | if=buff.lunar_beam.up |
| 3 | `blood_fury` | — |
| 4 | `berserking` | — |
| 5 | `fireblood` | — |
| 6 | `ancestral_call` | — |
| 7 | `bristling_fur` | if=!target.cooldown.pause_action.remains&cooldown.mangle.remains&cooldown.thrash.remains&(rage<60&talent.killing_blow.enabled\|rage<40&!talent.killing_blow.enabled)&!buff.ravage.up |
| 8 | `barkskin` | if=buff.bear_form.up |
| 9 | `lunar_beam` | if=(cooldown.incarnation_guardian_of_ursoc.up\|cooldown.berserk.up) |
| 10 | `heart_of_the_wild` | if=(active_enemies<=5&talent.moonkin_form.enabled&buff.cat_form.up\|!talent.moonkin_form.enabled&buff.cat_form.up)\|buff.moonkin_form.up&active_enemies>=6&talent.moonkin_form.enabled |
| 11 | `convoke_the_spirits` | if=buff.bear_form.up |
| 12 | `sundering_roar` | if=(dot.thrash.stack>4&talent.flashing_claws.rank=2\|dot.thrash.stack>3&talent.flashing_claws.rank=1\|dot.thrash.stack>2&!talent.flashing_claws.enabled)&!cooldown.thrash.up |
| 13 | `berserk` | if=(!cooldown.heart_of_the_wild.up&(talent.heart_of_the_wild.enabled)\|!talent.ravage.enabled\|!talent.heart_of_the_wild.enabled)&(!cooldown.thrash.up\|(buff.cat_form.up&!talent.convoke_the_spirits.enabled)) |
| 14 | `wild_guardian` | if=!buff.answered_calling.up&buff.lunar_beam.up |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Guardian APL can be found at https://github.com/dreamgrove/dreamgrove/blob/master/sims/bear/guardian.txt

# Executed before combat begins. Accepts non-harmful actions only.
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat=snapshot_stats
# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat+=/bear_form,if=buff.bear_form.down&!talent.heart_of_the_wild.enabled
actions.precombat+=/cat_form,if=buff.bear_form.down&talent.heart_of_the_wild.enabled
actions.precombat+=/variable,name=algethar_puzzle_box_precombat_cast,value=3,if=equipped.algethar_puzzle_box
actions.precombat+=/use_item,name=algethar_puzzle_box

# Executed every time the actor is available.
# Executed every time the actor is available.
actions=auto_attack
actions+=/call_action_list,name=cooldowns
actions+=/call_action_list,name=bear

actions.bear=bear_form,if=!buff.bear_form.up&!buff.feline_potential.up&!talent.fluid_form.enabled
actions.bear+=/mangle,if=buff.cat_form.up
actions.bear+=/ironfur,use_off_gcd=1,if=buff.gory_fur_ironfur.up
actions.bear+=/ironfur,use_off_gcd=1,if=rage>=40&!talent.killing_blow.enabled&!buff.answered_calling.up&!buff.dream_conduit.up
actions.bear+=/ironfur,use_off_gcd=1,if=rage>=80&!talent.killing_blow.enabled&buff.answered_calling.up
actions.bear+=/ironfur,use_off_gcd=1,if=(!buff.ironfur.up|(buff.incarnation_guardian_of_ursoc.up|buff.berserk.up))&!buff.answered_calling.up&talent.killing_blow.enabled&!buff.ravage.up&!buff.dream_conduit.up
actions.bear+=/ironfur,use_off_gcd=1,if=(!buff.ironfur.up|(buff.incarnation_guardian_of_ursoc.up|buff.berserk.up))&rage>=80&buff.answered_calling.up&talent.killing_blow.enabled&!buff.ravage.up&!buff.dream_conduit.up
actions.bear+=/thrash,target_if=refreshable|(dot.thrash.stack<5&talent.flashing_claws.rank=2|dot.thrash.stack<4&talent.flashing_claws.rank=1|dot.thrash.stack<3&!talent.flashing_claws.enabled)
actions.bear+=/mangle,if=buff.answered_calling.up&active_enemies=1&talent.fount_of_strength.enabled
actions.bear+=/thrash,if=talent.lunar_calling.enabled|set_bonus.midnight_season_2_4pc&(active_enemies>1|buff.answered_calling.up)
actions.bear+=/maul,if=buff.dream_conduit.up&!talent.fount_of_strength.enabled&!buff.answered_calling.up
actions.bear+=/maul,if=rage>=55&talent.killing_blow.enabled&!buff.answered_calling.up
actions.bear+=/maul,if=rage>=80&talent.killing_blow.enabled&buff.answered_calling.up
actions.bear+=/maul,if=buff.gory_fur_maul.up&talent.raze.enabled
actions.bear+=/maul,if=buff.gory_fur_maul.up&!talent.raze.enabled&active_enemies<3
actions.bear+=/thrash,if=active_enemies>=3&talent.fount_of_strength.enabled
actions.bear+=/mangle,if=dot.red_moon.ticking|(buff.gorestained_claws.up|buff.answered_calling.up)&talent.fount_of_strength.enabled
actions.bear+=/rake,if=!buff.cat_form.up&talent.fluid_form.enabled&cooldown.heart_of_the_wild.up&talent.heart_of_the_wild.enabled&(active_enemies<=5&talent.moonkin_form.enabled|!talent.moonkin_form.enabled)
actions.bear+=/cat_form,if=!buff.cat_form.up&!talent.fluid_form.enabled&cooldown.heart_of_the_wild.up&talent.heart_of_the_wild.enabled&(active_enemies<=5&talent.moonkin_form.enabled|!talent.moonkin_form.enabled)&(rage<30&!talent.fount_of_strength.enabled|talent.fount_of_strength.enabled)
actions.bear+=/moonkin_form,if=!buff.moonkin_form.up&cooldown.heart_of_the_wild.up&active_enemies>=6&talent.moonkin_form.enabled
actions.bear+=/thrash,target_if=refreshable|(dot.thrash.stack<5&talent.flashing_claws.rank=2|dot.thrash.stack<4&talent.flashing_claws.rank=1|dot.thrash.stack<3&!talent.flashing_claws.enabled)
actions.bear+=/ferocious_bite,if=(buff.cat_form.up&buff.feline_potential.up&(buff.incarnation_guardian_of_ursoc.up|buff.berserk.up)&!dot.rip.refreshable)
actions.bear+=/rake,if=!buff.cat_form.up&talent.fluid_form.enabled&buff.feline_potential_counter.stack=6&talent.wildpower_surge.enabled&active_enemies<=2
actions.bear+=/rip,if=(buff.cat_form.up&buff.feline_potential.up)&active_enemies<=2
actions.bear+=/red_moon,if=cooldown.mangle.up&!dot.red_moon.ticking&(!talent.convoke_the_spirits.enabled|talent.convoke_the_spirits.enabled&cooldown.convoke_the_spirits.remains>=5)
actions.bear+=/mangle,if=(((buff.incarnation_guardian_of_ursoc.up|buff.berserk.up)&buff.feline_potential_counter.stack<6&talent.wildpower_surge.enabled))
actions.bear+=/shred,if=(buff.feline_potential_counter.stack=6&!buff.cat_form.up&!dot.rake.refreshable&talent.fluid_form.enabled)
actions.bear+=/rake,if=(buff.feline_potential_counter.stack=6&!buff.cat_form.up&talent.fluid_form.enabled)
actions.bear+=/maul,if=!buff.ravage.up&rage>=90&talent.fount_of_strength.enabled&!talent.raze.enabled
actions.bear+=/mangle,if=(buff.incarnation_guardian_of_ursoc.up|buff.berserk.up)|talent.red_moon.enabled&(cooldown.red_moon.remains>3&(((rage<88)&!talent.fount_of_strength.enabled)|((rage<83)&!talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled)|((rage<108)&talent.fount_of_strength.enabled)|((rage<103)&talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled)))
actions.bear+=/mangle,if=!talent.red_moon.enabled&(((rage<88)&!talent.fount_of_strength.enabled)|((rage<83)&!talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled)|((rage<108)&talent.fount_of_strength.enabled)|((rage<103)&talent.fount_of_strength.enabled&talent.soul_of_the_forest.enabled))
actions.bear+=/thrash
actions.bear+=/moonfire,if=talent.lunation.enabled&buff.bear_form.up&!talent.red_moon.enabled&(buff.galactic_guardian.up|active_enemies<3|refreshable)
actions.bear+=/swipe_bear,if=!talent.lunation.enabled|(talent.lunation.enabled&talent.red_moon.enabled)|talent.lunation.enabled&active_enemies>3

actions.cooldowns=use_items
actions.cooldowns+=/potion,if=buff.lunar_beam.up
actions.cooldowns+=/blood_fury
actions.cooldowns+=/berserking
actions.cooldowns+=/fireblood
actions.cooldowns+=/ancestral_call
actions.cooldowns+=/bristling_fur,if=!target.cooldown.pause_action.remains&cooldown.mangle.remains&cooldown.thrash.remains&(rage<60&talent.killing_blow.enabled|rage<40&!talent.killing_blow.enabled)&!buff.ravage.up
actions.cooldowns+=/barkskin,if=buff.bear_form.up
actions.cooldowns+=/lunar_beam,if=(cooldown.incarnation_guardian_of_ursoc.up|cooldown.berserk.up)
actions.cooldowns+=/heart_of_the_wild,if=(active_enemies<=5&talent.moonkin_form.enabled&buff.cat_form.up|!talent.moonkin_form.enabled&buff.cat_form.up)|buff.moonkin_form.up&active_enemies>=6&talent.moonkin_form.enabled
actions.cooldowns+=/convoke_the_spirits,if=buff.bear_form.up
actions.cooldowns+=/sundering_roar,if=(dot.thrash.stack>4&talent.flashing_claws.rank=2|dot.thrash.stack>3&talent.flashing_claws.rank=1|dot.thrash.stack>2&!talent.flashing_claws.enabled)&!cooldown.thrash.up
actions.cooldowns+=/berserk,if=(!cooldown.heart_of_the_wild.up&(talent.heart_of_the_wild.enabled)|!talent.ravage.enabled|!talent.heart_of_the_wild.enabled)&(!cooldown.thrash.up|(buff.cat_form.up&!talent.convoke_the_spirits.enabled))
actions.cooldowns+=/wild_guardian,if=!buff.answered_calling.up&buff.lunar_beam.up
```
