"""
Username Function

Copeland’s Corporate Company has finalized what they want their username and temporary password 
creation to be and have enlisted your help, once again, to build the function to generate them. 
In this exercise, you will create two functions, username_generator and password_generator.

Let’s start with username_generator. Create a function called username_generator take two inputs, 
first_name and last_name and returns a user_name. The username should be a slice of the first 
three letters of their first name and the first four letters of their last name. 
If their first name is less than three letters or their last name is less than four letters 
it should use their entire names.

Password Function

Now for the temporary password, they want the function to take the input user name and 
shift all of the letters by one to the right, so the last letter of the username ends up 
as the first letter and so forth. For example, if the username is AbeSimp, 
then the temporary password generated should be pAbeSim.
"""

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
