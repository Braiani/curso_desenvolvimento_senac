class TipoTracao:
    def __init__(self, nome, forca_propulsora):
        self.nome = nome
        self.forca_propulsora = forca_propulsora
    
    def tipo_tracao(self):
        if self.forca_propulsora == "Combustão":
            return "Automotor"
        elif self.forca_propulsora == "Energia Elétrica":
            return "Elétrico"
        elif self.forca_propulsora == "Animal":
            return "Propulsão Animal"
        elif self.forca_propulsora == "Humana":
            return "Propulsão Humana"
        elif self.forca_propulsora == "Outro veículo":
            return "Reboque/Semi-reboque"
        else:
            return "Desconhecido"
        
    def descricao_tracao(self):
        return f"Tipo de tração: {self.nome}, Força propulsora: {self.forca_propulsora}"