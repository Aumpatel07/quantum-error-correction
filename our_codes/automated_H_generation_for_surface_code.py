import numpy as np

def H_matrix_generation(order_of_codes):

    two_power_order_of_codes =  2 ** order_of_codes
    no_of_checks = 2 ** (2 * order_of_codes - 1 )
    no_of_qubits = 2 * no_of_checks 

    range_of_y = two_power_order_of_codes  
    range_of_x = two_power_order_of_codes // 2


    representation_matrix_for_x = np.zeros((no_of_checks,4), dtype=int)
    representation_matrix_for_z = np.zeros((no_of_checks,4), dtype=int)

    row_number = 0 
    for x in range(range_of_x):
        for y in range(range_of_y):

            #calculating a row of Hx matrix
            representation_matrix_for_x[row_number,0] = (2* x) * range_of_y + (y)  

            representation_matrix_for_x[row_number,1] = (2* x) * range_of_y + (y + 1  if y  != range_of_y - 1  else 0)
            
            if y % 2 == 0: representation_matrix_for_x[row_number,2] = (2*x + 1) * range_of_y + (y)
            else: representation_matrix_for_x[row_number,2] = (2*x -1 if x != 0 else two_power_order_of_codes -1) * range_of_y + (y)
            
            if y % 2 == 0: representation_matrix_for_x[row_number,3] = (2*x + 1) * range_of_y + (y + 1 if y  != range_of_y- 1 else 0)
            else: representation_matrix_for_x[row_number,3] = (2*x -1 if x != 0 else two_power_order_of_codes -1) * range_of_y + (y + 1 if y  != range_of_y- 1 else 0)

            #calculating a row of Hz matrix
            representation_matrix_for_z[row_number,0] = (2* x) * range_of_y + (y)  

            representation_matrix_for_z[row_number,1] = (2* x) * range_of_y + (y + 1  if y  != range_of_y - 1  else 0)
            
            if y % 2 != 0: representation_matrix_for_z[row_number,2] = (2*x + 1) * range_of_y + (y)
            else: representation_matrix_for_z[row_number,2] = (2*x -1 if x != 0 else two_power_order_of_codes -1) * range_of_y + (y)
            
            if y % 2 != 0: representation_matrix_for_z[row_number,3] = (2*x + 1) * range_of_y + (y + 1 if y  != range_of_y- 1 else 0)
            else: representation_matrix_for_z[row_number,3] = (2*x -1 if x != 0 else two_power_order_of_codes -1) * range_of_y + (y + 1 if y  != range_of_y- 1 else 0)
            
            row_number += 1
            

    #generating H matrix from this representation

    Hx_matrix = np.zeros((no_of_checks,no_of_qubits),dtype=int)
    Hz_matrix = np.zeros((no_of_checks,no_of_qubits),dtype=int)
    
    for i in range(representation_matrix_for_x.shape[0]):
        for j in range (representation_matrix_for_x.shape[1]):
            Hx_matrix[i,representation_matrix_for_x[i,j]] =1 

    for i in range(representation_matrix_for_z.shape[0]):
        for j in range (representation_matrix_for_z.shape[1]):
            Hz_matrix[i,representation_matrix_for_z[i,j]] =1 
    
    return Hx_matrix,Hz_matrix




def edge_augmentated_H_matrix(order_of_codes):

    two_power_order_of_codes =  2 ** order_of_codes
    no_of_checks = 2 ** (2 * order_of_codes + 1 )
    #not the actual number of checks, used only for implementation purposes
    no_of_checks_for_z = 2 ** (2* order_of_codes - 1)
    no_of_qubits = no_of_checks 

    range_of_y = two_power_order_of_codes * 2 
    range_of_x = two_power_order_of_codes 


    representation_matrix_for_x = np.zeros((no_of_checks,4), dtype=int)
   
    #calculating representation matrix for x 
    row_number = 0 
    for x in range(range_of_x):
        for y in range(range_of_y):

            if ( y % 2 == 0 and x >= range_of_x // 2 ): 
                representation_matrix_for_x[row_number,:] = -1
                row_number += 1
                continue

            if ( y % 2 == 0 ):
                representation_matrix_for_x[row_number,0] = (2* x) * range_of_y+ (y)  

                representation_matrix_for_x[row_number,1] = (2* x) * range_of_y+ (y + 1  if y  != range_of_y - 1  else 0)
                
                if y % 4 == 0: representation_matrix_for_x[row_number,2] = (2*x + 1) * range_of_y + (y)
                else: representation_matrix_for_x[row_number,2] = (2*x -1 if x != 0 else range_of_x -1) * range_of_y + (y)
                
                if y % 4 == 0: representation_matrix_for_x[row_number,3] = (2*x + 1) * range_of_y + (y + 1 if y  != range_of_y- 1 else 0)
                else: representation_matrix_for_x[row_number,3] = (2*x -1 if x != 0 else range_of_x -1) * range_of_y + (y + 1 if y  != range_of_y- 1 else 0)

            else:
                representation_matrix_for_x[row_number,0] = x * range_of_y + (y) 
                representation_matrix_for_x[row_number,1] = x * range_of_y + (y+1 if y != range_of_y -1 else 0)
                representation_matrix_for_x[row_number,2] = -1 
                representation_matrix_for_x[row_number,3] = -1 

            row_number += 1

    #generating H matrix from this representation
    Hx_matrix = np.zeros((no_of_checks,no_of_qubits),dtype=int)    
    for i in range(representation_matrix_for_x.shape[0]):
        for j in range (representation_matrix_for_x.shape[1]):
            if( j == 0 and representation_matrix_for_x[i,j] == -1): Hx_matrix[i,:] = -1
            if ( representation_matrix_for_x[i,j] != -1): Hx_matrix[i,representation_matrix_for_x[i,j]] =1 

    #elimitaing rows with all -1 values
    mask = ~(Hx_matrix == -1).all(axis =1)
    filtered_Hx_matrix = Hx_matrix[mask]


    #calculating representation for z
    range_of_x = range_of_x // 2 
    range_of_y = range_of_y // 2 
    representation_matrix_for_z = np.zeros((no_of_checks_for_z,8),dtype=int)
    row_number = 0 
    for x in range(range_of_x):
        for y in range(range_of_y):
            representation_matrix_for_z[row_number,0] = ( 2* x) * 2*range_of_y + (2*y -1 if y != 0 else 2*range_of_y -1)
            representation_matrix_for_z[row_number,1] = ( 2* x) * 2*range_of_y + (2*y)
            representation_matrix_for_z[row_number,2] = ( 2* x) * 2*range_of_y + (2*y + 1)
            representation_matrix_for_z[row_number,3] = ( 2* x) * 2*range_of_y + (2*y + 2 if y != range_of_y -1 else 0)
            if ( y % 2 == 0 ):
                representation_matrix_for_z[row_number,4] = ( 2*x-1 if x != 0 else 2*range_of_x -1) * 2*range_of_y + (2*y -1 if y != 0 else 2*range_of_y -1)
                representation_matrix_for_z[row_number,5] = ( 2*x-1 if x != 0 else 2*range_of_x -1) * 2*range_of_y + (2*y)
                representation_matrix_for_z[row_number,6] = ( 2*x-1 if x != 0 else 2*range_of_x -1) * 2*range_of_y + (2*y + 1)
                representation_matrix_for_z[row_number,7] = ( 2*x-1 if x != 0 else 2*range_of_x -1) * 2*range_of_y + (2*y + 2 if y != range_of_y -1 else 0)
            else: 
                representation_matrix_for_z[row_number,4] = ( 2*x+1 ) * 2*range_of_y + (2*y -1 if y != 0 else 2*range_of_y -1)
                representation_matrix_for_z[row_number,5] = ( 2*x+1 ) * 2*range_of_y + (2*y)
                representation_matrix_for_z[row_number,6] = ( 2*x+1 ) * 2*range_of_y + (2*y + 1)
                representation_matrix_for_z[row_number,7] = ( 2*x+1 ) * 2*range_of_y + (2*y + 2 if y != range_of_y -1 else 0)
            
            row_number+= 1 
    
    Hz_matrix = np.zeros((no_of_checks_for_z,no_of_qubits))
    for i in range(representation_matrix_for_z.shape[0]):
        for j in range (representation_matrix_for_z.shape[1]):
            Hz_matrix[i,representation_matrix_for_z[i,j]] =1 
    return filtered_Hx_matrix, Hz_matrix

