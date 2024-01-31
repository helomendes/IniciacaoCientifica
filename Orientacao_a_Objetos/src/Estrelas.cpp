#include <stdexcept>
#include "Estrelas.hpp"

unsigned short int calculoEstrelas(short int xp){
	if(xp < 0)
		throw std::invalid_argument{"Tempo inválido."};
	else if(xp < 5)
		throw (int)0;
	else if(xp < 10)
		throw (int)1;
	else if(xp < 15)
		throw (int)2;
	else if(xp < 20)
		throw (int)3;
	else if(xp < 25)
		throw (int)4;
	else
		throw (int)5;
}	
