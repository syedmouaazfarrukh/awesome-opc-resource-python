
# ------ USING ASYNCUA FUNCTION---------

import asyncio
from asyncua import Client, Node, ua

# ----------FOR OPCUA FUNCTION----------
# *COMMENT THE AYSNCUA LIBRARY & FUNCTION BEFORE USING OPCUA  
# from opcua import opcuaClient


async def using_asyncua_lib():
    
       # -----ESTABLISHES CLIENT & READS ROOT NODE------
       
       url = "ADD YOUR SERVER IP-ADDRESS WITHIN THIS"
       async with Client(url=url) as client:
            root = client.get_root_node()
            print("Root node using asyncua library is",root)

def using_opcua_lib():
       
        # -----ESTABLISHES CLIENT & READS ROOT NODE------

        url = "ADD YOUR SERVER IP-ADDRESS WITHIN THIS"
        client = Client(url)
        client.connect()
        root = client.get_objects_node()
        print("Root node using opcua library is",root)
        

if __name__ == '__main__':
     
    establish_asyncclient = asyncio.run(using_asyncua_lib())
    
    # ---------USE FOR OPCUA TESTING---------
    #establish_opcuaclient = using_opcua_lib()
     