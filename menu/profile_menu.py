from menu import BaseMenu
from models import Context
from custom_exceptions import ExitFromMenuException
from utils import *


class ProfileMenu(BaseMenu):
    __menu_heading = '\n' + '=' * 10 + ' | Profile Menu | ' + '=' * 10
    __options = '[1] Edit first name\n[2] Edit second name\n[3] Edit last name\n[4] Edit age\n[5] Back to main menu'

    def __init__(self, user_controller, profile_controller, post_controller):
        self.__user_controller = user_controller
        self.__profile_controller = profile_controller
        self.__post_controller = post_controller
        self.__context = Context()

        self.__next_menus = {
            '1': self.edit_first_name,
            '2': self.edit_second_name,
            '3': self.edit_last_name,
            '4': self.edit_age,
            '5': lambda *_: raise_exception(ExitFromMenuException)
        }


    def display(self):
        input_func = get_option_input()

        def get_input():
            print(self.__menu_heading)
            print(f'f.name - {self.__context.profile.first_name}, s.name - {self.__context.profile.second_name}, l.name - {self.__context.profile.last_name}, age - {self.__context.profile.age}\n')       
            print(self.__options)
        
            selected_option = input_func('\nEnter option\'s id: ')
            if selected_option not in self.__next_menus.keys():
                raise UserInputOptionException
            return selected_option
        
        while True:
            selected_option = self.input_secure_wrap(get_input)
            try:
                next_menu = self.__next_menus[selected_option]()
            except ExitFromMenuException:
                return


    def edit_first_name(self):
        input_name_func = get_name_input()

        def get_first_name():
            print(self.__menu_heading)
            return input_name_func('Enter a new first name: ')
    
        new_first_name = self.input_secure_wrap(get_first_name)

        self.__context.profile.first_name = new_first_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print('\n>>> Failed to save changes to profile data; something wrong database connection <<<')
        else:
            print('\nChanges to profile\'s first name were saved successfuly!')


    def edit_second_name(self):
        input_name_func = get_name_input()

        def get_second_name():
            print(self.__menu_heading)
            return input_name_func('Enter a new second name: ')
    
        new_second_name = self.input_secure_wrap(get_second_name)

        self.__context.profile.second_name = new_second_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print('\n>>> Failed to save changes to profile data; something wrong database connection <<<')
        else:
            print('\nChanges to profile\'s second name were saved successfuly!')


    def edit_last_name(self):
        input_name_func = get_name_input()

        def get_last_name():
            print(self.__menu_heading)
            return input_name_func('Enter a new first name: ')
    
        new_last_name = self.input_secure_wrap(get_last_name)

        self.__context.profile.last_name = new_last_name

        if not self.__profile_controller.update_profile(self.__context.profile):
            print('\n>>> Failed to save changes to profile data; something wrong database connection <<<')
        else:
            print('\nChanges to profile\'s last name were saved successfuly!')

    
    def edit_age(self):
        input_age_func = get_age_input()

        def get_age():
            print(self.__menu_heading)
            return input_age_func('Enter a new age: ')
        
        new_age = self.input_secure_wrap(get_age)

        self.__context.profile.age = new_age

        if not self.__profile_controller.update_profile(self.__context.profile):
            print('\n>>> Failed to save changes to profile data; something wrong database connection <<<')
        else:
            print('\nChanges to profile\'s age were saved successfuly!')

        