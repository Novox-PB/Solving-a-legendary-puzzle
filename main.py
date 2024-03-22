from itertools import permutations

def combine_integers_list(lst_int_a, lst_int_b):
    return int(str(lst_int_a) + str(lst_int_b))

perm_lst = list(permutations([1,2,3,4,5,6,7,8,9])) 

for lst in perm_lst:
    combined_int = combine_integers_list(lst[0],lst[1])

    if combined_int * lst[2] < 100:

        if list(map(int,list(str(combined_int * lst[2])))) == list(lst[3:5]):
            
            if combine_integers_list(lst[3],lst[4]) + combine_integers_list(lst[5],lst[6]) == combine_integers_list(lst[7],lst[8]):
                
                print(lst)
  
    

