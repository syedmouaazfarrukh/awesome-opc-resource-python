

import asyncio
from asyncua import Client, Node, ua
import json
from datetime import datetime
#from csv_reader import read_column_from_csv


async def main():
       file_path = "data.json"
       file_path2 = "TagNames.csv"
       column_name = "TagNames"
       #Tag_names = read_column_from_csv(file_path, column_name)
       Tag_names = ["ACC4","AIN_Alt_AT_Mul","Alarm_Ack", 'Air_Flow', ]

       url = "opc.tcp://168.63.250.196:49320"
       async with Client(url=url) as client:
        root = client.get_root_node()
        

        # Find the "Objects" node and get its children
        objects_node = await root.get_child(["Objects"])
        objects_children = await objects_node.get_children()

        # Use the browse method to find the "Oil_Gas" node
        oil_gas_node = None
        for child in objects_children:
            browse_name = await child.read_browse_name()
            if browse_name.Name == "Oil_Gas":
                oil_gas_node = child
                break

        if oil_gas_node is not None:
            # Use the browse method to find the "site1" node inside the "Oil_Gas" node
            site1_node = None
            oil_gas_children = await oil_gas_node.get_children()
            for child in oil_gas_children:
                browse_name = await child.read_browse_name()
                if browse_name.Name == "site1":
                    site1_node = child
                    break

            if site1_node is not None:
                # Use the browse method to get all the children nodes inside the "Oil_Gas.site1" node
                site1_children = await site1_node.get_children()

                print("\nChildren of 'Oil_Gas.site1' node:")
                Tags_count = len(Tag_names)
                
                data_dict = {}
                for child in site1_children:
                   #print("Yet to recieve variables: ", Tags_count)
                   if (Tags_count == 0):
                    break 
                   browse_name = await child.read_browse_name()
                   if browse_name.Name in Tag_names:

                        timestamp = datetime.now().isoformat()  # Get current timestamp
                        node_id = child.nodeid.Identifier
                        
                        # data_type_nodeid = await child.read_attribute(ua.AttributeIds.DataType)
                        # data_type_id = data_type_nodeid.Value.Value.Identifier
                        # data_type_str = ua.VariantType(data_type_id).name

                        value = await child.read_value()
                        
                        description = await child.read_attribute(ua.AttributeIds.Description)
                        description_text = description.Value.Value.Text if description.Value.Value else ""


                        print("NodeId: {}\nTimestamp: {}\nDescription: {}\nValue: {}\n"
                              .format(node_id, timestamp,description_text,value))
                        print("Currently writing Tag Number", Tags_count)
                        Tags_count -= 1

                        data_dict[node_id] = {
                            "Timestamp": timestamp,
                            "Description": description_text,
                            "Value": value
                        }
                                                
                # Read the existing JSON data from the file (if it exists)
                with open("data.json", "r") as json_file:
                    existing_data = json.load(json_file)
                # Append the new data dictionary to the existing data dictionary
                existing_data.update(data_dict)
                print(existing_data)
                
                # Write the updated data back to the file
                with open(file_path, "w") as json_file:
                    json.dump(existing_data, json_file, indent=2)
                # Write the data dictionary to a JSON file
                #with open("data.json", "w") as json_file:
                #    json.dump(data_dict, json_file, indent=2)
                
            else:
                print("No 'site1' node found inside 'Oil_Gas' node!")

        else:
            print("No 'Oil_Gas' node found!")

if __name__ == '__main__':
     asyncio.run(main())