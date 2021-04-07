from menu import BaseMenu
from models import Context
from utils import get_option_input


class MainMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Main Menu | ' + '=' * 10
    __options = ''
    __next_menus = {

    }


    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()

    
    def display(self):
        print(self.__menu_heading)
        print('Welcome, ', self.__context.user.username, self.__context.profile.last_name)
