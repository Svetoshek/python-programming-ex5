address = input("Введите адрес и маску сети: ")
ip = (address.split("/")[0])
new = ip.split(".")

mask = (address.split("/")[1])
index = ("1"*int(mask)+"0"*(32-int(mask)))
n = 8
chunks = [index[i:i+n] for i in range(0, len(index), n)]

print("""
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
"""
.format(int(new[0]), int(new[1]), int(new[2]), int(new[3]),
        int(new[0]), int(new[1]), int(new[2]), int(new[3])))
print(
"""
Mask:
/{}
{}      {}      {}      {}
{}
""".format((mask),
    (int(chunks[0],2)),(int(chunks[1],2)),(int(chunks[2],2)),(int(chunks[3],2)),
    (" ".join(chunks))))

