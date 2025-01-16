#include "libJogador.hpp"
#include <iostream>
#include "Banco.hpp"
#include "Menus.hpp"

#define LIN 10
#define COL 30

Jogador* addJogador(Banco* bench) {
	unsigned short int jog;
	std::list<Jogador*>::iterator it;
	unsigned short int tipo;
	std::cout << "\nSelecione a Categoria de Jogador:" << '\n';
	addJog();
	std::cin >> tipo;
	switch(tipo) {
		case 0:
			return nullptr;
		case 1:
			std::cout << "Selecione o Jogador: " << '\n';
			imprimirJogadores(bench->getGoleiros());
			std::cin >> jog;
			jog--;
			it = std::next(bench->getGoleiros()->begin(), jog);
			break;
		case 2:
			std::cout << "Selecione o Jogador: " << '\n';
			imprimirJogadores(bench->getDefensores());
			std::cin >> jog;
			jog--;
			it = std::next(bench->getDefensores()->begin(), jog);
			break;
		case 3:
			std::cout << "Selecione o Jogador: " << '\n';
			imprimirJogadores(bench->getMeiocampistas());
			std::cin >> jog;
			jog--;
			it = std::next(bench->getMeiocampistas()->begin(), jog);
			break;
		case 4:
			std::cout << "Selecione o Jogador: " << '\n';
			imprimirJogadores(bench->getAtacantes());
			std::cin >> jog;
			jog--;
			it = std::next(bench->getAtacantes()->begin(), jog);
			break;
		default:
			std::cout << "Opção inválida.\n";
			break;
	}
	return *it;
}

Jogador* criarJogador(){
    std::string nome;
	unsigned short int posicao;
	std::string time;

	std::cout << "Nome: ";
	std::cin.ignore();
	getline(std::cin, nome);
	
	std::cout << "Posição:\n";
	std::cout << "\t1. Goleiro" << '\n';
	std::cout << "\t2. Defesa" << '\n';
	std::cout << "\t3. Meio-Campo" << '\n';
	std::cout << "\t4. Atacante" << '\n';
	std::cin >> posicao;
	if(posicao < 1 || posicao > 4)
		std::cout << "Opção inválida." << '\n';
	
	std::cout << "Time: ";
	std::cin.ignore();
	getline(std::cin, time);

	Jogador* j1 = new Jogador(nome, posicao, time);
		
	unsigned short int opcao = 0;
	while(opcao != 4){
		atributosJogador();
		std::cin >> opcao;
		switch(opcao){
			case 1:{
			    std::string pais;
			    std::cout << "País: ";
				std::cin.ignore();
				getline(std::cin, pais);
				j1->setPais(pais);
		       	}
		       	break;
			case 2:{
				unsigned short int idade;
				std::cout << "Idade: ";
				std::cin >> idade;
				j1->setIdade(idade);
			    }
		       	break;
			case 3:{
				unsigned short int numero;
				std::cout << "Número da Camisa: ";
				std::cin >> numero;
				j1->setNumCamisa(numero);
			       }
		       	break;
			case 4:
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
	delete j1;
	return j1;
}

Jogador* editarJogador(Jogador* j) {
	if (!j)
		return nullptr;
	short int op = 1;
	while (op != 0) {
		editJogador_menu();
		std::cin >> op;
		switch(op) {
			case 0:
				break;
			case 1: {
				std::string novoNome;
				std::cout << "Novo Nome: ";
				std::cin.ignore();
				getline(std::cin, novoNome);
				j->setNome(novoNome);
			}
				break;
			case 2: {
				unsigned short int novaIdade;
				std::cout << "Nova Idade: ";
				std::cin >> novaIdade;
				j->setIdade(novaIdade);
			}
				break;
			case 3: {
				std::string novoPais;
				std::cout << "Novo País: ";
				std::cin.ignore();
				getline(std::cin, novoPais);
				j->setPais(novoPais);
			}
				break;
			case 4: {
				unsigned short int novoNum;
				std::cout << "Novo Número: ";
				std::cin >> novoNum;
				j->setNumCamisa(novoNum);
			}
				break;
			case 5: {
				unsigned short int novaPos;
				std::cout << "Nova Posição: " << '\n';
				std::cout << "\t1. Goleiro" << '\n';
				std::cout << "\t2. Defesa" << '\n';
				std::cout << "\t3. Meio-Campo" << '\n';
				std::cout << "\t4. Atacante" << '\n';
				std::cin >> novaPos;
				j->setPosicao(novaPos);
			}
				break;
			case 6: {
				std::string novoTime;
				std::cout << "Novo Time: ";
				std::cin.ignore();
				getline(std::cin, novoTime);
				j->setTime(novoTime);
			}
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
	return j;
}

void imprimirJogador(Jogador* j) {
	if (j) {
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
					std::cout << "Nome: " << j->getNome();
					h = h + 6 + j->getNome().size();
				}
				if (i == 4 && h == 3) {
					std::cout << "País: " << j->getPais();
					h = h + 6 + j->getPais().size();
				}
				if (i == 5 && h == 3) {
					std::cout << j->getPosicao();
					h = h + j->getPosicao().size();
				}
				if (i == 6 && h == 3) {
					std::cout << "Camisa " << j->getNumCamisa();
					if (j->getNumCamisa() < 10)
						h = h + 8;
					else
						h = h + 9;
				}
				if (i == 7 && h == 3) {
					std::cout << j->getTime();
					h = h + j->getTime().size();
				}
			}
			std::cout << '\n';
		}
	}
}

void imprimirJogadores(std::list<Jogador*>* lista) {
	unsigned short int i = 1;
	std::list<Jogador*>::iterator it;
	for (it = lista->begin(); it != lista->end(); it++) {
		std::cout << '\n' << "\t-----" << i << "-----" << '\n';
		imprimirJogador(*it);
		i++;
	}
}
