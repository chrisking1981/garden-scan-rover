# Garden Scan Rover

Stap voor stap een bestuurbaar scankarretje bouwen, eerst in de woonkamer en later voor een hoogtekaart van de tuin.

## Eerste mijlpaal
Handmatig rijden en op de laptop zien welke vloer geldig gescand is en waar nog gaten zitten. Geen autonome navigatie of zandtransport in de eerste versie.

## Aanwezige hardware
- 3 × Creality 42-40 en 2 × 42-34 stappenmotoren; vier motoren bedoeld voor de wielen.
- Bestaande CR-10S-kast/moederbord met aangepaste firmware; Python-aansturing heeft eerder gewerkt. Firmware is nog niet in deze repo opgenomen.
- Aluminium 2040-profiel: **460 × 40 × 20 mm**. Twee kopse gaten: 20 mm hart-op-hart, 10 mm vanaf de zijkanten. Gatdiameter/draad nog te meten.
- RealSense D435, schuin naar de vloer gericht.
- Samsung Galaxy S24 in een vaste houder voor AprilTags en eventueel bewegingssensoren.
- Laptop voor kaartopbouw en besturing.
- Arduino Nano 33 IoT en Nano Motor Carrier beschikbaar, voorlopig optioneel.

## Modellen
| Bestand | Doel |
|---|---|
| `models/vendor/creality/42-34.step` en `.SLDPRT` | Origineel motormodel |
| `models/vendor/creality/42-40.step` en `.SLDPRT` | Origineel motormodel; upstream STEP heet 40-42, intern 42-40 |
| `models/vendor/creality/2040-profile-original.step` en `.SLDPRT` | Originele doorsnede/referentie; **nog niet op 460 mm gebracht** |
| `models/vendor/realsense/d435.dae` | Officieel visualisatiemodel, geen productietekening |
| `models/vendor/realsense/_d435.urdf.xacro` | Referentie voor sensorframes; vereist de overige ROS-packagebestanden om zelfstandig te werken |

De SolidWorks-CAD van de D435 kan lokaal worden opgehaald met `python3 tools/download_d435_cad.py`. Die download is geen STEP-bestand en wordt niet opnieuw gepubliceerd zonder duidelijke herdistributietoestemming.

Zie [bronnen en licenties](docs/SOURCES.md) en [openstaande punten](codex/known_issues.md). De modellen zijn referenties; controleer fysieke assen, gaten en connectoren voor het ontwerpen van passende houders.
