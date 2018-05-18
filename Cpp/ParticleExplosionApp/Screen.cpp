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
                   buffer(NULL),
                   blur_buffer(NULL) { }

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
    blur_buffer = new Uint32[WIDTH*HEIGHT];

    // We can use the function memset to write data into our buffer,
    // here we are writing 0 (0x00) in the entire buffer
    memset(buffer, 0x00, WIDTH*HEIGHT*sizeof(Uint32));

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

void Screen::clear() {
    // after creating the boxBlur this function would not be used anymore
    memset(buffer, 0x00, WIDTH*HEIGHT*sizeof(Uint32));
    memset(blur_buffer, 0x00, WIDTH*HEIGHT*sizeof(Uint32));
}

void Screen::boxBlur() {
    // This is an expensive algorithm in terms of processing requirements
    // The logic is to look at the screen state and calculate the next screen
    // with blured particles, based on the current state
    // We're swaping pointers to copy the buffer content to the blur_buffer
    Uint32 *temp = buffer;
    buffer = blur_buffer;
    blur_buffer = temp;

    for(int y=0; y<HEIGHT; y++) {
        for(int x=0; x<WIDTH; x++) {
            // We want get the average color value of the pixels around a central pixel
            // and change the colors of the pixels to be that average value.
            // So if we would have something like this:
            // 0 0 0 -> 28 28 28
            // 0 255 0 -> 28 28 28
            // 0 0 0 -> 28 28 28

            // For each pixel in the screen we would iterate through the 9 pixels surrounding it
            int red_total = 0;
            int green_total = 0;
            int blue_total = 0;
            for(int row=-1; row<=1; row++) {
                for(int col=-1; col<=1; col++) {
                    int current_x = x + col;
                    int current_y = y + row;
                    // we need to ignore pixels outside of the screen
                    if(current_x >=0 && current_x < WIDTH && current_y >=0 && current_y < HEIGHT){
                        // lets get the pixel color
                        Uint32 color = blur_buffer[current_y*WIDTH+current_x];
                        // lets get the RGB components and sum it up
                        red_total += (color & 0xFF000000) >> 24;
                        green_total += (color & 0x00FF0000) >> 16;
                        blue_total += (color & 0x0000FF00) >> 8;
                    }
                }
            }

            setPixel(x, y, red_total/9, green_total/9, blue_total/9);
        }
    }
}

void Screen::close() {
    // destroy the components freeing memory space
    delete [] buffer;
    delete [] blur_buffer;
    SDL_DestroyTexture(texture);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}

}