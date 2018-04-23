// Section to understand the basics of functions
// A Function is a snippet of code that can be called at any time
// It might receive arguments/variables as input and return something as an output
// Or it might not receive or return anything
// The basic syntax for declaring a function is like the following:
// returnType functionName(arg1Type arg1Name, ...) { code to be executed; return returnVariable}
// We can use any of the default variable types as arguments or as outputs
// If the function doesn't return anything it must be initialized with the type 'void'

// Let's make a simple dummy (it does nothing) command line program to exemplify these concepts

#include <iostream>

// Let`s include our custom util header, with some functions and prototype functions definitions
#include "util.h" // non standard headers should be included with the "module.h" syntax

using namespace std;

// Note that the function definition must always be done before the funcion call
// All functions will be called in the main program, so all of them must have been defined
// before the main program
// But the function code doesn`t necessarily has to be defined, we can just 'prototype' the 
// funcion, declaring it like a variable without a value assignment
// And we can actually put our functions or our protoype functions in a header file and include
// it in the beginning of our program.

// Just for the sake of viewing the different kinds of approaches for defining functions
// we`re using direct defined functions, prototypes and headers for this program

void createMenu() {
    // this function doesn't need any inputs and it doesn't return anything
    // to a variable (printing in the command prompt with cout is not returning any value!)
    cout << "1 - Search Records" << endl;
    cout << "2 - View Record" << endl;
    cout << "3 - Process Record" << endl;
    cout << "4 - Print Selection Menu" << endl;
    cout << "5 - Quit" << endl;
}

// This is a function prototype, we can now put the definition after the function is called (after main)
int getSelection();

void processSelection(short int selection) {
    // This function receives the selection inputed by the user as an input argument
    // but it doesn't return anything, so it is initialized with the void type keyword
    switch (selection) {
        case 1:
            cout << "There are 1325666 records avalible" << endl;
            break;
        case 2:
            cout << "This record talks about C++ programming... It is so exciting! :)" << endl;
            break;
        case 3:
            cout << "The record was processed." << endl;
            break;
        case 4:
            // note that we can call function inside our functions!
            createMenu();
            break;
        case 5:
            cout << "Quitting... See you next time!" << endl;
            break;
        default:
            cout << "Invalid Selection! Please input a number corresponding to a valid selection." << endl;
    }
}


int main(){
    // Instead of crowding our main programm with all that code we can now call it
    // If the same code would be used many times or in different applications it makes
    // total sense to declare-it as functions and maintain it in a single location, calling it whenever 
    // needed
    
    createMenu();
    // initialize the userSelection variable
    unsigned short int userSelection;
    // We can put our little program in a loop and exit uppon the selection condition
    do {
        // the userSelection variable will receive the returned value from the getSelection function
        userSelection = getSelection(); 
        printSpacer(1);
        processSelection(userSelection);
        printSpacer(2);
    } while(userSelection != 5);

    return 0;
}

// Function being defined after call, just for the sake of understanding prototypes
int getSelection() {
    // This function doesn't have any inputs, but it will return the user input, beeing an int
    cout << "Please select one of the options in the menu by entering the corresponding number: " << flush;
    int input;
    cin >> input;
    return input;
}