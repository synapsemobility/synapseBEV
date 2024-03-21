# synapseBEV
A BEV visualization tool for Synapse Mobility products


## 3-step Library Installation
```
git clone https://github.com/synapsemobility/synapseBEV.git
pip install synapsebev
cd synapsebev
```


## Synapse Eyes
```
python launch_synapse_eyes.py --config_file configs/synapse_eyes/config_file.yml
```
The visualization below shows how the perception score increased when multiple robots could share their perception data through synapse eyes. \
\
### Key: 
- Blue: Ego robot\
- Red: Other robots in the scene\
- Grayscale: White: Fully visible; Black: Non-visible\
- Trailing shadow: Slowly decaying visibility (White to black) to the non-visible region as time passes (Due to the dynamic environment)\

### Assumptions
- Detection range of individual robot is 5*5 grid, centered at the robot.
- Required perception range is 10*10 grid, centered at the robot.
- Perception score: Sum of the 10*10 grid cell values, centered at the robot. Non-visible cell is 0, and visible cell is 1. Partial visibility ranges are: (0, 1)

![synapse_eyes-ezgif com-video-to-gif-converter](https://github.com/synapsemobility/synapseBEV/assets/163760520/a67aceae-fec2-4e1a-8d79-f6bb277abc65)

Assumptions





## Synapse Plan
```
python launch_synapse_plan.py --config_file configs/synapse_plan/config_file.yml --output_file configs/synapse_plan/output_file.yml 
```

Below, two robots collaboratively planned their path from the starting position to the goal position. 

|            Current Approach (Failure)           |            with Synapse (Success)           |
|:--------------------------------------:|:--------------------------------------:|
| ![current-ezgif com-video-to-gif-converter](https://github.com/synapsemobility/synapseBEV/assets/163760520/542f194e-d374-4f32-b872-d24b2756a27a) | ![synapse_plan-ezgif com-video-to-gif-converter](https://github.com/synapsemobility/synapseBEV/assets/163760520/9cdc695d-95ce-45eb-81b4-186e7b1c205e) |






