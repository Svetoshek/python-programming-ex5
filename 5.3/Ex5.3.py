
template = {
    "access_template": {
        "switchport mode access", "switchport access vlan {}",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    },
    "trunk_template": {
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
    }
}

name_interfaces = input("Введите режим работы интерфейса (access/trunk): ")
version_system = input("Введите тип и номер интерфейса : ")
numbers_vlan = input("Введите номер влан(ов): ")

interfaces = (name_interfaces+"_template")
print("interface {}".format(version_system))
print('\n'.join(template[interfaces]).format(numbers_vlan))

