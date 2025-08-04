"""reading files older method you need to close the file"""
# f= open("files/file.txt","r")
# print(f.readline())
# print(f.readlines())
# f.close()


# """new method you do not need to close the file"""
with open("files/filex.txt","r+") as file:
    file.write("Hello my name is Yubek Shrestha.")
    print("written file")
    file.seek(0)
    print(file.read(10))
    # file.seek(0)
    print(file.read())
    # print(file.read())

# import os

# print(os.listdir("files/"))
# if os.path.exists("files/filex6iuk,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  9 .txt"):
#     os.remove("files/filex.txt")
    
# with open("files/filex.txt","w+") as file:
#     pass


# if "newdir" in os.listdir("."):
#     pass
# else:
#     os.mkdir("newdir")
    
# with open("newdir/newfile.txt","w") as file:
#     pass

# if len(os.listdir("newdir"))!=0:
#     print(os.listdir("newdir"))
#     for file in os.listdir("newdir"):
#         os.remove("newdir/"+file)
# os.rmdir("newdir")