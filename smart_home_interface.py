import json, pdb

with open("property_data.json") as f:
    data = json.load(f)

def start_program():
    first_name = input("Welcome.  Please enter your first name:\n> ")
    last_name = input("And your last name:\n> ")
    if authorize(first_name, last_name):
        greet(first_name)
    else:
        print("You are not authorized to access this program.  Please double-check your login information.")
        exit(0)

def authorize(first_name, last_name):
    authorized = False
    for person in data["people"]:
        if person["first_name"].lower() == first_name.lower() and person["last_name"].lower() == last_name.lower() and "Admin" in person["roles"]:
            authorized = True
    return authorized

def greet(first_name):
    print("Welcome, {}.".format(first_name.capitalize()))
    main_menu()

def main_menu():

    response = 0
    while response != 4:
        print("{} MAIN MENU {}".format("*" * 6, "*" * 6))
        print("Please choose an option.")
        print("""
1 -> See residents for one unit
2 -> See information about one resident
3 -> Move a resident in or out of a unit
4 -> Quit program
        """)
        response = input("> ")
        if response == "1":
            resident_names()
        elif response == "2":
            resident_information()
        elif response == "3":
            move_resident()
        elif response == "4":
            exit(0)
        else:
            print("\nThat is not a valid choice.")

def resident_names():
    unit_number = input("Enter unit number\n> ")
    residents = []
    for person in data["people"]:
        if person["unit"] == unit_number:
            residents.append("{} {}".format(person["first_name"], person["last_name"]))
    if residents:
        print_resident_list(residents)
    else:
        print("This unit is unoccupied.")

def print_resident_list(resident_list):
    for resident in resident_list:
        print("- {}".format(resident))
    print("\n")

def resident_information():
    name = input("Enter resident name.\n> ")
    name_list = name.split(" ")
    for resident in data["people"]:
        if resident["first_name"].lower() == name_list[0].lower() and resident["last_name"].lower() == name_list[1].lower():
            is_admin = "Admin" in resident["roles"]
            devices = get_devices(resident["unit"], is_admin)
            print_resident_info(resident)
            print("Accessible Devices:")
            print_devices(devices)

def get_devices(unit_number, is_admin):
    accessible_devices = []
    for device_name, devices in data['devices'].items():
        for device_info in devices:
            if device_info['unit'] == int(unit_number):
                accessible_devices.append(device_info)
            elif device_info['admin_accessible'] == 'true' and is_admin:
                accessible_devices.append(device_info)
    return accessible_devices

def print_resident_info(info):
    print(f'''
Resident Name: {info["first_name"]} {info["last_name"]}
Unit Number: {info["unit"]}
Property Roles: {", ".join(info["roles"])}
''')

def print_devices(devices):
    for device in devices:
        print(f"""
\tModel: {device["model"]}
\tAdmin Accessible: {device["admin_accessible"]}
\tUnit Number: {device["unit"]}
""", end=' ')

def move_resident():
    direction = ''
    while direction.lower() not in ['in', 'out']:
        direction = input("Move resident in or out?\n> ")
        if direction.lower() == 'in':
            move_resident_in()
        elif direction.lower() == 'out':
            move_resident_out()
        else:
            print("Please input 'in' or 'out'.\n")

def move_resident_in():
    first_name = input("New resident's first name:\n> ")
    last_name = input("New resident's last name:\n> ")
    unit = ''
    while not unit.isdigit():
        unit = input("New residents' unit number:\n> ")
    new_resident = {
        'first_name': first_name,
        'last_name': last_name,
        'unit': unit,
        'roles': ['Resident']
    }
    if input("Is the new resident an admin? (Yes or No)\n> ").lower() == 'yes':
        new_resident['roles'].append('Admin')
    data['people'].append(new_resident)
    data_file_copy = open('property_data_copy.json', 'w').write(json.dumps(data))
    print('Move complete.')

def move_resident_out():
    first_name = input("Outgoing resident's first name:\n> ")
    last_name = input("Outgoing resident's last name:\n> ")
    for resident in data["people"]:
        if resident['first_name'].lower() == first_name.lower() and resident['last_name'].lower() == last_name.lower():
            data["people"].remove(resident)
            data_file_copy = open('property_data_copy.json', 'w').write(json.dumps(data))
            print('Move complete.')
# account for no name


start_program()
