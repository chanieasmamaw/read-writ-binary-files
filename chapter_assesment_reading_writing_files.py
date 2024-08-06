"""
########################################### 10.1.1 #####################################################################
1. Search and Replace
Create a program to perform a simple search and replace process on a filename.

The program will ask the user for input filename, and 2 words. It will then create a new file, with an added extension
 “.new” (for example, if original filename was info.txt, the program will create info.txt.new). In the new file, all of
  the occurences of the first word will be replaced by the second word.
"""

# Get user input
file_name = input("Enter the file name: ")
two_words = input("Enter two words: ")

# Write user input to the file
with open(file_name + '.txt.new', 'w') as file:
    file.write(two_words + '\n')

# Read and print the content of the file
with open(file_name + '.txt.new', 'r') as file:
    data = file.readlines()  # Read all lines from the file
    for line in data:
        print(line.strip())  # Print each line, stripping any extra newlines

######################################### 10.1.2 #######################################################################

with open("timesheet.rtf", 'r') as file:
    data = file.readlines()
    for line in data:
        print(line)
        
with open("timesheet_JAN23.rtf", 'w') as file:
     file.writelines(data)

with open("timesheet_FEB23.rtf", 'w') as file:
    file.writelines(data)"""
######################################### 10.1.3 Country files #########################################################
# Read and process each line from countries.txt
with open("countries.txt", 'r') as file:
    data = file.readlines()  # Read all lines into a list

# Create or open Spain.txt for writing
with open("Spain.txt", 'w') as file:
    for line in data:
        line = line.strip()  # Remove leading/trailing whitespace characters
        split_data = line.split()  # Split the line into words
        
        if split_data:  # Check if split_data is not empty
            file.write(split_data[0] + '\n')  # Write the first word to the file


######################################### 10.1.4 Bonuce ################################################################

######################################### csv ##########################################################################


with open("sounds-multiply.csv", 'r') as fileobj:
     data = fileobj.readlines()
    
with open("sounds-multiply-dublicate.csv", 'w') as fileobj:
     fileobj.writelines(data)
     
with open("sounds-multiply-dublicate.csv", 'r') as fileobj:
    data1 = fileobj.readlines()
    for line in data1:
        print(line)

######################################### alert.mp3 ####################################################################

with open("alert.mp3", 'rb') as fileobj:
    data = fileobj.readlines()

with open("alert.mp3-dublicate.mp3", 'wb') as fileobj:
    fileobj.writelines(data)
    fileobj.writelines(data)

with open("alert.mp3-dublicate.mp3", 'rb') as fileobj:
    data1 = fileobj.readlines()
    for line in data1:
        print(line)
######################################### ringtone.mp3 #################################################################

with open("ringtone.mp3", 'rb') as fileobj:
    data = fileobj.readlines()

with open("ringtone.mp3-dublicate.mp3", 'wb') as fileobj:
    fileobj.writelines(data)
    fileobj.writelines(data)

with open("ringtone.mp3-dublicate.mp3", 'rb') as fileobj:
    data1 = fileobj.readlines()
    for line in data1:
        print(line)


 
 
 
 
 
 












