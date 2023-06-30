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
