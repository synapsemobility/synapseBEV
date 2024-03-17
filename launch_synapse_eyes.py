from synapsebev import main_synapse_eyes
import fire

def main(config_file):
    main_synapse_eyes(config_file)

if __name__ == "__main__":
    fire.Fire()