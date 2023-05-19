# Open the input file
with open("docs/references.bib", "r") as input_file:
    # Read the content of the input file
    content = input_file.readlines()

# Remove lines containing "url = {"
cleaned_content = [line for line in content if "url = {" not in line]

# Open the output file
with open("docs/references_cleaned.bib", "w") as output_file:
    # Write the cleaned content to the output file
    output_file.writelines(cleaned_content)

print("Cleaning complete. The cleaned content has been saved to 'docs/references_clean.bib'.")
