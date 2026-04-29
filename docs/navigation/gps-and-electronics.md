---
tags:
  - navigation
  - gps
  - electronics
  - technology
  - satellite
  - modern
---
# GPS and Electronic Navigation

> Modern electronics extend your navigation capability — but only if you manage their limitations and always carry a backup.

## At a Glance

- GPS accuracy is typically 10–16 feet (3–5 m) in open sky; degrades under canopy, in canyons, and near cliffs
- Smartphone GPS works without cell service — download offline maps before your trip
- Battery is your most critical resource; manage it aggressively from hour one
- Satellite communicators (InReach, SPOT) and PLBs provide emergency contact beyond cell range
- Electronics fail; always carry a map, compass, and the skills to use them

## How GPS Works

GPS receivers triangulate position from signals broadcast by 24+ satellites orbiting at 12,550 miles (20,200 km). Your device needs line-of-sight to at least four satellites to calculate a 3D fix (latitude, longitude, altitude).

### Accuracy Limitations

| Factor | Effect on Accuracy |
|---|---|
| Open sky | 10–16 ft (3–5 m) |
| Forest canopy | 30–100 ft (10–30 m) |
| Deep canyon | Fix may fail entirely |
| Near cliffs/buildings | Multipath errors to 50 ft (15 m) |

!!! warning "CAUTION"
    GPS altitude readings are less accurate than horizontal position — errors of 50–150 feet (15–45 m) are common. Do not rely on GPS altitude for critical decisions.

## Smartphone GPS

Your phone contains a full GPS receiver. It works without cell service — the key is preparation.

### Before You Leave

1. Download offline maps for your entire area plus a buffer zone.
2. Test offline mode at home: enable airplane mode and verify maps load.
3. Charge your phone to 100%. Bring a power bank rated at least 10,000 mAh.
4. Carry your phone in a waterproof case or dry bag.

### Recommended Offline Map Apps

=== "iOS"
    - Gaia GPS — topo maps, public land boundaries, route tracking
    - onX Backcountry — detailed trail data, offline satellite imagery
    - Maps.me — free, lightweight, global coverage

=== "Android"
    - Gaia GPS — same feature set as iOS
    - OsmAnd — open-source, highly configurable
    - Maps.me — free, lightweight, global coverage

!!! tip
    Save waypoints for your trailhead, camp, water sources, and bail-out points before you start hiking.

## Battery Conservation

Every hour of battery life is a navigation resource. Protect it.

1. Enable airplane mode when you do not need communication.
2. Reduce screen brightness to minimum usable level.
3. Close all background apps.
4. Disable Bluetooth, Wi-Fi, and location services when not actively navigating.
5. Turn the phone off between navigation checks.
6. Keep the phone warm — cold drains lithium batteries fast. Carry it against your body in winter.

!!! note
    A phone in airplane mode with the screen off can last 3–5 days on a single charge. A phone actively running GPS navigation lasts 4–8 hours.

## Solar Chargers

Portable solar panels weigh 6–12 oz (170–340 g) and produce 5–15 watts in direct sun.

- Charge a power bank during the day; charge your phone from the bank at night.
- Attach the panel to the outside of your pack while hiking.
- Expect 50–70% of rated output in real conditions (angle, clouds, altitude).
- Solar chargers are unreliable under heavy canopy or in overcast conditions. Do not depend on them as your sole power source.

## Satellite Communicators and PLBs

### Satellite Communicators (InReach, SPOT)

- Two-way messaging via satellite network (Iridium for InReach, Globalstar for SPOT).
- SOS button triggers coordinated rescue through a monitoring center.
- Require active subscription plan.
- Allow check-in messages to contacts — reduces unnecessary search-and-rescue calls.

### Personal Locator Beacons (PLBs)

- One-way emergency distress signal on 406 MHz to the COSPAS-SARSAT satellite system.
- No subscription required. Register with your national authority (NOAA in the US).
- Battery lasts 24–48 hours of continuous transmission.
- Use only for life-threatening emergencies.

!!! danger "WARNING"
    A PLB is a last resort. Activating it commits search-and-rescue resources. Use it only when life is at risk and self-rescue is impossible.

## Coordinate Systems

Know which system your map and device use. A mismatch means your position is wrong.

=== "Latitude/Longitude"
    - Global standard. Expressed in degrees, minutes, seconds (DMS) or decimal degrees.
    - Example: 45°30'15"N, 122°40'30"W or 45.50417, -122.67500
    - Used by most smartphone apps and international SAR.

=== "UTM (Universal Transverse Mercator)"
    - Grid-based system in meters. Easier for measuring distance on a map.
    - Example: 10T 525000mE 5040000mN
    - Used on USGS topographic maps and by many land management agencies.

!!! tip
    Set your GPS device and your paper map to the same coordinate system and datum (usually WGS84) before your trip. Verify by checking a known point.

## Waypoint Marking

Mark waypoints for critical locations: trailhead, camp, water sources, trail junctions, and emergency bail-out routes.

1. Stand still for 30 seconds to let the GPS settle before marking.
2. Name waypoints clearly — "Camp1" not "Waypoint 047."
3. Record waypoints in a notebook as backup.
4. Share your waypoint list with someone who is not on the trip.

## When Electronics Fail

Electronics fail from water, impact, cold, dead batteries, and software crashes. Prepare for it.

1. Carry a baseplate compass and a paper topographic map of your area.
2. Know how to take a bearing and plot your position before you need to.
3. Mark your last known GPS position on your paper map when electronics are working.
4. Practice terrain association — matching what you see to what the map shows.

!!! note
    The best electronic navigation tool is the one backed up by a non-electronic method you have practiced.

## Common Mistakes

- **Trusting GPS under heavy canopy.** Position can drift hundreds of feet. Cross-check with terrain features.
- **Not downloading offline maps.** Cell service ends long before the trailhead in most wilderness areas.
- **Running GPS continuously.** Check position periodically, then turn the screen off.
- **Ignoring coordinate system mismatch.** Lat/long on your device and UTM on your map means your plotted position is wrong.
- **Carrying electronics without a backup.** One drop in a creek and your only navigation tool is gone.
- **Waiting until the battery is dead to conserve power.** Start conservation immediately.

## Quick Reference

| Item | Key Fact |
|---|---|
| GPS accuracy (open sky) | 10–16 ft (3–5 m) |
| Smartphone GPS battery life | 4–8 hrs active, 3–5 days airplane mode |
| PLB signal duration | 24–48 hrs continuous |
| InReach/SPOT | Two-way messaging, SOS, subscription required |
| PLB | One-way SOS, no subscription, register with NOAA |
| Solar panel output | 50–70% of rated wattage in real conditions |
| Coordinate datum standard | WGS84 |

## See Also

- [Map and Compass Navigation](../navigation/map-and-compass.md)
- [Natural Navigation](../navigation/natural-navigation.md)
- [Signaling for Rescue](../navigation/signaling-for-rescue.md)
- [Communication Plans](../preparedness/communication-plans.md) — integrating electronic devices into family emergency plans.
- [Terrain Association](terrain-association.md) — backup navigation when batteries die.

## Sources

- US Air Force Survival Manual (AF 64-4)
- Garmin InReach and SPOT product documentation
- NOAA SARSAT PLB registration and specifications
- USGS topographic map standards and UTM reference
- Wilderness Medical Society practice guidelines on field communication
