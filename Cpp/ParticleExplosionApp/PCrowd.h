#ifndef PCROWD_H_
#define PCROWD_H_

#include "Particle.h"

// We're creating this class to be able to initialize a bunch of particles at once.

namespace sdlApp {

class PCrowd {
public:
    const static int N_PARTICLES = 5000;

private:
    Particle *pParticles;

public:
    PCrowd();
    virtual ~PCrowd();
	const Particle * const getParticles() { return pParticles; };
};
}
#endif