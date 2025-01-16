#include "Jogo.hpp"
#include <list>
#include "Comparadores.hpp"

Jogo::Jogo() {
	bench = new Banco();
}

Jogo::~Jogo() {
	delete bench;
	times.clear();
}

Banco* Jogo::getBanco() const {
	return bench;
}

std::list<Time*>* Jogo::getTimes(){
	return &times;
}

void Jogo::adicionarTime(Time* novoTime) {
	times.push_back(novoTime);
	//times.sort(comparadorTimes);
}

void Jogo::removerTime(const short int& t) {
	std::list<Time*>::iterator it;
	it = std::next(times.begin(), t);
	times.erase(it);
}