## Firey Particle Explosion App

Visual application that simulates particle trajectories, generating a colorful view of their movement.

Uses the SDL (Simple DirectMedia Layer) C++ library to enable the visualization. 

**This project is based on the final project of the Udemy course: C++ for Complete Beginners**

### Using C++ Libraries

It is important to understand the basic structure of a C++ program flow:
* Libraries and Program Code Definition
* Preprocessing
* Compilation - Creation of the .o object files
* Link object files to create an executable file

It is also important to understand that there are two kinds of libraries:

* Static Libraries: files contaning c++ code that it is actually compiled into the program. On Windows they have the sufix .lib; on UNIX/Linux/MAC they usually have a prefix lib and a sufix .a
* Dynamic Libraries: files that are accessed during execution when needed. Ex.: cout from the standard library, the program find the definition at run time. On windows they have a .dll sufix; on UNIX/Linux/MAC they have lib prefix and a .so sufix. On MAC it is also possible to have a .dylib sufix.

We're going to be using the static and dynamic libraries of SDL to develop this program.

### Acquiring SDL Graphics Library - Version 2.0

SDL is a simple game library that enables pixel level access to our programming. Any C++ game library could be used for writing this Particle Explosion App, but SDL is a very basic but stable/reliable library. We need to link the SDL header files to our project. The steps for doing that are the following:
* Download the .tar.gz SDL 2.0 Development Library for the MinGW compiler;
* Extract the files and open the "i686-w64-mingw32" folder;
* Copy the contents of the include folder (copy the SDL2 folder), lib folder and bin folder to the respective include, lib and bin folders in the MinGW installation path;
* Configure the compile options in the tasks.json file to enable the link with the SDL library:
    * Add the following arguments: "-lmingw32", "-lSDL2main", "-lSDL2"
* Run a simple test program initializing the library and check if it works.

The instructions for running the code with the SDL library were based on the following link: 

https://w3.cs.jmu.edu/bernstdh/web/common/help/cpp_mingw-sdl-setup.php



