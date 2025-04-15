#include "Jogador.hpp"
#include <iostream>

Jogador::Jogador() : Pessoa{} {};

Jogador::Jogador(const std::string& nome, const unsigned short int& posicao) {
	this->nome = nome;
	this->posicao = posicao;
}

Jogador::Jogador(const std::string& nome, const std::string& time) {
	this->nome = nome;
	this->time = time;
}

Jogador::Jogador(const std::string& nome, const unsigned short int& posicao, const std::string& time) {
	this->nome = nome;
	this->posicao = posicao;
	this->time = time;
}

Jogador::Jogador(const Jogador& outra) {
	this->nome = outra.nome;
	std::cout << "Construindo cópia Jogador" << std::endl;
}

unsigned short int Jogador::getNumCamisa() const{
	return (unsigned short int)numCamisa;
}

void Jogador::setNumCamisa(const unsigned short int& numCamisa){
	this->numCamisa = (unsigned char)numCamisa;
}

unsigned char Jogador::getNPosicao() const{
	return posicao;
}

std::string Jogador::getPosicao() const{
	if (posicao == 1)
		return "Goleiro";
	if (posicao == 2)
		return "Defesa";
	if (posicao == 3)
		return "Meio-Campo";
	if (posicao == 4)
		return "Atacante";
	return "Não informado";
}

void Jogador::setPosicao(const unsigned short int& posicao){
	this->posicao = (unsigned short int)posicao;
}

std::string Jogador::getTime() const{
	return time;
}

void Jogador::setTime(const std::string& time){
	this->time = time;
}

bool Jogador::operator==(const Jogador& outro) const {
	return this->nome == outro.nome;
}