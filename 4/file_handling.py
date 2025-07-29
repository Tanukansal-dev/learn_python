# # types-
# #text files- .txt, .docx, .log etc.
# # binary files- .mp4, .mov, .png, .jpeg etc.
#
# f = open("demo.txt","r")
# # data = f.read()          for all data
# # data = f.read(5)
# # print(data)
# # print(type(data))
# # f.close()
#
# line1 = f.readline()        # line by line
# print(line1)
#
#
# line2 = f.readline()
# print(line2)
#
#
# # writing to a file -
# file = open("demo.txt","w")
# file.write("i want to write something.123")
# file.close()
#
# file = open("demo.txt","a")               # add
# file.write(" adding these no..123")
#
#
#
# f = open("demo.txt","r+")       #read,over write-- no truncate
# f.write("abc")
# print(f.read())
# f.close()
#
# f = open("demo.txt","w+")       #read,over write-- truncate
# f.write("abc")
# print(f.read())
# f.close()
                                #read, append-- no truncate


# with syntax-

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
#
# with open("demo.txt","w") as f:
#     f.write("new data")



# deleting a file -

# import os
# os.remove("sample.txt")



# example-

# with open("example.txt","w") as f:
#     f.write("hi everyone java\nwe are write something java.")


with open("example.txt", "r") as f:
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("example.txt", "w") as f:
    f.write(new_data)




# file me something hai ya nahi --find



word = "something"
with open("example.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")




# ................

file = open("new.txt", "w")
file.write("this is my first statement.\n")
file.write("this is my first statement.\n")
file.write("this is my first statement.\n")
file.write("this is my first statement.\n")
file.write("this is my first statement.\n")
file.close()
print("completed")



file = open("new.txt", "r")
# print(file.read())
print(file.readline())
file.close()



file = open("new.txt", "a")
file.write("sixth line \n")
file.write("seven line\n")
file.close()
print("complete")