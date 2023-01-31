import json
import xmltodict

# Open the discovery.json file
with open("discovery.json") as json_file:
    json_data = json.load(json_file)

# Convert the JSON data to XML
xml_data = xmltodict.unparse(json_data, pretty=True)

# Write the XML data to a file
with open("discovery.xml", "w") as xml_file:
    xml_file.write(xml_data)
