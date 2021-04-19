from menu import BaseMenu
from menu.main_menu import MainMenu
from custom_exceptions import RepositoryError, UserInputOptionException, ExitFromMenuException
from utils import get_option_input, get_username_input, get_password_input, raise_exception
from models import User


class RegistrationMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Registration Menu | ' + '=' * 10
    __options = '[1] Confirm\n[2] Cancel'

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

        self.__next_menus = {
        '1': lambda *_: None,
        '2': lambda *_: raise_exception(ExitFromMenuException)
        }

   
    def display(self):
        option_input_func = get_option_input()
        username_input_func = get_username_input()
        password_input_func = get_password_input()

        def get_option():
            print(self.__menu_heading)
            print(self.__options)
            
            selected_option = option_input_func('\nEnter option\'s id: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        
        def get_username():
            print(self.__menu_heading)
            return username_input_func('Enter your new account\'s username (username must start with a letter and be at least 5 characters long): ')

        
        def get_password():
            print(self.__menu_heading)
            return password_input_func('Enter your new account\'s password (password must be at least 8 characters long): ')
        
        while True:
            username = self.input_secure_wrap(get_username)
            password = self.input_secure_wrap(get_password)
            
            if self.__user_controller.read_user_by_username(username):
                print('\n>>> Entered username is already occupied by another user. Try a different username <<<')
                continue

            selected_option = self.input_secure_wrap(get_option)
            try:
                self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return

            profile_id = self.__profile_controller.create_blank_profile()
            
            if profile_id:
                user = User(username, password, profile_id)
                self.__user_controller.create_user(user)
                print('\nCongrats! Your account was created. You can add/edit your accont\'s personal info in main menu in \'My profile\',\nwhich you can access after logging in.')
                input('Press any key to continue to back the start page\n')
                return
            else:
                print('\n>>> An error occured while working with database; try registrating again <<<')
            
                
    
        

