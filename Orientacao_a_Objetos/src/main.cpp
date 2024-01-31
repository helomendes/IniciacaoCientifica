#include <iostream>
#include "Jogo.hpp"
#include "Banco.hpp"
#include "Time.hpp"
#include "Jogador.hpp"
#include "libTime.hpp"
#include "Menus.hpp"
#include "libJogador.hpp"

int main() {
	Jogo* game = new Jogo();
	Time* team = new Time();
	short int op = 0;
	while (op != 3) {
		system("clear");
		menu();
		std::cin >> op;
		switch(op) {
			case 1:{
				//criar time
				op = criarTime(game->getBanco(), team);
				game->adicionarTime(team);
				break;
			}
			case 2: {
				//continuar
				system("clear");
				size_t t;
				std::cout << "digite 0 para voltar\n\n";
				if (game->getTimes()->size() <= 0) {
					std::cout << "Não existem times." << std::endl;
					std::cin >> t;
				} else {
	  			    	std::cout << "Selecione o time:\n";
					imprimirTimes(game);
					std::cin >> t;
					while (t > game->getTimes()->size() && t != 0) 
						std::cin >> t;
					if (t != 0) {
						t = t-1;
						std::list<Time*>::iterator it = std::next(game->getTimes()->begin(), t);
						editarTime(*it, &op);
						if (op == 100) {
							game->adicionarTime(*it);
							game->removerTime(t);
						}
					}
				}
				break;
			}
			case 3:
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
	delete team;
	delete game;
	return 0;
}
