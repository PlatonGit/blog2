from utils import get_option_input, raise_exception
from custom_exceptions import UserInputOptionException, UserExitException
from menu import BaseMenu
from menu.login_menu import LoginMenu 
from menu.registration_menu import RegistrationMenu 


class StartMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Start Menu | ' + '=' * 10
    __options = '[1] Log in\n[2] Sign up\n[3] Exit'
    __next_menus = {
        '1': LoginMenu,
        '2': RegistrationMenu,
        '3': lambda *_: raise_exception(UserExitException)
    }


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

    
    def display(self):
        input_func = get_option_input()

        def get_input():
            print(self.__menu_heading)
            print(self.__options)
            
            selected_option = input_func('\nEnter option\'s id: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            selected_option = self.input_secure_wrap(get_input)

            next_menu = self.__next_menus[selected_option](
                self.__user_controller,
                self.__profile_controller,
                self.__post_controller
            )
            next_menu.display()
