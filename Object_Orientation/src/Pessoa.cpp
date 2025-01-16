#include "Pessoa.hpp"
#include <iostream>

Pessoa::Pessoa() {}

Pessoa::Pessoa(const std::string& nome) {
	this->nome = nome;
}

Pessoa::Pessoa(const std::string& nome, const unsigned short int& idade) {
	this->nome = nome;
	this->idade = idade;
}

Pessoa::Pessoa(const std::string& nome, const unsigned short int& idade, const std::string& pais) {
	this->nome = nome;
	this->idade = idade;
	this->pais = pais;
}

Pessoa::Pessoa(const Pessoa& outra) {
	this->nome = outra.nome;
	std::cout << "Construindo cópia Pessoa" << std::endl;
}


std::string Pessoa::getNome() const{
	return nome;
}

void Pessoa::setNome(const std::string& nome){
	this->nome = nome;
}

unsigned short int Pessoa::getIdade() const{
	return (unsigned short int)idade;
}

void Pessoa::setIdade(const unsigned short int& idade){
	this->idade = (unsigned char)idade;
}

std::string Pessoa::getPais() const{
	return pais;
}

void Pessoa::setPais(const std::string& pais){
	this->pais = pais;
}