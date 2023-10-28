
def find_repeat_val(usr_list):
    
    rep_ele_lst = []
    for j in range(1,len(usr_list)):
        cur_ele = usr_list[j]
        for i in range(j+1, len(usr_list)):
            nxt_ele = usr_list[i]
            if(cur_ele == nxt_ele):
                rep_ele_lst.append(cur_ele)
                break

    return print(rep_ele_lst)

def get_usr_lst():
    usr_list = [int(item) for item in input("Enter the list items : ").split()]
    print(usr_list)
    return(usr_list)
    
    
 # ----------------------------- Run this block of code for experiments and testing ---------------------
def exp_fun():
    print("THIS IS AN EXPERIMENTAL CODE")
    #----------------- Start your code from here -------------------
    print(len(usr_list))


usr_list = get_usr_lst()
find_repeat_val(usr_list)
# exp_fun()