# # Check if number is odd or even
# odd_even_number = int(input("Enter a number: "))

# if odd_even_number % 2 == 0:
#     print(f"{odd_even_number} is EVEN!")
# else:
#     print(f"{odd_even_number} is ODD!")

# # Print numbers 1 to 10
# print("\nPrinting numbers 1 to 10:")
# for num in range(1, 11):
#     print(num)

# # Name input loop
# print("\nEnter names (type 'exit' to quit):")
# name = ""
# while name != "exit":
#     name = input("Enter your name: ")
#     if name != "exit":
#         print(f"Hello, {name}!")

# # # *** My First Python Code With Mosh *** #
# # # print("Hello World")
# # # student_count = 1000
# # # print(student_count)
# # # course = "Python Course"
# # # print(len(course))
# # # print(course[0:3])

# # #age = int(input("Enter UR age: "))
# # #message = "U can enter!" if age >= 18 else "NO enter!!"
# # #print(message)

# # #f_name = input("Enter UR name: ")
# # #l_name = input("Enter UR last name: ")
# # #print(f"UR name is {f_name} & UR last name is {l_name} \nU R {age} years old")


# # # *** if Statement
# # #if len(f_name) >= 8:
# # #    print("Wow! Such long name!")
# # #elif 5 < len(f_name) < 8:
# # #    print("Nice name")
# # #else:
# # #    print("OMG!!")

# # # Nested Loops

# # # for x in range(5):
# # #   for y in range(3):
# # #     print(f"({x}, {y})")

# # # passcode = ""

# # # while passcode != "1234":
# # #   passcode = input("Enter UR pass: ")
# # # print(f"UR passcode is {passcode}!")


# # # i = 1
# # # while i <= 5:
# # #     print(i)
# # #     i += 1
# # # count = 0
# # # for i in range(1, 10):
# # #   if i % 2 == 0:
# # #     count += 1
# # #     print(i)
# # # print(f"we have {count} even nambers")

# # # age = int(input("Enter UR age: "))
# # # if age > 18:
# # #  print(f"Wow!")
# # # elif 15 <=  age <= 18:
# # #   print (f"Hmm!")
# # # else:
# # #  print(f"Hahaha")

# # def get_greeting(name = "guest"):
# #   return f"Hi {name}"

# # message = get_greeting("Ali")

# # print(message)


# # #message = get_greeting("Ali")
# # #print(message)

# # #file = open("content.txt", "w")
# # #file.write(message)

# # #f_name = input("enter your name")
# # #l_name = input("enter your last name")

# # #def con_to_fullname(f_name, l_name):
# #  # return f"your full name is {f_name} {l_name}"

# # #fullname = con_to_fullname(f_name , l_name)

# # #print(fullname)


# # def multiply(*numbers):

# #   total = 1

# #   for number in numbers:
# #     total *= number
# #     print(total)

# # (multiply(2, 3, 4, 5))

# # Keep asking the user for their name until they type "exit"

# while True:
#     name = input("Enter your name: ")
#     if name == "exit":
#         break
#     print(f"Hello, {name}!")

numbers_list = [1, 2, 3, 4, 5]
matrix = [0] * 10

# print(matrix)


# def save_user(a, b, **user):
#     # print(a, b, user['id'])


# save_user(1, 2, id=4)

items = [1, 'a']
first, second = items

print(first, second)


numbers = [1, 2, 3, 5, 56]
num1, num2, *num3 = numbers

print(num1, num3)
