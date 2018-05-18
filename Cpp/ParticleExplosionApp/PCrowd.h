#ifndef PCROWD_H_
#define PCROWD_H_

#include "Particle.h"

// We're creating this class to be able to initialize a bunch of particles at once.

namespace sdlApp {

class PCrowd {
public:
    const static int N_PARTICLES = 10000;

private:
    Particle *pParticles;
    // time of the last iteraction, to compare with elapsed
    int last_time;

public:
    PCrowd();
    virtual ~PCrowd();
	const Particle * const getParticles() { return pParticles; };
    // The elapsed time is used to update the speed by a known amount
    void update(int elapsed);
};
}
#endif