from menu import BaseMenu
from menu.profile_menu import ProfileMenu
from menu.user_page_menu import UserPageMenu
from menu.user_feed_menu import UserFeedMenu
from models import Context
from custom_exceptions import UserInputOptionException, ExitFromMenuException
from utils import get_option_input, raise_exception


class MainMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Main Menu | ' + '=' * 10
    __options = '[1] My profile\n[2] My page\n[3] My feed\n[4] Log out'
    __next_menus = {
        '1': ProfileMenu,
        '2': UserPageMenu,
        '3': UserFeedMenu,
        '4': lambda *_: raise_exception(ExitFromMenuException)
    }


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()

    
    def display(self):
        print(f'\nWelcome, {self.__context.user.username}!')
        
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