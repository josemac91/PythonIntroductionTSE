# Exercise 1)

number_list = [8, 2, 3]
print(sorted(number_list))
print(len(number_list))

if len(number_list) < 1:
    return number_list
if len(number_list) % 2 == 0:
    return float(sum(len(sorted(number_list))/2 - 1 : len(sorted(number_list))/2 + 1)))
else:
    return 1

# see solutions

# Exercise 2)

# see solutions

