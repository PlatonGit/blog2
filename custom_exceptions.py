class RepositoryError(Exception):
    pass


class DatabaseError(Exception):
    pass


class UserInputOptionException(Exception):
    pass


class ExitFromMenuException(Exception):
    pass


class UserExitException(KeyboardInterrupt):
    pass


class InvalidUsernameException(Exception):
    pass


class InvalidPasswordException(Exception):
    pass