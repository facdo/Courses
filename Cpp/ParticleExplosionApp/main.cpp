/*
    -------------- Particle Fire Explosion ----------------
    
    Program that uses the SDL graphical library to generate
    colorful particle explosion visualizations/simulations.

    It is important to explain a few SDL components:
    - Window: visual component in which the views and effects
    takes place.
    - Renderer: component that receives the textures/forms
    to be displayed in the window. Window renderization is the
    process in which the objects/particles/textures are drawn 
    into the window.
    - Texture: pixel definition to be passed to the renderer.
    - Buffer: memory allocation space to store the objects that
    compose the texture, maning, is the component that allocates
    memory to store the information for each pixel in the window.
    - Screen: class that computes the rendered window.
    - Particle: class that holds the particle attributes and methods
    - PCrowd: class to represent a swarm of particles, a particle collection

    All this components are buiilding blocks for our screen. Instead
    of mixing the screen code with the visualization patterns functionaliity,
    that we're building in the next steps, the best practice would be to
    put all that code in a Screen class.

    ----------------------------------------------------------
*/

#include "Screen.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h> // to use sin(). Needs std namespace.
#include "PCrowd.h"

using namespace std;
using namespace sdlApp;

int main() {

    // unique initialization of our random seed, for generating random positions for the particles
    srand(time(NULL));

    // create a instance of our screen class
    Screen screen;

    if(screen.init()==false) {
        cout << "Error initialising SDL components" << endl;
    }

    // Let's create a crowd of particles
    PCrowd particleCrowd;

    // Now we will create an infinite loop to display the window until
    // the user clicks in the close button, triggering a SDL_QUIT event
    while(true) {
        // Here we will:
        // - Update and draw partiicles
        // - Check for messages/events

        // we're creating a pointer to a particle, corresponding to the first element of the array of
        // particles, an instance of PCrowd
        const Particle * const pParticles = particleCrowd.getParticles();

        // now lets iterate to all particles and assign each one to a pixel
        for(int i=0; i<PCrowd::N_PARTICLES; i++){
            // Particle particle = pParticles[i];

            int x = (pParticles[i].x + 1) * Screen::WIDTH/2;
            int y = (pParticles[i].y + 1) * Screen::HEIGHT/2;
            cout << x << ' ' << y << endl;

            screen.setPixel(x, y, 0, 0, 0);
        }

        /*

        // In order to animate our colors we need to supply a constant changing number
        // to our RGB values. We're using the sine function, fed with the elapsed time
        // that the program is running
        int elapsed = SDL_GetTicks();// returns the time in miliseconds that the program is running
        double smooth_factor = 0.0002; // to avoid sudden changes in the color
        unsigned char red = (unsigned char)((1+sin(elapsed * smooth_factor))*128);
        unsigned char green = (unsigned char)((1+sin(elapsed * smooth_factor * 3))*128);
        unsigned char blue = (unsigned char)((1+sin(elapsed * smooth_factor * 5))*128);

        // Lets update the whole screen using our setPixel method
        for(int x=0; x<screen.WIDTH; x++){
            for(int y=0; y<screen.HEIGHT; y++){
                screen.setPixel(x, y, red, green, blue);
            }
        }

        */
        screen.update();
        // if the user clicks in the close window button, terminates the program
        if(screen.processEvents()==false) {
            break;
        }
    }

    screen.close();

    return 0;

}

