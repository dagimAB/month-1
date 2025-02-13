


# Write a function that sums numbers in a list.

lists = [4, 6, 3, 8, 5,9]

def sum_list(lists):
    sum = 0
    for x in lists:
        sum += x

    return sum

sums = sum_list(lists)

print(f"the sum is: {sums}")



# Print even numbers between 1 and 20 using a loop.

for x in range(1,21):
    if x % 2 == 0:
        print(x)




# Write a program to find the largest number in a list.

lists2 = [2, 4, 8, 9, 5, 6]

largest = lists2[0]

for x in lists2:
    if largest < x:
        largest = x

print(f"The largest number is: {largest}")
