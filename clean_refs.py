# Open the input file
with open("docs/references.bib", "r") as input_file:
    # Read the content of the input file
    content = input_file.readlines()

# Remove lines containing "url = {"
cleaned_content = []
for line in content:
    if "url = {" in line and 'publikasjoner.nve.no' not in line:
        continue
    line = line.replace('rapport2012{\_}38', 'rapport2012_38')
    cleaned_content.append(line)

# Open the output file
with open("docs/references_cleaned.bib", "w") as output_file:
    # Write the cleaned content to the output file
    output_file.writelines(cleaned_content)

print("Cleaning complete. The cleaned content has been saved to 'docs/references_clean.bib'.")
