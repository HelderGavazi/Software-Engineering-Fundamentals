"""
hyperiondev - Software Engineering (Fundamentals)
Task 8 - "IO Operations"
Author: Helder P - HP24010013265
Date: 27/03/2024

Practical Task 1 - "dob_task.py"
"""
import os.path as path
import pandas as pd

# # Read the data from the text file into a DataFrame
# df = pd.read_csv('DOB.txt', header=None, names=['Name', 'Birthdate'])

# # Print the 'Name' section
# print("Name")
# print(df['Name'].to_string(index=False))

# # Print a newline for separation
# print()

# # Print the 'Birthdate' section
# print("Birthdate")
# print(df['Birthdate'].to_string(index=False))



# Define the path to the text file
#fileName = ("dob_1.txt")

# Open the text file in read mode
f = open("dod_1.txt", "r+")
    # Read the entire contents of the file
content = f.read()
    # Print the content
print(content)
