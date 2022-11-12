def get_twocompartment_model_params(X, y, alpha_phase_idx_list, beta_phase_idx_list, beta = 0, halflife = 0):
    """Fit missing values from two compartment model. The user provides
    idx values for the alpha phase and beta phase. Excluded timepoints
    are assumed to be outliers and are excluded from the fitting. The user
    may provide beta if known.

    Keyword arguments:
    X: list of timepoint values
    y: list of concentration values
    alpha_phase: idx values of timepoints to be used for alpha phase
    beta_phase: idx values of timepoints to be used for beta phase
    beta: beta parameter (float, optional)
    
    Returns:
    a, alpha, b, beta: returns four parameters are float values
    """
    # Fit the beta-phase
    x = [X[i] for i in beta_phase_idx_list]
    y = [X[i] for i in beta_phase_idx_list]
    
    if beta == 0:
        popt, pcov = curve_fit(f2, x, y)
        b, beta = popt
    else:
        popt, pcov = curve_fit(f1, x, y)
        b = popt[0]   
        
    halflife = np.log(2) / beta
        
    # Fit the alpha-phase
    idx_list = alpha_phase_idx_list + beta_phase_idx_list
    x = [X[i] for i in idx_list]
    y = [X[i] for i in idx_list]    
    popt, pcov = curve_fit(f3, x, y)
    a, alpha = sorted(popt)
    
    return a, alpha, b, beta, halflife
