
# *** My First Python Code With Mosh *** #
# print("Hello World")
# student_count = 1000
# print(student_count)
# course = "Python Course"
# print(len(course))
# print(course[0:3])

#age = int(input("Enter UR age: "))
#message = "U can enter!" if age >= 18 else "NO enter!!"
#print(message)

#f_name = input("Enter UR name: ")
#l_name = input("Enter UR last name: ")
#print(f"UR name is {f_name} & UR last name is {l_name} \nU R {age} years old")


# *** if Statement 
#if len(f_name) >= 8:
#    print("Wow! Such long name!")
#elif 5 < len(f_name) < 8:
#    print("Nice name")
#else:
#    print("OMG!!")

# Nested Loops

# for x in range(5):
#   for y in range(3):
#     print(f"({x}, {y})")

# passcode = ""

# while passcode != "1234":
#   passcode = input("Enter UR pass: ")
# print(f"UR passcode is {passcode}!")



# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# count = 0
# for i in range(1, 10):
#   if i % 2 == 0:
#     count += 1
#     print(i)
# print(f"we have {count} even nambers")

# age = int(input("Enter UR age: "))
# if age > 18:
#  print(f"Wow!")
# elif 15 <=  age <= 18:
#   print (f"Hmm!")
# else:
#  print(f"Hahaha")

def get_greeting(name = "guest"):
  return f"Hi {name}"

message = get_greeting("Ali")
print(message)


#message = get_greeting("Ali")
#print(message)

#file = open("content.txt", "w")
#file.write(message)

