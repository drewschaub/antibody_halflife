from pathlib import Path
from scipy.optimize import curve_fit
from scipy import stats
import configparser
import numpy as np
import pandas as pd

def feather_terminal_phase(x, y, antibody='antibody'):
    print('{}\nn, b, beta, halflife, r, r2, adjusted r2'.format(antibody))
    log_y = np.log(y)

    unique_time_points = sorted(np.unique(np.array(x)))

    best_adjusted_r2 = 0.0
    best_parameters = []
    for n in range(3, len(unique_time_points)+1):
    
        terminal_time_points = unique_time_points[-n:]
        
        x_term = []
        y_term = []
        for i in range(0, len(x)):
            if x[i] in terminal_time_points:
                x_term.append(x[i])
                y_term.append(log_y[i])
 
        res = stats.linregress(x_term, y_term)
        slope = res.slope
        intercept = res.intercept
        r_value = res.rvalue
        p_value = res.pvalue
        std_err = res.stderr
        intercept_stderr = res.intercept_stderr

        b = np.exp(intercept)
        beta = -slope
        r2 = r_value**2
        adjusted_r2 = 1 - ( (1-r2)*(n-1) / (n-2)   )
        if adjusted_r2 > best_adjusted_r2:
            best_adjusted_r2 = adjusted_r2
            best_parameters = [n, terminal_time_points, b, beta, np.log(2)/beta, r_value, r2, adjusted_r2 ]

        print('{}, {:.6f}, {:.6f}, {:.6f}, {:.6f}, {:.6f}'.format(n, b, beta, np.log(2)/beta, r2, adjusted_r2))

    n, terminal_time_points, b, beta, halflife, r_value, r2, adjusted_r2 = best_parameters
    print('{} best Fit - n: {}, terminal time points: {}, b: {:.10f}, beta: {:.10f}, halflife: {:.6f}, adjusted r2: {:.6f}, r2: {:.6f}\n'.format(antibody, n, terminal_time_points, b, beta, halflife, adjusted_r2, r2))

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
    print(Path(input_path, input_file))
    df = pd.read_csv(Path(input_path, input_file))

    # Generate lists of unique antibodies and group numbers
    antibodies = df['antibody'].unique().tolist()
    groups = df['group'].unique().tolist()

    for antibody in antibodies:
        antibody_df = df[df['antibody'] == antibody]
        x = antibody_df['day'].tolist()
        y = antibody_df['conc'].tolist()

        feather_terminal_phase(x, y, antibody)


if __name__ == "__main__":
    main()
