#include "Comparadores.hpp"

bool comparadorJogadores(const Jogador* j1, const Jogador* j2) {
	if (j1->getNome() < j2->getNome())
		return true;
	return false;
}

bool comparadorTecnicos(const Tecnico* t1, const Tecnico* t2) {
	if (t1->getNome() < t2->getNome())
		return true;
	return false;
}

bool comparadorTimes(const Time* team1, const Time* team2) {
	if (team1->getNomeTime() < team2->getNomeTime())
		return true;
	return false;
}