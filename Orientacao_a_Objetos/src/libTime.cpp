#include <iostream>
#include <cstring>
#include "Menus.hpp"
#include "Jogo.hpp"
#include "Jogador.hpp"
#include "Tecnico.hpp"
#include "libJogador.hpp"
#include "libTecnico.hpp"

int criarTime(Banco* bench, Time* novoTime){
	std::string teamName;
	std::cout << "Nome do Time: ";
	std::cin.ignore();
	std::getline(std::cin, teamName);
	novoTime->setNomeTime(teamName);

	short int op = 1;
	while (op != 0 && op != 6) {
		novotime_menu();
		std::cin >> op;
		switch (op)
		{
			case 0:
				break;
			case 1:
				novoTime->mostrarTime();
				break;
			case 2: {
				novoTime->adicionarJogador(addJogador(bench));
				break;
			}
			case 3: {
				novoTime->adicionarJogador(criarJogador());
				break;
				}
			case 4:
				novoTime->setTecnico(addTecnico(bench));
				break;
			case 5: {
				novoTime->setTecnico(criarTecnico());
				break;
				}
			case 6:
				return 3;
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
	return 0;
}

void editarTime(Time *team, short int *op) {
	short int opcao = 1;
	while (opcao != 0 && opcao != 5 && opcao != 6) {
		edit_menu();
		std::cin >> opcao;
		switch(opcao) {
			case 0:
				break;
			case 1:
				team->mostrarTime();
				break;
			case 2: {
				std::string novoNome;
				std::cout << "Novo nome: ";
				std::cin.ignore();
				getline(std::cin, novoNome);
				team->setNomeTime(novoNome);
				break;
			}
			case 3: {
				if (team->getTime().size() == 0) {
					std::cout << "Não existem jogadores." << std::endl;
					break;
				}
				short int excluir;
				std::cout << "Escolha o Jogador:\n";
				std::cout << team->getNomeTime() << '\n';
				team->mostrarTime();
				std::cin >> excluir;
				excluir--;
				std::list<Jogador*>::iterator it;
				it = std::next(team->getTime().begin(), excluir);
				short int op2 = 1;
				while (op2 != 0) {
					edit2_menu();
					std::cin >> op2;
					switch(op2) {
						case 0:
							break;
						case 1:
							editarJogador(*it);
							break;
						case 2:
						{
							team->getTime().erase(it);
							short int pos = (*it)->getNPosicao();
							switch(pos) {
								case 1:
									team->setGoleiro(NULL);
									break;
								case 2:
									team->getDefesa().erase(it);
									break;
								case 3:
									team->getMeiocampo().erase(it);
									break;
								case 4:
									team->getAtaque().erase(it);
									break;
							}
							op2 = 0;
						}
							break;
						default:
							std::cout << "Opção inválida.\n";
							break;
					}
				}
				break;
			}
			case 4: {
				if (!team->getTecnico()) {
					std::cout << "Não há tecnico." << std::endl;
					break;
				}
				team->setTecnico(editarTecnico(team->getTecnico()));
				break;
			}
			case 5:
				*op = 100;
				break;
			case 6:
				*op = 3;
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
}



void imprimirTimes(Jogo* j) {
	std::list<Time*>* lista = j->getTimes();
	std::list<Time*>::iterator it2;
	short int i = 1;
	for (it2 = lista->begin(); it2 != lista->end(); it2++) {
		std::cout << i << ".\t" << (*it2)->getNomeTime() << '\n';
		i++;
	}
}
