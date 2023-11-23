# how to implement payment processer without strategy pattern: 

class PaymentProcessor:
    def execute_payment(self, amount, payment_type):
        if payment_type == "credit_card":
            return f"Processing Rs {amount} via Credit Card"
        elif payment_type == "debit_card":
            return f"Processing Rs {amount} via Debit Card"
        elif payment_type == "crypto":
            return f"Processing Rs {amount} via Crypto"
        else:
            raise ValueError("Unsupported payment method")


processor = PaymentProcessor()
print(processor.execute_payment(100, "credit_card"))
print(processor.execute_payment(10, "crypto"))


# Lack of Flexibility and Scalability
# Any change in a payment method's process would require changes in the PaymentProcessor class.
# Adding new payment methods over time would make the class increasingly complex and harder to maintain.
# Testing becomes harder as the class grows in size with more payment methods.
# violates open close: the class is not closed for modification whenever new functionality is added.
