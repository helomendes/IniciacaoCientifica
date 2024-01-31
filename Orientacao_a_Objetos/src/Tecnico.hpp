#ifndef TECNICO_HPP
#define TECNICO_HPP

#include "Pessoa.hpp"

class Tecnico : public Pessoa{
	public:
		Tecnico();
		Tecnico(const std::string& nome, const std::string& time);
		Tecnico(const std::string& nome, const short int& xp);
		Tecnico(const std::string& nome, const std::string& time, const short int& xp);
		Tecnico(const Tecnico& outra);
		virtual ~Tecnico() = default;

		std::string getTime() const;
		void setTime(const std::string& time);

		short int getXp() const;
		void setXp(const short int& xp);

		unsigned short int getEstrelas() const;

	private:
		std::string time;
		char xp;
		unsigned char estrelas;
};

#endif
