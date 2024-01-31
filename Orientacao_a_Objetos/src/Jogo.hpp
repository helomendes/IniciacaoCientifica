#ifndef JOGO_HPP
#define JOGO_HPP

#include "Banco.hpp"
#include "Time.hpp"

class Jogo{
	public:
		Jogo();
		virtual ~Jogo();

		Banco* getBanco() const;

		std::list<Time*>* getTimes();
		void adicionarTime(Time* novoTime);
		void removerTime(const short int& t);

	protected:
		Banco* bench;
		std::list<Time*> times;
};

#endif
