"====== QUESTION 01 FIND THE LARGEST NUMBER IN LIST ===== "
# numbers = [5,7,3,6,8]

# largest = numbers[3]  # pehle element ko maan lo largest

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest number is:", largest)

"======= QUESTION 02 sum values in list ======"


# numbers = [5,7,3,6,8]

# total = numbers[0]+numbers[1]+numbers[2]+numbers[3]+numbers[4]
# print("Total numbers",total)

"======= QUESTION 03 create a list of 5 int number and print it all with different different way ===="

# nums = [10,20,30,40,50]
# print(nums)
# print(f"number1:", nums[0])
# print(f"number1:", nums[1])
# print(f"number1:", nums[2])
# print(f"number1:", nums[3])
# print(f"number1:", nums[4])

"=====QUESTION 04 ACCESS THE FIRST,LAST, AND LAST ELEMENT OF A LIST====="

# num = [1,2,3,4,5]

# print(num[0])
# print(num[2])
# print(num[-1])


"===== QUESTION 05 find the length of a list and Tuple====="

# num = [1,2,3,4]
# print(len(num))

# num = (1,2,3,4)
# print(len(num))
# print(type(num))

"=====QUESTION 06 add the element in the end of a list====="
# num = [1,2,3]
# num.append(4)
# print(num)

"=====QUESTION 07 check whether an element in a list===="

# num = [1,2,3]
# if 2 in num:
#     print("yes")
# else:
#     print("no")

"======QUESTION 08 remove an element from a list======"

# num = [1,2,3]
# num.remove(2)
# print(num)

"=======QUESTION 09 find the maximum and minimum num in list===="

# numbers = [1, 4, 2, 5, 8]

# maximum = numbers[0]
# minimum = numbers[0]

# for num in numbers:
#     if num > maximum:
#         maximum = num
#     if num < minimum:
#         minimum = num

# print("Maximum number is:", maximum)
# print("Minimum number is:", minimum)

"=====QUESTION NUMBER 10 create a tuple with one element===="

# num = (12,)
# print(num)
# print(type(num))

"======QUESTION NUMBER 11 find the average of numbers in list====="

# num = [1,2,3,4]
# average = (num[0]+num[1]+num[2]+num[3]) / 4
# print(average)

"=====QUESTION NUMBER 12 reverse a list without using reverse====="

# num = [1,2,3,4]
# print(num[::-1])

"=====QUESTION NUMBER 13 sort a list in ascending order and descending order===="

# num = [1,2,5,3,7]
# num.sort(reverse=True)
# print(num)

"====QUESTION NUMBER 14 count how many times an element from a list====" 

# num = [1,2,2,3,4,5]
# print(num.count(3))


" =====QUESTION NUMBER 15 remove a duplicate element from a list===="
# num = [1,2,2,3,4]
# num = list(set(num))
# print(num)

"======QUESTION NUMBER 16 Find the second largest num in list===="

# num = [1, 2, 3, 4]

# num = list(set(num))  # duplicates remove
# num.sort()            # ascending order

# print("Second largest:", num[-2])

"=====QUESTION NUMBER 18 merge two list in one===="

# num1 = [1,2,3,4]
# num2 = [5,6,8,9]
# merged = num1 + num2
# print(merged)

"=====QUESTION NUMBER= 19 convert a list into a Tuple===="

# num = [1,2,3,4]
# num_tuple = tuple(num)
# print(num_tuple)
