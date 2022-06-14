# const tokenIdentifier = (principal, index) => {
#   const padding = Buffer("\x0Atid");
#   const array = new Uint8Array([
#     ...padding,
#     ...Principal.fromText(principal).toUint8Array(),
#     ...to32bits(index),
#   ]);
#   console.log(array);
#   return Principal.fromUint8Array(array).toText();
# };


# tokenIdentifier(canister_id, index)
# tokenIdentifier("bzsui-sqaaa-aaaah-qce2a-cai", 4350) -> aaaa-a
#
#  byteArray = ["\x0Atid" + canister_id.bytes + Index.bytes]
#  return Principal.fromBytes(byteArray)
#


# index = 4350
# reg_p = Principal.from_str("bzsui-sqaaa-aaaah-qce2a-cai").bytes
# output = b"\x0Atid"+reg_p + index.to_bytes(4, 'big')
# result = Principal.from_hex(bytes.hex(output))
# print(result)
