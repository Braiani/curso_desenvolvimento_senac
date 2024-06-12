from Eletrico import Eletrico
from Automotor import Automotor

tesla = Eletrico(1500, 520, "Particular", "Tesla", "Model x", 2024, "Azul")
ferrari = Automotor("Gasolina", 200, "Aluguel", "Ferrari", "F250", 2023, "Vermelha")

ferrari.exibir_informacoes()
print()
print()
tesla.exibir_informacoes()