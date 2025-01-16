#ifndef LIBTECNICOS_HPP
#define LIBTECNICOS_HPP

#include <list>
#include "Banco.hpp"
#include "Tecnico.hpp"

Tecnico* addTecnico(Banco* bench);

Tecnico* criarTecnico();

Tecnico* editarTecnico(Tecnico* t);

void imprimirTecnico(Tecnico* t);

void imprimirTecnicos(std::list<Tecnico*>* lista);

#endif