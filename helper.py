import random
import string


class Helper:
    @staticmethod
    def get_email():
        return f"kmikhalev18{random.randint(100,999)}@ya.ru"

    @staticmethod
    def get_password():
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
