# behavioral/decision_tree.py

from typing import List, Optional, Tuple, Any, Dict
from collections import Counter

class DecisionNode:
    """
    A class representing a node in the decision tree.
    
    Attributes:
        feature (Optional[int]): The index of the feature to split on.
        threshold (Optional[float]): The threshold value for the split.
        left (Optional[DecisionNode]): The left subtree.
        right (Optional[DecisionNode]): The right subtree.
        value (Optional[Any]): The predicted value at leaf node.
    """
    def __init__(self, feature: Optional[int] = None, threshold: Optional[float] = None,
                 left: Optional['DecisionNode'] = None, right: Optional['DecisionNode'] = None,
                 value: Optional[Any] = None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTreeClassifier:
    """
    A simple Decision Tree Classifier.
    
    Methods:
        fit(X: List[List[float]], y: List[Any]): Train the decision tree model.
        predict(X: List[List[float]]) -> List[Any]: Make predictions based on the input features.
    """
    def __init__(self, max_depth: Optional[int] = None):
        self.root = None
        self.max_depth = max_depth

    def fit(self, X: List[List[float]], y: List[Any]) -> None:
        """
        Train the decision tree model on provided data.

        Args:
            X (List[List[float]]): Feature data.
            y (List[Any]): Target labels.
        """
        self.root = self._build_tree(X, y)

    def _build_tree(self, X: List[List[float]], y: List[Any], depth: int = 0) -> DecisionNode:
        """
        Recursively build the decision tree.

        Args:
            X (List[List[float]]): Feature data.
            y (List[Any]): Target labels.
            depth (int): Current depth in the tree.

        Returns:
            DecisionNode: Root of the subtree.
        """
        if len(set(y)) == 1 or (self.max_depth and depth >= self.max_depth):
            return DecisionNode(value=Counter(y).most_common(1)[0][0])

        feature_index, threshold = self._best_split(X, y)
        if feature_index is None:
            return DecisionNode(value=Counter(y).most_common(1)[0][0])

        left_indices = [i for i in range(len(X)) if X[i][feature_index] < threshold]
        right_indices = [i for i in range(len(X)) if X[i][feature_index] >= threshold]

        left_node = self._build_tree([X[i] for i in left_indices], [y[i] for i in left_indices], depth + 1)
        right_node = self._build_tree([X[i] for i in right_indices], [y[i] for i in right_indices], depth + 1)

        return DecisionNode(feature=feature_index, threshold=threshold, left=left_node, right=right_node)

    def _best_split(self, X: List[List[float]], y: List[Any]) -> Tuple[Optional[int], Optional[float]]:
        """
        Find the best feature and threshold to split on.

        Args:
            X (List[List[float]]): Feature data.
            y (List[Any]): Target labels.

        Returns:
            Tuple[Optional[int], Optional[float]]: Index of the feature and the threshold for splitting.
        """
        best_gain = 0
        best_feature = None
        best_threshold = None
        base_gini = self._gini_index(y)

        for feature_index in range(len(X[0])):
            thresholds = set(x[feature_index] for x in X)
            for threshold in thresholds:
                left_labels = [y[i] for i in range(len(y)) if X[i][feature_index] < threshold]
                right_labels = [y[i] for i in range(len(y)) if X[i][feature_index] >= threshold]

                if not left_labels or not right_labels:
                    continue

                left_gini = self._gini_index(left_labels)
                right_gini = self._gini_index(right_labels)

                gain = base_gini - (len(left_labels) / len(y) * left_gini + len(right_labels) / len(y) * right_gini)

                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_index
                    best_threshold = threshold

        return best_feature, best_threshold

    def _gini_index(self, y: List[Any]) -> float:
        """
        Calculate the Gini index for a list of labels.

        Args:
            y (List[Any]): Target labels.

        Returns:
            float: Gini index.
        """
        label_count = Counter(y)
        total_count = len(y)
        return 1 - sum((count / total_count) ** 2 for count in label_count.values())

    def predict(self, X: List[List[float]]) -> List[Any]:
        """
        Make predictions based on the input features.

        Args:
            X (List[List[float]]): Feature data.

        Returns:
            List[Any]: Predicted target labels.
        """
        return [self._predict_instance(instance) for instance in X]

    def _predict_instance(self, instance: List[float]) -> Any:
        """
        Predict the label for a single instance.

        Args:
            instance (List[float]): Feature data for one instance.

        Returns:
            Any: Predicted label.
        """
        node = self.root
        while node.value is None:
            if instance[node.feature] < node.threshold:
                node = node.left
            else:
                node = node.right
        return node.value

# Sample usage:
if __name__ == "__main__":
    features = [[2.5, 2.4], [1.0, 1.1], [1.5, 1.5], [3.0, 3.0], [2.0, 2.2]]
    labels = [0, 0, 0, 1, 1]
    
    tree = DecisionTreeClassifier(max_depth=3)
    tree.fit(features, labels)
    
    test_data = [[1.5, 1.5], [3.1, 3.1]]
    predictions = tree.predict(test_data)
    
    print(predictions)  # Expected output: [0, 1]