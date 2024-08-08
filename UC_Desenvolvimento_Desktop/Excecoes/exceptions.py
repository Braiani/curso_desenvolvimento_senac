class NumeroGigante(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print("Você não pode calcular números tão grandes!")


class Divisao:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def executar(self):
        try:
            return self.a / self.b
        except ArithmeticError:
            print("Você tentou fazer uma divisão por zero!")


class Matematica:

    def __init__(self) -> None:
        while True:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if num1 > 100 or num2 > 100:
                    raise NumeroGigante()
                
                divisao = Divisao(num1, num2)

                print(f"A divisão do número {num1} pelo {num2} é {divisao.executar()}")
            except NumeroGigante:
                continue
            except ValueError:
                print("Você não digitou um número!") 

if __name__ == "__main__":
    Matematica()