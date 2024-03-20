def area(base, height):
    a = base* height 
    return a

if __name__ == "__main__":

    #This line means that __name__ is a predefined variable that calls the main function __main__ 
    #This also means that __name__ can signify the filename.py

    ar = area(10,15)
    print(ar)

    #if we print(__name__ in this file, it iwll alwyas pooint to main), but if we do it in another file, That file will be set to the name of the file called 
    