#include "PCrowd.h"

namespace sdlApp {

PCrowd::PCrowd() {
    // An instance of this class corresponds to a lot of particles
    pParticles = new Particle[N_PARTICLES];
}

PCrowd::~PCrowd() {
    delete [] pParticles;
}
}