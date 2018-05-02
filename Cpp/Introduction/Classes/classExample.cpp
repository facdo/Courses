/*  ----------------------------- Copy Constructors ----------------------

    Code example on:
        - how to create a copy constructor for a class.
        - How to copy an object to other obect.


    ------------------------- New and Delete Operators -------------------

    Usage of the new and delete operator:
        - explicitly allocate memory for an object
        - define when the destructor will be called for freeing the memory
        associated with an object
        - returning pointers to objectes created wtihin functions

    We use new when we want to decide when our objects will be destroyed, to use
    then outside the scope in whiche they are instanciated and to create undetermined
    size arrays. Ex: ClassName *myArray = new ClassName[variableSize]; ... ; delete []myArray;

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
    // Lets also define a simple destructor
    ~Animal() { cout << "Animal destroyed... " << species << " " << name << endl; }
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

// Example on how to properly return an object from a function
Animal *createAnimal(string species) {
    // by using the new operator we make sur that the animal is not destroyed
    // once the function scope ends. But we must make sure to delete it afert usage
    Animal *pAnimal = new Animal();
    pAnimal->setSpecies(species);
    return pAnimal; // note that we are returning a pointer to the animal
}

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

    // The new operator can be used for instanciating an object
    // Instead of creating the object itself a pointer to that object
    // is created.
    Animal *pCat = new Animal(); // If no arguments are passed for the constructor the () is optitional
    // Since pCat is a pointer we can't use the class methods directly with the . notation 
    // We could dereference the pointer and apply the methods, but the . operator has higher precedence
    // than the dereference operator, so we need to use (). Ex: (*pCat).setName("Garfield")
    // But the prefered way is to use a special syntax for pointers, the arroy notation, like we
    // did with the "this" keyword
    pCat->setName("Garfield");
    pCat->printInfo();

    // Since we used the new operator we have to explicitly delete the object to
    // call the destructor, otherwise we can see that the destructor is not called
    // Commenting the line bellow we can see that Garfield is not destroyed
    delete pCat;

    // If we don't use this we might have bugs associated with memory leaks
    // Also, it is very important to only call delete on objects created with the
    // new command. Deleting other objects might cause random crashes in our program

    // Let's use our function to create a new animal
    Animal *pFrog = createAnimal("frog");
    // since this is a pointer we must use the -> notation
    pFrog->printInfo();

    // After usage we must delete it
    delete pFrog;

    return 0;
}