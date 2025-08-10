import numpy as np

def H_matrix_generation(order_of_codes):

    two_power_order_of_codes =  2 ** order_of_codes
    no_of_checks = 2 ** (2 * order_of_codes - 1 )
    no_of_qubits = 3 * no_of_checks 
    #not the actual number of qubits, used for implemetation purpose only

    range_of_y = two_power_order_of_codes  
    range_of_x = two_power_order_of_codes // 2

    range_of_j = two_power_order_of_codes // 2 * 3 
    range_of_i = two_power_order_of_codes


    representation_matrix_for_x = np.zeros((no_of_checks,8), dtype=int)

    row_number = 0 
    for x in range(range_of_x):
        for y in range(range_of_y):

            #calculating a row of Hx matrix

            if y % 2 == 0:
                representation_matrix_for_x[row_number][0] = (x) * range_of_j + (3*(y//2)) 
                representation_matrix_for_x[row_number][1] = (x - 1 if x != 0 else ((range_of_i//2) - 1)) * range_of_j + (3*(y//2)) 
                representation_matrix_for_x[row_number][2] = (2*x) * range_of_j + ((3*(y//2))  +1)
                representation_matrix_for_x[row_number][3] = (2*x -1 if x != 0 else range_of_i -1) * range_of_j + ((3*(y//2))  +1)
                representation_matrix_for_x[row_number][4] = (x) * range_of_j + ((3*(y//2))-1 if y != 0 else range_of_j -1)
                representation_matrix_for_x[row_number][5] = (x - 1 if x != 0 else ((range_of_i//2) - 1)) * range_of_j + ((3*(y//2))-1 if y != 0 else range_of_j -1)
                representation_matrix_for_x[row_number][6] = (2*x) * range_of_j + ((3*(y//2))-2 if y != 0 else range_of_j -2)
                representation_matrix_for_x[row_number][7] = (2*x -1 if x != 0 else range_of_i -1) * range_of_j + ((3*(y//2))-2 if y != 0 else range_of_j -2)

            else:                
                representation_matrix_for_x[row_number][0] = (x) * range_of_j + (3*((y-1)//2))
                representation_matrix_for_x[row_number][1] = (2*x) * range_of_j + ((3*((y-1)//2)) + 1)
                representation_matrix_for_x[row_number][2] = (2*x + 1) * range_of_j + ((3*((y-1)//2)) + 1)
                representation_matrix_for_x[row_number][3] = (x) * range_of_j + ((3*((y-1)//2)) + 2)
                representation_matrix_for_x[row_number][4] = -1
                representation_matrix_for_x[row_number][5] = -1
                representation_matrix_for_x[row_number][6] = -1
                representation_matrix_for_x[row_number][7] = -1

            row_number += 1

    #generating H matrix from this representation
    Hx_matrix = np.zeros((no_of_checks,no_of_qubits),dtype=int)
    
    for i in range(representation_matrix_for_x.shape[0]):
        for j in range (representation_matrix_for_x.shape[1]):
            if representation_matrix_for_x[i,j] != -1:
                Hx_matrix[i,representation_matrix_for_x[i,j]] =1 

    #removing unnecessary qubits(columns)
    mask = ~np.all(Hx_matrix == 0, axis=0)
    filtered_Hx_matrix = Hx_matrix[:,mask]

    #for colour codes Hx and Hz are identical
    return filtered_Hx_matrix,filtered_Hx_matrix

H_matrix_generation(3)