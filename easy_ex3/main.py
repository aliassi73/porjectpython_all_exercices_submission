def fonct(my_list):
    first = my_list[0]       
    last = my_list[-1]   
    newlist = [first, last]
    return newlist          

# example 
a = [1, 3, 5, 7, 8, 9, 11]
result = fonct(a)
print(result)
