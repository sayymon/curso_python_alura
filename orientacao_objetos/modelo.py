class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    #Equivale ao Iterable
    #Exemplo de dondle metode duck type
    def __getitem__(self, item):
        return self._programas[item]    
    
    def __len__(self):
        return len(self._programas)
    
    __
    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)
    
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Filme(Programa) :
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
     return f'{self.nome} - {self.duracao} Mins: Likes {self.likes}'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
     return f'{self.nome} - {self.temporadas} Temporadas: Likes {self.likes}'
 
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
#print(f'{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}')
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()
#print(f'{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}')

filmes_e_series = [vingadores,atlanta]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)
print(atlanta in playlist_fim_de_semana)
print(len(playlist_fim_de_semana))
for programa in playlist_fim_de_semana:
    print(programa)