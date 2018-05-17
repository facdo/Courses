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

    All this components are buiilding blocks for our screen. Instead
    of mixing the screen code with the visualization patterns functionaliity,
    that we're building in the next steps, the best practice would be to
    put all that code in a Screen class.

    ----------------------------------------------------------
*/


#include <iostream>
// This line is important, don't know why...
#define SDL_MAIN_HANDLED
#include "SDL2/SDL.h"
#include <string.h>

using namespace std;

int main() {

    // Definition of the window size
    const int WIDTH = 640;
    const int HEIGHT = 480;

    // Initialization of the SDL video capabilities, print error on fail
    if(SDL_Init(SDL_INIT_VIDEO) < 0) {
        cout << "SDL video initialization failed, error: " << SDL_GetError() << endl;
        return 1;
    }

    // Create a SDL window object
    SDL_Window *window = SDL_CreateWindow("Particle Fire Explosion View",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          WIDTH,
                                          HEIGHT,
                                          SDL_WINDOW_SHOWN);
    
    // Checks if the window was successfully created, print error on fail
    if(window == NULL) {
        cout << "Failed to create window, error: " << SDL_GetError() << endl;
        SDL_Quit();
        return 2;
    }

    // Creates the renderer component
    SDL_Renderer *renderer = SDL_CreateRenderer(window,
                                                -1,
                                                SDL_RENDERER_PRESENTVSYNC);

    // Checks if the renderer was created, print error on fail
    if(renderer == NULL) {
        cout << "Failed to create renderer, error: " << SDL_GetError() << endl;
        // we need to destroy the created components to avoid memory leak
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 3;
    }

    // Creates the texture component
    SDL_Texture *texture = SDL_CreateTexture(renderer,
                                             SDL_PIXELFORMAT_RGBA8888,
                                             SDL_TEXTUREACCESS_STATIC,
                                             WIDTH,
                                             HEIGHT);

    // Checks if the texture was created, print error on fail
    if(texture == NULL) {
        cout << "Failed to create texture, error: " << SDL_GetError() << endl;
        // we need to destroy the created components to avoid memory leak
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 4;
    }

    // We have to create a buffer to allocate memory for the pixel data
    // The pixel size is defined by the SDL built in class Uint32, which is
    // basically a unsigned 32 bit integer (4bytes)
    // Since we are using "new" we must delete it after use
    Uint32 *buffer = new Uint32[WIDTH*HEIGHT];

    // We can use the function memset to write data into our buffer,
    // here we are writing 255 (0xFF) in the entire buffer
    memset(buffer, 0xFF, WIDTH*HEIGHT*sizeof(Uint32));

    // We must update the texture with the values in the buffer
    SDL_UpdateTexture(texture,
                      NULL,
                      buffer,
                      WIDTH*sizeof(Uint32));

    // Next we clear the renderer and then copy the updated texture
    // to the renderer, finally presenting the renderer in the window
    SDL_RenderClear(renderer);
    SDL_RenderCopy(renderer, texture, NULL, NULL);
    SDL_RenderPresent(renderer);

    // Object to listen to events
    SDL_Event event;
    
    // Now we will create an infinite loop to display the window until
    // the user clicks in the close button, triggering a SDL_QUIT event
    while(true) {
        // Here we should add our code to draw and update particles

        if(SDL_PollEvent(&event)) {
            if(event.type == SDL_QUIT) {
                break;
            }
        }
    }

    delete [] buffer;
    SDL_DestroyTexture(texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;

}