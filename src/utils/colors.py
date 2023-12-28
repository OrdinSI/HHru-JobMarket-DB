from colorama import Fore, Style


class Colors:
    RESET_ALL = Style.RESET_ALL
    RED = Fore.RED
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN

    @staticmethod
    def print_red(message):
        print(f'{Colors.RED}{message}{Colors.RESET_ALL}')

    @staticmethod
    def print_blue(message):
        print(f'{Colors.BLUE}{message}{Colors.RESET_ALL}')

    @staticmethod
    def print_magenta(message):
        print(f'{Colors.MAGENTA}{message}{Colors.RESET_ALL}')

    @staticmethod
    def input_cyan(message):
        return input(f'{Colors.CYAN}{message}{Colors.RESET_ALL}')

