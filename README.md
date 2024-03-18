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
Key: \
Blue: Ego robot\
Red: Other robots in the scene\
Grayscale: White: Fully visible; Black: Non-visible\
Trailing shadow: Slowly decaying visibility (White to black) to the non-visible region as time passes (Due to the dynamic environment)\



![synapse_eyes-ezgif com-video-to-gif-converter](https://github.com/synapsemobility/synapseBEV/assets/163760520/a67aceae-fec2-4e1a-8d79-f6bb277abc65)





## Synapse Plan
```
python launch_synapse_plan.py --config_file configs/synapse_plan/config_file.yml --output_file configs/synapse_plan/output_file.yml 
```

Below, two robots collaboratively planned their path from the starting position to the goal position. 

|            Current Approach (Failure)           |            with Synapse (Success)           |
|:--------------------------------------:|:--------------------------------------:|
| https://github.com/synapsemobility/synapseBEV/assets/163760520/1e3839bb-0937-4795-8cff-3641ea965f04 | https://github.com/synapsemobility/synapseBEV/assets/163760520/c88a9e92-d436-4a8d-8672-bd9b30293056
|




