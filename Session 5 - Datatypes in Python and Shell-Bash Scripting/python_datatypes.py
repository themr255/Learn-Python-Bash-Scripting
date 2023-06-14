# Title: Datatypes in Python

# int (Integer): Represents whole numbers without any fractional part. 

print("-----------------------------------------------------------------------------------")
print("\n***************** Examples for Integer Datatype *****************\n")

age = 25
print("Datatype for age variable: {}\n".format(type(age)))
print("Age: {}".format(age))

num_students = 30
print("\nNumber of Students: {}".format(num_students))

print("\n-----------------------------------------------------------------------------------\n")

# str (String) : Represents a sequence of characters enclosed in single quotes (' ') or double quotes (" ").

print("***************** Examples for String Datatype *****************\n")

name = "John Doe"
print("Datatype for name variable: {}".format(type(name)))
print("Name: {}".format(name))

message = "Welcome to our website!"
print("\nMessage: {}".format(message))

print("\n-----------------------------------------------------------------------------------\n")

# bool (Boolean): Represents either True or False. It is used in logical operations and conditional statements.

print("***************** Examples for Boolean Datatype *****************\n")

is_logged_in = True
print("Datatype for is_logged_in variable: {}".format(type(is_logged_in)))
print("is_logged_in: {}".format(is_logged_in))

is_valid = False
print("\nis_valid: {}".format(is_valid))

print("\n-----------------------------------------------------------------------------------\n")

# list (List): Represents an ordered collection of items enclosed in square brackets ([]). The items can be of different data types.

print("***************** Examples for List Datatype *****************\n")

shopping_list = ['apples', 'bananas', 'milk']
print("Datatype for shopping_list variable: {}".format(type(shopping_list)))
print("Shopping List: {}".format(shopping_list))

grades = [90, 85, 95]
print("\nGrades: {}".format(grades))

print("\n-----------------------------------------------------------------------------------\n")

# tuple (Tuple): Similar to a list, but it is immutable, meaning its elements cannot be changed after creation. It is represented by items enclosed in parentheses (()).

print("***************** Examples for Tuple Datatype *****************\n")

point = (2, 5)
print("Datatype for point variable: {}".format(type(point)))
print("Point: {}".format(point))

color = (255, 0, 0)
print("\nColor: {}".format(color))

print("\n-----------------------------------------------------------------------------------\n")

# dict (Dictionary): Represents a collection of key-value pairs enclosed in curly braces ({ }). Each key is unique and associated with a value. 

print("***************** Examples for Dictionary Datatype *****************\n")

person = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Datatype for person variable: {}".format(type(person)))
print("Person: {}".format(person))

product = {'name': 'Phone', 'price': 599, 'brand': 'Apple'}
print("\nProduct: {}".format(product))

print("\n-----------------------------------------------------------------------------------\n")

# set (Set): Represents an unordered collection of unique elements. It is enclosed in curly braces ({ }).

print("***************** Examples for Set Datatype *****************\n")

email_set = {'user1@example.com', 'user2@example.com', 'user3@example.com'}
print("Datatype for email_set variable: {}".format(type(email_set)))
print("email_set: {}".format(email_set))

tags = {'python', 'programming', 'tutorial'}
print("\nTags: {}".format(tags))

print("\n-----------------------------------------------------------------------------------\n")
