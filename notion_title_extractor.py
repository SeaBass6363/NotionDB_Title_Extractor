

with open("notion_book_titles_withLinks.txt", "r+") as file:
    # Read the content of the file
    content = file.read()

    # Edit the content as needed
    new_content = content.replace("old text", "new text")

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Write the new content
    file.write(new_content)

    # Truncate the file to remove any remaining old content
    file.truncate()