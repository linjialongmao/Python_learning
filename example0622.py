# coding=utf-8

# delete a integer's factoring

# inout a string
num_num = raw_input('enter a number: ')

# translate the inout to int
num = int(num_num)

# get the list
fac_list = range(1, num+1)
print 'before', fac_list


for i in range(1, num+1):
    if num % i == 0:
        fac_list.remove(i)

print 'after', fac_list
