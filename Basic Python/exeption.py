#An exception is an error that occurs during execution of a program

# We can handle exceptions using try: except:

a = int(input("Enter a number:"))
b = int(input("Enter a number b: "))

try:
    z = a/b

except Exception as e:
    print("Exception has occured",e)
    z = None

print("z :", z) #Will print None if exception occured and will print result if no exception occured