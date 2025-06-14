from dataclasses import dataclass

# Data Transfer Object (DTO)
@dataclass
class DTO_name:
    istanza1 : int # chiave primaria dell'oggetto
    istanza2 : str
    istanza3 : float

    def __str__(self):
        return f"{self.istanza2}" # cosa visualizzo quando chiamo l'oggetto

    def __hash__(self):
        return hash(self.istanza1) # definisce la chiave primaria dell'oggetto

    def __eq__(self, other):
        return self.istanza1 == other.istanza1 # confronta la chiave primaria dei due oggetti per verificare che siano lo stesso