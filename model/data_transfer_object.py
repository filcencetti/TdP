from dataclasses import dataclass

# Data Transfer Object (DTO)
@dataclass
class DTO_name:
    istanza1 : int
    istanza2 : str
    istanza3 : float

    def __str__(self):
        return f"{self.istanza2}"

    def __hash__(self):
        return hash(self.istanza1)

    def __eq__(self, other):
        return self.istanza1 == other.istanza1