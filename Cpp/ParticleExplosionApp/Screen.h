#ifndef SCREEN_H_
#define SCREEN_H_

#define SDL_MAIN_HANDLED
#include "SDL2/SDL.h"

// Lets define a namespace to avoid any name conflict
namespace sdlApp {

class Screen {
// Definition of the attributes
public:
// Definition of the window size
const static int WIDTH = 640;
const static int HEIGHT = 480;

private:
// SDL window object
SDL_Window *window;
// Renderer component
SDL_Renderer *renderer;
// Texture component
SDL_Texture *texture;
// Buffer to allocate memory for all the pixels in the screen
Uint32 *buffer;

// Definition of the class methods
public:
// constructor
Screen();
// method to initialize the SDL components
bool init();
// method to set the pixel at the x,y coordinate, with the RGB color (Uint8 is a 8 bit int, same as a char)
void setPixel(int x, int y, Uint8 red, Uint8 green, Uint8 blue);
// method to update our screen after drawing and modifying the pixels
void update();
// method to deal with events (close window event)
bool processEvents();
// method to close/destroy all components, freeing memory space
void close();
};

}

#endif