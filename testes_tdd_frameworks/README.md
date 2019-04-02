Testes Unitarios com Python 


framework build-in do python unittest

Lembrando que o teste deve ter o prefixo test_* para que a biblioteca unittest a reconheça como um teste.

A Classe de teste tem que herdar de (TestCase):

Como rodar testes unitarios pelo terminal

python -m unittest src/leilao/test_avaliador.py

setUp que é executado antes de cada método de testes. 

Os métodos tearDown e tearDownClass são muito utilizados em testes que integram duas partes do sistema - banco de dados, sistemas externos, ou então desejamos fechar uma conexão que foi aberta.

Esses tipos de testes, que verificam como duas partes do sistema se integram, são chamados de testes de integração.

formas comuns de nomear os testes, neste link https://dzone.com/articles/7-popular-unit-test-naming de um artigo em inglês mostra algumas formas de nomeação.

https://en.wikipedia.org/wiki/Law_of_Demeter


http://blog.alura.com.br/como-fazer-copia-de-lista-python/

Biblioteca para suite de testes funcionais

https://docs.pytest.org/en/latest/

Instalar pytest

Neste post https://blog.alura.com.br/montando-cenarios-de-testes-com-o-pytest são mostrados algumas outras fixtures.
