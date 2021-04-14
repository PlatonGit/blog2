from custom_exceptions import *
from utils import get_option_input


class BaseMenu:
    menu_heading = None
    menu_options = None
    next_menus = None


    @staticmethod
    def input_secure_wrap(input_func, *args, **kwargs):
        while True:
            try:
                return input_func(*args, **kwargs)
            except UserInputOptionException:
                print('\n>>> Invalid option id <<<')
            except KeyboardInterrupt:
                print('\n\n\n>>> Programm was interrupted <<<')
                raise KeyboardInterrupt
            except Exception as ex:
                print('\n>>> Error:', ex, '<<<')


    def display(self):
        raise NotImplementedError



