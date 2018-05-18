#include "PCrowd.h"

namespace sdlApp {

PCrowd::PCrowd(): last_time(0) {
    // An instance of this class corresponds to a lot of particles
    pParticles = new Particle[N_PARTICLES];
}

PCrowd::~PCrowd() {
    delete [] pParticles;
}

void PCrowd::update(int elapsed){
    // reference of the time between updates
    int interval = elapsed - last_time;

    // loops through all particles and run the Particle::update method in each one
     for(int i=0; i<PCrowd::N_PARTICLES; i++){
         pParticles[i].update(interval);
     }

     last_time = elapsed;
}
}