# Open the file in read mode
with open('docs/01_introduction.md', 'r') as file:
    # Read the content of the file
    file_lines = file.readlines()

# Find the line index containing the tag
tag_line_index = -1
for index, line in enumerate(file_lines):
    if "## The RGI 7.0 Consortium" in line:
        tag_line_index = index
        break

# Define the replacement text
new_text = """## The RGI 7.0 Consortium

*Members of the RGI 7.0 Consortium:*

<ADD RGI CONSORTIUM>
"""

# Replace lines from the tag line index onward
updated_lines = file_lines[:tag_line_index] + [new_text]

# Open the file in write mode to overwrite its contents
with open('docs/01_introduction.md', 'w') as file:
    # Write the updated lines to the file
    file.writelines(updated_lines)
