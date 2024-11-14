devices=["R1","R2","R3","S1","S2"]
switches=[]
routers=[]
for item in devices:
    if "R" in item:
        routers.append(item)
        print(item)
for item in devices:
    if "S" in item:
        switches.append(item)
        print(item)

print(f"my routers are: {routers}")
print(f"my switches are: {switches}")
