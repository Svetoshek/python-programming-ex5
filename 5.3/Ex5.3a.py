
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

question_template = {
    "access": "Введите номер VLAN: ",
    "trunk": "Введите разрешенные VLANы: "
}

name_interfaces = input("Введите режим работы интерфейса (access/trunk): ")
version_system = input("Введите тип и номер интерфейса : ")
temp_vlan = input(question_template[name_interfaces])

interfaces = (name_interfaces+"_template")
print("interface {}".format(version_system))
print('\n'.join(template[interfaces]).format(temp_vlan))

