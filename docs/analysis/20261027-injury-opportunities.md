# Injury opportunities: 27 Oct 2026

- Prepared 27 Oct 2026, 06:00 UTC, by Claude. This is **a report, not a council verdict**.
- **Question asked:** which NBA players are expected to be out for **more than a week**, and which teammates gain role or usage while they are out and are worth a pickup during that window?
- **Out more than a week** means an expected return after Tue 3 Nov. Each case was checked two ways:
  - ESPN's injury feed (`site.api.espn.com/.../injuries`, 83 entries), with its return estimates
  - the latest team or beat reporting on the injury, linked below
- **Data:** the full ESPN player pool for league 423671879 (700 players), with 2027 current, 2027 projected and 2026 splits and each player's league status.
  - All 700 re-score with `scripts/league_scoring.py` to ESPN's league-scored totals (0 mismatches).
  - The per-game lines under *Who took the minutes* are re-scored from ESPN's final box scores with `council/slump_watch.py`'s `box_points`.
- **Status:** every candidate below is a **free agent**, which means an instant add with no waiver wait.
  - Jalen Williams and Jalen Suggs are on **waivers** (24-hour claim).
  - Our IR slot is taken by Duren.
- **Schedule:** matchup week 2 runs Mon 26 Oct to Sun 1 Nov. *Games* below means games left this week / games next week (2 to 8 Nov).
- **Sample:** teams have played 3 or 4 games, and the newest injuries have 0 or 1 game of "without" evidence. Read the post-injury line, not just the average.

## Shortlist

Free agents whose role has grown because of an injury of more than a week, ordered by current FP/g.

| Player | NBA | Who is out | How long | Current FP/g (min) | Since the injury | Owned | Games |
|---|---|---|---|---:|---|---:|---|
| Precious Achiuwa | SAC | Keegan Murray (ankle); Raynaud | re-eval 5–9 Nov | **36.7** (31.3) | started 25 Oct: 39 min, **42 FP** | 21% | 3 / 4 |
| Jaxson Hayes | UTAH | Nurkic (toe) | ≥4 weeks from 4 Oct | **35.7** (23.7) | 45, 38, 24 FP in 19–26 min; missed 26 Oct with shoulder soreness, next chance Wed | 19% | 2 / 4 |
| Daniel Gafford | DAL | Lively (foot), Aldama (knee) | Lively: no timetable | **31.2** (21.5) | starting C; last two: **45, 39** | 28% | 2 / 4 |
| Isaiah Jackson | LAC | Ingram, Beal, Strus | Ingram ~Nov–Dec | 29.3 (22.3) | starting C every game: 24, 32, 32 | 4% | 3 / 3 |
| Derrick Jones Jr. | LAC | Ingram, Beal, Strus | Ingram ~Nov–Dec | 28.7 (30.3) | starting F every game: 30, 34, 22 | 5% | 3 / 3 |
| Isaiah Hartenstein | OKC | Holmgren (short); J. Williams, Wallace (months) | Holmgren ~days | 28.2 (23.2) | 26 Oct: 26 min, **46 FP** | 38% | 2 / 4 |
| Jalen Smith | CHI | Claxton (hamstring) | ≥1 more week | 27.8 (21.8) | starting C; last two: 17, 11 | 21% | 2 / 3 |
| Tristan da Silva | ORL | **Banchero** (ankle), Suggs (knee) | **4–6 weeks**; ≥2 weeks | 26.0 (28.0) | first game without Banchero: 27 min, **37 FP** | 6% | 3 / 3 |
| Jared McCain | OKC | **J. Williams** (leg), **Wallace** (shoulder) | **months** | 18.0 (22.8) | started 26 Oct: 30 min, 35 FP | 35% | 2 / 4 |
| Aday Mara | OKC | Holmgren; J. Williams, Wallace | Holmgren ~days | 16.8 (14.8) | 26 Oct: 20 min, 32 FP | 10% | 2 / 4 |
| Mo Bamba | UTAH | Nurkic; Hayes, Markkanen, Jackson day-to-day | depends on Hayes | 46.0 (29.0), 1 game | debut 26 Oct: 14 pts, 7 reb, 4 blk | 0% | 2 / 4 |

How these compare with our roster's bottom five on current FP/g:

| Player | FP/g |
|---|---:|
| Bane | 21.0 |
| Murphy | 28.0 |
| Pritchard | 28.3 |
| Reed | 31.3 |
| VanVleet | 32.0 |

- **Achiuwa** and **Hayes** average more than all five of those players.
- **Gafford** averages more than Bane, Murphy and Pritchard.
- Everyone else on the shortlist is a role bet rather than a production bet.
  - **McCain** and **da Silva** have the longest windows (months, and 4–6 weeks), but their production so far is below our bottom five.
  - **Hartenstein, Mara and Bamba** gain mostly from injuries of a few days (Holmgren, Hayes, Markkanen, Jackson). Their bump may last only days.

Watch, not yet:

- **Alex Caruso** (OKC, 30.8 FP/g in 19 min) is the obvious Wallace replacement. He sprained his right ankle on 26 Oct, and the MRI result is pending.
- **Daniss Jenkins** (DET, 28.7) is filling in for Ausar Thompson's ankle sprain, which is day-to-day. That opening is short.

## The injuries: out more than a week

### New since the season started

These open roles the current averages do not show yet.

| Player | NBA | Injury | Reported timeline | ESPN est. | Minutes left (this season) | Fantasy status |
|---|---|---|---|---|---:|---|
| **Jalen Williams** | OKC | fractured fibula, dislocated left ankle (25 Oct); surgery | **likely the season** | 2 Mar | 31.7 | Waivers |
| **Cason Wallace** | OKC | torn left labrum (25 Oct); surgery | **5–6 months** | 2 Mar | 16.3 | Free agent |
| **Paolo Banchero** | ORL | low-grade high right ankle sprain (23 Oct) | **4–6 weeks** | 22 Nov | 33.5 | Dr White Slong |
| **Jalen Suggs** | ORL | right knee bone bruise (25 Oct) | re-eval in 2 weeks; at least 6 games | 10 Nov | 33.3 | Waivers |
| **Keegan Murray** | SAC | left ankle capsulitis | re-eval in 10–14 days from 26 Oct | 6 Nov | 27.0 | Dr White Slong |
| **Jalen Duren** | DET | right hamstring strain (23 Oct) | re-eval in 2 weeks; ~8 Nov at the earliest | 9 Nov | 19.0 | **us** (IR) |

### Out since the preseason

The current minutes already reflect these absences.

| Player | NBA | Injury | Reported timeline | ESPN est. |
|---|---|---|---|---|
| Jusuf Nurkic | UTAH | partial plantar plate tear, right second toe (4 Oct) | at least 4 weeks; early Nov at the earliest | 4 Nov |
| Nic Claxton | CHI | hamstring (training camp) | at least one more week, then re-evaluated | 4 Nov |
| Dereck Lively II | DAL | right foot (Dec 2025 surgery) | no timetable; week-to-week | 2 Nov |
| Santi Aldama | DAL | knee (March surgery) | week-to-week | 2 Nov |
| Brandon Ingram | LAC | partial Achilles tear, found in May heel surgery | Nov–early Dec estimate; Lue: "vague" | 8 Nov |
| Bradley Beal | LAC | right knee inflammation | no timetable reported | 8 Nov |
| Max Strus | LAC | right foot plantar fasciitis | no timetable reported | 8 Nov |
| Maxime Raynaud | SAC | right kneecap subluxation (10 Oct) | re-eval was due 25 Oct; no update found | 10 Nov |
| Kristaps Porziņģis | GS | undisclosed illness | indefinite | 1 Dec |
| Moses Moody | GS | left knee surgery | no timetable reported | 1 Dec |
| Jimmy Butler III | GS | torn right ACL | out until at least 2 Jan | 2 Jan |
| Shaedon Sharpe | POR | right knee surgery | no timetable reported | 2 Mar |
| Mark Williams | PHX | left shoulder surgery | no timetable reported | 3 Feb |
| Donte DiVincenzo | MIN | right Achilles surgery | no timetable reported | 2 Apr |

These players have small roles, and their teammates gain little:

| Player | NBA | Injury | ESPN est. |
|---|---|---|---|
| Julian Strawther | DEN | left knee sprain | 29 Nov |
| Ben Sheppard | IND | left knee | 1 Dec |
| Johnny Furphy | IND | right knee surgery | 2 Jan |
| Mouhamed Gueye | ATL | left foot fracture, surgery (re-eval in 3–4 months, per ESPN's note) | 20 Nov |
| Dominick Barlow | PHI | back fracture | 2 Nov |
| Jayden Quaintance | SA | right knee surgery | 3 Dec |
| Devin Carter | BOS | illness | 8 Nov |
| Tristan Vukcevic | WSH | left hip, pinched nerve | 2 Nov |
| Jamir Watkins | WSH | left knee surgery | 2 Apr |
| Jordan Miller | LAC | left shoulder surgery | 2 Mar |
| Noah Penda | ORL | right hamstring, partial tear | 18 Nov |
| Izaiyah Nelson | ORL | left ankle surgery | 18 Nov |
| Dylan Cardwell | SAC | left calf strain | 6 Nov |

### Short of a week

These are not in scope here, but each still has an expected return.

| Player | NBA | Injury | Reported timeline | ESPN est. |
|---|---|---|---|---|
| Chet Holmgren | OKC | right patellar tendinitis | next chance Wed vs DAL | 28 Oct |
| Alex Caruso | OKC | right ankle sprain (26 Oct) | MRI pending; monitor for Wed | 28 Oct |
| Ivica Zubac | IND | left ankle sprain | no timetable; "improving" | 28 Oct |
| Lauri Markkanen | UTAH | right wrist (26 Oct) | no diagnosis reported | 28 Oct |
| Jaren Jackson Jr. | UTAH | right knee (26 Oct) | no diagnosis reported | 28 Oct |
| Jaxson Hayes | UTAH | right shoulder soreness | next chance Wed vs SA | 28 Oct |
| Ausar Thompson | DET | right ankle sprain | questionable Tue vs NY | 27 Oct |
| Coby White | CHA | left calf strain | no timetable reported | 31 Oct |
| Kon Knueppel | CHA | left hamstring | no timetable reported | 31 Oct |
| Grant Williams | CHA | right hamstring | no timetable reported | 31 Oct |
| AJ Dybantsa | WSH | left ankle sprain | no timetable reported | 28 Oct |
| Yves Missi | NO | left knee bruise | no timetable reported | 2 Nov |
| Steven Adams | HOU | right calf strain | no timetable reported | 2 Nov |
| Tobias Harris | SA | left calf strain | no timetable reported | 28 Oct |

## Who took the minutes

Per-game minutes and league-scored FP from ESPN's final box scores. An asterisk marks a starter.

### OKC: Jalen Williams and Wallace gone for months; Holmgren day-to-day

| Player | 20 Oct | 22 Oct | 25 Oct | **26 Oct, without all three** | Status |
|---|---|---|---|---|---|
| Ajay Mitchell | 23m 15 | 23m 29 | 28m 45 | **25m 48\*** | Lauri Birds |
| Jared McCain | 22m 37 | 18m −2 | 21m 2 | **30m 35\*** | Free agent |
| Isaiah Hartenstein | 17m 18\* | 23m 15\* | 27m 34\* | **26m 46\*** | Free agent |
| Kenrich Williams | 7m 8 | 6m 7 | 7m 6 | **24m 16\*** | Free agent |
| Jaylin Williams | 17m 7 | 15m 15 | 5m −1 | **26m 21** | Free agent |
| Aday Mara | 12m 15 | 13m 13 | 14m 7 | **20m 32** | Free agent |
| Bennett Stirtz | 1m 0 | 2m −1 | 11m 7 | **25m 3** | Free agent |
| Alex Caruso | 25m 24 | 20m 30 | 22m 48 | 9m 21 (ankle) | Free agent |

- 48 minutes of guard and wing time (Williams 32, Wallace 16) are gone for the season.
- In the first game without them, McCain and Mitchell started. NBC Sports calls McCain a must-add, and CBS notes his efficiency still has to come.
- Holmgren's absence is tendinitis and should be short. Once he is back, the frontcourt bump for Hartenstein, Mara and Jaylin Williams shrinks, and the guard minutes stay open.

### ORL: Banchero 4–6 weeks; Suggs at least 2 weeks

| Player | 21 Oct | 23 Oct (Banchero hurt) | **25 Oct, without Banchero** | Status |
|---|---|---|---|---|
| Franz Wagner | 29m 35\* | 33m 25\* | **37m 49\*** | Cream Abdul-Yammar |
| **Desmond Bane** | 33m 27\* | 27m −1\* | **35m 37\*** | **us** |
| Tristan da Silva | 28m 30 | 29m 11 | **27m 37** | Free agent |
| Wendell Carter Jr. | 31m 46\* | 29m 47\* | 33m 27\* | Dr White Slong |
| Nikola Vučević | 5m 3 | 4m 1 | 15m 20 | Free agent |
| Jase Richardson | 14m 17 | 14m 12 | 17m 4\* | Free agent |

- Suggs got hurt late in the 25 Oct game, so there is no game yet without both.
- Anthony Black is the likely starting point guard, but he is rostered by Cream Abdul-Yammar.
- Jase Richardson started the Banchero-less game, but did little with it.

### SAC: Keegan Murray 10–14 days; Raynaud and Cardwell out

| Player | 21 Oct | 23 Oct | **25 Oct, without Murray** | Status |
|---|---|---|---|---|
| Precious Achiuwa | 29m 35 | 26m 33 | **39m 42\*** | Free agent |
| De'Andre Hunter | 20m 9\* | 25m 13\* | 29m 12\* | Free agent |
| Jonathan Mogbo | 8m −2 | — | 18m 18 | Free agent |

- Achiuwa started in Murray's spot and posted 12 points, 10 rebounds, 2 steals and 3 blocks. He had been 26–29 minutes off the bench before that.

### UTAH: Nurkic out; Hayes, Markkanen and Jackson day-to-day

- Hayes has taken Nurkic's minutes: 26m 45\* in the opener, then 26m 38 and 19m 24 off the bench. He missed 26 Oct with right shoulder soreness, and his next chance is Wednesday.
- **Mo Bamba** made his debut on 26 Oct in Hayes's absence, after Markkanen (wrist) and Jackson (knee) both left early: 29 minutes, 14 points, 7 rebounds, 4 blocks (46 FP).
- Filipowski (8 minutes a game, −0.3 FP/g) is not the beneficiary.

### DAL: Lively has no timetable; Aldama week-to-week

- **Gafford** has started every game: 22m 15, 15m 26, 23m 45, 26m 39.
- One caveat: Dusty May has also used Morez Johnson Jr. at small-ball center. A Lively return would put Gafford back on the bench.

### CHI: Claxton at least one more week

- **Jalen Smith** has started all four games, but his line is fading: 32, 51, 17, 11.

### LAC: Ingram, Beal and Strus out

- Lue's starters have been the same in all three games: Garland, Dunn, **Derrick Jones Jr.**, Hachimura, **Isaiah Jackson**.
- Both free agents have held starting minutes the whole way.
- The window closes when Ingram returns, estimated for November to early December.

### DET: Duren at least 2 weeks

- Our own **Paul Reed** started on 25 Oct: 23 minutes, 27 FP. He averages 31.3 FP/g.
- Reed and Tolu Smith are expected to split center minutes, with John Collins as the small-ball option.
- Daniss Jenkins (38m 44 FP on 25 Oct) was covering Ausar Thompson's ankle, not Duren.

### GS: Porziņģis, Moody and Butler out

- These absences predate the season, and our **Yaxel Lendeborg** is the main beneficiary: 33.2 minutes, 46.0 FP/g.
- Gui Santos, De'Anthony Melton and Brandon Williams (all free agents, 21–24 FP/g) share the rest. None stands out.

## Our players in this picture

- **Bane**: Banchero and Suggs are both out. In the one game without Banchero he played 35 minutes for 37 FP, his best line of the season. The slump watch has him at −17.2 against projection.
- **Reed**: he is the Duren replacement. He started on 25 Oct and is averaging 31.3 FP/g.
- **Lendeborg**: Golden State's frontcourt absences keep him at 33 minutes.
- **Duren**: he holds our only IR slot until roughly 8 Nov. Jalen Williams (waivers) can't be stashed as long as Duren is there.
- **Pending trades**: VanVleet is in both open offers.
  - The Lauri Birds offer brings back Zubac, who is day-to-day with a sprained ankle and averaging 25.3 FP/g.
  - The Melbourne offer brings back Brunson and Castle.

## Sources

- ESPN NBA injury feed, read 27 Oct 2026 05:10 UTC. ESPN fantasy API, league 423671879: `kona_player_info`, `mSettings`, `mStatus`, `mMatchupScore`. ESPN NBA box scores for every game listed.
- Jalen Williams and Wallace:
  - [ESPN](https://www.espn.com/nba/story/_/id/50290179/thunder-jalen-williams-cason-wallace-undergo-surgery)
  - [Yahoo Sports](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-out-indefinitely-with-fractured-fibula-dislocated-ankle-after-gruesome-injury-in-win-over-clippers-220320179.html)
  - [Yahoo Sports, Wallace labrum](https://sports.yahoo.com/articles/cason-wallace-sustains-torn-labrum-224600236.html)
  - [ClutchPoints, Wallace 5–6 months](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-cason-wallace-miss-significant-time-shoulder-injury)
- Holmgren: [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/chet-holmgren-knee-out-monday-vs-suns)
- OKC on 26 Oct:
  - [Basketnews, starting lineup](https://basketnews.com/news-258199-okc-thunder-reveal-new-starting-lineup-after-jalen-williams-cason-wallace-injuries.html)
  - [AOL/AP](https://www.aol.com/articles/ajay-mitchell-shai-gilgeous-alexander-024816000.html)
- McCain: [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/jdub-suffered-fractured-fibula-dislocated-ankle); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/thunders-jared-mccain-held-in-check-sunday/)
- Caruso: [ESPN](https://www.espn.com/nba/story/_/id/50293075/suddenly-thin-thunder-lose-alex-caruso-ankle-sprain); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/thunders-alex-caruso-wont-return-vs-phoenix/)
- Banchero: [Yahoo Sports](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-reportedly-to-miss-time-with-high-ankle-sprain-could-be-out-4-6-weeks-165247328.html); [ClutchPoints](https://clutchpoints.com/nba/orlando-magic/magic-news-paolo-banchero-injury-update-suggests-he-may-miss-over-1-month)
- Suggs: [ESPN](https://www.espn.com/nba/story/_/id/50289397/magic-jalen-suggs-least-2-weeks-knee-injury); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/magics-jalen-suggs-out-at-least-two-weeks/)
- Orlando guards:
  - [Yahoo Sports](https://sports.yahoo.com/articles/magic-jalen-suggs-avoids-significant-194901807.html)
  - [NBC Sports, Jase Richardson](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/magic-leaning-toward-starting-jase-richardson)
- Keegan Murray and Achiuwa:
  - [NBC Sports, 10–14 days](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/murray-ankle-to-be-evaluated-in-10-14-days)
  - [NBC Sports, Achiuwa spot start](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/precious-achiuwa-posts-double-double-in-spot-start)
  - [NBC Sports, SAC starters](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/sac-starts-acuff-lavine-hunter-achiuwa-sabonis)
- Raynaud: [ESPN](https://www.espn.com/nba/story/_/id/50159419/kings-c-maxime-raynaud-knee-reevaluated-2-weeks); [Hoops Rumors](https://www.hoopsrumors.com/2026/10/kings-maxime-raynaud-leaves-court-in-wheelchair-after-knee-injury.html)
- Duren: [ESPN](https://www.espn.com/nba/story/_/id/50277066/pistons-jalen-duren-hamstring-strain-least-2-weeks); [Detroit Jock City](https://detroitjockcity.com/what-jalen-duren-hamstring-injury-means-pistons-01m5vtqhsk1z)
- Ausar Thompson and Jenkins: [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-starting-sunday/); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/ausar-thompson-ankle-questionable-vs-new-york)
- Nurkic: [SI](https://www.si.com/nba/jazz/onsi/utah-jazz-c-jusuf-nurkic-to-miss-4-weeks-with-foot-injury-what-it-means); [Salt Lake Tribune](https://www.sltrib.com/sports/jazz/2026/10/11/jusuf-nurkics-injury-creates/)
- Hayes: [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/jazzs-jaxson-hayes-wont-play-monday/); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/jaxson-hayes-shoulder-downgraded-to-out-monday)
- Bamba: [KSL Sports](https://sports.ksl.com/nba/utah-jazz/jazz-grizzlies-young-core-shine/578516); [Deseret News](https://deseret.com/sports/2026/10/26/utah-jazz-lose-110-105-to-memphis-grizzlies-markkanen-jackson-injured)
- Lively and Gafford: [CBS Sports, Lively](https://www.cbssports.com/fantasy/basketball/news/mavericks-dereck-lively-remains-without-return-timetable/); [CBS Sports, Gafford starting](https://www.cbssports.com/fantasy/basketball/news/mavericks-daniel-gafford-starting-sans-lively/)
- Aldama: [Yahoo Sports](https://sports.yahoo.com/articles/santi-aldama-timeframe-return-remains-150000021.html); [RotoWire](https://www.rotowire.com/basketball/headlines/santi-aldama-injury-wont-play-saturday-535859)
- Claxton: [Yahoo Sports](https://sports.yahoo.com/articles/nic-claxton-two-weeks-leaves-203348775.html); [Heavy](https://heavy.com/sports/nba/chicago-bulls/injury-report-vs-celtics-october-26/)
- Ingram: [Yahoo Sports](https://sports.yahoo.com/articles/clippers-brandon-ingram-miss-start-020736294.html); [ClutchPoints](https://clutchpoints.com/nba/los-angeles-clippers/clippers-news-whats-really-going-on-with-brandon-ingram-partially-torn-achilles-injury)
- LAC lineup: [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-21/lac-starts-garland-dunn-jones-rui-jackson)
- Porziņģis: [CBS Sports](https://www.cbssports.com/nba/news/warriors-kristaps-porzingis-mysterious-health-issues-timeline/); [SF Chronicle](https://www.sfchronicle.com/sports/warriors/article/kristaps-porzingis-breaks-silence-warriors-22477452.php)
