/*  ----------------------------- Copy Constructors ----------------------

    Code example on how to create a copy constructor for a class.
    How to copy an object to other obect.

*/

#include <iostream>

using namespace std;

class Animal {
private:
    string species = "";
    string name = "";

public:
    Animal() { cout << "Animal created by the standard constructor." << endl; };
    Animal(string species): species(species) { cout << "Animal created by the custom constructor" << endl; };
    // Lets define our copy constructor here
    // We establish that the the animal to be copied is constant, meaning that its attribuites
    // can not be modified by our copy constructor
    Animal(const Animal &otherAnimal): name(otherAnimal.name), species(otherAnimal.species) { cout << "Copied" << endl; };
    void setName(string name) {
        this->name=name;
    };
    void setSpecies(string species) {
        this->species=species;
    };
    void printInfo() {
        if(species != "") {
            cout << "I am a " << species << ". " << flush;
        } else {
            cout << "Unknown species. " << flush;
        }
        if(name != "") {
            cout << "My name is " << name << ". " << endl;
        } else {
            cout << "I don't have a name." << endl;
        }
    }


};

int main() {
    // Testing the class functionality
    Animal dog("dog");
    Animal cat;
    cat.setName("Mimi <3");
    cat.setSpecies("super cute cat");
    dog.printInfo();
    cat.printInfo();

    // When we create a new object with an atribuition to
    // another object the constructor used is the copy
    // constructor by default. This constructor is created
    // implicityl, but we can define our own explicitly
    Animal dog2 = dog;
    dog.setName("Rusty");
    dog.printInfo();
    dog2.setName("Bobby");
    dog2.printInfo();

    return 0;
}