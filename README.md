# synapseBEV
A BEV visualization tool for Synapse Mobility products


```
pip install synapsebev
cd synapsebev
```


## Synapse Eyes
```
python launch_synapse_eyes.py --config_file configs/synapse_eyes/config_file.yml
```
Below visualization shows how the perception score increased when multiple robots are able to share their perception data through synapse eyes. 
Blue: Ego robot
Red: Other robot in the scene.
Gray scale: White: Fully visible; Black: Non-visible. 
Trailing shadow: Slowly decaying visible region to non-visible region as time passes (Due to dynamic environment). 



https://github.com/synapsemobility/synapseBEV/assets/163760520/b9915dc3-f4cf-4eb8-9dbd-dc85c4908026




## Synapse Plan
```
python launch_synapse_plan.py --config_file configs/synapse_plan/config_file.yml --output_file configs/synapse_plan/output_file.yml 
```

Below, two robots collaboratively planned their path to go from the starting position to the goal position. 

https://github.com/synapsemobility/synapseBEV/assets/163760520/217065bb-8fd5-4bb4-9577-3c99faf49480

