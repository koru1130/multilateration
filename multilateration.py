from geopy import distance
from scipy.optimize import least_squares
import numpy as np

def residuals_fn(points, dist):
    def fn(location):        
        return np.array( [ (dist(p, location).km - r)*(r*r) for (p, r) in points ] )
    return fn

def multilateration(points, dist_type ='geodesic'):
    if dist_type == 'geodesic' :
        dist = distance.distance
    elif dist_type == 'great_circle' :
        dist = distance.great_circle
    else:
        raise Exception("dist_type error")

    ps = [x[0] for x in points] 
    x0 = np.mean(np.array(ps),axis=0)
    return least_squares(residuals_fn(points, dist), x0).x