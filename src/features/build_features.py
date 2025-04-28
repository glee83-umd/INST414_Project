import pandas as pd

def split_usage_groups(df):
    median_usage = df['Social Media Usage'].median()
    low_usage = df[df['Social Media Usage'] <= median_usage]
    high_usage = df[df['Social Media Usage'] > median_usage]
    return low_usage, high_usage