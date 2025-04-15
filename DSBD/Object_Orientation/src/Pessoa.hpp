#ifndef PESSOA_HPP
#define PESSOA_HPP

#include <string>

class Pessoa{
	public:
		Pessoa();
		Pessoa(const std::string& novoNome);
		Pessoa(const std::string& novoNome, const unsigned short int& novaIdade);
		Pessoa(const std::string& novoNome, const unsigned short int& novaIdade, const std::string& novoPais);
		Pessoa(const Pessoa& outra);
		virtual ~Pessoa() = default;

		std::string getNome() const;
		void setNome(const std::string& nome);

		unsigned short int getIdade() const;
		void setIdade(const unsigned short int& idade);

		std::string getPais() const;
		void setPais(const std::string& pais);
	protected:
		std::string nome;
		unsigned char idade;
		std::string pais;
};

#endif
