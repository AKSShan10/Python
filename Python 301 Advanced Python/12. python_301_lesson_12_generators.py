def my_generator():
    for num in range(14):
        #print(num)
        #return num**num
        yield num**num  #yield?

# total = my_generator()
# print(total)
all_numbers = list(my_generator())
print(all_numbers)

# for big_num in my_generator():
#     print(big_num)