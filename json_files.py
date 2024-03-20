#JSON - JavaScriptObjectNotation

#Format of data exchange similar to XML

#JSON Example

'''
{
    "name:"tom",
   "address":"green street,NY",
    "phno": "12345678"
}
'''

#XML Example

'''
<name>tom</name>


'''

#Difference b/w JSON and XML

#1.JSON is more lightweight than XML

#Lets perform a json  program


book = {}

book['Ashton'] = {
    "name":"Ashton",
    "age":20,
    "college": "SJEC"
}
book['Samuel'] = {
    "name": "Samuel",
    "age":21,
    "college": "SJHC"
}

import json

s = json.dumps(book) #Dumps the entire json into a string
with open(r"C:\Users\Ashton\Desktop\CodeBasics\new.txt","w") as f: #Use r'' to avoid conflict of backslash as it can be used as an escape character in python
    f.write(s)
# f = open(r"C:\Users\Ashton\Desktop\CodeBasics\new.txt","r")
# s = f.read() #This will give a string

# book = json.load(s) #This will give a dictionary


