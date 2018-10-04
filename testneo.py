from neorpc.Client import RPCClient

class SettingsHolder:
    """
    This class holds all the settings. Needs to be setup with one of the
    `setup` methods before using it.
    """
    RPC_LIST = None

    # Setup methods
    def setup(self, addr_list):
        """ Load settings from a JSON config file """
        self.RPC_LIST = addr_list

    def setup_privnet(self):
        """ Load settings from the privnet JSON config file """
        self.setup(
            [
                "127.0.0.1:20333"
            ]
        )

# Settings instance used by external modules
settings = SettingsHolder()

client = RPCClient( )

print(client.get_height())

# client. = "http://localhost:30333"
# RPCEndpoint addr has to be = "http://localhost:30333"
# client.default_endpoint = "http://localhost:30333"