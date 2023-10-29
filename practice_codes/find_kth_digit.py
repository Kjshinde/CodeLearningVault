#-----------------------------------------------------------------------
#   Date        :-  30/10/2023  
#   Author      :-  Krutyanjay Shinde  
#   Description :-  Finding the kth digit of a number number
#------------------------------------------------------------------------

def get_num():
   
    inp_num = input("Enter the number :-  ")
    k_pos = input("Which position you want to find out  :-  ")
    num_len = len(inp_num)
    inp_val_lst = [inp_num,k_pos,num_len]
    return inp_val_lst
    

def find_k_pos(inp_num,k_pos,num_len):
    inp_num_int = int(inp_num)  #converting the input number into an integer
    k_pos_int = int(k_pos)      #converting the position value to integer
    num_len_int = int(num_len)  #converting the length of number into an integer
    print("length of number entered = ",num_len_int)

    #logic to find the kth position from right starting from 1
    ttl_dig_val = 10 ** num_len_int 
    mod_val = 10 ** (k_pos_int - 1) 

    div_val = ttl_dig_val / mod_val

    val_at_k = inp_num_int % div_val
    str_val_at_k = str(val_at_k)
    final_val = str_val_at_k[0]
    print(final_val)




inp_val_lst = get_num()
inp_num = inp_val_lst[0]
k_pos = inp_val_lst[1]
num_len = inp_val_lst[2]
find_k_pos(inp_num,k_pos,num_len)