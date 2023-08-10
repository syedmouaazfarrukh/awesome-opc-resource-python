

import asyncio
from asyncua import Client, Node, ua


async def using_asyncua_lib():
       
       url = "opc.tcp://168.63.250.196:49320"
       async with Client(url=url) as client:
            root = client.get_root_node()
        
            # Find the "Objects" node and get its children
            objects_node = await root.get_child(["Objects"])
            print(objects_node)
            objects_children = await objects_node.get_children()
            for i in objects_children:
                print(i,"\n")
            print(objects_children)


async def using_opcua_lib():
       
        url = "opc.tcp://168.63.250.196:49320"
        client = Client(url)
        root = client.get_root_node()
        
        # Find the "Objects" node and get its children
        objects_node = await root.get_child(["Objects"])
        print(objects_node)
            objects_children = await objects_node.get_children()
            for i in objects_children:
                print(i,"\n")
            print(objects_children)



if __name__ == '__main__':
     
     asyncio.run(using_asyncua_lib())
     main()
     