from menu import BaseMenu
from utils import get_option_input


class RegistrationMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Registration Menu | ' + '=' * 10
    __options = ''

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        
        self.__next_menus = {
 
        }

    
    def display(self):
           
        while True:
            print(self.__menu_heading)
            
            username = input('Enter your new user account\'s username: ')
            password = input('Enter your new user account\'s password: ')

            print(username, password)
            return

