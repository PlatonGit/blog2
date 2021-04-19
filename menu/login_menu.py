from menu import BaseMenu
from menu.main_menu import MainMenu
from models import Context
from utils import get_option_input, raise_exception
from custom_exceptions import UserInputOptionException, ExitFromMenuException


class LoginMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Login Menu | ' + '=' * 10
    __options = '[1] Retry\n[2] Back'

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller

        self.__next_menus = {
        '1': lambda *_: None,
        '2': lambda *_: raise_exception(ExitFromMenuException)
        }


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
            print(self.__menu_heading)

            username = self.input_secure_wrap(lambda *_: input('Enter your account\'s username: '))
            password = self.input_secure_wrap(lambda *_: input('Enter your account\'s password: '))

            context = self.__user_controller.read_user_login_info(username, password)

            if context['status'] == 'success':
                menu_context = Context(context['user'], context['profile'])
                next_menu = MainMenu(
                    self.__user_controller,
                    self.__profile_controller,
                    self.__post_controller
                )                
                next_menu.display()
                return

            elif context['status'] == 'fail':
                print('\n>>> Login failed; incorect username or password were given <<<')  
                
                selected_option = self.input_secure_wrap(get_input)
                
                try:
                    self.__next_menus[selected_option](
                        self.__user_controller,
                        self.__profile_controller,
                        self.__post_controller
                    )
                except ExitFromMenuException:
                    return












# class LogInMenu(BaseMenu):
#     __menu_heading = '----- Logging in -----'
#     __options = '[1] Enter your username: {username}\n[2] Enter your password: {password}\n[3] Confirm\n[4] Cancel'
#     __next_menus = {
#         '1' : None,
#         '2' : None,
#         '3' : None,
#         '4' : None
#     }
    