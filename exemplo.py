
class Fisica:

    def __init__(self,velocidade = 0,tempo = 0,deslocamento = 0):
        self.velocidade = velocidade
        self.tempo = tempo
        self.deslocamento = deslocamento
    @property
    def velocidade(self):
        return self._velocidade
    @velocidade.setter 
    def velocidade(self,valor):
        self._velocidade = valor
    
    @property
    def tempo(self):
        return self._tempo
    @tempo.setter 
    def tempo(self,valor):
        self._tempo = valor
    @property 
    def deslocamento(self):
        return self._deslocamento
    @deslocamento.setter 
    def deslocamento(self,valor):
        self._deslocamento = valor
    
    def calcular(self):
        if self.velocidade == 0:
            self.velocidade = self.deslocamento / self.tempo
            print(f'Velocidade: {self.velocidade}')
        elif self.tempo == 0:
            self.tempo = self.deslocamento * self.velocidade
            print(f'Tempo: {self.tempo}')
        elif self.deslocamento == 0:
            self.deslocamento = self.tempo * self.velocidade
            print(f'Deslocamento: {self.deslocamento}')
    def dados(self):
        print('   DADOS   ')
        print('----------------------------')
        if self.velocidade == 0:
            print(f'Velocidade = ?')
        else:
             print(f'Velocidade = {self.velocidade}')
        if self.tempo == 0:
            print(f'Tempo = ? ')
        else:
             print(f'Tempo = {self.tempo}')
        if self.deslocamento == 0:
            print('Deslocamento: ?')
        else:
            print(f'Desclocamento = {self.deslocamento}')
