import pandas as pd
import numpy as np

def create_dataset():
    ages = np.array([13, 14, 15, 16, 17, 18, 19, 20])
    social_media_usage = np.array([2.99, 3.41, 3.65, 3.97, 4.02, 4.14, 3.94, 4.13])
    depressive_symptom = np.array([1.62, 1.73, 1.83, 1.91, 1.94, 1.87, 1.86, 1.94])
    anxiety = np.array([0.96, 1.06, 1.18, 1.30, 1.37, 1.45, 1.44, 1.43])
    
    df = pd.DataFrame({
        "Age": ages,
        "Social Media Usage": social_media_usage,
        "Depressive Symptom": depressive_symptom,
        "Anxiety": anxiety
    })
    
    return df