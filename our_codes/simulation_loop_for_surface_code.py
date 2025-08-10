import numpy as np
from bposd.hgp import hgp
from bposd.css_decode_sim import css_decode_sim
from bposd.css import css_code
from automated_H_generation_for_surface_code import H_matrix_generation,edge_augmentated_H_matrix
import matplotlib.pyplot as plt

#simulation of H matrix without edge augmentation, with defined order 
def surface_code_without_edge_augmentation(order_of_codes,values):

    Hx,Hz = H_matrix_generation(order_of_codes)

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
        lk = css_decode_sim(Hx,Hz, **osd_options)
        lk_array[k]= lk
        k += 1 

    return lk_array


#simulation of H matrix with edge augmentation, with defined order
def surface_code_with_edge_augmentation(order_of_codes,values):

    Hx,Hz = edge_augmentated_H_matrix(order_of_codes)

    lk_array = np.empty(values.shape[0], dtype=object)
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
        lk = css_decode_sim(Hx,Hz, **osd_options)
        lk_array[k]= lk
        k += 1 

    return lk_array