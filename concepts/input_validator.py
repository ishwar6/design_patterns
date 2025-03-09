# concepts/data_validator.py

import re

class DataValidator:
    """A class to perform various validations on data inputs."""

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate an email address using regex.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_phone_number(phone: str) -> bool:
        """
        Validate a phone number as a US number.

        Args:
            phone (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        phone_regex = r'^\+?1?\d{10}$'
        return re.match(phone_regex, phone) is not None

    @staticmethod
    def is_valid_integer(value: str) -> bool:
        """
        Validate if a string is a valid integer.

        Args:
            value (str): The string to validate.

        Returns:
            bool: True if the string is a valid integer, False otherwise.
        """
        return value.isdigit() or (value.startswith('-') and value[1:].isdigit())

    @staticmethod
    def is_valid_url(url: str) -> bool:
        """
        Validate a URL using regex.

        Args:
            url (str): The URL to validate.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        url_regex = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*$'
        return re.match(url_regex, url) is not None


if __name__ == "__main__":
    # Sample usage of the DataValidator class

    emails = ["test@example.com", "invalid-email.com"]
    phone_numbers = ["1234567890", "+11234567890", "invalid-phone"]
    integers = ["123", "-456", "12.34", "hello"]
    urls = ["https://www.example.com", "invalid-url"]

    print("Email Validations:")
    for email in emails:
        print(f"{email}: {DataValidator.is_valid_email(email)}")

    print("\nPhone Number Validations:")
    for phone in phone_numbers:
        print(f"{phone}: {DataValidator.is_valid_phone_number(phone)}")

    print("\nInteger Validations:")
    for value in integers:
        print(f"{value}: {DataValidator.is_valid_integer(value)}")

    print("\nURL Validations:")
    for url in urls:
        print(f"{url}: {DataValidator.is_valid_url(url)}")