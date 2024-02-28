"""module for implementing Regular Expressions"""
import re
import logging


logging.basicConfig(filename='app.log', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('This will get logged')

logger = logging.getLogger(__name__)
class UserValidation:
    """class to define the methods for usser info validations"""
    def __init__(self) -> None:
        self.__first_name = None

    @property
    def first_name(self):
        """getter for first name"""
        return self.__first_name

    def validate_fname(self,first_name):
        """method for validating first name"""
        fname_pattern = re.compile("[A-Z][a-z]{3,}$")
        fname_valid=fname_pattern.match(first_name)
        if fname_valid:
            # print("Enter a valid first name : first letter must be capital")
            self.__first_name = first_name
            logging.info('Valid first name')
            return
        else:
            logging.info('Invalid first name')
            raise ValueError("Invalid first Name")


if __name__ == '__main__':
    try:
        user = UserValidation()
        fname=input("Enter first name :")
        user.validate_fname(fname)
    except ValueError as e:
        logger.exception(e)
