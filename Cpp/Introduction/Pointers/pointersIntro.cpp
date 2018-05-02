/*
    Code based on the first part of Section 5 - Pointers and Memory, 
    of the C++ for Complete Beginners Course on Udemy.
    
    It includes basics of Pointers and Char arrays.
*/


#include <iostream>
using namespace std;

// function prototype that uses the pointer concepts learned in this tutorial
void manipulate(int* value);

int main() {

    // A pointer is a variable that stores the memory address for some variable type
    // We can define a pointer for any kind of variable type, by using the special
    // character '*' right after the type keyword (int* pointer, int *pointer are the same)
    // The pointer should receive the memory address for a variable
    // To get the address from a variable we can use the special character '&' right before it
    // Example:
    int nValue = 8; // int variable declaration
    int* pValue = &nValue; // creates a pointer with the value equals to the address of nValue

    // Lets look at the values stored
    cout << "Int value: " << nValue << endl;
    cout << "Pointer to the int address: " << pValue << endl;

    // We can retrieve the actual variable value associated with that pointer by
    // using the *pointer syntax, which dereferences the pointer
    cout << "Int variable value retrieved via ponter: " << *pValue << endl;

    // The function receives a pointer to an int, so we need to pass the memory
    // address of that int (we do that with the '&' char)
    manipulate(&nValue); // the same as passing pValue
    cout << nValue << endl;


    // Pointers and Arrays
    cout << endl;
    cout << "==========================================" << endl;
    cout << "----------- Pointers and Arrays ----------" << endl;
    cout << "==========================================" << endl;
    cout << endl;
    // Arrays can be seen as pointers to the memory address of the first element,
    // but unlike a simple pointer, an array also stores the size of the array, or
    // the number of elements that it has
    // So we can do stuff like:
    string texts[] = {"one", "two", "three"};
    string *pTexts = texts;

    // The standard way to iterate through the array elements is:
    for(int i=0; i<sizeof(texts)/sizeof(string); i++) {
        cout << texts[i] << "  " << flush;
    }

    // But we can also use the pointer
    // Adding one to the pointer means going to next chunk of memory
    // The standard way to iterate through the array elements is:
    for(int i=0; i<sizeof(texts)/sizeof(string); i++, pTexts++) {
        cout << *pTexts << "  " << flush;
    }

    cout << endl;

    // We can have two pointer, one for the first memory address of the array
    // and another for the last memory address
    string *pFirst = texts; // we don't need to pass the address because texts is a pointer
    string *pLast = &texts[2]; // we need to pass the address of the element

    // We can do a while loop and add 1 to pFirst while pFirst is less or equal than pLast
    while(pFirst <= pLast) {
        cout << *pFirst << "  " << flush;
        pFirst++;
    }
    cout << endl;

    // Pointers Arithmetics
    cout << endl;
    cout << "==========================================" << endl;
    cout << "-------- Pointers Arithmetics ------------" << endl;
    cout << "==========================================" << endl;
    cout << endl;

    // We can do operations with pointers. We saw that adding one to a pointer
    // moves it to the next memory location. If the pointer is pointing to the first
    // element of an array, adding one to it will make it point to the next element
    const int NARRAY = 5; // usually constants names are capitalized
    string myArray[NARRAY] = {"zero", "one", "two", "three", "four"};

    string *pArray = myArray;
    string *pEnd = &(myArray[NARRAY-1]);

    cout << *pArray << endl;
    pArray += 3; // adding 3 to pArray
    cout << *pArray << endl;
    pArray -= 2;
    cout << *pArray << endl;

    pArray = myArray;

    long elements = (long)(pEnd+1-pArray);
    cout << elements << endl;

    // Char Arrays
    cout << endl;
    cout << "==========================================" << endl;
    cout << "-------------- Char Arrays ---------------" << endl;
    cout << "==========================================" << endl;
    cout << endl;
    // We can make an array of chars to build a string
    // It is easy to loop through the characters to manipulate a string
    char text[] = "hello"; 
    for(int i=0; i<sizeof(text) - 1; i++) {
        // note that the sizeof char is 1, so we can omit the denominator,
        // but we need to subtract one to avoid printing the last element,
        // which is null
        cout << i << " : " << text[i] << endl; 
    }

    // We can use this to create a function that reverts strings inplace
    // Function prototype
    void reverseInplace(char *str, int len);

    // Function call
    reverseInplace(text, sizeof(text) - 1); // The last character in the array is Null!

    cout << endl;
    for(int i=0; i<sizeof(text) - 1; i++) {
        cout << i << " : " << text[i] << endl; 
    }

    // Reference Values
    cout << endl;
    cout << "==========================================" << endl;
    cout << "------------ Reference Values ------------" << endl;
    cout << "==========================================" << endl;
    cout << endl;

    // We can create a variable passing the address for another variable
    // In that way, the created variable will be a reference for the other
    // variable. Everything that happens to it will happens to the other variable
    int value1 = 9;
    int &value2 = value1; // value2 takes an address for value 1
    // when we do an atribuition to value2, value1 also changes
    value2 = 12;
    cout << "Value1: " << value1 << endl;
    cout << "Value2: " << value2 << endl;

    // This is particulary useful for when we want a function to change the
    // value of something without returning anything
    // Lets declare a prototype for function as an example
    void changeSomething(double &value);

    double newValue = 4.23;
    changeSomething(newValue);
    cout << "New value is: " << newValue << endl;

    return 0;
}

// This function can manipulate the value passed and the changes will remain in the
// main program. That is possible because we're passing a pointer to the variable memory address
void manipulate(int* value) {
    *value = 10;
    cout << *value << endl;
}

// function to reverse a string inplace. Doesn't return anything, but changes the string (char array)
void reverseInplace(char *str, int len) {
    char *pEnd = str + len - 1; // Pointer to the last element of the string
    while(str < pEnd) {
        char buffer = *str;
        *str = *pEnd;
        *pEnd = buffer;
        str++;
        pEnd--;
    }
}

void changeSomething(double &value) {
    value = 123.5;
}