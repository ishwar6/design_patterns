# concepts/data_validator.py

import re

class DataValidator:
    """A class for validating various types of data."""

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate an email address using a regular expression.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate a phone number to ensure it contains only digits.

        Args:
            phone (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid (only digits), False otherwise.
        """
        return phone.isdigit() and len(phone) >= 10

    @staticmethod
    def validate_zip_code(zip_code: str) -> bool:
        """Validate a U.S. zip code.

        Args:
            zip_code (str): The zip code to validate.

        Returns:
            bool: True if the zip code is valid (5 or 9 digits), False otherwise.
        """
        return re.match(r'^\d{5}(-\d{4})?$', zip_code) is not None

def main():
    """Demonstration of the DataValidator class functionalities."""
    test_emails = ['test@example.com', 'invalid-email', 'user@domain.co.uk']
    test_phones = ['1234567890', '123abc', '123']
    test_zip_codes = ['12345', '12345-6789', '1234', '123456']

    print("Email Validation:")
    for email in test_emails:
        print(f"{email}: {DataValidator.validate_email(email)}")

    print("\nPhone Validation:")
    for phone in test_phones:
        print(f"{phone}: {DataValidator.validate_phone(phone)}")

    print("\nZip Code Validation:")
    for zip_code in test_zip_codes:
        print(f"{zip_code}: {DataValidator.validate_zip_code(zip_code)}")

if __name__ == "__main__":
    main()