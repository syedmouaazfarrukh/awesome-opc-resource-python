from opcua import Server

if __name__ == "__main__":
    # Create a server instance
    server = Server()

    # Setup server endpoint
    server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

    # Setup server namespace
    uri = "http://example.org"
    idx = server.register_namespace(uri)

    # Create a new object under the root
    objects = server.nodes.objects
    myobj = objects.add_object(idx, "MyObject")

    # Add a variable to the object
    myvar = myobj.add_variable(idx, "MyVariable", 0)
    myvar.set_writable()

    # Start the server
    server.start()
    
    try:
        while True:
            pass
    finally:
        # Stop the server on exit
        server.stop()
