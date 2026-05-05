# Monk – Windwalker

Auto-generated from SimulationCraft APL | Last updated: 2026-05-05 05:47 UTC

Source: `apl/default/monk/windwalker.simc`

---

## Overview

- **Action Lists:** 10
- **Total Actions:** 143
- **Lists:** `precombat`, `default`, `big_coc`, `default_st`, `fallback`, `multitarget`, `opener`, `racials`, `trinket`, `zenith`

## Action List: `precombat`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `snapshot_stats` | — |
| 2 | `use_item` | name=algethar_puzzle_box,if=!talent.flurry_strikes&(trinket.1.is.algethar_puzzle_box\|trinket.2.is.algethar_puzzle_box) |

## Action List: `default`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `auto_attack` | target_if=max:target.time_to_die |
| 2 | `touch_of_karma` | target_if=max:target.time_to_die |
| 3 | `roll` | if=movement.distance>5 |
| 4 | `chi_torpedo` | if=movement.distance>5 |
| 5 | `flying_serpent_kick` | if=movement.distance>5 |
| 6 | `spear_hand_strike` | if=target.debuff.casting.react |
| 7 | `potion` | if=buff.invoke_xuen_the_white_tiger.remains>15\|fight_remains<=30 |
| 8 | `potion` | if=talent.flurry_strikes&chi>2&(time<5\|cooldown.zenith.up&time<5\|time>300&((trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100\|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)\|!trinket.1.has_use_buff&!trinket.2.has_use_buff)&talent.flurry_strikes\|time>300&buff.zenith.up) |
| 9 | `variable` | name=has_external_pi,value=cooldown.invoke_power_infusion_0.duration>0 |
| 10 | `call_action_list` | name=opener,if=time<2 |
| 11 | `call_action_list` | name=trinket |
| 12 | `invoke_external_buff` | name=power_infusion,if=buff.zenith.up&(buff.invoke_xuen_the_white_tiger.up\|talent.flurry_strikes) |
| 13 | `call_action_list` | name=big_coc,if=talent.celestial_conduit |
| 14 | `call_action_list` | name=zenith |
| 15 | `call_action_list` | name=racials |
| 16 | `call_action_list` | name=default_st,if=active_enemies=1 |
| 17 | `call_action_list` | name=multitarget,if=active_enemies>1 |
| 18 | `call_action_list` | name=fallback |
| 19 | `arcane_torrent` | if=chi<chi.max&energy<55 |
| 20 | `thorn_bloom` | — |
| 21 | `haymaker` | — |
| 22 | `bag_of_tricks` | — |
| 23 | `arcane_pulse` | — |
| 24 | `rocket_barrage` | — |
| 25 | `lights_judgment` | — |

## Action List: `big_coc`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `invoke_xuen_the_white_tiger` | target_if=max:target.time_to_die,if=(target.time_to_die>35&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&((cooldown.zenith.up\|buff.zenith.remains>13)&!buff.heart_of_the_jade_serpent.up)&(!fight_style.dungeonslice\|active_enemies>1\|time<60) |
| 2 | `invoke_xuen_the_white_tiger` | target_if=max:target.time_to_die,if=(target.time_to_die>35&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&(trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100\|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)&(!fight_style.dungeonslice\|active_enemies>1\|time<60) |
| 3 | `invoke_xuen_the_white_tiger` | target_if=max:target.time_to_die,if=fight_style.dungeonslice&target.time_to_die>15&active_enemies>4\|fight_remains<=25 |
| 4 | `celestial_conduit` | target_if=max:target.time_to_die,if=buff.zenith.remains<12&buff.zenith.up&(!buff.bloodlust.up\|buff.power_infusion.up)\|fight_remains<4 |
| 5 | `whirling_dragon_punch` | if=buff.power_infusion.up&(!buff.heart_of_the_jade_serpent_unity_within.up\|buff.heart_of_the_jade_serpent_unity_within.remains<2) |
| 6 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&talent.celestial_conduit&buff.zenith.remains>11&chi<=2&cooldown.rising_sun_kick.remains&!buff.rushing_wind_kick.up&talent.obsidian_spiral&buff.combo_breaker.up |
| 7 | `tiger_palm` | target_if=max:target.time_to_die,if=combo_strike&talent.celestial_conduit&buff.zenith.remains>11&chi<=2&cooldown.rising_sun_kick.remains&!buff.rushing_wind_kick.up&(!talent.obsidian_spiral\|!buff.combo_breaker.up\|prev.blackout_kick) |
| 8 | `celestial_conduit` | target_if=max:target.time_to_die,if=buff.zenith.up&(cooldown.rising_sun_kick.remains\|active_enemies>2)&cooldown.fists_of_fury.remains&(cooldown.strike_of_the_windlord.remains\|talent.whirling_dragon_punch)&(cooldown.whirling_dragon_punch.remains\|talent.strike_of_the_windlord)&!buff.rushing_wind_kick.up&!buff.combo_breaker.up&chi>1&(!buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent.remains<4) |
| 9 | `celestial_conduit` | target_if=max:target.time_to_die,if=buff.zenith.up&!buff.heart_of_the_jade_serpent.up&!buff.heart_of_the_jade_serpent_yulons_avatar.up&chi>1&(cooldown.rising_sun_kick.remains\|active_enemies>2)&(cooldown.strike_of_the_windlord.remains\|(cooldown.whirling_dragon_punch.remains\|cooldown.fists_of_fury.remains)) |
| 10 | `celestial_conduit` | target_if=max:target.time_to_die,if=buff.zenith.up&buff.heart_of_the_jade_serpent.remains<2&prev.rising_sun_kick&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains&buff.heart_of_the_jade_serpent.up&chi>1 |

## Action List: `default_st`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `whirling_dragon_punch` | if=!buff.heart_of_the_jade_serpent_unity_within.up&buff.whirling_dragon_punch.remains<1&(buff.zenith.up\|cooldown.invoke_xuen_the_white_tiger.remains>5\|talent.flurry_strikes\|!fight_style.patchwerk) |
| 2 | `zenith_stomp` | if=buff.zenith.up&(buff.zenith.remains<5&buff.zenith_stomp.stack=2\|buff.zenith.remains<4)\|talent.celestial_conduit&chi<5&!buff.heart_of_the_jade_serpent_unity_within.up |
| 3 | `whirling_dragon_punch` | if=buff.power_infusion.up&(!buff.heart_of_the_jade_serpent_unity_within.up\|buff.heart_of_the_jade_serpent_unity_within.remains<2) |
| 4 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.remains<1&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.up&talent.celestial_conduit |
| 5 | `fists_of_fury` | if=buff.heart_of_the_jade_serpent.remains<1&buff.heart_of_the_jade_serpent.up\|buff.flurry_charge.stack=30&!buff.zenith.up |
| 6 | `whirling_dragon_punch` | if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2&(buff.zenith.up\|cooldown.invoke_xuen_the_white_tiger.remains>5\|!fight_style.patchwerk)\|talent.flurry_strikes |
| 7 | `tiger_palm` | if=chi<3-1*!talent.ascension+1*talent.celestial_conduit+1*(buff.tigereye_brew_1.stack<15&time>60&time<120)&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&(!buff.bloodlust.up\|chi<2)&buff.combo_breaker.stack<2 |
| 8 | `strike_of_the_windlord` | if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2&(buff.zenith.up\|cooldown.invoke_xuen_the_white_tiger.remains>5\|!fight_style.patchwerk)\|talent.flurry_strikes |
| 9 | `rising_sun_kick` | if=!buff.bloodlust.up&!buff.zenith.up&(chi>4\|energy>50\|cooldown.fists_of_fury.remains>5)\|buff.zenith.up&buff.zenith.remains<2&combo_strike |
| 10 | `fists_of_fury` | if=combo_strike&(buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_yulons_avatar.up\|buff.heart_of_the_jade_serpent_unity_within.up)&buff.bloodlust.up\|buff.bloodlust.up&talent.flurry_strikes\|!buff.zenith.up&(talent.flurry_strikes\|cooldown.invoke_xuen_the_white_tiger.remains>3\|!fight_style.patchwerk)\|buff.zenith.up&(talent.flurry_strikes\|!buff.bloodlust.up)&(fight_style.patchwerk\|target.time_to_die>5) |
| 11 | `rushing_wind_kick` | — |
| 12 | `rising_sun_kick` | if=combo_strike&buff.bloodlust.up\|combo_strike&(buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_yulons_avatar.up\|buff.heart_of_the_jade_serpent_unity_within.up) |
| 13 | `fists_of_fury` | if=buff.bloodlust.up\|combo_strike&(buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_yulons_avatar.up\|buff.heart_of_the_jade_serpent_unity_within.up) |
| 14 | `tiger_palm` | if=buff.zenith.up&chi<2&talent.celestial_conduit&(buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_unity_within.up)&!cooldown.fists_of_fury.remains&combo_strike |
| 15 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.remains<5&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.up\|combo_strike&buff.dance_of_chiji.stack=2&buff.combo_breaker.stack<2&talent.sequenced_strikes&(talent.flurry_strikes\|!buff.bloodlust.up) |
| 16 | `rising_sun_kick` | if=buff.zenith.up&talent.flurry_strikes&!cooldown.fists_of_fury.remains |
| 17 | `rising_sun_kick` | if=combo_strike |
| 18 | `fists_of_fury` | if=talent.flurry_strikes\|!buff.zenith.up&(talent.flurry_strikes\|cooldown.invoke_xuen_the_white_tiger.remains>3\|!fight_style.patchwerk)\|buff.bloodlust.up&talent.jadefire_stomp&cooldown.celestial_conduit.remains |
| 19 | `rising_sun_kick` | if=buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_unity_within.up\|buff.heart_of_the_jade_serpent_yulons_avatar.up |
| 20 | `touch_of_death` | if=!buff.zenith.up\|fight_remains<5\|((trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100\|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)\|!trinket.1.has_use_buff&!trinket.2.has_use_buff) |
| 21 | `strike_of_the_windlord` | if=buff.heart_of_the_jade_serpent_unity_within.remains<2&(buff.zenith.up\|cooldown.invoke_xuen_the_white_tiger.remains>5\|!fight_style.patchwerk)\|talent.flurry_strikes |
| 22 | `rising_sun_kick` | if=combo_strike&(buff.flurry_charge.stack<30\|chi>3\|buff.zenith.up\|buff.bloodlust.up\|energy>50&chi>2)\|combo_strike&buff.heart_of_the_jade_serpent.up |
| 23 | `tiger_palm` | if=combo_strike&buff.zenith.up&(chi<1\|chi<2&!buff.combo_breaker.up)&talent.celestial_conduit |
| 24 | `zenith_stomp` | if=buff.zenith.up&chi<5-1*!talent.ascension&(talent.flurry_strikes\|chi<3\|buff.zenith.remains<5)&buff.combo_breaker.stack<2&buff.dance_of_chiji.stack<2&(!buff.combo_breaker.up\|talent.echo_technique) |
| 25 | `blackout_kick` | if=combo_strike&buff.zenith.up&chi>1&(talent.obsidian_spiral\|cooldown.fists_of_fury.remains\|buff.combo_breaker.up)&(chi<6\|buff.combo_breaker.up\|cooldown.rising_sun_kick.remains<3) |
| 26 | `blackout_kick` | if=combo_strike&buff.combo_breaker.up |
| 27 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.up&talent.sequenced_strikes |
| 28 | `spinning_crane_kick` | if=combo_strike&buff.zenith.up&talent.flurry_strikes&chi>3+1*!talent.ascension |
| 29 | `slicing_winds` | — |
| 30 | `spinning_crane_kick` | if=talent.flurry_strikes&buff.zenith.up&chi>5-1*!talent.ascension&combo_strike\|combo_strike&buff.bloodlust.up&buff.dance_of_chiji.up&buff.combo_breaker.stack<2 |
| 31 | `tiger_palm` | if=combo_strike&((energy>55&talent.inner_peace\|energy>60&!talent.inner_peace)&chi.max-chi>=3-1*talent.celestial_conduit&(talent.energy_burst&!buff.combo_breaker.up\|!talent.energy_burst)&!buff.zenith.up\|(talent.energy_burst&!buff.combo_breaker.up\|!talent.energy_burst)&!buff.zenith.up&!cooldown.fists_of_fury.remains&chi<3) |

## Action List: `fallback`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `blackout_kick` | if=combo_strike |
| 2 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.up |
| 3 | `spinning_crane_kick` | if=chi>5&combo_strike&talent.flurry_strikes |
| 4 | `tiger_palm` | if=combo_strike |
| 5 | `spinning_crane_kick` | if=chi>5&combo_strike |

## Action List: `multitarget`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `fists_of_fury` | target_if=max:target.time_to_die,if=buff.heart_of_the_jade_serpent.remains<1&buff.heart_of_the_jade_serpent.up |
| 2 | `zenith_stomp` | target_if=max:target.time_to_die,if=buff.zenith.up&(buff.zenith.remains<5&buff.zenith_stomp.stack=2\|buff.zenith.remains<4)\|talent.celestial_conduit&chi<5&!buff.heart_of_the_jade_serpent_unity_within.up |
| 3 | `whirling_dragon_punch` | if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2 |
| 4 | `whirling_dragon_punch` | target_if=max:target.time_to_die,if=!buff.heart_of_the_jade_serpent_unity_within.up&buff.whirling_dragon_punch.remains<1 |
| 5 | `tiger_palm` | target_if=max:target.time_to_die,if=buff.zenith.up&chi<2&talent.celestial_conduit&(buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_unity_within.up)&!cooldown.fists_of_fury.remains&combo_strike |
| 6 | `tiger_palm` | target_if=max:target.time_to_die,if=chi<5&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&!buff.bloodlust.up&buff.combo_breaker.stack<2\|combo_strike&chi<3-1*buff.zenith.up&!cooldown.fists_of_fury.remains&(!buff.combo_breaker.up\|!talent.energy_burst)&!buff.zenith_stomp.up |
| 7 | `strike_of_the_windlord` | if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2 |
| 8 | `fists_of_fury` | target_if=max:target.time_to_die,if=buff.flurry_charge.stack=30&!buff.zenith.up\|buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_unity_within.up\|buff.heart_of_the_jade_serpent_yulons_avatar.up\|talent.flurry_strikes |
| 9 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.up&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.remains<3 |
| 10 | `rushing_wind_kick` | target_if=max:target.time_to_die |
| 11 | `rising_sun_kick` | target_if=max:target.time_to_die,if=(active_enemies<5\|cooldown.fists_of_fury.remains>1\|buff.zenith.up)&(buff.rushing_wind_kick.up\|buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_unity_within.up\|buff.heart_of_the_jade_serpent_yulons_avatar.up) |
| 12 | `zenith_stomp` | target_if=max:target.time_to_die,if=buff.zenith.up&chi<5-1*!talent.ascension&(talent.flurry_strikes\|chi<3\|buff.zenith.remains<5)&buff.combo_breaker.stack<2&buff.dance_of_chiji.stack<2&(!buff.combo_breaker.up\|talent.echo_technique) |
| 13 | `touch_of_death` | target_if=min:target.time_to_die,if=!buff.zenith.up\|fight_remains<5\|((trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100\|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)\|!trinket.1.has_use_buff&!trinket.2.has_use_buff) |
| 14 | `strike_of_the_windlord` | if=buff.zenith.up\|cooldown.zenith.remains>5&buff.heart_of_the_jade_serpent_unity_within.remains<2 |
| 15 | `whirling_dragon_punch` | if=buff.zenith.up\|cooldown.zenith.remains>5&buff.heart_of_the_jade_serpent_unity_within.remains<2 |
| 16 | `fists_of_fury` | target_if=max:target.time_to_die,if=talent.flurry_strikes\|!buff.zenith.up\|buff.bloodlust.up&talent.jadefire_stomp&cooldown.celestial_conduit.remains |
| 17 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.stack=2&buff.combo_breaker.stack<2&talent.sequenced_strikes |
| 18 | `rising_sun_kick` | target_if=max:target.time_to_die,if=(active_enemies<5\|cooldown.fists_of_fury.remains>1\|buff.zenith.up)&(combo_strike&(buff.flurry_charge.stack<30\|chi>3\|buff.zenith.up\|buff.bloodlust.up\|energy>50&chi>2)\|combo_strike&buff.heart_of_the_jade_serpent.up) |
| 19 | `spinning_crane_kick` | target_if=max:target.time_to_die,if=talent.flurry_strikes&buff.zenith.up&chi>3&combo_strike&(!talent.shadowboxing_treads\|active_enemies>3) |
| 20 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&buff.zenith.up&chi>1&(talent.obsidian_spiral\|buff.combo_breaker.up\|cooldown.rising_sun_kick.remains<3&cooldown.rising_sun_kick.remains\|talent.shadowboxing_treads&cooldown.rising_sun_kick.remains)&chi<6 |
| 21 | `spinning_crane_kick` | if=combo_strike&buff.dance_of_chiji.up&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.remains<4 |
| 22 | `slicing_winds` | — |
| 23 | `spinning_crane_kick` | target_if=max:target.time_to_die,if=talent.flurry_strikes&buff.zenith.up&chi>3&combo_strike |
| 24 | `spinning_crane_kick` | target_if=max:target.time_to_die,if=combo_strike&(buff.dance_of_chiji.up\|(chi>2\|energy>55))&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains&!talent.shadowboxing_treads&!buff.zenith.up |
| 25 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.up&(buff.heart_of_the_jade_serpent.up\|buff.heart_of_the_jade_serpent_unity_within.up) |
| 26 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.up |
| 27 | `tiger_palm` | target_if=max:target.time_to_die,if=chi<5&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&!buff.bloodlust.up |
| 28 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.stack=2 |
| 29 | `spinning_crane_kick` | target_if=max:target.time_to_die,if=combo_strike&buff.dance_of_chiji.stack=2 |
| 30 | `spinning_crane_kick` | if=combo_strike&!buff.zenith.up&chi>5&buff.combo_breaker.up&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains |
| 31 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.up |
| 32 | `tiger_palm` | target_if=max:target.time_to_die,if=chi<5&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&active_enemies<3 |
| 33 | `tiger_palm` | target_if=max:target.time_to_die,if=combo_strike&((energy>55&talent.inner_peace\|energy>60&!talent.inner_peace)&chi.max-chi>=2&(talent.energy_burst&!buff.combo_breaker.up\|!talent.energy_burst)&!buff.zenith.up\|(talent.energy_burst&!buff.combo_breaker.up\|!talent.energy_burst)&!buff.zenith.up&!cooldown.fists_of_fury.remains&chi<3) |
| 34 | `blackout_kick` | target_if=max:target.time_to_die,if=combo_strike&talent.shadowboxing_treads |
| 35 | `spinning_crane_kick` | target_if=max:target.time_to_die,if=combo_strike&(chi>3\|energy>55)&(!talent.shadowboxing_treads&active_enemies>2\|active_enemies>5)&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains |
| 36 | `rising_sun_kick` | target_if=max:target.time_to_die,if=combo_strike |
| 37 | `spinning_crane_kick` | target_if=max:target.time_to_die,if=combo_strike&chi>2 |

## Action List: `opener`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `tiger_palm` | if=combo_strike&chi<4 |
| 2 | `use_item` | name=algethar_puzzle_box,if=target.time_to_die>25&(cooldown.invoke_xuen_the_white_tiger.remains<2\|talent.flurry_strikes&cooldown.zenith.up)\|fight_remains<25 |

## Action List: `racials`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `berserking` | if=buff.invoke_xuen_the_white_tiger.remains>15\|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14\|fight_remains<20 |
| 2 | `ancestral_call` | if=buff.invoke_xuen_the_white_tiger.remains>15\|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14\|fight_remains<20 |
| 3 | `blood_fury` | if=buff.invoke_xuen_the_white_tiger.remains>15\|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14\|fight_remains<20 |
| 4 | `fireblood` | if=buff.invoke_xuen_the_white_tiger.remains>15\|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14\|fight_remains<20 |

## Action List: `trinket`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `use_item` | slot=main_hand |
| 2 | `use_item` | name=algethar_puzzle_box,if=fight_remains>5&(!buff.zenith.up&!talent.flurry_strikes&(target.time_to_die>35&fight_style.dungeonroute\|target.time_to_die>25)&(cooldown.potion.remains>30\|fight_remains<45\|fight_remains>80)&(cooldown.invoke_xuen_the_white_tiger.remains<2\|talent.flurry_strikes&cooldown.zenith.up)\|fight_remains<25\|talent.flurry_strikes&(target.time_to_die>35&fight_style.dungeonroute\|target.time_to_die>25)&!buff.zenith.up\|fight_style.dungeonslice&(time<5&chi>3\|active_enemies>3&target.time_to_die>15)) |
| 3 | `use_item` | slot=trinket1,if=trinket.1.has_use_buff&!trinket.2.has_use_buff&(pet.xuen_the_white_tiger.active&talent.invoke_xuen_the_white_tiger\|talent.flurry_strikes&buff.zenith.remains>14) |
| 4 | `use_item` | slot=trinket2,if=trinket.2.has_use_buff&!trinket.1.has_use_buff&(pet.xuen_the_white_tiger.active&talent.invoke_xuen_the_white_tiger\|talent.flurry_strikes&buff.zenith.remains>14) |
| 5 | `use_item` | slot=trinket1,if=trinket.1.has_use_buff&trinket.2.has_use_buff&(pet.xuen_the_white_tiger.active&talent.invoke_xuen_the_white_tiger\|talent.flurry_strikes&buff.zenith.remains>14) |
| 6 | `use_item` | slot=trinket2,if=trinket.1.has_use_buff&trinket.2.has_use_buff&(cooldown.invoke_xuen_the_white_tiger.remains>30&(buff.zenith.up\|(cooldown.strike_of_the_windlord.remains<2&talent.strike_of_the_windlord\|cooldown.whirling_dragon_punch.remains<2&talent.whirling_dragon_punch))\|talent.flurry_strikes&buff.zenith.remains>10) |
| 7 | `use_item` | slot=trinket1,if=!trinket.1.has_use_buff&trinket.2.has_use_buff&trinket.2.cooldown.remains>30 |
| 8 | `use_item` | slot=trinket2,if=!trinket.2.has_use_buff&trinket.1.has_use_buff&trinket.1.cooldown.remains>30 |
| 9 | `use_item` | slot=trinket1,if=!trinket.1.has_use_buff&!trinket.2.has_use_buff |
| 10 | `use_item` | slot=trinket2,if=!trinket.1.has_use_buff&!trinket.2.has_use_buff |

## Action List: `zenith`

| # | Action | Conditions |
|---|--------|------------|
| 1 | `zenith` | target_if=max:target.time_to_die,if=buff.invoke_xuen_the_white_tiger.up&(!buff.zenith.up\|talent.flurry_strikes) |
| 2 | `zenith` | target_if=max:target.time_to_die,if=buff.bloodlust.remains>30&(active_enemies>2\|cooldown.rising_sun_kick.remains)&!buff.zenith.up |
| 3 | `zenith` | target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&(buff.bloodlust.up&cooldown.celestial_conduit.remains&(cooldown.rising_sun_kick.remains\|active_enemies>2)&!buff.zenith.up&talent.celestial_conduit) |
| 4 | `zenith` | target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&(talent.flurry_strikes&(buff.bloodlust.up\|cooldown.potion.remains>295))&!buff.zenith.up&(buff.bloodlust.remains>30\|talent.spiritual_focus) |
| 5 | `zenith` | target_if=max:target.time_to_die,if=time>250&cooldown.potion.remains>295&(!trinket.1.has_use_buff&!trinket.2.has_use_buff\|trinket.1.has_use_buff&trinket.1.cooldown.remains>30\|trinket.2.has_use_buff&trinket.2.cooldown.remains>30)&(fight_remains>120\|fight_remains<50&fight_remains>cooldown.zenith.full_recharge_time) |
| 6 | `zenith` | target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&talent.flurry_strikes&!trinket.1.has_use_buff&!trinket.2.has_use_buff&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains<5&(cooldown.whirling_dragon_punch.remains<10\|cooldown.strike_of_the_windlord.remains<10)&cooldown.zenith.full_recharge_time<40&!fight_style.dungeonslice&!buff.zenith.up |
| 7 | `zenith` | target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&(!buff.bloodlust.up&(trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100\|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)&(cooldown.rising_sun_kick.remains\|active_enemies>2\|talent.drinking_horn_cover&chi<2))&!buff.zenith.up |
| 8 | `zenith` | target_if=max:target.time_to_die,if=(fight_style.patchwerk\|fight_style.dungeonroute&target.time_to_die>27+5*talent.drinking_horn_cover)&talent.flurry_strikes&(buff.tigereye_brew_1.stack>19-2*talent.echo_technique\|buff.tigereye_brew_1.stack>11&talent.spiritual_focus-2*talent.echo_technique)&(target.time_to_die>30&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute)&(cooldown.rising_sun_kick.remains\|active_enemies>1)&(!trinket.1.has_use_buff&!trinket.2.has_use_buff\|trinket.1.has_use_buff&(trinket.1.cooldown.remains>40\|trinket.1.cooldown.remains>30&talent.spiritual_focus)\|trinket.2.has_use_buff&(trinket.2.cooldown.remains>40\|trinket.2.cooldown.remains>30&talent.spiritual_focus))&(talent.strike_of_the_windlord&cooldown.strike_of_the_windlord.remains<15-5*talent.revolving_whirl&talent.drinking_horn_cover\|talent.whirling_dragon_punch&cooldown.whirling_dragon_punch.remains<15-7*talent.revolving_whirl&talent.drinking_horn_cover\|talent.strike_of_the_windlord&cooldown.strike_of_the_windlord.remains<10\|talent.whirling_dragon_punch&cooldown.whirling_dragon_punch.remains<10)&cooldown.fists_of_fury.remains<9+4*talent.spiritual_focus |
| 9 | `zenith` | target_if=max:target.time_to_die,if=(cooldown.rising_sun_kick.remains\|active_enemies>2)&fight_style.dungeonslice&time>130&time<150&active_enemies>1&talent.flurry_strikes&!buff.zenith.up |
| 10 | `zenith` | target_if=max:target.time_to_die,if=fight_style.dungeonslice&target.time_to_die>15&active_enemies>4&(talent.flurry_strikes\|talent.celestial_conduit&talent.restore_balance&cooldown.invoke_xuen_the_white_tiger.remains<cooldown.zenith.full_recharge_time)&!fight_style.patchwerk&!buff.zenith.up |
| 11 | `zenith` | target_if=max:target.time_to_die,if=!buff.zenith.up&(talent.celestial_conduit&fight_remains<cooldown.invoke_xuen_the_white_tiger.remains&(cooldown.rising_sun_kick.remains\|active_enemies>2)&(target.time_to_die>30&fight_style.dungeonroute\|target.time_to_die>25&!fight_style.dungeonroute\|target.time_to_die>15&active_enemies>4)&!fight_style.patchwerk) |
| 12 | `zenith` | target_if=max:target.time_to_die,if=!buff.zenith.up&talent.flurry_strikes&fight_style.dungeonroute&cooldown.zenith.full_recharge_time<30&target.time_to_die>25 |
| 13 | `zenith` | target_if=max:target.time_to_die,if=fight_style.patchwerk&!buff.zenith.up&cooldown.fists_of_fury.remains<10&(cooldown.whirling_dragon.remains<10\|cooldown.strike_of_the_windlord.remains<10)&(cooldown.rising_sun_kick.remains\|chi<2&energy<50\|active_enemies>1)&cooldown.zenith.full_recharge_time<30&(!trinket.1.has_use_buff&!trinket.2.has_use_buff\|trinket.1.has_use_buff&trinket.1.cooldown.remains>30\|trinket.2.has_use_buff&trinket.2.cooldown.remains>30)&(fight_remains>120\|fight_remains<50&fight_remains>cooldown.zenith.full_recharge_time) |
| 14 | `zenith` | target_if=max:target.time_to_die,if=fight_remains<=24&(cooldown.rising_sun_kick.remains\|active_enemies>2) |
| 15 | `zenith` | target_if=max:target.time_to_die,if=fight_remains<45&cooldown.zenith.full_recharge_time<5&(cooldown.rising_sun_kick.remains\|active_enemies>1) |
| 16 | `zenith` | target_if=max:target.time_to_die,if=!buff.zenith.up&(fight_style.patchwerk&!trinket.1.is.algethar_puzzle_box&!trinket.2.is.algethar_puzzle_box&trinket.1.has_use_buff&(trinket.1.cooldown.ready\|cooldown.zenith.full_recharge_time<5)) |
| 17 | `zenith` | target_if=max:target.time_to_die,if=!buff.zenith.up&(fight_style.patchwerk&!trinket.1.is.algethar_puzzle_box&!trinket.2.is.algethar_puzzle_box&trinket.2.has_use_buff&(trinket.2.cooldown.ready\|cooldown.zenith.full_recharge_time<5)) |

## Raw APL

```
# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
# Snapshot raid buffed stats before combat begins.
actions.precombat=snapshot_stats
actions.precombat+=/use_item,name=algethar_puzzle_box,if=!talent.flurry_strikes&(trinket.1.is.algethar_puzzle_box|trinket.2.is.algethar_puzzle_box)

# Executed every time the actor is available.
# Default List
actions=auto_attack,target_if=max:target.time_to_die
actions+=/touch_of_karma,target_if=max:target.time_to_die
# Move to target
actions+=/roll,if=movement.distance>5
actions+=/chi_torpedo,if=movement.distance>5
actions+=/flying_serpent_kick,if=movement.distance>5
actions+=/spear_hand_strike,if=target.debuff.casting.react
actions+=/potion,if=buff.invoke_xuen_the_white_tiger.remains>15|fight_remains<=30
actions+=/potion,if=talent.flurry_strikes&chi>2&(time<5|cooldown.zenith.up&time<5|time>300&((trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)|!trinket.1.has_use_buff&!trinket.2.has_use_buff)&talent.flurry_strikes|time>300&buff.zenith.up)
# Enable PI if available
actions+=/variable,name=has_external_pi,value=cooldown.invoke_power_infusion_0.duration>0
actions+=/call_action_list,name=opener,if=time<2
actions+=/call_action_list,name=trinket
actions+=/invoke_external_buff,name=power_infusion,if=buff.zenith.up&(buff.invoke_xuen_the_white_tiger.up|talent.flurry_strikes)
actions+=/call_action_list,name=big_coc,if=talent.celestial_conduit
actions+=/call_action_list,name=zenith
actions+=/call_action_list,name=racials
actions+=/call_action_list,name=default_st,if=active_enemies=1
actions+=/call_action_list,name=multitarget,if=active_enemies>1
actions+=/call_action_list,name=fallback
actions+=/arcane_torrent,if=chi<chi.max&energy<55
actions+=/thorn_bloom
actions+=/haymaker
actions+=/bag_of_tricks
actions+=/arcane_pulse
actions+=/rocket_barrage
actions+=/lights_judgment

# Celestial of the Conduit Burst Windows
actions.big_coc=invoke_xuen_the_white_tiger,target_if=max:target.time_to_die,if=(target.time_to_die>35&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&((cooldown.zenith.up|buff.zenith.remains>13)&!buff.heart_of_the_jade_serpent.up)&(!fight_style.dungeonslice|active_enemies>1|time<60)
actions.big_coc+=/invoke_xuen_the_white_tiger,target_if=max:target.time_to_die,if=(target.time_to_die>35&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&(trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)&(!fight_style.dungeonslice|active_enemies>1|time<60)
actions.big_coc+=/invoke_xuen_the_white_tiger,target_if=max:target.time_to_die,if=fight_style.dungeonslice&target.time_to_die>15&active_enemies>4|fight_remains<=25
actions.big_coc+=/celestial_conduit,target_if=max:target.time_to_die,if=buff.zenith.remains<12&buff.zenith.up&(!buff.bloodlust.up|buff.power_infusion.up)|fight_remains<4
actions.big_coc+=/whirling_dragon_punch,if=buff.power_infusion.up&(!buff.heart_of_the_jade_serpent_unity_within.up|buff.heart_of_the_jade_serpent_unity_within.remains<2)
actions.big_coc+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&talent.celestial_conduit&buff.zenith.remains>11&chi<=2&cooldown.rising_sun_kick.remains&!buff.rushing_wind_kick.up&talent.obsidian_spiral&buff.combo_breaker.up
actions.big_coc+=/tiger_palm,target_if=max:target.time_to_die,if=combo_strike&talent.celestial_conduit&buff.zenith.remains>11&chi<=2&cooldown.rising_sun_kick.remains&!buff.rushing_wind_kick.up&(!talent.obsidian_spiral|!buff.combo_breaker.up|prev.blackout_kick)
actions.big_coc+=/celestial_conduit,target_if=max:target.time_to_die,if=buff.zenith.up&(cooldown.rising_sun_kick.remains|active_enemies>2)&cooldown.fists_of_fury.remains&(cooldown.strike_of_the_windlord.remains|talent.whirling_dragon_punch)&(cooldown.whirling_dragon_punch.remains|talent.strike_of_the_windlord)&!buff.rushing_wind_kick.up&!buff.combo_breaker.up&chi>1&(!buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent.remains<4)
actions.big_coc+=/celestial_conduit,target_if=max:target.time_to_die,if=buff.zenith.up&!buff.heart_of_the_jade_serpent.up&!buff.heart_of_the_jade_serpent_yulons_avatar.up&chi>1&(cooldown.rising_sun_kick.remains|active_enemies>2)&(cooldown.strike_of_the_windlord.remains|(cooldown.whirling_dragon_punch.remains|cooldown.fists_of_fury.remains))
actions.big_coc+=/celestial_conduit,target_if=max:target.time_to_die,if=buff.zenith.up&buff.heart_of_the_jade_serpent.remains<2&prev.rising_sun_kick&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains&buff.heart_of_the_jade_serpent.up&chi>1

# Single Target
actions.default_st=whirling_dragon_punch,if=!buff.heart_of_the_jade_serpent_unity_within.up&buff.whirling_dragon_punch.remains<1&(buff.zenith.up|cooldown.invoke_xuen_the_white_tiger.remains>5|talent.flurry_strikes|!fight_style.patchwerk)
actions.default_st+=/zenith_stomp,if=buff.zenith.up&(buff.zenith.remains<5&buff.zenith_stomp.stack=2|buff.zenith.remains<4)|talent.celestial_conduit&chi<5&!buff.heart_of_the_jade_serpent_unity_within.up
actions.default_st+=/whirling_dragon_punch,if=buff.power_infusion.up&(!buff.heart_of_the_jade_serpent_unity_within.up|buff.heart_of_the_jade_serpent_unity_within.remains<2)
actions.default_st+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.remains<1&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.up&talent.celestial_conduit
actions.default_st+=/fists_of_fury,if=buff.heart_of_the_jade_serpent.remains<1&buff.heart_of_the_jade_serpent.up|buff.flurry_charge.stack=30&!buff.zenith.up
actions.default_st+=/whirling_dragon_punch,if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2&(buff.zenith.up|cooldown.invoke_xuen_the_white_tiger.remains>5|!fight_style.patchwerk)|talent.flurry_strikes
actions.default_st+=/tiger_palm,if=chi<3-1*!talent.ascension+1*talent.celestial_conduit+1*(buff.tigereye_brew_1.stack<15&time>60&time<120)&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&(!buff.bloodlust.up|chi<2)&buff.combo_breaker.stack<2
actions.default_st+=/strike_of_the_windlord,if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2&(buff.zenith.up|cooldown.invoke_xuen_the_white_tiger.remains>5|!fight_style.patchwerk)|talent.flurry_strikes
actions.default_st+=/rising_sun_kick,if=!buff.bloodlust.up&!buff.zenith.up&(chi>4|energy>50|cooldown.fists_of_fury.remains>5)|buff.zenith.up&buff.zenith.remains<2&combo_strike
actions.default_st+=/fists_of_fury,if=combo_strike&(buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_yulons_avatar.up|buff.heart_of_the_jade_serpent_unity_within.up)&buff.bloodlust.up|buff.bloodlust.up&talent.flurry_strikes|!buff.zenith.up&(talent.flurry_strikes|cooldown.invoke_xuen_the_white_tiger.remains>3|!fight_style.patchwerk)|buff.zenith.up&(talent.flurry_strikes|!buff.bloodlust.up)&(fight_style.patchwerk|target.time_to_die>5)
actions.default_st+=/rushing_wind_kick
actions.default_st+=/rising_sun_kick,if=combo_strike&buff.bloodlust.up|combo_strike&(buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_yulons_avatar.up|buff.heart_of_the_jade_serpent_unity_within.up)
actions.default_st+=/fists_of_fury,if=buff.bloodlust.up|combo_strike&(buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_yulons_avatar.up|buff.heart_of_the_jade_serpent_unity_within.up)
actions.default_st+=/tiger_palm,if=buff.zenith.up&chi<2&talent.celestial_conduit&(buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_unity_within.up)&!cooldown.fists_of_fury.remains&combo_strike
actions.default_st+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.remains<5&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.up|combo_strike&buff.dance_of_chiji.stack=2&buff.combo_breaker.stack<2&talent.sequenced_strikes&(talent.flurry_strikes|!buff.bloodlust.up)
actions.default_st+=/rising_sun_kick,if=buff.zenith.up&talent.flurry_strikes&!cooldown.fists_of_fury.remains
actions.default_st+=/rising_sun_kick,if=combo_strike
actions.default_st+=/fists_of_fury,if=talent.flurry_strikes|!buff.zenith.up&(talent.flurry_strikes|cooldown.invoke_xuen_the_white_tiger.remains>3|!fight_style.patchwerk)|buff.bloodlust.up&talent.jadefire_stomp&cooldown.celestial_conduit.remains
actions.default_st+=/rising_sun_kick,if=buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_unity_within.up|buff.heart_of_the_jade_serpent_yulons_avatar.up
actions.default_st+=/touch_of_death,if=!buff.zenith.up|fight_remains<5|((trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)|!trinket.1.has_use_buff&!trinket.2.has_use_buff)
actions.default_st+=/strike_of_the_windlord,if=buff.heart_of_the_jade_serpent_unity_within.remains<2&(buff.zenith.up|cooldown.invoke_xuen_the_white_tiger.remains>5|!fight_style.patchwerk)|talent.flurry_strikes
actions.default_st+=/rising_sun_kick,if=combo_strike&(buff.flurry_charge.stack<30|chi>3|buff.zenith.up|buff.bloodlust.up|energy>50&chi>2)|combo_strike&buff.heart_of_the_jade_serpent.up
actions.default_st+=/tiger_palm,if=combo_strike&buff.zenith.up&(chi<1|chi<2&!buff.combo_breaker.up)&talent.celestial_conduit
actions.default_st+=/zenith_stomp,if=buff.zenith.up&chi<5-1*!talent.ascension&(talent.flurry_strikes|chi<3|buff.zenith.remains<5)&buff.combo_breaker.stack<2&buff.dance_of_chiji.stack<2&(!buff.combo_breaker.up|talent.echo_technique)
actions.default_st+=/blackout_kick,if=combo_strike&buff.zenith.up&chi>1&(talent.obsidian_spiral|cooldown.fists_of_fury.remains|buff.combo_breaker.up)&(chi<6|buff.combo_breaker.up|cooldown.rising_sun_kick.remains<3)
actions.default_st+=/blackout_kick,if=combo_strike&buff.combo_breaker.up
actions.default_st+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.up&talent.sequenced_strikes
actions.default_st+=/spinning_crane_kick,if=combo_strike&buff.zenith.up&talent.flurry_strikes&chi>3+1*!talent.ascension
actions.default_st+=/slicing_winds
actions.default_st+=/spinning_crane_kick,if=talent.flurry_strikes&buff.zenith.up&chi>5-1*!talent.ascension&combo_strike|combo_strike&buff.bloodlust.up&buff.dance_of_chiji.up&buff.combo_breaker.stack<2
actions.default_st+=/tiger_palm,if=combo_strike&((energy>55&talent.inner_peace|energy>60&!talent.inner_peace)&chi.max-chi>=3-1*talent.celestial_conduit&(talent.energy_burst&!buff.combo_breaker.up|!talent.energy_burst)&!buff.zenith.up|(talent.energy_burst&!buff.combo_breaker.up|!talent.energy_burst)&!buff.zenith.up&!cooldown.fists_of_fury.remains&chi<3)

# Fallback
actions.fallback=blackout_kick,if=combo_strike
actions.fallback+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.up
actions.fallback+=/spinning_crane_kick,if=chi>5&combo_strike&talent.flurry_strikes
actions.fallback+=/tiger_palm,if=combo_strike
actions.fallback+=/spinning_crane_kick,if=chi>5&combo_strike

# Multi Target
actions.multitarget=fists_of_fury,target_if=max:target.time_to_die,if=buff.heart_of_the_jade_serpent.remains<1&buff.heart_of_the_jade_serpent.up
actions.multitarget+=/zenith_stomp,target_if=max:target.time_to_die,if=buff.zenith.up&(buff.zenith.remains<5&buff.zenith_stomp.stack=2|buff.zenith.remains<4)|talent.celestial_conduit&chi<5&!buff.heart_of_the_jade_serpent_unity_within.up
actions.multitarget+=/whirling_dragon_punch,if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2
actions.multitarget+=/whirling_dragon_punch,target_if=max:target.time_to_die,if=!buff.heart_of_the_jade_serpent_unity_within.up&buff.whirling_dragon_punch.remains<1
actions.multitarget+=/tiger_palm,target_if=max:target.time_to_die,if=buff.zenith.up&chi<2&talent.celestial_conduit&(buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_unity_within.up)&!cooldown.fists_of_fury.remains&combo_strike
actions.multitarget+=/tiger_palm,target_if=max:target.time_to_die,if=chi<5&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&!buff.bloodlust.up&buff.combo_breaker.stack<2|combo_strike&chi<3-1*buff.zenith.up&!cooldown.fists_of_fury.remains&(!buff.combo_breaker.up|!talent.energy_burst)&!buff.zenith_stomp.up
actions.multitarget+=/strike_of_the_windlord,if=talent.celestial_conduit&buff.heart_of_the_jade_serpent_unity_within.remains<2
actions.multitarget+=/fists_of_fury,target_if=max:target.time_to_die,if=buff.flurry_charge.stack=30&!buff.zenith.up|buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_unity_within.up|buff.heart_of_the_jade_serpent_yulons_avatar.up|talent.flurry_strikes
actions.multitarget+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.up&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.remains<3
actions.multitarget+=/rushing_wind_kick,target_if=max:target.time_to_die
actions.multitarget+=/rising_sun_kick,target_if=max:target.time_to_die,if=(active_enemies<5|cooldown.fists_of_fury.remains>1|buff.zenith.up)&(buff.rushing_wind_kick.up|buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_unity_within.up|buff.heart_of_the_jade_serpent_yulons_avatar.up)
actions.multitarget+=/zenith_stomp,target_if=max:target.time_to_die,if=buff.zenith.up&chi<5-1*!talent.ascension&(talent.flurry_strikes|chi<3|buff.zenith.remains<5)&buff.combo_breaker.stack<2&buff.dance_of_chiji.stack<2&(!buff.combo_breaker.up|talent.echo_technique)
actions.multitarget+=/touch_of_death,target_if=min:target.time_to_die,if=!buff.zenith.up|fight_remains<5|((trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)|!trinket.1.has_use_buff&!trinket.2.has_use_buff)
actions.multitarget+=/strike_of_the_windlord,if=buff.zenith.up|cooldown.zenith.remains>5&buff.heart_of_the_jade_serpent_unity_within.remains<2
actions.multitarget+=/whirling_dragon_punch,if=buff.zenith.up|cooldown.zenith.remains>5&buff.heart_of_the_jade_serpent_unity_within.remains<2
actions.multitarget+=/fists_of_fury,target_if=max:target.time_to_die,if=talent.flurry_strikes|!buff.zenith.up|buff.bloodlust.up&talent.jadefire_stomp&cooldown.celestial_conduit.remains
actions.multitarget+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.stack=2&buff.combo_breaker.stack<2&talent.sequenced_strikes
actions.multitarget+=/rising_sun_kick,target_if=max:target.time_to_die,if=(active_enemies<5|cooldown.fists_of_fury.remains>1|buff.zenith.up)&(combo_strike&(buff.flurry_charge.stack<30|chi>3|buff.zenith.up|buff.bloodlust.up|energy>50&chi>2)|combo_strike&buff.heart_of_the_jade_serpent.up)
actions.multitarget+=/spinning_crane_kick,target_if=max:target.time_to_die,if=talent.flurry_strikes&buff.zenith.up&chi>3&combo_strike&(!talent.shadowboxing_treads|active_enemies>3)
actions.multitarget+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&buff.zenith.up&chi>1&(talent.obsidian_spiral|buff.combo_breaker.up|cooldown.rising_sun_kick.remains<3&cooldown.rising_sun_kick.remains|talent.shadowboxing_treads&cooldown.rising_sun_kick.remains)&chi<6
actions.multitarget+=/spinning_crane_kick,if=combo_strike&buff.dance_of_chiji.up&buff.combo_breaker.stack<2&talent.sequenced_strikes&buff.dance_of_chiji.remains<4
actions.multitarget+=/slicing_winds
actions.multitarget+=/spinning_crane_kick,target_if=max:target.time_to_die,if=talent.flurry_strikes&buff.zenith.up&chi>3&combo_strike
actions.multitarget+=/spinning_crane_kick,target_if=max:target.time_to_die,if=combo_strike&(buff.dance_of_chiji.up|(chi>2|energy>55))&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains&!talent.shadowboxing_treads&!buff.zenith.up
actions.multitarget+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.up&(buff.heart_of_the_jade_serpent.up|buff.heart_of_the_jade_serpent_unity_within.up)
actions.multitarget+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.up
actions.multitarget+=/tiger_palm,target_if=max:target.time_to_die,if=chi<5&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&!buff.bloodlust.up
actions.multitarget+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.stack=2
actions.multitarget+=/spinning_crane_kick,target_if=max:target.time_to_die,if=combo_strike&buff.dance_of_chiji.stack=2
actions.multitarget+=/spinning_crane_kick,if=combo_strike&!buff.zenith.up&chi>5&buff.combo_breaker.up&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains
actions.multitarget+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&buff.combo_breaker.up
actions.multitarget+=/tiger_palm,target_if=max:target.time_to_die,if=chi<5&combo_strike&energy.time_to_max<=gcd.max*3&!buff.zenith.up&active_enemies<3
actions.multitarget+=/tiger_palm,target_if=max:target.time_to_die,if=combo_strike&((energy>55&talent.inner_peace|energy>60&!talent.inner_peace)&chi.max-chi>=2&(talent.energy_burst&!buff.combo_breaker.up|!talent.energy_burst)&!buff.zenith.up|(talent.energy_burst&!buff.combo_breaker.up|!talent.energy_burst)&!buff.zenith.up&!cooldown.fists_of_fury.remains&chi<3)
actions.multitarget+=/blackout_kick,target_if=max:target.time_to_die,if=combo_strike&talent.shadowboxing_treads
actions.multitarget+=/spinning_crane_kick,target_if=max:target.time_to_die,if=combo_strike&(chi>3|energy>55)&(!talent.shadowboxing_treads&active_enemies>2|active_enemies>5)&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains
actions.multitarget+=/rising_sun_kick,target_if=max:target.time_to_die,if=combo_strike
actions.multitarget+=/spinning_crane_kick,target_if=max:target.time_to_die,if=combo_strike&chi>2

# Opener
actions.opener=tiger_palm,if=combo_strike&chi<4
actions.opener+=/use_item,name=algethar_puzzle_box,if=target.time_to_die>25&(cooldown.invoke_xuen_the_white_tiger.remains<2|talent.flurry_strikes&cooldown.zenith.up)|fight_remains<25

# Racials (Good)
actions.racials=berserking,if=buff.invoke_xuen_the_white_tiger.remains>15|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14|fight_remains<20
actions.racials+=/ancestral_call,if=buff.invoke_xuen_the_white_tiger.remains>15|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14|fight_remains<20
actions.racials+=/blood_fury,if=buff.invoke_xuen_the_white_tiger.remains>15|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14|fight_remains<20
actions.racials+=/fireblood,if=buff.invoke_xuen_the_white_tiger.remains>15|!talent.invoke_xuen_the_white_tiger&buff.zenith.remains>14|fight_remains<20

# Use Weapon
actions.trinket=use_item,slot=main_hand
# Use Algethar
actions.trinket+=/use_item,name=algethar_puzzle_box,if=fight_remains>5&(!buff.zenith.up&!talent.flurry_strikes&(target.time_to_die>35&fight_style.dungeonroute|target.time_to_die>25)&(cooldown.potion.remains>30|fight_remains<45|fight_remains>80)&(cooldown.invoke_xuen_the_white_tiger.remains<2|talent.flurry_strikes&cooldown.zenith.up)|fight_remains<25|talent.flurry_strikes&(target.time_to_die>35&fight_style.dungeonroute|target.time_to_die>25)&!buff.zenith.up|fight_style.dungeonslice&(time<5&chi>3|active_enemies>3&target.time_to_die>15))
# Stat on use with passive or DMG on use
actions.trinket+=/use_item,slot=trinket1,if=trinket.1.has_use_buff&!trinket.2.has_use_buff&(pet.xuen_the_white_tiger.active&talent.invoke_xuen_the_white_tiger|talent.flurry_strikes&buff.zenith.remains>14)
actions.trinket+=/use_item,slot=trinket2,if=trinket.2.has_use_buff&!trinket.1.has_use_buff&(pet.xuen_the_white_tiger.active&talent.invoke_xuen_the_white_tiger|talent.flurry_strikes&buff.zenith.remains>14)
# Stat on use with Stat on use
actions.trinket+=/use_item,slot=trinket1,if=trinket.1.has_use_buff&trinket.2.has_use_buff&(pet.xuen_the_white_tiger.active&talent.invoke_xuen_the_white_tiger|talent.flurry_strikes&buff.zenith.remains>14)
actions.trinket+=/use_item,slot=trinket2,if=trinket.1.has_use_buff&trinket.2.has_use_buff&(cooldown.invoke_xuen_the_white_tiger.remains>30&(buff.zenith.up|(cooldown.strike_of_the_windlord.remains<2&talent.strike_of_the_windlord|cooldown.whirling_dragon_punch.remains<2&talent.whirling_dragon_punch))|talent.flurry_strikes&buff.zenith.remains>10)
# DMG on use with stat on use
actions.trinket+=/use_item,slot=trinket1,if=!trinket.1.has_use_buff&trinket.2.has_use_buff&trinket.2.cooldown.remains>30
actions.trinket+=/use_item,slot=trinket2,if=!trinket.2.has_use_buff&trinket.1.has_use_buff&trinket.1.cooldown.remains>30
# DMG on use without stat on use
actions.trinket+=/use_item,slot=trinket1,if=!trinket.1.has_use_buff&!trinket.2.has_use_buff
actions.trinket+=/use_item,slot=trinket2,if=!trinket.1.has_use_buff&!trinket.2.has_use_buff

# Zenith Usage
actions.zenith=zenith,target_if=max:target.time_to_die,if=buff.invoke_xuen_the_white_tiger.up&(!buff.zenith.up|talent.flurry_strikes)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=buff.bloodlust.remains>30&(active_enemies>2|cooldown.rising_sun_kick.remains)&!buff.zenith.up
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&(buff.bloodlust.up&cooldown.celestial_conduit.remains&(cooldown.rising_sun_kick.remains|active_enemies>2)&!buff.zenith.up&talent.celestial_conduit)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&(talent.flurry_strikes&(buff.bloodlust.up|cooldown.potion.remains>295))&!buff.zenith.up&(buff.bloodlust.remains>30|talent.spiritual_focus)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=time>250&cooldown.potion.remains>295&(!trinket.1.has_use_buff&!trinket.2.has_use_buff|trinket.1.has_use_buff&trinket.1.cooldown.remains>30|trinket.2.has_use_buff&trinket.2.cooldown.remains>30)&(fight_remains>120|fight_remains<50&fight_remains>cooldown.zenith.full_recharge_time)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&talent.flurry_strikes&!trinket.1.has_use_buff&!trinket.2.has_use_buff&cooldown.rising_sun_kick.remains&cooldown.fists_of_fury.remains<5&(cooldown.whirling_dragon_punch.remains<10|cooldown.strike_of_the_windlord.remains<10)&cooldown.zenith.full_recharge_time<40&!fight_style.dungeonslice&!buff.zenith.up
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=(target.time_to_die>30&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&(!buff.bloodlust.up&(trinket.1.is.algethar_puzzle_box&trinket.1.cooldown.remains>100|trinket.2.is.algethar_puzzle_box&trinket.2.cooldown.remains>100)&(cooldown.rising_sun_kick.remains|active_enemies>2|talent.drinking_horn_cover&chi<2))&!buff.zenith.up
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=(fight_style.patchwerk|fight_style.dungeonroute&target.time_to_die>27+5*talent.drinking_horn_cover)&talent.flurry_strikes&(buff.tigereye_brew_1.stack>19-2*talent.echo_technique|buff.tigereye_brew_1.stack>11&talent.spiritual_focus-2*talent.echo_technique)&(target.time_to_die>30&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute)&(cooldown.rising_sun_kick.remains|active_enemies>1)&(!trinket.1.has_use_buff&!trinket.2.has_use_buff|trinket.1.has_use_buff&(trinket.1.cooldown.remains>40|trinket.1.cooldown.remains>30&talent.spiritual_focus)|trinket.2.has_use_buff&(trinket.2.cooldown.remains>40|trinket.2.cooldown.remains>30&talent.spiritual_focus))&(talent.strike_of_the_windlord&cooldown.strike_of_the_windlord.remains<15-5*talent.revolving_whirl&talent.drinking_horn_cover|talent.whirling_dragon_punch&cooldown.whirling_dragon_punch.remains<15-7*talent.revolving_whirl&talent.drinking_horn_cover|talent.strike_of_the_windlord&cooldown.strike_of_the_windlord.remains<10|talent.whirling_dragon_punch&cooldown.whirling_dragon_punch.remains<10)&cooldown.fists_of_fury.remains<9+4*talent.spiritual_focus
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=(cooldown.rising_sun_kick.remains|active_enemies>2)&fight_style.dungeonslice&time>130&time<150&active_enemies>1&talent.flurry_strikes&!buff.zenith.up
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=fight_style.dungeonslice&target.time_to_die>15&active_enemies>4&(talent.flurry_strikes|talent.celestial_conduit&talent.restore_balance&cooldown.invoke_xuen_the_white_tiger.remains<cooldown.zenith.full_recharge_time)&!fight_style.patchwerk&!buff.zenith.up
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=!buff.zenith.up&(talent.celestial_conduit&fight_remains<cooldown.invoke_xuen_the_white_tiger.remains&(cooldown.rising_sun_kick.remains|active_enemies>2)&(target.time_to_die>30&fight_style.dungeonroute|target.time_to_die>25&!fight_style.dungeonroute|target.time_to_die>15&active_enemies>4)&!fight_style.patchwerk)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=!buff.zenith.up&talent.flurry_strikes&fight_style.dungeonroute&cooldown.zenith.full_recharge_time<30&target.time_to_die>25
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=fight_style.patchwerk&!buff.zenith.up&cooldown.fists_of_fury.remains<10&(cooldown.whirling_dragon.remains<10|cooldown.strike_of_the_windlord.remains<10)&(cooldown.rising_sun_kick.remains|chi<2&energy<50|active_enemies>1)&cooldown.zenith.full_recharge_time<30&(!trinket.1.has_use_buff&!trinket.2.has_use_buff|trinket.1.has_use_buff&trinket.1.cooldown.remains>30|trinket.2.has_use_buff&trinket.2.cooldown.remains>30)&(fight_remains>120|fight_remains<50&fight_remains>cooldown.zenith.full_recharge_time)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=fight_remains<=24&(cooldown.rising_sun_kick.remains|active_enemies>2)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=fight_remains<45&cooldown.zenith.full_recharge_time<5&(cooldown.rising_sun_kick.remains|active_enemies>1)
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=!buff.zenith.up&(fight_style.patchwerk&!trinket.1.is.algethar_puzzle_box&!trinket.2.is.algethar_puzzle_box&trinket.1.has_use_buff&(trinket.1.cooldown.ready|cooldown.zenith.full_recharge_time<5))
actions.zenith+=/zenith,target_if=max:target.time_to_die,if=!buff.zenith.up&(fight_style.patchwerk&!trinket.1.is.algethar_puzzle_box&!trinket.2.is.algethar_puzzle_box&trinket.2.has_use_buff&(trinket.2.cooldown.ready|cooldown.zenith.full_recharge_time<5))
```
