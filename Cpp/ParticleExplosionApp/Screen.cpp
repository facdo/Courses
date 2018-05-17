// We don't have to include the SDL lib here because it is already
// included in our class header file
#include "Screen.h"
#include <string.h> // necessary for memset function
#include <iostream>

using namespace std;

// Defining the implementation in the same namespace
// used in the header file

namespace sdlApp {

// Implementation of our constructor
// All attribuites are created as null
Screen::Screen() : window(NULL), 
                   renderer(NULL), 
                   texture(NULL),
                   buffer(NULL) { }

// The initialization of all components will be carried in this method
bool Screen::init(){

    // Initialization of the SDL video capabilities, print error on fail
    if(SDL_Init(SDL_INIT_VIDEO) < 0) {
        cout << "SDL video initialization failed, error: " << SDL_GetError() << endl;
        return false;
    }

    // Create a SDL window object
    window = SDL_CreateWindow("Particle Fire Explosion View",
                                SDL_WINDOWPOS_CENTERED,
                                SDL_WINDOWPOS_CENTERED,
                                WIDTH,
                                HEIGHT,
                                SDL_WINDOW_SHOWN);
    
    // Checks if the window was successfully created, print error on fail
    if(window == NULL) {
        cout << "Failed to create window, error: " << SDL_GetError() << endl;
        SDL_Quit();
        return false;
    }

    // Creates the renderer component
    renderer = SDL_CreateRenderer(window,
                                    -1,
                                    SDL_RENDERER_PRESENTVSYNC);

    // Checks if the renderer was created, print error on fail
    if(renderer == NULL) {
        cout << "Failed to create renderer, error: " << SDL_GetError() << endl;
        // we need to destroy the created components to avoid memory leak
        SDL_DestroyWindow(window);
        SDL_Quit();
        return false;
    }

    // Creates the texture component
    texture = SDL_CreateTexture(renderer,
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
        return false;
    }

    // We have to create a buffer to allocate memory for the pixel data
    // The pixel size is defined by the SDL built in class Uint32, which is
    // basically a unsigned 32 bit integer (4bytes)
    // Since we are using "new" we must delete it after use
    buffer = new Uint32[WIDTH*HEIGHT];

    // We can use the function memset to write data into our buffer,
    // here we are writing 255 (0xFF) in the entire buffer
    memset(buffer, 0xFF, WIDTH*HEIGHT*sizeof(Uint32));

    return true;
}

void Screen::setPixel(int x, int y, Uint8 red, Uint8 green, Uint8 blue) {
    // to avoid trying to set pixels out of the screen, lets do a check on x and y values
    if( x<0 || x>=WIDTH || y<0 || y>=HEIGHT){
        return;
    }

    Uint32 color = 0;

    color += red;
    color <<= 8;
    color += green;
    color <<= 8;
    color += blue;
    color <<= 8;
    color += 0xFF; // alpha value = 0xFF => opaque

    // we need to set the x,y pixel as the specified color
    // to do that we need to save the color into the right position of our
    // buffer. The buffer is a 1D array with lenght equals to the screen width multiplied
    // by its height, so we need to go to the y*WIDTH + x position of the array
    buffer[(y*WIDTH + x)] = color;

}

void Screen::update() {
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
}

bool Screen::processEvents() {
    // Object to listen to events
    SDL_Event event;
    
    // Checks for clicks in the close button, triggering a SDL_QUIT event
    if(SDL_PollEvent(&event)) {
        if(event.type == SDL_QUIT) {
            return false;
        }
    }
    return true;
}

void Screen::close() {
    // destroy the components freeing memory space
    delete [] buffer;
    SDL_DestroyTexture(texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}

}