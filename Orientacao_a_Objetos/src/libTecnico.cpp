#include "libTecnico.hpp"
#include <iostream>
#include "Menus.hpp"

#define LIN 10
#define COL 30

Tecnico* addTecnico(Banco* bench) {
	unsigned short int tec;
	std::list<Tecnico*>::iterator it;
	std::cout << "Selecione o Tecnico: " << '\n';
	imprimirTecnicos(bench->getTecnicos());
	std::cin >> tec;
	tec--;
	it = std::next(bench->getTecnicos()->begin(), tec);
	return *it;
}

Tecnico* criarTecnico() {
	std::string nome;
	std::string time;

	std::cout << "Nome: ";
	std::cin.ignore();
	getline(std::cin, nome);
	std::cout << "Time: ";
	std::cin.ignore();
	getline(std::cin, time);

	Tecnico* t = new Tecnico(nome, time);

	unsigned short int opcao = 0;
	while(opcao != 3){
		atributosTecnico();
		std::cin >> opcao;
		switch(opcao) {
			case 1: {
				std::string pais;
				std::cout << "País: ";
				std::cin.ignore();
				getline(std::cin, pais);
				t->setPais(pais);
				break;
			}
			case 2: {
				short int xp;
				std::cout << "Experiência (em anos): ";
				std::cin >> xp;
				t->setXp(xp);
				break;
			}
			case 3:
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
	delete t;
	return t;
}

Tecnico* editarTecnico(Tecnico* t) {
	if (!t)
		return NULL;
	short int op = 1;
	while (op != 0) {
		editTecnico_menu();
		std::cin >> op;
		switch (op) {
			case 0:
				break;
			case 1: {
				std::string novoNome;
				std::cout << "Novo Nome: ";
				std::cin.ignore();
				getline(std::cin, novoNome);
				t->setNome(novoNome);
				break;
			}
			case 2: {
				unsigned short int novaIdade;
				std::cout << "Nova Idade: ";
				std::cin >> novaIdade;
				t->setIdade(novaIdade);
				break;
			}
			case 3: {
				std::string novoPais;
				std::cout << "Novo País: ";
				std::cin.ignore();
				getline(std::cin, novoPais);
				t->setPais(novoPais);
				break;
			}
			case 4: {
				std::string novoTime;
				std::cout << "Novo Time: ";
				std::cin.ignore();
				getline(std::cin, novoTime);
				t->setTime(novoTime);
				break;
			}
			case 5: {
				short int novoXp;
				std::cout << "Novo Tempo de Experiência (em anos): ";
				std::cin >> novoXp;
				t->setXp(novoXp);
				break;
			}
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
	return t;
}

void imprimirTecnico(Tecnico* t) {
	if (t) {
		char carta[LIN][COL];
		for (int i = 0; i < LIN; i++)
			for (int j = 0; j < COL; j++)
				carta[i][j] = ' ';

		for (int i = 1; i < COL-2; i++) {
			carta[LIN-1][i] = '_';
			carta[LIN-2][i] = '_';
			carta[0][i] = '_';
			carta[1][i] = '_';
		}
		for(int j = 1; j < LIN; j++) {
			carta[j][0] = '|';
			carta[j][1] = ' ';
			carta[j][2] = '|';
			carta[j][COL-2] = '|';
			carta[j][COL-3] = ' ';
			carta[j][COL-4] = '|';
		}

		carta[1][2] = carta[1][COL-4] = carta[LIN-1][2] = carta[LIN-1][COL-4] = ' ';
		carta[LIN-1][1] = carta[LIN-1][2] = carta[LIN-1][COL-3] = carta[LIN-1][COL-4] = '_';

		for (int i = 0; i < LIN; i++) {
			for (int h = 0; h < COL; h++) {
				std::cout << carta[i][h];
				if (i == 3 && h == 3) {
					for(int i = 0; i < t->getEstrelas(); i++)
						std::cout << "*";
					h = h + t->getEstrelas();
				}
				if (i == 4 && h == 3) {
					std::cout << "Nome: " << t->getNome();
					h = h + 6 + t->getNome().size();
				}
				if (i == 5 && h == 3) {
					std::cout << "País: " << t->getPais();
					h = h + 6 + t->getPais().size();
				}
				if (i == 6 && h == 3) {
					std::cout << t->getTime();
					h = h + t->getTime().size();
				}
			}
			std::cout << '\n';
		}
	}
}

void imprimirTecnicos(std::list<Tecnico*>* lista) {
	if (lista->size() <= 0) {
		std::cout << "Não existes técnicos." << std::endl;
	}
	unsigned short int i = 1;
	std::list<Tecnico*>::iterator it;
	for (it = lista->begin(); it != lista->end(); it++) {
		std::cout << '\n' << "\t-----" << i << "-----" << '\n';
		imprimirTecnico(*it);
		i++;
	}
}
