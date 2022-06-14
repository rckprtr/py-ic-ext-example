from pprint import pprint
from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types
from ic.principal import Principal


def get_owned_tokens(principal, registry):
    owned_tokens = []
    aid = principal.to_account_id().to_str()[2:]
    for item in registry[0]:
        id = item[0]
        account_id = item[1]
        if aid == account_id:
            owned_tokens.append(id)
    return owned_tokens


def get_nft_registry(canister_id):
    iden = Identity()
    client = Client()
    agent = Agent(iden, client)
    print(client)
    # read governance candid from file
    ext_did = open("ext.did").read()
    # create a governance canister instance
    ext = Canister(
        agent=agent, canister_id=canister_id, candid=ext_did)
    return ext.getRegistry()

# Registry data structure
# data = [
#  [
#   [ID, Owner],
#   [ID, Owner],
#   [ID, Owner],
#  ]
# ]
# i.e.
# [9972, '685f131937e3d4057144fdfd6a892d70b8bcefa77d79a00d954fe26089d7034f']


registry = get_nft_registry("bzsui-sqaaa-aaaah-qce2a-cai")

my_principal = Principal.from_str(
    'slrjv-o4wlb-7mjt3-rjegb-psx7i-5ndvk-qkesi-ks3c3-mplfb-ort5m-bqe')


results = get_owned_tokens(my_principal, registry)
print(results)
