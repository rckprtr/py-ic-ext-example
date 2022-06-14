from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types

iden = Identity()
client = Client()
agent = Agent(iden, client)
print(client)
# read governance candid from file
ext_did = open("ext.did").read()
# create a governance canister instance
ext = Canister(
    agent=agent, canister_id="bzsui-sqaaa-aaaah-qce2a-cai", candid=ext_did)
# call canister method with instance
print(ext.getRegistry())
