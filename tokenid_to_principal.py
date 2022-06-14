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
