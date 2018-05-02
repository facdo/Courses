#ifndef UTIL_H_ // pre-processor command that checks if the module util.h was defined already
#define UTIL_H_ // if not, defines it. This is the way to avoid the same module being included
// more than one time, while being called from different files/modules/programs

// Here we put our functions and/or functions prototypes
// Typically we would have a header file with the prototypes and another .cpp file with
// the actual functions definitions
// But for this example we`re puting the function definition here in the header file
void printSpacer(short int rows) {
    // This function receives an integer as an input argument and it doesn't return anything
    for(int i=0; i<rows; i++) {
        cout << "=======================================================" << endl;
    }
}

#endif