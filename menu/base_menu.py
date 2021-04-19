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

            except InvalidUsernameException:
                print('\n>>> An invalid username was entered; it must start with a letter and be at least 5 characters long <<<')

            except InvalidPasswordException:
                print('\n>>> An invalid password was entered; it must be at least 8 characters long <<<')

            except InvalidNameException:
                print('\n>>> An invalid name was entered; it must be only letters <<<')
            
            except InvalidAgeException:
                print('\n>>> An invalid age was entered; it must be a number <<<')

            except KeyboardInterrupt:
                print('\n\n\n>>> Programm was interrupted <<<')
                raise KeyboardInterrupt
                
            except Exception as ex:
                print('\n>>> Error:', ex, '<<<')


    def display(self):
        raise NotImplementedError



