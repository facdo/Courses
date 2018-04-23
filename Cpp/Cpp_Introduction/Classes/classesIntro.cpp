// Main program to test the class Person
// The files Person.h and Person.cpp are associated with this tutorial

#include <iostream>

// We must include our module with our Person class definition
#include "Person.h"

using namespace std;

int main() {
    // to use a class we can make an instance of that class, just like
    // declaring a variable
    // That instance of a class is what we call an object, and it will
    // have the methods (functions) and data associated with that particular class
    Person felipe;
    Person rita;

    // We can use class methods and variables from an instance using the dot ('.') notation
    felipe.name = "Felipe Costa";
    felipe.setGoodMood(true);

    // Instead of seting the class properites manually we can initialize some of them
    // when the object is instatiated. We need a constructor, which is a special method
    // to do that (initialize certain variables and methods when the object is created)
    felipe.introduction();
    felipe.greeting();
    felipe.goodbye();
    felipe.setAge(26);
    cout << "Felipe is " << felipe.getAge() << " years old" << endl;

    rita.name = "Rita Costa";
    rita.setGoodMood(false);
    rita.greeting();

    // We can have a specific scope for our objects/variables/functions by using
    // the curly brackets
    {
        // This person would be a local variable inside this curly brackets
        // The variable won't be accessible outside this scope
        // We can use the constructor that receives input parameters
        // The compiler will pick the constructor depending upon the parameters
        // that were passed
        Person person("Mr. Pickles", 43);
        person.introduction();
        // We can see from the destructor message that this object is
        // destroyed after the curly brackets
    }

    // Note that after defining a destructor for our class, all instances of that
    // class are destroyed after the scope on which they are running (the main program)
    // ends
    cout << "Now all the objects will be destroyed and the memory will be free!" << endl;

    return 0;

}
