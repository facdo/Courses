#ifndef PARTICLE_H_
#define PARTICLE_H_

namespace sdlApp {

class Particle {
public:
    double x;
    double y;

public:
    Particle();
    virtual ~Particle();
};
}
#endif