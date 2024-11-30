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

for line in content:
    # Initiates cleaned_line without any leading spaces
    cleaned_line = line.lstrip()
    # Removes asterisks (*), brackets ([]), and parentheses ()
    cleaned_line = re.sub(r'[\*\[\]\(\)]', '', cleaned_line)
    # Removes hashtags (#) and their immediately followed spaces
    cleaned_line = re.sub(r'#\s', '', cleaned_line)
    # Removes URLs (matching typical HTTP/HTTPS links)
    cleaned_line = re.sub(r'http[s]?://\S+', '', cleaned_line)
        
    # Write the cleaned line to the output file
    output_file.write(cleaned_line)
    
output_file.close
