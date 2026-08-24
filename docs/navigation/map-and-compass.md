---
tags:
  - navigation
  - map
  - compass
  - orienteering
  - bearings
  - wilderness
---
# Map and Compass Navigation

> Core land navigation using topographic maps and magnetic compass — the primary backup when GPS fails.

## At a Glance

- A compass points to magnetic north, not true north — adjust for declination or every bearing is wrong
- Triangulation with three bearings fixes your position on a map within 100 meters (330 feet) in most terrain
- Pace counting is the only reliable way to track distance without electronics
- Always orient your map to north before plotting or reading anything
- Combine compass bearings with terrain features — never rely on compass alone

## Compass Anatomy and Terminology

A baseplate compass (the standard for land navigation) has these parts:

- **Baseplate** — flat, transparent plate with a direction-of-travel arrow
- **Rotating bezel (housing)** — numbered ring from 0 to 360 degrees
- **Magnetic needle** — red end points to magnetic north
- **Orienting arrow** — fixed inside the bezel, used to align with the needle ("red in the shed")
- **Orienting lines** — parallel lines inside the bezel that align with map grid lines
- **Index line** — where the bezel meets the direction-of-travel arrow; read your bearing here
- **Declination adjustment screw** — on better compasses, allows you to set local declination once

!!! note
    Lensatic (military) compasses use a different sighting method but the same principles apply. The procedures below work with either type.

## Declination: Magnetic vs. True North

True north is the geographic North Pole. Magnetic north is where compass needles point,
and it moves. It has migrated out of the Canadian Arctic, across the Arctic Ocean, and now
sits around 86°N 164°E — closer to Siberia than to Canada, roughly 250 miles (400 km) from
the geographic pole, and travelling about 35 miles (55 km) a year.

This is why declination printed on an old map is not the declination today. Check the date
in the margin, and if the map is more than a few years old, get a current figure.

The angle between true north and magnetic north at your location is **magnetic declination**. It varies by region and changes slowly over time.

### Finding Your Local Declination

1. Check the margin of your topographic map — declination is printed there with the date of measurement.
2. Use the NOAA Magnetic Declination Calculator (online, before your trip).
3. In the continental US, declination runs from roughly **14 degrees EAST in Washington
   state** to **17 degrees WEST in Maine**, with a line of zero declination running down
   the middle of the country. Note the direction carefully — see the warning below.

### Adjusting for Declination

!!! warning "CAUTION"
    A bearing error of 1 degree puts you about **92 feet (28 m) off for every mile
    travelled** — call it 100 feet per mile. That compounds:

    | Error | Over 1 mile | Over 10 miles | Over 20 miles |
    |---|---|---|---|
    | 1° | 92 ft (28 m) | 0.17 mi (0.3 km) | 0.35 mi (0.6 km) |
    | 10° | 0.17 mi (0.3 km) | 1.7 mi (2.8 km) | 3.5 mi (5.6 km) |
    | 15° | 0.26 mi (0.4 km) | 2.6 mi (4.2 km) | 5.2 mi (8.3 km) |

    Fifteen degrees uncorrected over a twenty-mile walk lands you five miles from where
    you intended — far enough to miss a valley entirely.

!!! danger "WARNING: getting the direction backwards doubles your error"
    West and east declination take opposite corrections, so reversing them does not leave
    you uncorrected — it puts you **twice as far off as doing nothing**. In Washington
    state, at about 14 degrees east, the correct move is to subtract 14. Add it instead and
    you are 28 degrees out.

    The reliable check: **west of the zero line, declination is EAST; east of it, it is
    WEST.** It reads backwards, which is exactly why it gets mixed up. The needle leans
    toward the magnetic pole, so from the western US it leans east, and from the eastern US
    it leans west.

    Read the figure off your map margin or the NOAA calculator rather than recalling which
    way round it goes.

=== "West Declination"
    Magnetic north is west of true north. Add the declination to your map bearing to get a compass bearing. Memory aid: "West is best, add to the rest."

=== "East Declination"
    Magnetic north is east of true north. Subtract the declination from your map bearing. Memory aid: "East is least, subtract at least."

If your compass has a declination adjustment screw, set it once and all readings convert automatically.

## Check the Compass Itself First

!!! danger "WARNING: a compass can be reversed and still look perfectly normal"
    A compass needle can be **re-magnetised backwards** by storing it near a strong
    magnet. The red end then points *south*. Nothing about the compass looks wrong — the
    needle swings freely, settles confidently, and is wrong by 180 degrees.

    This has become common rather than rare. Phone speakers, magnetic phone mounts and
    cases, tablet covers, earbud cases, and other compasses all contain rare-earth magnets
    strong enough to do it, and it happens in a pack pocket without anyone noticing.

    **Check before every trip and any time the compass has shared a pocket with
    electronics:**

    - Step outside and confirm the red end points at the sun around midday in the Northern
      Hemisphere the needle should read roughly south toward the sun, i.e. the red north
      end points away from it.
    - Or check it at night against Polaris.
    - Or compare it against a second compass held well apart from the first.

    A partially reversed needle is worse again: it settles at an odd angle or swings
    sluggishly. Any compass that hesitates, wanders, or disagrees with the sky is not to be
    trusted. Do not store a compass against your phone.

## Taking a Bearing

A bearing is the direction from your position to a target, measured in degrees from north.

### Field Bearing (compass to terrain)

1. Hold the compass flat at waist height with the direction-of-travel arrow pointing at the target.
2. Rotate the bezel until the orienting arrow frames the red end of the needle ("red in the shed").
3. Read the number at the index line. That is your bearing in degrees.

### Map Bearing (map to compass)

1. Place the compass on the map with the baseplate edge connecting your position to your destination.
2. Ensure the direction-of-travel arrow points toward the destination, not away from it.
3. Rotate the bezel until the orienting lines are parallel to the map's north-south grid lines, with the orienting arrow pointing toward the top of the map.
4. Read the bearing at the index line.
5. Adjust for declination before following this bearing in the field.

## Following a Bearing

1. Set the desired bearing at the index line.
2. Hold the compass level and rotate your entire body until the red needle sits inside the orienting arrow.
3. Look along the direction-of-travel arrow and pick a visible landmark on that line — a specific tree, rock, or ridge feature.
4. Walk to that landmark. Do not stare at the compass while walking.
5. At the landmark, repeat the process: recheck the bearing, pick the next landmark, walk.

!!! tip
    In thick forest or fog, use a partner. Send them ahead and direct them onto the bearing line by voice or hand signals.

## Map Reading Basics

### Contour Lines

Contour lines connect points of equal elevation. Learn these patterns:

- **Close together** — steep slope
- **Far apart** — gentle slope or flat ground
- **Concentric circles** — hilltop or depression (depressions have tick marks pointing inward)
- **V-shapes pointing uphill** — valleys and stream drainages
- **V-shapes pointing downhill** — ridgelines and spurs

The **contour interval** (elevation change between lines) is printed in the map margin. Common intervals: 20 feet (6 m), 40 feet (12 m), or 10 meters.

### Scale

Map scale tells you the ratio of map distance to real distance. On a 1:24,000 map, 1 inch (2.5 cm) on the map equals 24,000 inches (2,000 feet / 610 m) on the ground. Use the bar scale in the margin for quick measurement.

### Legend

Read the legend before navigating. Key symbols: trails (dashed lines), water (blue), vegetation (green tint), roads (red or black lines), buildings (small black squares).

## Triangulation

Triangulation determines your position using bearings to known landmarks.

1. Identify two or three features visible both in the terrain and on the map (peaks, towers, lake points, road intersections).
2. Take a field bearing to the first feature.
3. Convert to a map bearing (apply declination in reverse).
4. On the map, place the compass edge on that feature with the bearing set.
5. Draw or visualize a line from the feature back toward you (the back bearing).
6. Repeat for the second and third features.
7. Your position is where the lines intersect. Three lines form a small triangle — you are inside it.

!!! note
    Use landmarks at least 30 degrees apart for the best fix. Landmarks close together produce a vague, elongated intersection zone.

## Orienting a Map

Before reading or plotting on a map, orient it so map-north faces real-world north.

1. Set the bezel to 0 degrees (or your declination value if pre-adjusted).
2. Place the compass on the map with the baseplate edge along a north-south grid line.
3. Rotate the map and compass together until the red needle sits in the orienting arrow.
4. The map now matches the terrain. Features on your left in the real world are on your left on the map.

## Route Planning

1. Orient the map.
2. Mark your start and destination.
3. Identify **handrails** — linear features (rivers, ridgelines, trails, power lines) that run roughly parallel to your direction of travel. Follow these instead of a raw bearing when possible.
4. Identify a **catching feature** (also called a backstop) — a large, unmissable feature
   *beyond* your destination that tells you when you have gone too far.
5. Identify an **attack point** — a distinct feature *near* your destination. Navigate
   loosely to it, then precisely over the last short leg, where a bearing error costs
   metres instead of miles.
6. Break the route into legs. Take a bearing and estimate distance for each leg.
7. Note the terrain for each leg: elevation gain, water crossings, thick vegetation, cliff bands.

## Pace Counting

Pace counting measures distance traveled by counting steps.

### Calibrate Your Pace Count

1. Mark a known distance of 100 meters (330 feet) on flat ground.
2. Walk it at a natural pace, counting every time your left foot hits the ground.
3. Repeat three times and average. Most people get 62-68 paces per 100 meters on flat ground.

### Adjustments

| Condition | Adjustment |
|-----------|------------|
| Uphill | Add 2-5 paces per 100 m |
| Thick brush | Add 3-5 paces per 100 m |
| Snow (deep) | Add 5-10 paces per 100 m |
| Downhill (steep) | Add 1-3 paces per 100 m |
| Sand/gravel | Add 3-5 paces per 100 m |

Use ranger beads or knots in a cord to track groups of 100 meters.

## Deliberate Offset (Aiming Off)

When navigating to a point on a linear feature — a bridge on a river, a cabin on a trail,
a gate in a fence line — **do not aim straight at it.** Aim deliberately 5-10 degrees to
one side.

Aim straight and you arrive at the river having missed the bridge, with no way to know
whether it is upstream or downstream of you. Aim deliberately left and you arrive knowing
to turn right, every time.

This is the single most useful navigation habit on this page. Your bearing will have some
error in it; deliberate offset converts an unknown error into a known direction.

## Handrail Navigation

A handrail is any linear feature roughly parallel to your direction of travel: a ridge, river, trail, fence line, power line, or edge of a forest. Follow handrails whenever possible. They reduce navigation to a single task: stay near the feature.

## Night Compass Navigation

!!! warning "CAUTION"
    Travel at night only when necessary. The risk of injury from falls, unseen obstacles, and disorientation increases dramatically.

1. Take your bearing during remaining daylight if possible.
2. Use a red-light headlamp to preserve night vision while reading the compass.
3. Choose landmarks silhouetted against the sky — ridgelines and lone trees stand out at night.
4. Shorten your legs. Move 50-100 meters (165-330 feet) at a time.
5. Have a partner walk ahead with a light as a moving reference point.
6. Use Polaris (North Star) as a constant reference in the Northern Hemisphere. Check your bearing against its position every few minutes.

## When GPS Fails

GPS fails for predictable reasons: dead batteries, broken screen, lost signal under dense canopy or in deep canyons, satellite geometry errors in narrow valleys.

Carry a compass and paper map as primary backup on every trip. Practice compass navigation before you need it. A GPS-dependent navigator who loses the device is functionally lost.

!!! tip
    Print or photograph key map sections on your phone before the trip. A phone with a dead cell signal still displays stored images and many have a built-in magnetic compass app.

## Common Mistakes

- **Forgetting declination adjustment.** This is the single most common navigation error. Every uncorrected bearing drifts further from the true line.
- **Following the compass needle instead of the bearing.** The needle points north, not at your destination. Align the needle in the orienting arrow, then follow the direction-of-travel arrow.
- **Not calibrating pace count.** Using someone else's pace count or an uncalibrated guess produces cumulative distance errors.
- **Navigating without catching features.** Walking on a bearing with no backstop means overshooting the target with no way to know it.
- **Holding the compass near metal.** Belt buckles, knives, firearms, vehicles, and power lines deflect the needle. Hold the compass away from your body and metal objects by at least 18 inches (45 cm).
- **Aiming directly at a target on a linear feature.** Use deliberate offset instead.
- **Trusting a compass you have not checked.** Phone magnets reverse needles, and a reversed compass looks completely normal. Check it against the sun or Polaris before you rely on it.

## Quick Reference

| Task | Key Steps |
|------|-----------|
| Take a bearing | Point at target, red in shed, read index line |
| Follow a bearing | Set bearing, red in shed, pick landmark, walk |
| Declination (west) | Add to map bearing |
| Declination (east) | Subtract from map bearing |
| Orient map | Compass on grid line, rotate map until red in shed |
| Triangulate | Bearings to 2-3 known features, back-plot lines, position at intersection |
| Pace count (flat) | ~65 paces per 100 m (330 ft) — calibrate your own |
| Deliberate offset | Aim 5-10 degrees to one side of target on a linear feature |

## See Also

- [Natural Navigation](natural-navigation.md) — direction without instruments, and why you cannot hold a bearing by feel.
- [Signaling for Rescue](signaling-for-rescue.md) — being found is usually faster than walking out.
- [GPS and Electronics](gps-and-electronics.md) — electronic navigation as a complement to map and compass.
- [Terrain Association](terrain-association.md) — reading the landscape to confirm map position.
- [Lost in the Woods](../scenarios/lost-in-woods.md) — using navigation skills when disoriented.

## Sources

**Primary — authoritative, revised, and publicly checkable:**

- U.S. Army. *ATP 3-50.21: Survival.* Department of the Army, 2018. Current doctrine; successor to FM 21-76 via FM 3-05.70.
- U.S. Army. *FM 21-76: Survival.* Department of the Army, 1992. The predecessor, and what most reprinted "Army Survival Manual" editions actually contain.
- U.S. Army. *FM 3-25.26: Map Reading and Land Navigation.* Department of the Army, 2001.
- NOAA National Centers for Environmental Information — Magnetic Declination Calculator
  and World Magnetic Model (WMM 2025). The pole position and declination figures above
  come from WMM 2025 and will drift; recheck before a trip.
- U.S. Air Force. *AFR 64-4: Survival Training.* Department of the Air Force, 1985.

**Additional reading — trade books and first-hand accounts.** Useful, but not
revised, not peer-reviewed, and not what a claim should rest on alone:

- Wiseman, John "Lofty." *SAS Survival Handbook.* 3rd ed., William Collins, 2014.
- *Be Expert with Map and Compass* — Bjorn Kjellstrom, revised edition, 2009
