from menu import BaseMenu
from custom_exceptions import UserInputOptionException, ExitFromMenuException
from utils import get_option_input, raise_exception


class UserPageMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | My page | ' + '=' * 10
    __options = '[1] Create a post\n[2] Edit a post\n[3] Delete a post\n[4] Back to main menu'
    __next_menus = {
        '1': None,
        '2': None,
        '3': None,
        '4': lambda *_: raise_exception(ExitFromMenuException)
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
            
            try:
                next_menu = self.__next_menus[selected_option](
                    self.__user_controller,
                    self.__profile_controller,
                    self.__post_controller
                )
                next_menu.display()
            except ExitFromMenuException:
                return
        