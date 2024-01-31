#ifndef LIBJOGADOR_HPP
#define LIBJOGADOR_HPP

#include <list>
#include "Banco.hpp"
#include "Jogador.hpp"

Jogador* addJogador(Banco* bench);

Jogador* criarJogador();

Jogador* editarJogador(Jogador* j);

void imprimirJogador(Jogador* j);

void imprimirJogadores(std::list<Jogador*>* lista);

#endif