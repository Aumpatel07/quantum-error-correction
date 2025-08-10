import numpy as np
from bposd.hgp import hgp
from css_decode_sim1 import css_decode_sim1
from bposd.css import css_code
from automated_H_genreration_for_colour_codes import H_matrix_generation
from automated_H_generation_for_surface_code import edge_augmentated_H_matrix
import matplotlib.pyplot as plt

#simulation of H matrix of a colour code with restriction mapping, with defined order 
def colour_code(order_of_codes,values):
    if ( order_of_codes < 2  ): 
        print("invalid order of codes")
        return
    
    Hx,Hz = H_matrix_generation(order_of_codes)
    Hx1,Hz1 = edge_augmentated_H_matrix(order_of_codes-1)
    lk_array = np.empty(values.shape[0],dtype=object)
    k = 0 

    for i in values:
        osd_options={
        'error_rate': i,
        'target_runs': 1000,
        'xyz_error_bias': [0, 0, 1],
        'output_file': 'test.json',
        'bp_method': "ms",
        'ms_scaling_factor': 0,
        'osd_method': "osd_cs",
        'osd_order': 0,
        'channel_update': None,
        'seed': 3,
        'max_iter': 20,
        'output_file': "test.json"
        }
        lk = css_decode_sim1(Hx1,Hx,Hz, **osd_options)
        lk_array[k]= lk
        k += 1 

    return lk_array
