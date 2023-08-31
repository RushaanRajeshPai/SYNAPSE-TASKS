import random

lst = ['0001', '0011', '0101', '1011']
new_lst = [int(i, base=2) for i in lst]
least_difference_new_lst = sorted([int(i, base=2) for i in lst]) 

while len(new_lst) > 2:
    index = random.sample(range(len(new_lst)), 2)
    i, j = index
    
    temp = new_lst[i] + new_lst[j]
    temp_least = least_difference_new_lst[0] + least_difference_new_lst[1]
    
    del new_lst[max(i, j)]
    del new_lst[min(i, j)]
    least_difference_new_lst.pop(0)
    least_difference_new_lst.pop(0)

    
print(new_lst)
print(least_difference_new_lst)
