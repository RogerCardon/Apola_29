## 1. Events Analysis 

### ColonyMoon

| Device                               |   Excellent |   Good |   Warning |   Faulty |   Killed |   Unknown |
|:-------------------------------------|------------:|-------:|----------:|---------:|---------:|----------:|
| other_componentsdata_mission_devices |          14 |     16 |        15 |       17 |       19 |         9 |
| satelite                             |           9 |     17 |        15 |       12 |       19 |        18 |
| space_vehicle                        |          14 |     21 |        11 |       20 |       17 |         7 |
| spacecraft                           |           7 |     14 |        18 |       17 |       16 |        18 |
| spacesuit                            |          12 |     18 |        15 |       14 |       17 |        14 |

### GalaxyTwo

| Device                               |   Excellent |   Good |   Warning |   Faulty |   Killed |   Unknown |
|:-------------------------------------|------------:|-------:|----------:|---------:|---------:|----------:|
| other_componentsdata_mission_devices |          15 |     16 |        11 |       12 |       11 |        13 |
| satelite                             |          13 |     17 |         9 |        8 |       11 |        20 |
| space_vehicle                        |          12 |     13 |        13 |       16 |       15 |         9 |
| spacecraft                           |          18 |      8 |        11 |       12 |       16 |        13 |
| spacesuit                            |          11 |     12 |        18 |       12 |       12 |        13 |

### OrbitOne

| Device                               |   Excellent |   Good |   Warning |   Faulty |   Killed |   Unknown |
|:-------------------------------------|------------:|-------:|----------:|---------:|---------:|----------:|
| other_componentsdata_mission_devices |          11 |     10 |        23 |       11 |       18 |        17 |
| satelite                             |          19 |     14 |        11 |        9 |       16 |        21 |
| space_vehicle                        |          17 |     16 |        14 |        9 |       12 |        22 |
| spacecraft                           |          15 |     13 |        12 |       13 |       23 |        14 |
| spacesuit                            |          18 |     16 |        14 |       10 |       15 |        17 |

### Unknow

| Device                               |   Excellent |   Good |   Warning |   Faulty |   Killed |   Unknown |
|:-------------------------------------|------------:|-------:|----------:|---------:|---------:|----------:|
| other_componentsdata_mission_devices |          16 |     17 |        15 |       17 |       13 |        10 |
| satelite                             |          17 |     20 |        13 |       12 |       15 |        11 |
| space_vehicle                        |          21 |     17 |        11 |       13 |       14 |        12 |
| spacecraft                           |          11 |     13 |        18 |       12 |       16 |        18 |
| spacesuit                            |          21 |     11 |        11 |       20 |        9 |        16 |

### VacMars

| Device                               |   Excellent |   Good |   Warning |   Faulty |   Killed |   Unknown |
|:-------------------------------------|------------:|-------:|----------:|---------:|---------:|----------:|
| other_componentsdata_mission_devices |           8 |     15 |        17 |       25 |       16 |        11 |
| satelite                             |          13 |     21 |        15 |       14 |       15 |        14 |
| space_vehicle                        |          13 |     19 |        15 |       16 |        6 |        23 |
| spacecraft                           |          12 |     13 |        13 |       21 |       17 |        16 |
| spacesuit                            |          17 |     18 |        18 |       14 |       14 |        11 |

## 2. Disconnection Management

| Device                               | Mission    |   Disconnections |
|:-------------------------------------|:-----------|-----------------:|
| space_vehicle                        | VacMars    |               23 |
| space_vehicle                        | OrbitOne   |               22 |
| satelite                             | OrbitOne   |               21 |
| satelite                             | GalaxyTwo  |               20 |
| satelite                             | ColonyMoon |               18 |
| spacecraft                           | ColonyMoon |               18 |
| spacecraft                           | Unknow     |               18 |
| other_componentsdata_mission_devices | OrbitOne   |               17 |
| spacesuit                            | OrbitOne   |               17 |
| spacesuit                            | Unknow     |               16 |
| spacecraft                           | VacMars    |               16 |
| spacesuit                            | ColonyMoon |               14 |
| spacecraft                           | OrbitOne   |               14 |
| satelite                             | VacMars    |               14 |
| other_componentsdata_mission_devices | GalaxyTwo  |               13 |
| spacecraft                           | GalaxyTwo  |               13 |
| spacesuit                            | GalaxyTwo  |               13 |
| space_vehicle                        | Unknow     |               12 |
| satelite                             | Unknow     |               11 |
| other_componentsdata_mission_devices | VacMars    |               11 |

## 3. Mission Consolidation

| Device                                            |   Total Inoperable (Killed + Unknown) |
|:--------------------------------------------------|--------------------------------------:|
| ColonyMoon - other_componentsdata_mission_devices |                                    28 |
| ColonyMoon - satelite                             |                                    37 |
| ColonyMoon - space_vehicle                        |                                    24 |
| ColonyMoon - spacecraft                           |                                    34 |
| ColonyMoon - spacesuit                            |                                    31 |
| GalaxyTwo - other_componentsdata_mission_devices  |                                    24 |
| GalaxyTwo - satelite                              |                                    31 |
| GalaxyTwo - space_vehicle                         |                                    24 |
| GalaxyTwo - spacecraft                            |                                    29 |
| GalaxyTwo - spacesuit                             |                                    25 |
| OrbitOne - other_componentsdata_mission_devices   |                                    35 |
| OrbitOne - satelite                               |                                    37 |
| OrbitOne - space_vehicle                          |                                    34 |
| OrbitOne - spacecraft                             |                                    37 |
| OrbitOne - spacesuit                              |                                    32 |
| Unknow - other_componentsdata_mission_devices     |                                    23 |
| Unknow - satelite                                 |                                    26 |
| Unknow - space_vehicle                            |                                    26 |
| Unknow - spacecraft                               |                                    34 |
| Unknow - spacesuit                                |                                    25 |
| VacMars - other_componentsdata_mission_devices    |                                    27 |
| VacMars - satelite                                |                                    29 |
| VacMars - space_vehicle                           |                                    29 |
| VacMars - spacecraft                              |                                    33 |
| VacMars - spacesuit                               |                                    25 |

## 4. Percentage Calculation

| Device                               | Mission    | Percentage Excellent   | Percentage Good   | Percentage Warning   | Percentage Faulty   | Percentage Killed   | Percentage Unknown   |
|:-------------------------------------|:-----------|:-----------------------|:------------------|:---------------------|:--------------------|:--------------------|:---------------------|
| other_componentsdata_mission_devices | ColonyMoon | 0.64%                  | 0.73%             | 0.68%                | 0.78%               | 0.87%               | 0.41%                |
| satelite                             | ColonyMoon | 0.41%                  | 0.78%             | 0.68%                | 0.55%               | 0.87%               | 0.82%                |
| space_vehicle                        | ColonyMoon | 0.64%                  | 0.96%             | 0.50%                | 0.91%               | 0.78%               | 0.32%                |
| spacecraft                           | ColonyMoon | 0.32%                  | 0.64%             | 0.82%                | 0.78%               | 0.73%               | 0.82%                |
| spacesuit                            | ColonyMoon | 0.55%                  | 0.82%             | 0.68%                | 0.64%               | 0.78%               | 0.64%                |
| other_componentsdata_mission_devices | GalaxyTwo  | 0.68%                  | 0.73%             | 0.50%                | 0.55%               | 0.50%               | 0.59%                |
| satelite                             | GalaxyTwo  | 0.59%                  | 0.78%             | 0.41%                | 0.37%               | 0.50%               | 0.91%                |
| space_vehicle                        | GalaxyTwo  | 0.55%                  | 0.59%             | 0.59%                | 0.73%               | 0.68%               | 0.41%                |
| spacecraft                           | GalaxyTwo  | 0.82%                  | 0.37%             | 0.50%                | 0.55%               | 0.73%               | 0.59%                |
| spacesuit                            | GalaxyTwo  | 0.50%                  | 0.55%             | 0.82%                | 0.55%               | 0.55%               | 0.59%                |
| other_componentsdata_mission_devices | OrbitOne   | 0.50%                  | 0.46%             | 1.05%                | 0.50%               | 0.82%               | 0.78%                |
| satelite                             | OrbitOne   | 0.87%                  | 0.64%             | 0.50%                | 0.41%               | 0.73%               | 0.96%                |
| space_vehicle                        | OrbitOne   | 0.78%                  | 0.73%             | 0.64%                | 0.41%               | 0.55%               | 1.00%                |
| spacecraft                           | OrbitOne   | 0.68%                  | 0.59%             | 0.55%                | 0.59%               | 1.05%               | 0.64%                |
| spacesuit                            | OrbitOne   | 0.82%                  | 0.73%             | 0.64%                | 0.46%               | 0.68%               | 0.78%                |
| other_componentsdata_mission_devices | Unknow     | 0.73%                  | 0.78%             | 0.68%                | 0.78%               | 0.59%               | 0.46%                |
| satelite                             | Unknow     | 0.78%                  | 0.91%             | 0.59%                | 0.55%               | 0.68%               | 0.50%                |
| space_vehicle                        | Unknow     | 0.96%                  | 0.78%             | 0.50%                | 0.59%               | 0.64%               | 0.55%                |
| spacecraft                           | Unknow     | 0.50%                  | 0.59%             | 0.82%                | 0.55%               | 0.73%               | 0.82%                |
| spacesuit                            | Unknow     | 0.96%                  | 0.50%             | 0.50%                | 0.91%               | 0.41%               | 0.73%                |
| other_componentsdata_mission_devices | VacMars    | 0.37%                  | 0.68%             | 0.78%                | 1.14%               | 0.73%               | 0.50%                |
| satelite                             | VacMars    | 0.59%                  | 0.96%             | 0.68%                | 0.64%               | 0.68%               | 0.64%                |
| space_vehicle                        | VacMars    | 0.59%                  | 0.87%             | 0.68%                | 0.73%               | 0.27%               | 1.05%                |
| spacecraft                           | VacMars    | 0.55%                  | 0.59%             | 0.59%                | 0.96%               | 0.78%               | 0.73%                |
| spacesuit                            | VacMars    | 0.78%                  | 0.82%             | 0.82%                | 0.64%               | 0.64%               | 0.50%                |
| Total                                |            | 16.16%                 | 17.58%            | 16.26%               | 16.26%              | 16.99%              | 16.76%               |

