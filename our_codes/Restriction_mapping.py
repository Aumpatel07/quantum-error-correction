import numpy as np 

def mapping_syndrome_from_colour_code_to_two_edge_augmented_surface_codes(H_colour_code,H_edge_augmented_surface_code,original_syndrome):
    syndrome1 = np.zeros(H_edge_augmented_surface_code.shape[0],dtype=int)
    syndrome2 = np.zeros(H_edge_augmented_surface_code.shape[0],dtype=int)

    range_of_y = int(np.sqrt(2 * H_colour_code.shape[0])) 
    range_of_x = range_of_y // 2 

    #variables to help implementation
    x1 = 1 
    y1=  1 
    rownumber = 0 

    for x in range(range_of_x):
        for y in range(range_of_y):

            if (  y % 2 == 0 and x >= range_of_x // 2 ): continue

            y1 = ((y + 2) if (y+2) < range_of_y else y + 2 - range_of_y) 

            if( y%2 == 1 ): 
                x1 =x 
                syndrome1[rownumber]=original_syndrome[x1* range_of_y + y1]
                syndrome2[rownumber]=original_syndrome[(x1-1 if x1 != 0 else range_of_x-1) * range_of_y + y1]
            
            elif ( y % 4 == 0):
                x1 = 2*x +1 
                syndrome1[rownumber]=original_syndrome[x1* range_of_y + y1]
                syndrome2[rownumber]=original_syndrome[(x1 -1) * range_of_y + y1]
                
            else:
                x1 = 2*x 
                syndrome1[rownumber]=original_syndrome[x1* range_of_y + y1]
                syndrome2[rownumber]=original_syndrome[(x1 -1 if x1 != 0 else range_of_x-1)* range_of_y + y1]

            rownumber += 1 

    return syndrome1, syndrome2


# to test this function, try running the below code
# with out defination of order, order x color code will be mapped to order  x - 1  edge augmented surface code

# from automated_H_generation_for_surface_code import edge_augmentated_H_matrix
# from automated_H_genreration_for_colour_codes import H_matrix_generation

# order = 2
# H_colour_code,H1 = H_matrix_generation(order_of_codes= order)
# H_edge_augmented_surface_code,H2 = edge_augmentated_H_matrix(order_of_codes= order -1) 

# original_syndrome =  np.random.choice([0, 1], size=(H_colour_code.shape[0]))
# print(original_syndrome)
# print(mapping_syndrome_from_colour_code_to_two_edge_augmented_surface_codes(H_colour_code,H_edge_augmented_surface_code,original_syndrome))




def mapping_error_on_qubits_of_two_edge_augmented_surface_codes_to_error_in_colour_codes(H_colour_code,H_edge_augmented_surface_code,error1,error2):

    two_power_order_of_codes = int(np.sqrt(2*H_colour_code.shape[0]))

    range_of_y = 3 * (two_power_order_of_codes // 2 )
    range_of_x = two_power_order_of_codes

    error_in_colour_code = np.full(range_of_x*range_of_y,-1,dtype=int)

    range_of_y_for_surface_codes = two_power_order_of_codes
    range_of_x_for_surface_codes = two_power_order_of_codes // 2 
    
    #we need to iterate x over only half its values
    r1 = range_of_x // 2
    for x in range(r1):
        for y in range(0,range_of_y,3): 

            #checking for even errors on the edges of a color code latice
            k = 0 
            k = error1[x * range_of_y_for_surface_codes + ((y//3)*2)]
            k += error1[x * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]
            k += error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + ((y//3)*2)]
            k += error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]
            if ( k  % 2 !=  0 ): print("not even")  


            if ( (y // 3)  % 2 == 0 ):
                if ( x % 2 == 0 ): 
                    error_in_colour_code[x * range_of_y + y] =1
                    error_in_colour_code[(2* x) * range_of_y + y + 1]=(error1[x * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2 
                    error_in_colour_code[(2* x  +1) * range_of_y + y + 1]=(error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2  
                    error_in_colour_code[(x) * range_of_y + y + 2]=(error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + ((y//3)*2)]  + error_in_colour_code[(2* x) * range_of_y + y + 1]) % 2 

                else:
                    error_in_colour_code[x * range_of_y + y] =1
                    error_in_colour_code[(2* x) * range_of_y + y + 1]=(error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2 
                    error_in_colour_code[(2* x  +1) * range_of_y + y + 1]=(error1[x * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2  
                    error_in_colour_code[(x) * range_of_y + y + 2]=(error1[x * range_of_y_for_surface_codes + ((y//3)*2)]  + error_in_colour_code[(2* x) * range_of_y + y + 1]) % 2 
                    
            
            else:
                if ( x % 2 != 0 ): 
                    error_in_colour_code[x * range_of_y + y] =1
                    error_in_colour_code[(2* x) * range_of_y + y + 1]=(error1[x * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2 
                    error_in_colour_code[(2* x  +1) * range_of_y + y + 1]=(error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2  
                    error_in_colour_code[(x) * range_of_y + y + 2]=(error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + ((y//3)*2)]  + error_in_colour_code[(2* x) * range_of_y + y + 1]) % 2 

                else:
                    error_in_colour_code[x * range_of_y + y] =1
                    error_in_colour_code[(2* x) * range_of_y + y + 1]=(error2[((x+1) if x + 1 != range_of_x_for_surface_codes else 0) * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2 
                    error_in_colour_code[(2* x  +1) * range_of_y + y + 1]=(error1[x * range_of_y_for_surface_codes + (((y//3)*2 - 1) if (y//3)*2 != 0 else range_of_y_for_surface_codes -1)]  + 1 ) % 2  
                    error_in_colour_code[(x) * range_of_y + y + 2]=(error1[x * range_of_y_for_surface_codes + ((y//3)*2)]  + error_in_colour_code[(2* x) * range_of_y + y + 1]) % 2 
                    
    filtered_error_in_colour_code= error_in_colour_code[error_in_colour_code != -1]

    return filtered_error_in_colour_code




def mapping_syndrome_from_edge_augmented_surface_codes_to_normal_surface_codes(H_edge_augmented,H_normal,syndrome):

    estimated_error = np.zeros(H_edge_augmented.shape[1],dtype=int)
    qubits_with_half_probability = np.zeros(H_normal.shape[1],dtype=int)
    new_syndrome = np.zeros(H_normal.shape[0],dtype= int)

    two_power_order_of_codes = int(np.sqrt(H_edge_augmented.shape[1] // 2)) 
    range_of_y_for_edge_augmented = 2 * two_power_order_of_codes
    range_of_x_for_edge_augmented = two_power_order_of_codes

    range_of_x_for_normal = two_power_order_of_codes //2
    range_of_y_for_normal = two_power_order_of_codes
    
    row_number = 0 

    for x in range(range_of_x_for_edge_augmented):
        for y in range(range_of_y_for_edge_augmented):
                if (y % 2 == 0 and x >= range_of_x_for_edge_augmented//2): continue

                if ( y % 2== 0 ):
                    new_syndrome[x * range_of_y_for_normal + (y //2)] = syndrome[row_number]
                
                row_number += 1 


    row_number = 0 

    for x in range(range_of_x_for_edge_augmented):
        for y in range(range_of_y_for_edge_augmented):
            if ( y % 2 == 0 and x >= range_of_x_for_edge_augmented//2): continue

            if ( y % 2 == 0 ):
                row_number += 1 
                continue

            if ( syndrome[row_number] == 1 ):
                
                estimated_error[x * range_of_y_for_edge_augmented + y]= 1  

                qubits_with_half_probability[x * range_of_y_for_normal + ( (y + 1) // 2 if y != range_of_y_for_edge_augmented -1 else 0)] = 1

                if ( (y -1) % 4  == 0 ):
                    new_syndrome[ ((x // 2) if x % 2 == 0 else ((x-1)//2) )  * range_of_y_for_normal + ((y - 1) //2)]  += 1
                    new_syndrome[ ((x // 2) if x % 2 == 0 else ((x-1)//2) )  * range_of_y_for_normal + ((y - 1) //2)]  %= 2

                else:
                    new_syndrome[ ((x // 2) if x % 2 == 0 else ( ((x+1)//2) if ((x+1)//2) != range_of_x_for_normal else 0) )  * range_of_y_for_normal + ((y - 1) //2)]  += 1
                    new_syndrome[ ((x // 2) if x % 2 == 0 else ( ((x+1)//2) if ((x+1)//2) != range_of_x_for_normal else 0) )  * range_of_y_for_normal + ((y - 1) //2)]  %= 2
            
            row_number+=1
    
    return new_syndrome,estimated_error,qubits_with_half_probability
                

#to test the above function 
# from automated_H_generation_for_surface_code import H_matrix_generation,edge_augmentated_H_matrix
# order = 1
# H1,hh = edge_augmentated_H_matrix(order)
# H2,hhhs= H_matrix_generation(order)
# syndrome = np.random.choice([0, 1],H1.shape[0])
# mapping_syndrome_from_edge_augmented_surface_codes_to_normal_surface_codes(H1,H2,syndrome)






def mapping_error_from_normal_surface_codes_to_edge_augmented(H_edge_augmented,H_normal,error):

    new_error = np.zeros(H_edge_augmented.shape[1],dtype=int)
    
    two_power_order_of_codes = int(np.sqrt(H_edge_augmented.shape[1] // 2)) 
    range_of_y_for_edge_augmented = 2 * two_power_order_of_codes
    range_of_x_for_edge_augmented = two_power_order_of_codes

    range_of_x_for_normal = two_power_order_of_codes 
    range_of_y_for_normal = two_power_order_of_codes

    for x in range(range_of_x_for_normal):
        for y in range(range_of_y_for_normal):
            if ( error[x * range_of_y_for_normal + y ] == 1):
                new_error[x * range_of_y_for_edge_augmented  + (2* y)] = 1
                new_error[x * range_of_y_for_edge_augmented  + ((2* y - 1) if y!= 0 else range_of_y_for_edge_augmented -1)] = 1

    return new_error


# to test the above function 
# from automated_H_generation_for_surface_code import H_matrix_generation,edge_augmentated_H_matrix
# order = 1
# H1,hh = edge_augmentated_H_matrix(order)
# H2,hhhs= H_matrix_generation(order)
# error = np.random.choice([0, 1],H2.shape[1])
# mapping_error_from_normal_surface_codes_to_edge_augmented(H1,H2,error)