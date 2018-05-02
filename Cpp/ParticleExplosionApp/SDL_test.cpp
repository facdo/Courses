/*
    ------------------------- SDL Library Sample Program -------------------------------

    Simple code to test the SDL library and verify that the files were included
    correctly (adding the path to the header files and static and dynamic library files
    to the includePath in the c_cpp_properties.json file).

    ------------------------------------------------------------------------------------
*/

#include <iostream>
#define SDL_MAIN_HANDLED
#include "SDL2/SDL.h"

using namespace std;


// We need to rename our main to WinMain so that the SDL runs
int main() {
    // Definition of the width and height of our simple SDL window
    const int WIDTH = 800;
    const int HEIGHT = 600;

    if(SDL_Init(SDL_INIT_VIDEO) < 0) {
        cout << "SDL Init Failed" <<  endl;
        return 1;
    }

    cout << "SDL Init succeeded!" << endl;

    SDL_Window *window = SDL_CreateWindow("SDL Test",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          WIDTH,
                                          HEIGHT,
                                          SDL_WINDOW_OPENGL);
    if(window==NULL) {
        cout << "Failed to load window" << endl;
        return 1;
    }

    // delay before destroying the window
    SDL_Delay(4000);

    // close and destroy the window, freeing memory space
    SDL_DestroyWindow(window);

    SDL_Quit();
    return 0;
}





