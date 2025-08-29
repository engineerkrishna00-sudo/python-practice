
#SINCE I ALREADY KNOW THE BASICS AND BASIC FUNCTIONS I AM JUST CODING SOMETHING THAT I FOUND NEW.
# strings are immutable. meaning you cannot change an existing string by using any functon.
# these functions will create a new string without changing anything into the existing string 
 
# 1) using string_name.replace() function

letter=(""" Dear krish
 You are selected
 date""") 
print(letter.replace("krish","Pawan").replace("date","23-09-2025"))

# 2)Removing double spaces from strings using strip() function

str="Krishna  is  an  eager  coder  ."
print(str.strip()) #you can do the same thing using replace() function

# 3)to find the index of a given string.

str="Krishna is an eager coder ."
print(str.find("an"))

#4) to count number of spaces

str="Krishna is an eager coder ."
count=0
for i in range(0,len(str)):
    if(str[i]==" "):
        count+=1

if(count==0):
    print("no spaces found.")
else:
    print(count)

# usage of casefold() function: its more aggresive than .lower()
# as it can also lowers the special characters
name="Krishna MITTAL"
print(name.casefold())    
