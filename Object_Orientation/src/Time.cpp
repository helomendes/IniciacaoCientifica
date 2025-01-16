#include <iostream>
#include "Jogador.hpp"
#include "Time.hpp"
#include "libJogador.hpp"
#include "libTecnico.hpp"
#include "Comparadores.hpp"

Time::Time() {}

Time::Time(const std::string& nomeTime) {
	this->nomeTime = nomeTime;
}

std::string Time::getNomeTime() const {
	return nomeTime;
}

void Time::setNomeTime(const std::string& nomeTime) {
	this->nomeTime = nomeTime;
}

void Time::mostrarTime() {
	system("clear");
	std::cout << "\t" << getNomeTime() << "\n\n";
	if (time.size() <= 0) {
		std::cout << "Não existem jogadores\n\n";
	} else {
		if (coach)
			std::cout << "\n\tTECNICO:\n";
		imprimirTecnico(coach);
		if (goleiro)
			std::cout << "\n\tGOLEIRO:\n";
		imprimirJogador(goleiro);
		if (defesa.size() > 0)
			std::cout << "\n\tDEFESA:\n";
		imprimirJogadores(&defesa);
		if (meioCampo.size() > 0)
			std::cout << "\n\tMEIO CAMPO:\n";
		imprimirJogadores(&meioCampo);
		if (ataque.size() > 0)
			std::cout << "\n\tATAQUE:\n";
		imprimirJogadores(&ataque);
		if (reserva.size() > 0)
			std::cout << "\n\tRESERVAS:\n";
		imprimirJogadores(&reserva);
	}
}

void Time::adicionarJogador(Jogador* novoJogador) {
	if (novoJogador) {
		time.push_back(novoJogador);
		int posicao = novoJogador->getNPosicao();
		unsigned char op = 'x';
		switch(posicao)
		{
			case 1:
				if (goleiro) {
					std::cout << "Substituir? (y/n) ";
					while (op == 'x') {
						std::cin >> op;
						if (op == 'y' || op == 'Y') {
							goleiro = novoJogador;
						} else if (op == 'n' || op == 'N') {
							reserva.push_back(novoJogador);
						} else {
							std::cout << "Inválido\n";
							op = 'x';
						}
					}
				} else {
					goleiro = novoJogador;
				}
				break;
			case 2:
				if (defesa.size() < 4) {
					defesa.push_back(novoJogador);
				} else {
					std::cout << "Substituir? (y/n) ";
					while (op == 'x') {
						std::cin >> op;
						if (op == 'y' || op == 'Y') {
							unsigned short int jog;
							std::cout << "Escolha o Jogador a ser Substituído: " << '\n';
							imprimirJogadores(&defesa);
							std::cin >> jog;
							jog--;
							std::list<Jogador*>::iterator it;
							it = std::next(defesa.begin(), jog);
							defesa.erase(it);
							defesa.push_back(novoJogador);
							//defesa.sort(comparadorJogadores);
						} else if (op == 'n' || op == 'N') {
							reserva.push_back(novoJogador);
						} else {
							std::cout << "Inválido\n";
							op = 'x';
						}
					}
				}
				break;
			case 3:
				if (meioCampo.size() < 4) {
					meioCampo.push_back(novoJogador);
				} else {
					std::cout << "Substituir? (y/n) ";
					while (op == 'x') {
						std::cin >> op;
						if (op == 'y' || op == 'Y') {
							unsigned short int jog;
							std::cout << "Escolha o Jogador a ser Substituído: " << '\n';
							imprimirJogadores(&meioCampo);
							std::cin >> jog;
							jog--;
							std::list<Jogador*>::iterator it;
							it = std::next(meioCampo.begin(), jog);
							meioCampo.erase(it);
							meioCampo.push_back(novoJogador);
							//meioCampo.sort(comparadorJogadores);
						} else if (op == 'n' || op == 'N') {
							reserva.push_back(novoJogador);
						} else {
							std::cout << "Inválido\n";
							op = 'x';
						}
					}
				}
				break;
			case 4:
				if (ataque.size() < 2) {
					ataque.push_back(novoJogador);
				} else {
					std::cout << "Substituir? (y/n) ";
					while (op == 'x') {
						std::cin >> op;
						if (op == 'y' || op == 'Y') {
							unsigned short int jog;
							std::cout << "Escolha o Jogador a ser Substituído: " << '\n';
							imprimirJogadores(&ataque);
							std::cin >> jog;
							jog--;
							std::list<Jogador*>::iterator it;
							it = std::next(ataque.begin(), jog);
							ataque.erase(it);
							ataque.push_back(novoJogador);
							//ataque.sort(comparadorJogadores);
						} else if (op == 'n' || op == 'N') {
							reserva.push_back(novoJogador);
						} else {
							std::cout << "Inválido\n";
							op = 'x';
						}
					}
				}
				break;
			default:
				std::cout << "Opção inválida.\n";
				break;
		}
	}
}

void Time::setGoleiro(Jogador* novoGoleiro) {
	goleiro = novoGoleiro;
}

Jogador* Time::getGoleiro() const {
	return goleiro;
}

std::list<Jogador*> Time::getDefesa() const {
	return defesa;
}

std::list<Jogador*> Time::getMeiocampo() const {
	return meioCampo;
}

std::list<Jogador*> Time::getAtaque() const {
	return ataque;
}

std::list<Jogador*> Time::getReserva() const {
	return reserva;
}

std::list<Jogador*> Time::getTime() const {
	return time;
}

Tecnico* Time::getTecnico() const {
	return coach;
}

void Time::setTecnico(Tecnico* novoCoach) {
	coach = novoCoach;
}
