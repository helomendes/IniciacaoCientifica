#include <iostream>
#include "Menus.hpp"

//ok
void menu(){
	std::cout << "Selecione a Opção:\n";
	std::cout << "\t1. Criar Time\n";
	std::cout << "\t2. Continuar\n";
	std::cout << "\t3. Sair\n";
}

//ok
void novotime_menu(){
	std::cout << "\t0. Voltar\n";
	std::cout << "\t1. Ver Time\n";
	std::cout << "\t2. Adicionar Jogador\n";
	std::cout << "\t3. Criar Novo Jogador\n";
	std::cout << "\t4. Adicionar Tecnico\n";
	std::cout << "\t5. Criar Novo Tecnico\n";
	std::cout << "\t6. Jogar\n";
}

void edit_menu() {
	std::cout << "\t0. Voltar" << '\n';
	std::cout << "\t1. Ver Time\n";
	std::cout << "\t2. Editar Nome do Time" << '\n';
	std::cout << "\t3. Editar Jogadores" << '\n';
	std::cout << "\t4. Editar Técnico" << '\n';
	std::cout << "\t5. Excluir Time\n";
	std::cout << "\t6. Jogar\n";
}

void edit2_menu() {
	std::cout << "\t0. Voltar" << '\n';
	std::cout << "\t1. Editar" << '\n';
	std::cout << "\t2. Excluir" << '\n';
}

void editJogador_menu() {
	std::cout << "\t0. Voltar" << '\n';
	std::cout << "\t1. Nome" << '\n';
	std::cout << "\t2. Idade" << '\n';
	std::cout << "\t3. País" << '\n';
	std::cout << "\t4. Número da Camisa" << '\n';
	std::cout << "\t5. Posição" << '\n';
	std::cout << "\t6. Time" << '\n';
}

void editTecnico_menu() {
	std::cout << "\t0. Voltar" << '\n';
	std::cout << "\t1. Nome" << '\n';
	std::cout << "\t2. Idade" << '\n';
	std::cout << "\t3. País" << '\n';
	std::cout << "\t4. Time" << '\n';
	std::cout << "\t5. Tempo de Experiência" << '\n';
}

//ok
void atributosJogador(){
	system("clear");
	std::cout << "JOGADOR" << '\n';
	std::cout << "\t1. Adicionar País\n";
	std::cout << "\t2. Adicionar Idade\n";
	std::cout << "\t3. Adicionar Número da Camisa\n";
	std::cout << "\t4. Voltar ao Menu Anterior\n";
}

void atributosTecnico() {
	system("clear");
	std::cout << "TECNICO" << '\n';
	std::cout << "\t1. Adicionar País\n";
	std::cout << "\t2. Adicionar Experiência\n";
	std::cout << "\t3. Voltar ao Menu Anterior\n";
}

void addJog() {
	std::cout << "\t0. Voltar" << '\n';
	std::cout << "\t1. Goleiro" << '\n';
	std::cout << "\t2. Defensor" << '\n';
	std::cout << "\t3. Meio Campista" << '\n';
	std::cout << "\t4. Atacante" << '\n';
}