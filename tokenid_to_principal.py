from ic import Principal

# print(tokenIdentifier("bzsui-sqaaa-aaaah-qce2a-cai", 4350))


def tokenIdentifier(canister_id, index):
    cip = Principal.from_str(canister_id).bytes
    return Principal(b"\x0Atid" + cip + index.to_bytes(4, 'big'))
