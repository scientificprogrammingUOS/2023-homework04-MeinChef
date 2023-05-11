import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
        
    if( isinstance(loc, (int, float)) and isinstance(scale, (int, float)) and isinstance(upper_bound, (int, float)) and isinstance(lower_bound, (int, float)) and lower_bound < upper_bound ):
        
        SAMPLE_SIZE = 200;
        samples = np.random.normal(loc, scale, SAMPLE_SIZE);
        mask = (samples > lower_bound) & (samples < upper_bound);
        samples = samples[mask];

        mean = abs(np.sum(samples)/len(samples));    
        std = np.sqrt(np.sum(np.square(samples - mean)) / len(samples));

        return (mean, std);

    else:    
        raise TypeError("You either gave that funciont a ");

if __name__ == "__main__":
    # use this for your own testing!
    pass    
