#!/bin/bash

# Title: Datatypes in Bash

# int (Integer): Represents whole numbers without any fractional part. 

printf -- "-----------------------------------------------------------------------------------"
printf "\n\n***************** Examples for Integer Datatype *****************\n\n"

age=25
printf "Age: ${age}"

num_students=30
printf "\nNumber of Students: ${num_students}"

printf -- "\n\n-----------------------------------------------------------------------------------\n"

# str (String) : Represents a sequence of characters enclosed in single quotes (' ') or double quotes (" ").

printf "\n***************** Examples for String Datatype *****************\n\n"

name="John Doe"
printf "Name: ${name}"

message="Welcome to our website!"
printf "\nMessage: ${message}"

printf -- "\n\n-----------------------------------------------------------------------------------\n"

# bool (Boolean): Represents either True or False. It is used in logical operations and conditional statements.

printf "\n***************** Examples for Boolean Datatype *****************\n\n"

is_logged_in=True
printf "is_logged_in: ${is_logged_in}"

is_valid=False
printf "\nis_valid: ${is_valid}"

printf -- "\n\n-----------------------------------------------------------------------------------\n"

# array (Arrays): Collections of elements stored in a single variable. Arrays in Bash can contain both strings and integers. You can access individual elements using their indices or iterate over the entire array. 

printf "\n***************** Examples for Array Datatype *****************\n\n"

# shopping_list[*] for printing all elements of shopping_list

shopping_list=("apples", "bananas", "milk")
printf "Shopping List: ${shopping_list[*]}"

grades=(90, 85, 95)
printf "\nGrades: ${grades[*]}"

printf -- "\n\n-----------------------------------------------------------------------------------\n"

# Dictionary (Associative Array): An associative array called dictionary with key-value pairs. 

printf "\n***************** Examples for Dictionary (Associative Array) Datatype *****************\n\n"

declare -A person
person["name"]="John"
person["age"]=30
person["city"]="New York"

printf "Person: "
declare -p person

printf "\nPerson Name: ${person["name"]}\n\n"

declare -A product
product["name"]="Phone"
product["price"]=599
product["brand"]="Apple"

printf "Product: "
declare -p product

printf "\nProduct Brand: ${product["brand"]}"

printf -- "\n\n-----------------------------------------------------------------------------------\n"