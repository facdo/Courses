#include "Particle.h"
#include <stdlib.h>
#include <math.h>

using namespace std;
namespace sdlApp {

// To create the explosion the particles are initialized in the center (x=0, y=0)
Particle::Particle() {
    init(0, 0);
    // // The following code is part of the implementation evolution showed in the tutorial
    // // lets initialize our particle with random x and y coordinates
    // // rand();RAND_MAX throw a number between 0 and 1. We want it between -1 and 1
    // // and afterwards we will be mapping it to our screen x and y pixel position
    // x = ((2.0*rand())/RAND_MAX) - 1;
    // y = ((2.0*rand())/RAND_MAX) - 1;
    // // Each particle would also have a random speed
    // x_speed = 0.005*((2.0*rand()/RAND_MAX)-1);
    // y_speed = 0.005*((2.0*rand()/RAND_MAX)-1);
}

// Initialize the particle attribuites
void Particle::init(double init_x, double init_y) {

    // What we really want is to have all particles initialized from the center of
    // the screen, and then have a random speed in the polar coordinate system,
    // meaning that we have to define a speed intensity and an angle, in radians
    x = init_x;
    y = init_y;

    speed_angle = (2 * M_PI * rand())/RAND_MAX;
    speed_value = (0.025 * rand())/RAND_MAX;

    // To have a better particle motion let's square the speed value
    // The result is that the average speed of the particles gets bigger
    speed_value *= speed_value;

}

Particle::~Particle() {} // auto-generated destructor

void Particle::update(int interval) {
    // // The following code is part of the implementation evolution showed in the tutorial
    // // the position would be updated based on the particle speed,
    // // which was assigned as a random value in the particle instanciation
    // x += x_speed;
    // y += 0.01*sin(5*x);
    // // to make sure the particles doesn't go out of the screen
    // if(x >= 1.0 || x < -1.0){
    //     x_speed = -x_speed;
    // }
    // if(y >= 1.0 || y < -1.0){
    //     y_speed = -y_speed;
    // }

    // To make the particle circle arround lets change the angle incremetally, so that the particles spin
    // arround the center
    speed_angle += 0.00025*interval;

    // We have to convert the speed from the polar coordinate system to the cartesian (x and y)
    x_speed = speed_value * cos(speed_angle);
    y_speed = speed_value * sin(speed_angle);

    // Now we update our position
    // By multiplying the speed by the time interval we make sure the movement 
    // would be the same regardless of the system speed (might be bumpy in slow computers)
    x += x_speed * interval;
    y += y_speed * interval;

    // Let's make sure that the particles doesn't travel outside the screen
    if(x < -1 || x > 1 || y < -1 || y > 1) {
        // if it does we will reinitialize them with random positions
        init(((2.0*rand())/RAND_MAX-1), ((2.0*rand())/RAND_MAX-1));
    }
}

}


