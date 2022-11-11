from pathlib import Path
from scipy.optimize import curve_fit
import configparser
import pandas as pd

def main():
    # Load the config file
    config_path = Path('..','settings','config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)

    # Set input
    input_path = Path('..',config['PATH_INFORMATION']['input_path'])
    input_file = config['FILE_INFORMATION']['input_file']

    # Set output
    output_path = Path('..',config['PATH_INFORMATION']['output_path'])

    # Read input and generate dataframe
    df = pd.read_csv(Path(input_path, input_file))

if __name__ == "__main__":
    main()
