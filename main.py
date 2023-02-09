import tabula
import json
import os

pdf_files = ['data/03-02-2023.pdf','data/06-02-2023.pdf','data/07-02-2023.pdf','data/08-02-2023.pdf','data/09-02-2023.pdf']
# Iterate over the list of PDF files
for i, file_name in enumerate(pdf_files):

   # Extract the name of the file without the '.pdf' extension
    json_file_name = os.path.splitext(file_name)[0] + ".json"

    # Extract the table from the PDF file
    table = tabula.read_pdf(file_name, pages="all", multiple_tables=True)

    # Get the table you want to extract
    desired_table = table[0]
    json_str = desired_table.to_json(orient='records')

    # Save the table to a JSON file
    with open(json_file_name, "w") as file:
        file.write(json_str)

