#ifndef EXTRAS_HPP
#define EXTRAS_HPP

#include <list>
#include "Jogo.hpp"
#include "Time.hpp"
#include "Tecnico.hpp"

int criarTime(Banco* bench, Time* novoTime);

void editarTime(Time *team, short int *op);

void imprimirTimes(Jogo* j);

#endif
