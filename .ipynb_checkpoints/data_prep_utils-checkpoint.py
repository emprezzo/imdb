import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def boolean_df(item_lists, unique_items):
    '''
    Returns a Pandas.DataFrame object with boolean-valued cells indicating whether a movie stars the actor or not. 
    Column: Actor. Row: Movie
    
    Params:
        item_lists: A list of items (actors).
        unique_items: A list of 
    '''
# Create empty dict
    bool_dict = {}
    
    # Loop through all the tags
    for i, item in enumerate(unique_items):
        
        # Apply boolean mask
        bool_dict[item] = item_lists.apply(lambda x: item in x)
            
    # Return the results as a dataframe
    return pd.DataFrame(bool_dict)

def plot_unique_counts(df_col):
    '''
    Returns a matplotlib bar chart visualizing the frequencies of all the unique values in the dataframe column.
    '''
    # Get unique items & counts
    unique_values = df_col.explode().value_counts().index.tolist()
    unique_value_counts = df_col.explode().value_counts().values

    # Create plot
    fig, ax = plt.subplots(figsize = (14,4))
    ax.bar(unique_values, unique_value_counts)
    ax.set_ylabel("Frequency", size = 12)
    ax.set_title(df_col.columns, size = 14)
    