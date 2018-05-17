#include "Particle.h"
#include <stdlib.h>

using namespace std;
namespace sdlApp {

Particle::Particle() {
    // lets initialize our particle with random x and y coordinates
    // rand();RAND_MAX throw a number between 0 and 1. We want it between -1 and 1
    // and afterwards we will be mapping it to our screen x and y pixel position
    x = ((2.0*rand())/RAND_MAX) - 1;
    y = ((2.0*rand())/RAND_MAX) - 1;
}

Particle::~Particle() {} // auto-generated destructor

}
