from custom_exceptions import UserInputOptionException


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
                print('\n\n>>> Programm was interrupted <<<')
                exit(0)
            except Exception as ex:
                print('>>> Error:', ex, '<<<')


    def display(self):
        raise NotImplementedError



