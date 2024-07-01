import random
import string

# Listy przykładowych imion i nazwisk
first_names = ["Jan", "Anna", "Piotr", "Katarzyna", "Andrzej", "Maria", "Tomasz", "Agnieszka", "Krzysztof", "Barbara"]
last_names = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński", "Szymański", "Woźniak"]

# Funkcja do generowania losowego hasła
def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Generowanie poleceń
ppp_commands = []
interface_commands = []
list_commands_admin = []
list_commands_it = []

for i in range(40):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = f"{first_name}{last_name}"
    password = generate_password()
    ppp_command = f"/pp secret add name={username} password={password} profile=vpn service=l2tp"
    interface_command = f"/interface l2tp-server add name=L2TP{username} user={username}"
    ppp_commands.append(ppp_command)
    interface_commands.append(interface_command)
    if i < 35:
        list_command = f"/interface list member add interface=L2TP{username} list=IL_L2TP-Ksiegowosc"
        list_commands_admin.append(list_command)
    else:
        list_command = f"/interface list member add interface=L2TP{username} list=IL_L2TP-Dzial_IT"
        list_commands_it.append(list_command)

# Drukowanie poleceń
for command in interface_commands:
    print(command)
for command in ppp_commands:
    print(command)
for command in list_commands_admin:
    print(command)
for command in list_commands_it:
    print(command)