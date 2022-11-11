from pathlib import Path
import configparser

def main():
    # Load the config file
    config_path = Path('..','settings','config.ini')
    config = configparser.ConfigParser()

    config.read(config_path)

    # Set input and output paths
    input_path = Path('..',config['PATH_INFORMATION']['input_path'])
    print(input_path)

if __name__ == "__main__":
    main()
