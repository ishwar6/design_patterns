import json
from datetime import datetime

class Transaction:
    """
    Represents a financial transaction.
    """
    def __init__(self, amount, description):
        """
        Initializes a transaction with amount and description.
        """
        self.amount = amount
        self.description = description
        self.date = datetime.now().isoformat()

    def to_dict(self):
        """
        Converts the transaction to a dictionary.
        """
        return {
            'amount': self.amount,
            'description': self.description,
            'date': self.date
        }

class TransactionLogger:
    """
    Logs transactions to a JSON file.
    """
    def __init__(self, filename):
        """
        Initializes the logger with a specific filename.
        """
        self.filename = filename

    def log_transaction(self, transaction):
        """
        Logs a transaction by appending it to the JSON file.
        """
        with open(self.filename, 'a') as file:
            json.dump(transaction.to_dict(), file)
            file.write('\n')

    def read_transactions(self):
        """
        Reads all transactions from the JSON file.
        """
        transactions = []
        with open(self.filename, 'r') as file:
            for line in file:
                transactions.append(json.loads(line.strip()))
        return transactions

if __name__ == '__main__':
    logger = TransactionLogger('transactions.json')
    t1 = Transaction(100, 'Deposit')
    t2 = Transaction(50, 'Withdrawal')
    logger.log_transaction(t1)
    logger.log_transaction(t2)
    all_transactions = logger.read_transactions()
    print(all_transactions)