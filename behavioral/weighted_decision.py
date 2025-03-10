# behavioral/decision_maker.py

from typing import List, Any, Dict

class DecisionMaker:
    """
    A class to facilitate decision-making based on a criteria-weighted voting mechanism.
    """
    
    def __init__(self, options: List[str], weights: Dict[str, float]) -> None:
        """
        Initialize the DecisionMaker with options and their associated weights.
        
        :param options: A list of options to vote on.
        :param weights: A dictionary where keys are option names and values are their weights.
        """
        self.options = options
        self.weights = weights

    def validate_inputs(self) -> None:
        """
        Validate that all options have corresponding weights and that weights are positive.
        
        :raises ValueError: If any option is missing a weight or if any weight is negative or zero.
        """
        for option in self.options:
            if option not in self.weights:
                raise ValueError(f"Weight for option '{option}' is missing.")
            if self.weights[option] <= 0:
                raise ValueError(f"Weight for option '{option}' must be positive.")
    
    def make_decision(self) -> Any:
        """
        Make a decision based on the weighted options.
        
        :return: The option with the highest weighted score.
        """
        self.validate_inputs()
        total_weight = sum(self.weights[option] for option in self.options)
        weighted_scores = {option: self.weights[option] / total_weight for option in self.options}
        decision = max(weighted_scores, key=weighted_scores.get)
        return decision


# Sample usage
if __name__ == "__main__":
    options = ["Coffee", "Tea", "Juice"]
    weights = {
        "Coffee": 3,
        "Tea": 2,
        "Juice": 1
    }

    decision_maker = DecisionMaker(options, weights)
    decision = decision_maker.make_decision()
    print(f"Selected option: {decision}")