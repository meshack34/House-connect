import pyperclip

class Contact:
    """
    Class that generates new instances of contacts.
    """

    contact_list = []  # Empty contact list
 # Init method up here
    contact_list1 = []

    def save_contact(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        Contact.contact_list.append(self)

    def save_meshack(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        Contact.contact_list1.append(self)

    
    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)

    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    @classmethod
    def find_by_number(cls, number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    print("hello")
     


    @classmethod
    def copy_email(cls,number):
            contact_found = Contact.find_by_number(number)
            pyperclip.copy(contact_found.email)
    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list
    def __init__(self, first_name, last_name, number, email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
    
  

