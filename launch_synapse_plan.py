from synapsebev import main_synapse_plan
import fire

def main(config_file, output_file):
    main_synapse_plan(config_file, output_file)

if __name__ == "__main__":
    fire.Fire(main)