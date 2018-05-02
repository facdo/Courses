/*
    -------------- Passing and Returning Arrays to/from Functions-------------

    Code example on this topic.

    Remarks:
        - We loose the information about the size of the array when in
        function scope. The reason is because we don't really pass the array
        as an argument, just the pointer to the first element address. A way
        arround this is to also pass the size of the array as an argument.

*/

#include <iostream>

using namespace std;

// example function that takes an argument as input
// Equivalent syntax:
// printArray(const int len, string texts[])
// printArray(string (&texts)[size]) - Must specify the size when passing the array. sizeof(texts) will work!
void printArray(const int len, string *texts) {
    for(int i=0; i<len; i++) {
        cout << texts[i] << endl;
    }
}

// example function that returns a pointer to an array
int *genCoords() {
    // Never return a pointer to a local variable!! 
    // We should use the new operator, but keep in mind that we need
    // to delete the variable after use
    int *pCoords = new int[2];
    return pCoords;
}

// It is a good practice to have a function to delete our array
void freeMem(int *arr) {
    delete [] arr;
    cout << "array deleted" << endl;
}

int main() {
    string texts[] = {"blabla", "hahaha", "tanananan"};

    int len = sizeof(texts)/sizeof(string);
    printArray(len, texts);

    // lets use our function to generate an array
    int *pCoords = genCoords();
    pCoords[0] = 25;
    pCoords[1] = 127;
    cout << pCoords[0] << " " << pCoords[1] << endl;
    freeMem(pCoords);

    return 0;
}