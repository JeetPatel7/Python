# it is key : value pair

details = {
        "name" : "john stone",
        "age"  : 28,
        "phone" : 1282402740
        }

print(details["name"])
# print(details["city"]) ---> it will key key error

print(details.get("name"))

print(details.get("birthdate")) # ----> it will return none value because Birthdate is not defined


 # I can assign the default value of birthdate in the print bracket
 # if no value is assigned to the birthdate the it will assign the default value.......
print(details.get("birthdate" ,"01 jan 2000"))


