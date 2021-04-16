
from ..feature_types import secondary_feature
from ..raw.gps import gps
import pandas as pd
import numpy as np
import similaritymeasures

MS_IN_A_DAY = 86400000

'''
@secondary_feature(
    name='cortex.feature.frechet',
    dependencies=[gps]
'''
def frechet(LOOKBACK=MS_IN_A_DAY, **kwargs):
    """
    Calculate Frechet Distance between two trajectories
    """
    gps1 = gps(**kwargs)
    if gps1:
        arr1 = pd.DataFrame(gps1)[['latitude', 'longitude']].to_numpy()
    else:
        return None    
    start2 = kwargs['start'] - LOOKBACK
    end2 = kwargs['end'] - LOOKBACK
    gps2 = gps(id = kwargs['id'], start = start2, end = end2)
    if gps2:
        arr2 = pd.DataFrame(gps2)[['latitude', 'longitude']].to_numpy()
        discrete_frechet = similaritymeasures.frechet_dist(arr1, arr2)
    else:
        arr2 = None #testing 
    
    return {'timestamp':kwargs['start'], 'frechet_distance': discrete_frechet}
    
    
