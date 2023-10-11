class ContactList:
    def __init__(self, name: str, contacts: list):
        self._name = name
        self._contacts = contacts

    def __str__(self):
        return f"name:{self._name} phone Number: {self._number} part of the {self} contact list"

    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, new_name):
        self._name = new_name

    @property
    def get_contacts(self):
        return self._contacts
    @get_contacts.setter
    def set_contacts(self, new_contact):
        self._contacts = new_contact
    
    def add_contact(self,new_contact):
        self._contacts.append(new_contact)

    def remove_contact(self, name_to_delete):
        for obj in self._contacts:
            if name_to_delete == obj['name']:
                self._contacts.remove(obj)
    
    def find_shared_contacts(self,contact_list):
        shared_contacts=[]
        for people in self.get_contacts:
            if people in contact_list.get_contacts:
                shared_contacts.append(people)
                return shared_contacts