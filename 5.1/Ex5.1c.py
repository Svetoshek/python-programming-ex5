london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
try:
    name_interfaces = input("Введите имя устройства: ")
    keys = list(london_co[name_interfaces].keys())
    version_system = input(("Введите имя параметра ({}): ").format(",".join(keys)))
    print(london_co[name_interfaces][version_system])
except KeyError:
    print("Такого параметра нет")