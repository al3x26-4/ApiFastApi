import tabula
import json

# Read the PDF file into a pandas DataFrame
table = tabula.read_pdf("06-February-2023-Trade-Summary-Report.pdf", pages='all')
df = table[0]

# Convert the DataFrame to a JSON string
json_str = df.to_json(orient="records")

# Save the JSON string to a file
with open("new.json", "w") as file:
   file.write(json_str)

# Load the JSON file into a Python dictionary
#with open("new.json", "r") as file:
 #   data = json.load(file)

# Access the value for a specific key in the dictionary
#column = data[2]

#print(column)

