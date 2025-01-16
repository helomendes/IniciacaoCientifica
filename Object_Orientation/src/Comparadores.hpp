#ifndef COMPARADORES_HPP
#define COMPARADORES_HPP

#include "Jogador.hpp"
#include "Tecnico.hpp"
#include "Time.hpp"

bool comparadorJogadores(const Jogador* j1, const Jogador* j2);

bool comparadorTecnicos(const Tecnico* t1, const Tecnico* t2);

bool comparadorTimes(const Time* team1, const Time* team2);

#endif