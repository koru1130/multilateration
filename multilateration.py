from geopy import distance
from scipy.optimize import least_squares
import numpy as np

def residuals_fn(points):
    def fn(location):        
        return np.array( [ (distance.distance(p, location).km - r)*(r*r) for (p, r) in points ] )
    return fn

def multilateration(points):
    ps = [x[0] for x in points] 
    x0 = np.mean(np.array(ps),axis=0)
    return least_squares(residuals_fn(points), x0).x