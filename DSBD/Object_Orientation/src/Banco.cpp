#include "Banco.hpp"
#include <iostream>
#include <memory>
#include "Comparadores.hpp"

Banco::Banco() {
	criarGoleiros();
	criarDefensores();
	criarMeiocampistas();
	criarAtacantes();
	criarTecnicos();
}

Banco::~Banco() {
    goleiros.clear();
	defensores.clear();
	meiocampistas.clear();
	atacantes.clear();
	tecnicos.clear();	
}

void Banco::adicionarJogador(Jogador* novoJogador) {
	unsigned char posicao = novoJogador->getNPosicao();
	switch (posicao)
	{
		case 1:
			goleiros.push_back(novoJogador);
			goleiros.sort(comparadorJogadores);
			break;
		case 2:
			defensores.push_back(novoJogador);
			defensores.sort(comparadorJogadores);
			break;
		case 3:
			meiocampistas.push_back(novoJogador);
			meiocampistas.sort(comparadorJogadores);
			break;
		case 4:
			atacantes.push_back(novoJogador);
			atacantes.sort(comparadorJogadores);
			break;
		default:
			break;
	}
}

std::list<Jogador*>* Banco::getGoleiros(){	
	return &goleiros;
}

std::list<Jogador*>* Banco::getDefensores(){
	return &defensores;
}

std::list<Jogador*>* Banco::getMeiocampistas(){
	return &meiocampistas;
}

std::list<Jogador*>* Banco::getAtacantes(){
	return &atacantes;
}

std::list<Tecnico*>* Banco::getTecnicos(){
	return &tecnicos;
}

void Banco::criarGoleiros() {
	Jogador* j0 = new Jogador("Buffon", 1, "Parma");
	j0->setIdade(45);
	j0->setNumCamisa(1);
	j0->setPais("Italia");

	Jogador* j1 = new Jogador("Mike Maignan", 1, "Milan");
	j1->setIdade(27);
	j1->setNumCamisa(16);
	j1->setPais("França");

	Jogador* j2 = new Jogador("Unai Simon", 1, "Athletic Bilbao");
	j2->setIdade(25);
	j2->setNumCamisa(23);
	j2->setPais("Espanha");

	goleiros.push_back(j2);
	goleiros.push_back(j0);
	goleiros.push_back(j1);
	goleiros.sort(comparadorJogadores);
}

void Banco::criarDefensores() {
	Jogador* j3 = new Jogador("Giovanni di L.", 2, "Napoli");
	j3->setIdade(29);
	j3->setNumCamisa(22);
	j3->setPais("Italia");

	Jogador* j4 = new Jogador("Dani Carvajal", 2, "Real Madrid");
	j4->setIdade(31);
	j4->setNumCamisa(2);
	j4->setPais("Espanha");

	Jogador* j5 = new Jogador("Sergio Ramos", 2, "PSG");
	j5->setIdade(36);
	j5->setNumCamisa(4);
	j5->setPais("Espanha");

	Jogador* j6 = new Jogador("Raphael Varane", 2, "Manchester");
	j6->setIdade(29);
	j6->setNumCamisa(5);
	j6->setPais("França");

	Jogador* j7 = new Jogador("Bremer",2 , "Juventus");
	j7->setIdade(26);
	j7->setNumCamisa(3);
	j7->setPais("Brasil");

	Jogador* j8 = new Jogador("Rafael Toloi", 2, "Atalanta");
	j8->setIdade(32);
	j8->setNumCamisa(25);
	j8->setPais("Italia");

	Jogador* j9 = new Jogador("Theo Hernandez", 2, "Milan");
	j9->setIdade(25);
	j9->setNumCamisa(19);
	j9->setPais("França");

	Jogador* j10 = new Jogador("Joao Cancelo", 2, "Bayern Munchen");
	j10->setIdade(28);
	j10->setNumCamisa(20);
	j10->setPais("Portugal");

	defensores.push_back(j7);
	defensores.push_back(j4);
	defensores.push_back(j3);
	defensores.push_back(j10);
	defensores.push_back(j8);
	defensores.push_back(j6);
	defensores.push_back(j5);
	defensores.push_back(j9);
	defensores.sort(comparadorJogadores);
}

void Banco::criarMeiocampistas() {
	Jogador* j11 = new Jogador("Pedri", 3, "Barcelona");
	j11->setIdade(20);
	j11->setNumCamisa(8);
	j11->setPais("Espanha");

	Jogador* j12 = new Jogador("Gavi", 3, "Barcelona");
	j12->setIdade(18);
	j12->setNumCamisa(6);
	j12->setPais("Espanha");

	Jogador* j13 = new Jogador("Casemiro", 3, "Manchester");
	j13->setIdade(31);
	j13->setNumCamisa(14);
	j13->setPais("Brasil");

	Jogador* j14 = new Jogador("Nicolo Barella", 3, "Inter de Milao");
	j14->setIdade(26);
	j14->setNumCamisa(18);
	j14->setPais("Italia");

	Jogador* j15 = new Jogador("Camavinga", 3, "Real Madrid");
	j15->setIdade(20);
	j15->setNumCamisa(12);
	j15->setPais("França");

	Jogador* j16 = new Jogador("Lucas Paqueta", 3, "West Ham");
	j16->setIdade(25);
	j16->setNumCamisa(17);
	j16->setPais("Brasil");

	meiocampistas.push_back(j13);
	meiocampistas.push_back(j15);
	meiocampistas.push_back(j12);
	meiocampistas.push_back(j16);
	meiocampistas.push_back(j14);
	meiocampistas.push_back(j11);
	meiocampistas.sort(comparadorJogadores);
}

void Banco::criarAtacantes() {
	Jogador* j17 = new Jogador("Neymar", 4, "PSG");
	j17->setIdade(31);
	j17->setNumCamisa(10);
	j17->setPais("Brasil");

	Jogador* j18 = new Jogador("Lionel Messi", 4, "PSG");
	j18->setIdade(35);
	j18->setNumCamisa(30);
	j18->setPais("Argentina");

	Jogador* j19 = new Jogador("Cristiano R.", 4, "Al Nassar");
	j19->setIdade(38);
	j19->setNumCamisa(7);
	j19->setPais("Portugal");

	Jogador* j20 = new Jogador("Raspadori", 4, "Napoli");
	j20->setIdade(23);
	j20->setNumCamisa(81);
	j20->setPais("Italia");

	Jogador* j21 = new Jogador("Mbappe", 4, "PSG");
	j21->setIdade(24);
	j21->setNumCamisa(29);
	j21->setPais("França");

	Jogador* j22 = new Jogador("Angel Di Maria", 4, "PSG");
	j22->setIdade(35);
	j22->setNumCamisa(11);
	j22->setPais("Argentina");

	Jogador* j23 = new Jogador("Martinelli", 4, "Arsenal");
	j23->setIdade(21);
	j23->setNumCamisa(26);
	j23->setPais("Brasil");

	Jogador* j24 = new Jogador("Peter Crouch", 4, "Liverpool");
	j24->setIdade(42);
	j24->setNumCamisa(15);
	j24->setPais("Inglaterra");

	Jogador* j25 = new Jogador("Gabriel Jesus", 4, "Arsenal");
	j25->setIdade(25);
	j25->setNumCamisa(9);
	j25->setPais("Brasil");

	atacantes.push_back(j22);
	atacantes.push_back(j19);
	atacantes.push_back(j25);
	atacantes.push_back(j23);
	atacantes.push_back(j20);
	atacantes.push_back(j18);
	atacantes.push_back(j21);
	atacantes.push_back(j17);
	atacantes.push_back(j24);
	atacantes.sort(comparadorJogadores);
}

void Banco::criarTecnicos() {
	Tecnico* t0(new Tecnico("Pep Guardiola", "Manchester City", 15));
	t0->setPais("Espanha");
	Tecnico* t1 = new Tecnico("Antonio Conte", "Chelsea", 17);
	t1->setPais("Italia");
	Tecnico* t2 = new Tecnico("Diego Simeone", "Atletico Madrid", 17);
	t2->setPais("Argentina");
	Tecnico* t3 = new Tecnico("Carlo Ancelotti", "Bayern Munchen", 28);
	t3->setPais("Italia");
	Tecnico* t4 = new Tecnico("Jose Mourinho", "Manchester", 31);
	t4->setPais("Portugal");
	Tecnico* t5 = new Tecnico("Allegri", "Juventus", 19);
	t5->setPais("Italia");

	tecnicos.push_back(t0);
	tecnicos.push_back(t1);
	tecnicos.push_back(t2);
	tecnicos.push_back(t3);
	tecnicos.push_back(t4);
	tecnicos.push_back(t5);
	tecnicos.sort(comparadorTecnicos);
}