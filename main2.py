import json
import tabula

tables = tabula.read_pdf('06-February-2023-Trade-Summary-Report.pdf',pages='all')
df = tables[0]

# Example list

instru = df.Instrument.to_list()
instrument = instru

op = df.Opening.to_list()
opening_price = op

# Convert the list to a dictionary
my_dict = {"Instrument": instrument[2:],
            "Opening Price": opening_price[2:]}

json_str = df.to_json(orient="table")

# Save the dictionary to a JSON file
with open("my_list.json", "w") as file:
    json.dump(my_dict, file)
