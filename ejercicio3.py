class Vehiculo:
    
    def init(self, patente: int, descripcion: str):
        self.patente = patente
        self.descripcion = descripcion
    
    def mostrar(self):
        print (self.patente, self.descripcion)

    def validarPatente(self):
        if len(self.patente) == 6 or len(self.patente) == 8:
            return (True)
        return (False)


class Estadia():
    def init(self, Vehiculo,  horaEntrada, horaSalida):
        self.Vehiculo = Vehiculo
        self.horaEntrada = horaEntrada
        self.horaSalida = horaSalida

    def mostrar(self):
        print(self.horaEntrada, self.horaSalida)
        self.Vehiculo.mostrar

    def calcularTarifaTotal(self, tarifaHora: float):
        self.tarifaHora = tarifaHora
        if self.Vehiculo.validarPatente == True:
            return ((self.horaSalida - self.horaEntrada)* tarifaHora)
        elif self.horaSalida < self.horaEntrada:
            return ("Error de tiempo")
        else:
            return ("Error")