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
        self.__last_name = None
        self.__email = None
        self.__phone=None

    @property
    def first_name(self):
        """getter for first name"""
        return self.__first_name
    @property
    def last_name(self):
        """getter for last name"""
        return self.__last_name
    @property
    def email(self):
        """getter for email"""
        return self.__email
    @property
    def phone(self):
        """getter for phone number"""
        return self.__phone

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
    def validate_lname(self,last_name):
        """method for validating last name"""
        lname_pattern = re.compile("[A-Z][a-z]{3,}$")
        lname_valid=lname_pattern.match(last_name)
        if lname_valid:
            # print("Enter a valid first name : first letter must be capital")
            logging.info('Valid last name')
            self.__last_name = last_name
            return
        else:
            logging.info('Invalid last name')
            raise ValueError("Invalid last Name")
    def validate_email(self,email_id):
        """method for validating email"""
        email_pattern=re.compile("[^0-9][a-z0-9\\-\\+]+[.a-z0-9]*@[a-z0-9]+.[a-z]+[.in]*$")
        email_valid=email_pattern.match(email_id)
        if email_valid:
            # print("Enter a valid email : ie abc.xyz@bl.co.in ")
            self.__email = email_id
            logging.info('Valid email')
            return
        logging.info('Invalid email')
        raise ValueError("Invalid email ")
    def validate_phone(self,phone_no):
        """method for validating phone number"""
        phone_pattern=re.compile("[1-9][0-9]+[\\s][1-9][0-9]{9}$")
        phone_valid=phone_pattern.match(phone_no)
        if phone_valid:
            self.__phone=phone_no
            logging.info('Valid phone number')

        else:
            logging.info('Invalid phone number')
            raise ValueError("Invalid phone number")


if __name__ == '__main__':
    try:
        user = UserValidation()
        fname=input("Enter first name :")
        user.validate_fname(fname)
        lname= input("enter last name :")
        user.validate_lname(lname)
        email= input("Enter your email :")
        user.validate_email(email)
        phone= input("Enter your phone number  :")
        user.validate_phone(phone)
    except ValueError as e:
        logger.exception(e)
