# Chain of Responsibility Pattern

## Overview

The Chain of Responsibility is a behavioral design pattern that allows passing requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

## Definition

In the Chain of Responsibility pattern, multiple objects are given the chance to process a request or command. The pattern decouples senders and receivers of a request based on the type of request or other processing criteria.

## Components

- **Handler**: An interface defining how requests are handled.
- **Concrete Handler**: Classes implementing the Handler interface, processing the requests they are responsible for, and passing others to the next handler in the chain.
- **Client**: The originator of the request, which is passed along the chain of handlers.

## Benefits

- **Decoupling**: The sender of a request is decoupled from its receivers.
- **Flexibility**: Handlers can be added or changed dynamically without affecting the overall system.
- **Responsibility Segregation**: Each handler focuses on its specific logic or area of expertise.
- **Scalability**: Easy to extend and modify with new handlers.

## Example: ATM Cash Dispensing Mechanism

### Scenario

An ATM system needs to dispense a specific amount of cash, which could involve multiple denominations. The CoR pattern can be used to create a chain of handlers, each responsible for dispensing a specific denomination.

### Implementation

1. **Handler Interface (`ATMHandler`)**: An abstract class with a method `dispense(amount)`.

2. **Concrete Handlers**:
   - `Denomination2000Handler`, `Denomination500Handler`, `Denomination100Handler`, each responsible for dispensing notes of Rs 2000, Rs 500, and Rs 100 respectively.

3. **Chain Setup**:
   - The handlers are linked in a chain (e.g., 2000 -> 500 -> 100) to handle a combination of denominations.

4. **Client Code**:
   - The client code initiates the request to dispense a certain amount, which is processed through the chain of handlers.

### Code Snippet

```python
class Denomination2000Handler(ATMHandler):
    def dispense(self, amount):
        # Logic to dispense Rs 2000 notes
        pass

# Additional handlers and client code : check in atm.py file please. 
