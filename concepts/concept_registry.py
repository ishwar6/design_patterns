class Concept:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class ConceptManager:
    def __init__(self):
        self.concepts = {}

    def add_concept(self, name, description):
        if name not in self.concepts:
            self.concepts[name] = Concept(name, description)

    def remove_concept(self, name):
        if name in self.concepts:
            del self.concepts[name]

    def get_concept(self, name):
        return self.concepts.get(name)

    def list_concepts(self):
        return [str(concept) for concept in self.concepts.values()]


if __name__ == "__main__":
    manager = ConceptManager()
    manager.add_concept("Encapsulation", "The bundling of data with the methods that operate on that data.")
    manager.add_concept("Polymorphism", "The ability of different classes to be treated as instances of the same class through a common interface.")
    
    for concept in manager.list_concepts():
        print(concept)

    manager.remove_concept("Encapsulation")
    
    print("After removal:")
    for concept in manager.list_concepts():
        print(concept)