#ifndef TIME_HPP
#define TIME_HPP

#include <list>
#include <string>
#include "Jogador.hpp"
#include "Tecnico.hpp"

class Time {
	public:
		Time();
		Time(const std::string& nomeTime);
		virtual ~Time() = default;

		std::string getNomeTime() const;
		void setNomeTime(const std::string& nomeTime);

		void mostrarTime();
		void adicionarJogador(Jogador* novoJogador);

		void setGoleiro(Jogador* novoGoleiro);
		Jogador* getGoleiro() const;

		std::list<Jogador*> getDefesa() const;

		std::list<Jogador*> getMeiocampo() const;

		std::list<Jogador*> getAtaque() const;

		std::list<Jogador*> getReserva() const;

		std::list<Jogador*> getTime() const;

		Tecnico* getTecnico() const;
		void setTecnico(Tecnico* novoCoach);

	private:
		std::string nomeTime;
		Jogador* goleiro;
		std::list<Jogador*> defesa;
		std::list<Jogador*> meioCampo;
		std::list<Jogador*> ataque;
		std::list<Jogador*> reserva;
		std::list<Jogador*> time;
		Tecnico* coach;
};

#endif
