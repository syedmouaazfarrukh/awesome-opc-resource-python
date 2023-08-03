

import asyncio
from asyncua import Client, Node, ua
import json

 

async def main():
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

                        node_id = child.nodeid.Identifier
                        
                        data_type_nodeid = await child.read_attribute(ua.AttributeIds.DataType)
                        data_type_id = data_type_nodeid.Value.Value.Identifier
                        data_type_str = ua.VariantType(data_type_id).name

                        value = await child.read_value()
                        
                        description = await child.read_attribute(ua.AttributeIds.Description)
                        description_text = description.Value.Value.Text if description.Value.Value else ""

                        #description_text = description.text
                        print("NodeId: {}\nDataType: {}\nValue: {}\nDescription: {}".format(node_id, data_type_str, value, description_text))
                        print('\n')
                        Tags_count -= 1

                        data_dict[node_id] = {
                            "DataType": data_type_str,
                            "Value": value,
                            "Description": description_text
                        }
                        
                # Write the data dictionary to a JSON file
                with open("data.json", "w") as json_file:
                    json.dump(data_dict, json_file, indent=4)

                # Print grandchildren of 'site1' node along with their children
                # print("\nGrandchildren of 'Oil_Gas.site1' node:")
                # for child in site1_children:
                #     grandchildren = await child.get_children()
                #     for grandchild in grandchildren:
                #         print(grandchild)

            else:
                print("No 'site1' node found inside 'Oil_Gas' node!")

        else:
            print("No 'Oil_Gas' node found!")

if __name__ == '__main__':

    asyncio.run(main())
