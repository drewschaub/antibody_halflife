import seaborn as sns
import matplotlib.pyplot as plt

def plot_twocompartment_model(x, y, px, py, antibody, parameters, alpha_phase = [], beta_phase = [], colors = ['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00'], organism='human', figsize=(7, 4), image_path='model.png'):
    a, alpha, b, beta, halflife = parameters
    
    organism_timepoint_dict = {'human' : [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360],
                               'hFcRn': [1, 2, 5, 7, 9, 14, 21, 28, 35, 42, 49, 56]
                              }                           
        
    fig, ax = plt.subplots(figsize=figsize)
    sns.despine(right = True)
    
    if len(beta_phase) > 0:
        xb = [x[i] for i in beta_phase]
        yb = [y[i] for i in beta_phase]        
        plt.plot(xb, yb, color=colors[1], marker='o', linestyle='--', markersize=4, linewidth=0.5, label='used to model beta phase (halflife)')
    
    if len(alpha_phase) > 0:
        xa = [x[i] for i in alpha_phase]
        ya = [y[i] for i in alpha_phase]        
        plt.plot(xa, ya, color=colors[2], marker='o', linestyle='--', markersize=4, linewidth=0.5, label='used to model complete model')

    if (len(beta_phase) > 0) and (len(alpha_phase) > 0):
        outliers_idxs = []
        for i in range(0, len(x)):
            if (i not in alpha_phase) and (i not in beta_phase):
                outliers_idxs.append(i)
                
        if len(outliers_idxs) > 0:
            xo = [x[i] for i in outliers_idxs]
            yo = [y[i] for i in outliers_idxs] 
            plt.scatter(xo, yo, marker='+', color=colors[0], label='outliers excluded')
    
    plt.plot(px, py, color=colors[3], linewidth=1.5, label='model [halflife: {:.1f}, a: {:.1f}, alpha: {:.5f}, b: {:.1f}, beta: {:.5f}'.format(halflife, a, alpha, b, beta))
    
    plt.legend(fontsize=8)
    
    # y-axis
    plt.ylabel(r'mAb concentration (µg/mL)')
    plt.ylim(min(py), max(py)*1.1)
    plt.yscale('log')

    # x-axis
    plt.xlabel('days after infusion')
    plt.xlim(0, max(px))
    plt.xticks(organism_timepoint_dict[organism]);
    
    plt.savefig(image_path, dpi=300)