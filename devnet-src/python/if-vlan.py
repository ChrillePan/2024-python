nativeVLAN = input("number of the native VLAN: ")
dataVLAN = input ("number of the native data VLAN: ")
if nativeVLAN == dataVLAN:
    print(f'The native and data VLANs are the same: {"dataVLAN"}')
else:
    print(f'The native {"nativeVLAN"} and data VLANs {"dataVLAN"} are different')
