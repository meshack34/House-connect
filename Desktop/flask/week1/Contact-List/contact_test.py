import pyperclip
import unittest  # Importing the unittest module
from contact import Contact  # Importing the contact class


class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact(
            "James", "Muriuki", "0712345678", "james@ms.com")  # create contact object

        self.new_contactm = Contact(
            "James", "Muriuki", "07123456788", "james@ms.com")  # create contact object

    # setup and class creation up here
    def tearDown(self):
        '''
            tearDown method that does clean up after each test case has run.
            '''
        Contact.contact_list = []

# other test cases here
    def test_save_multiple_contact(self):
        '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                               "test@user.com")  # new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("0712345678")
        self.assertEqual(self.new_contact.email, pyperclip.paste())
     
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)


    def test_meshack(self):
        self.new_contactm.save_meshack()
        self.assertEqual(len(Contact.contact_list1),1)

    def test_find_contact_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223344",
                               "test@user.com")  # new contact
        test_contact.save_contact()

        found_contact = Contact.find_by_number("0711223344")

        self.assertEqual(found_contact.email, test_contact.email)

    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Contact.display_contacts(), Contact.contact_list)


    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223344",
                               "test@user.com")  # new contact
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0711223344")

        self.assertTrue(contact_exists)
        
    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_contact = Contact(
                "Test", "user", "0712345678", "test@user.com")  # new contact
            test_contact.save_contact()

            self.new_contact.delete_contact()  # Deleting a contact object
            self.assertEqual(len(Contact.contact_list), 1)


if __name__ == '__main__':
    unittest.main()
# Finally the unittest.main() provides a command line interface that collects all the tests methods and executes them
    
