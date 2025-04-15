parametrosCompilacao = -Wall
nomePrograma = simulacao

all: $(nomePrograma)

$(nomePrograma): main.o Banco.o Comparadores.o Estrelas.o Jogador.o Jogo.o libJogador.o libTecnico.o libTime.o Menus.o Pessoa.o Tecnico.o Time.o
	g++ -o $(nomePrograma) main.o Banco.o Comparadores.o Estrelas.o Jogador.o Jogo.o libJogador.o libTecnico.o libTime.o Menus.o Pessoa.o Tecnico.o Time.o $(parametrosCompilacao)

main.o: main.cpp
	g++ -c main.cpp $(parametrosCompilacao)

Banco.o: Banco.hpp Banco.cpp
	g++ -c Banco.cpp $(parametrosCompilacao)

Comparadores.o: Comparadores.hpp Comparadores.cpp
	g++ -c Comparadores.cpp $(parametrosCompilacao)

Estrelas.o: Estrelas.hpp Estrelas.cpp
	g++ -c Estrelas.cpp $(parametrosCompilacao)

Jogador.o: Jogador.hpp Jogador.cpp
	g++ -c Jogador.cpp $(parametrosCompilacao)

Jogo.o : Jogo.hpp Jogo.cpp
	g++ -c Jogo.cpp $(parametrosCompilacao)

libJogador.o : libJogador.hpp libJogador.cpp
	g++ -c libJogador.cpp $(parametrosCompilacao)

libTecnico.o : libTecnico.hpp libTecnico.cpp
	g++ -c libTecnico.cpp $(parametrosCompilacao)

libTime.o : libTime.hpp libTime.cpp
	g++ -c libTime.cpp $(parametrosCompilacao)

Menus.o : Menus.hpp Menus.cpp
	g++ -c Menus.cpp $(parametrosCompilacao)

Pessoa.o: Pessoa.hpp Pessoa.cpp
	g++ -c Pessoa.cpp $(parametrosCompilacao)

Tecnico.o: Tecnico.hpp Tecnico.cpp
	g++ -c Tecnico.cpp $(parametrosCompilacao)

Time.o: Time.hpp Time.cpp
	g++ -c Time.cpp $(parametrosCompilacao);

clean:
	rm -f *.o *.gch $(nomePrograma)
