#-----------------------------------------------------------
#Description -  Logic to find the repeated number form the
#               user defined list
#-----------------------------------------------------------
def find_repeat_val(usr_list):
    
    rep_ele_lst = []    #list of repeated elements 
    for j in range(0,len(usr_list)):
        cur_ele = usr_list[j]
        for i in range(j+1, len(usr_list)):
            nxt_ele = usr_list[i]
            if(cur_ele == nxt_ele):
                rep_ele_lst.append(cur_ele)
                break

    return print(rep_ele_lst)

#----------------------------------------------------------------
#Description -  This function take a sequence of number from 
#               user and make it into a list separated by space.
#----------------------------------------------------------------
def get_usr_lst():

    usr_list = [int(item) for item in input("Enter the list items : ").split()]
    print(usr_list)

    return(usr_list)
    

# --------------------------------------------------
#Description - This is a function used for experimental 
#              and testing purposes code inside this function
#              will not affect the main logic of 
#---------------------------------------------------
def exp_fun():
    print("THIS IS AN EXPERIMENTAL CODE")
    #---Start your code from here------- 
    print(len(usr_list))


#---------------------- MAIN  ---------------------------
usr_list = get_usr_lst()
find_repeat_val(usr_list)
# exp_fun()