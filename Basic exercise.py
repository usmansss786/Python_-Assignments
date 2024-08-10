"""1. Simple Message:
 Assign a message to a variable and then print that message."""
Message: str = "how are you"
print(Message)
"""2. Simple Messages:
● Assign a message to a variable and print that message.
● Change the value of the variable to a new message, and print the new message."""
Name:str = "My name is Usman"
print (Name)
Name ="My father is Shamas"
print (Name)
"""3. Personal Message:
● Use a variable to represent a person’s name.
● Print a message to that person, such as, “Hello Eric, would you like to learn some
Python today?”"""
Person_Name:str = "Hamza"
print(f'hello {Person_Name}, would you like to learn some Python today')
"""4. Name Cases:
● Use a variable to represent a person’s name.
● Print the person’s name in lowercase, uppercase, and title case."""
person_Name:str = "Faizan"
print(person_Name.lower())
print(person_Name.upper())
print(person_Name.title())
"""5. Famous Quote:
● Find a quote from a famous person you admire.
● Print the quote and the name of its author.
The output should look something like the following:
Albert Einstein once said, “A person who never made a mistake never
tried anything new.”"""
Auther_name:str = "Allama Iqbal"
Quote="“Nations are born in the hearts of poets, they prosper and die in the hands of politicians.”"
print(f'{Auther_name} once said, {Quote}')
"""6. Famous Quote 2
Task:
● Use a variable called famous_person to represent the famous person’s name.
● Compose the message and represent it with a variable called message.
● Print the message."""
Famous_person:str="Irfan malik"
Message="would you like to meet me"
print(f'{Famous_person}, {Message}')
""" 7. Stripping Names
 Task:
 ● Use a variable to represent a person’s name, and include some whitespace characters
 at the beginning and end of the name.
 ● Makesureyou use each character combination, \t and \n, at least once.
 ● Print the name once, so the whitespace around the name is displayed.
 ● Print the name using each of the three stripping functions: lstrip(), rstrip(), and
 strip()"""
person_name:str="   Muhammad Usman    "
person_name1="\t\n Muhammad Usman \t\n"
print(person_name .lstrip())
print(person_name.rstrip())
print(person_name.strip())
print(person_name)

""" 8. Variable Sum
 Task: Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum"""
x:int =5
y:int =10
z:int =15
print(x+y+z)
""" 9. Variable Swap
 Task: Swap the values of two variables a and b. Print the values before and after the swap"""
a:int =5
b:int =10
print(f'value of a and b before swaping {a,b}')
Temp=a
a=b
b=Temp
print(f'value of a and b after swaping{a,b}')
""" 10. Favorite Color
 Task: Create a variable with your favorite color and print it. Then change the variable name to
 something else and print the color again"""

Favorite_color:str="Green"
print(Favorite_color)

Best_color=Favorite_color
print(Best_color)
"""Task: Create a variable pet_name and set it to "Buddy". Change the value of pet_name to
 "Max" and print the new value"""
pet_name:str="tommy"
print(pet_name)
pet_name="jack"
print(pet_name)
""" 12. Observing Name Error
 Task: Assign the value "Sunshine" to a variable and print it. Then, mistakenly try to print a
 variable with a different name (like sunsine) and observe the error"""
Nature:str="Sunshine"
#print(ntre) // NAme error

#print(Nature)
""" Task: Assign the value 100 to a variable score and print it. Then assign a new value to score
 and print it again"""
Score:int=100
print(Score)
Score=150
print(Score)
""" 14. City Name
 Task: Create a string variable city and assign it the name of a city you like. Print the city
 name."""
City_Name:str="Lahore"
print(City_Name)
""" 15. Title Case Text
 Task: Create a variable text with the value "python programming" and print it in title case"""
python_variable:str="  python programming  "
print(python_variable.title())
"""16. Lowercase Conversion
 Task: Assign a string with mixed cases to a variable and print it in all lowercase letters"""
Mixed_Variable:str="MuhAmMaD uSmAn"
print(Mixed_Variable.lower())
""" 17. Uppercase Conversion
 Task: Assign a string with mixed cases to a variable and print it in all uppercase letters."""
Mixed_Case:str="muhammad usman"
print(Mixed_Case.upper())
""" 18. Current Temperature
 Task: Create a variable temperature with the value 25. Print "The current temperature is
 [temperature] degrees." using the variable."""
Temperature:int=30
print(f"The current temperature is [temperature] degrees")
print(Temperature)
""" 19. Printing a Poem
 Task: Create a variable poem with a short poem that has multiple lines. Print the poem with
 each line starting on a new line."""
Short_Poem:str="""In the quiet of the night,\nStars above, a gentel light,\nDreams take flight, hearts unite\nWhispers of the moon, so bright."""

print(Short_Poem)






























































































 