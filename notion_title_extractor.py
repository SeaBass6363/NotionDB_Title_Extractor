from dotenv import load_dotenv
import os 
import re

load_dotenv()

# File paths (original file and the new file for output)
input_file_path = os.getenv("IN_NOTION_FILE_PATH")
output_file_path = os.getenv("OUT_NOTION_FILE_PATH")

# Reads and extracts the text in input file
input_file = open(input_file_path, "r")
content = input_file.readlines()
input_file.close()

# Opens output file for editing
output_file = open(output_file_path, "w")

# Compiled regex expression to extract the string in between brackets 
# or followed by a hashtag and space
txtRegex = re.compile(r'((?<=(^#\s)).*)|((?<=(\[)).*(?=\]))')
#counter to number each line
counter = 1

for line in content:
    # Initiates cleaned_line without any leading spaces
    cleaned_line = line.lstrip()
    # Removes asterisks (*)
    cleaned_line = re.sub(r'[\*]', '', cleaned_line)
    # Matches pattern from cleaned_line into str match
    match = re.search(txtRegex, cleaned_line)
    # If match is successful cleaned_line is numbered, updated with matched string, 
    # and a newline is inputted at the end
    if match:
        cleaned_line = str(counter)+ ". " + match.group() + "\n"
        #counter increases by one, every successful match
        counter += 1
        #prints the new cleaned line before written on the output file
        print(cleaned_line) 

    # Write the cleaned line to the output file
    output_file.write(cleaned_line)
    
output_file.close
