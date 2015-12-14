# amity.py
from employees.model import Staff, Fellow
from rooms.models import Office, LivingSpace
import random
import sys

""" office names: will contain names of people after allocations """
office = {
    "allegro": [], "boma": [], "valhalla": [],
    "hogwarts": [], "krypton": [], "oculus": [],
    "gondolla": [], "amitoid": [], "punta": [], "borabora": []
}

""" living space names """
living = {
    'Green': [], 'Blue': [], 'Yellow': [], 'Lilac': [],
    'Orange': [], 'White': [], 'Brown': [],
    'Turquoise': [], 'Grey': [], 'Purple': []
}
""" create a list of rooms (both office and living space)
    which will be used to obtain the key to their respective
    dictionary definitions during allocations
"""
office_list = [
    'allegro', 'boma', 'valhalla',
    'hogwarts', 'krypton', 'oculus', 'gondolla',
    'amitoid', 'punta', 'borabora'
]

livingspace_list = [
    'Green', 'Blue', 'Yellow', 'Lilac',
    'Orange', 'White', 'Brown', 'Turquoise', 'Grey', 'Purple'
 ]


class Amity(object):
    """ get the list of allocations """
    def get_allocation(self):


    """ allocate office space """
    def allocate_office_space(self):
        office_space = Office(office)
        office_rooms = office_space.populate_room_names()

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)
        print room_index

        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]
        index = 0
        """ loop through each person to determine their affiliations """
        for person in employees:
            """ use space char as the delimeter """
            persons_description = [x.rstrip() for x in person.split(" ")]

            chosen_room = room_index[index % 10]
            office_key = office_list[chosen_room]

            """ allocate only office space """
            if len(office_rooms[office_key]) <= office_space.maximum_size:
                """ allocate office space to everyone """
                office_rooms[office_key].append(
                    persons_description[0] + ' ' + persons_description[1])
            else:
                continue
            """ pick a different room next iteration """
            index += 1

        return office_rooms

    """ allocate living space """
    def allocate_living_space(self):
        living_space = LivingSpace(living)
        living_rooms = living_space.populate_room_names()
        """ check for fellows who want accomodation """

        """ shuffle room numbers at random """
        room_index = list(range(10))
        random.shuffle(room_index)
        print room_index

        """ read the employees from the input .txt file """
        employees = [
            employees.rstrip('\n') for employees in open(sys.argv[1], 'r')
        ]
        index = 0
        """ loop through each person to determine their affiliations """
        for person in employees:
            """ use space char as the delimeter """
            persons_description = [x.rstrip() for x in person.split(" ")]
            chosen_room = room_index[index % 10]
            living_key = livingspace_list[chosen_room]
            if len(living_rooms[living_key]) <= living_space.maximum_size:
                if persons_description[2].upper() == 'FELLOW':
                    if len(persons_description) >= 4:
                        if persons_description[3] == 'Y':
                            """ fellow needs a place to live too """
                            living_rooms[living_key].append(
                                persons_description[0] +
                                ' ' + persons_description[1])
            else:
                continue
            index += 1
        print living_rooms
        return living_rooms

amity = Amity()
amity.allocate_living_space()

