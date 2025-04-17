import json
from json2xml import json2xml

# Open the discovery.json file and read its contents
with open("discovery.json", "r") as json_file:
    json_data = json.load(json_file)

# Convert the JSON data to XML
xml_data = json2xml.Json2xml(json_data).to_xml()

# Write the XML data to a file
with open("discovery.xml", "w") as xml_file:
    xml_file.write(xml_data)

print("discovery.json has been converted to discovery.xml")
