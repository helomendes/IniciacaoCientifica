#include <iostream>
#include "Tecnico.hpp"
#include "Estrelas.hpp"

Tecnico::Tecnico() : Pessoa{} {}

Tecnico::Tecnico(const std::string& nome, const std::string& time) {
	this->nome = nome;
	this->time = time;
}

Tecnico::Tecnico(const std::string& nome, const short int& xp) {
	this->nome = nome;

	this->xp = (char)xp;
	try{
		calculoEstrelas(this->xp);
	}
	catch(std::invalid_argument& erro){
		std::cout << erro.what() << '\n';
	}
	catch(int& retorno){
		estrelas = retorno;
	}
}

Tecnico::Tecnico(const std::string& nome, const std::string& time, const short int& xp) {
	this->nome = nome;
	this->time = time;

	this->xp = (char)xp;
	try{
		calculoEstrelas(this->xp);
	}
	catch(std::invalid_argument& erro){
		std::cout << erro.what() << '\n';
	}
	catch(int& retorno){
		estrelas = retorno;
	}
}

Tecnico::Tecnico(const Tecnico& outra) {
	this->nome = outra.nome;
	std::cout << "Construindo cópia Tecnico" << std::endl;
}

std::string Tecnico::getTime() const{
	return time;
}

void Tecnico::setTime(const std::string& time){
	this->time = time;
}

short int Tecnico::getXp() const{
	return (short int)xp;
}

void Tecnico::setXp(const short int& xp){
	this->xp = (char)xp;
	try{
		calculoEstrelas(this->xp);
	}
	catch(std::invalid_argument& erro){
		std::cout << erro.what() << '\n';
	}
	catch(int& retorno){
		estrelas = retorno;
	}
}

unsigned short int Tecnico::getEstrelas() const{
	return (unsigned short int)estrelas;
}