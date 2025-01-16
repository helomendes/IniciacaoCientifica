#ifndef JOGADOR_HPP
#define JOGADOR_HPP

#include "Pessoa.hpp"

class Jogador : public Pessoa {
	public:
		Jogador();
		Jogador(const std::string& nome, const unsigned short int& posicao);
		Jogador(const std::string& nome, const std::string& time);
		Jogador(const std::string& nome, const unsigned short int& posicao, const std::string& time);
		Jogador(const Jogador& outra);
		virtual ~Jogador() = default;

		unsigned short int getNumCamisa() const;
		void setNumCamisa(const unsigned short int& numCamisa);

		unsigned char getNPosicao() const;
		std::string getPosicao() const;
		void setPosicao(const unsigned short int& posicao);

		std::string getTime() const;
		void setTime(const std::string& time);

		bool operator==(const Jogador& outro) const;
		
	private:
		unsigned char numCamisa;
		unsigned char posicao;
		std::string time;
};

#endif
