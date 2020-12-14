# try:
#     for i in ['a','b','c']:
#         print(i**2)
#     pass
# except:
#     pass
 

# try:
#     x = 5
#     y = 0

#     z = x/y
#     print (z)
#     pass
# except:
#     print ("Error")
#     pass
# finally:
#     print ("All Done")


def ask():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")
        print(val)
ask()