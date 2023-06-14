# Define the replacement text
section = 1
contributors = {1: [], 2: [], 3: []}
all_contributors = []
with open('rgi_consortium.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if '#' in line:
            if 'Implementation' in line:
                section += 1
            if 'Outlines' in line:
                section += 1
            continue
        li = contributors[section]
        if line in all_contributors or 'Bruce H.' in line:
            continue
        li.append(line)
        all_contributors.append(line)

consortium_list = contributors[1] + sorted(contributors[2]) + sorted(contributors[3])
consortium_list = '; '.join(consortium_list).rstrip()

consortium_list += f"""

*The first {len(contributors[1])} authors were members of the RGI Working Group steering committee and responsible for the design, development, implementation and assembly of RGI 7.0. The following  {len(contributors[2])} members (listed in alphabetical order) assisted with the implementation. The remaining {len(contributors[3])} authors (listed in alphabetical order) contributed with outline review and/or outlines used in RGI 7.0.*

*For a more detailed listing of contributions, visit [](appendix/contributors).*

"""

# Open the file in read mode
with open('docs/01_introduction.md', 'r') as file:
    # Read the content of the file
    file_content = file.read()

# Find and replace the tag in the file content
updated_content = file_content.replace("<ADD RGI CONSORTIUM>", consortium_list)

# Open the file in write mode to overwrite its contents
with open('docs/01_introduction.md', 'w') as file:
    # Write the updated content to the file
    file.write(updated_content)
