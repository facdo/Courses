/*
    Example on how to implement Inheritance in classes

    The main idea is that a class can inherit the attribuites and methods of a 
    parent class, but also retaining its own specific attribuites and methods.

    The classical example is a class Cat which may inherit generic features from
    a class Animal.

*/

#include <iostream>
using namespace std;

// Lets create an Animal class with some generic Animal attribuites
class Animal {

private:
    string name = "";
    string species = "";

public:

    Animal() { cout << "Animal created." << endl; }
    // Constructor that takes a species parameter
    Animal(string species): species(species) { cout << species << " created." << endl; }
    void setName(string name) {
        this->name = name;
    };
    void noise() { 
        cout<< "Grrrr" << endl; 
    }
    void printInfo() {
        cout << "I am an Animal. " << flush;
        if(species!="") {
            cout << "I am also a " << species << ". " << flush;
        }
        if(name!=""){
            cout << "My name is " << name << flush;
        }
        cout << endl;
    }
        
};

// Now lets use the predefined Animal class to pass those generic attribuites
// to a Cat class. The general syntax is: class ClassName: public ParentClassName { class definition};
// This process can be repeated indefitly. For instance, we can have a parent class Animal, a child Feline,
// and then a Cat class will inherit Feline which inherit Animal. We can even have a specific special cat
// that would inherit Cat and have all Animal, Feline, Cat features and some more
class Cat: public Animal {
// Let's have some specific Cat attribuites and methods
private:
    unsigned short int nLives = 7;
public:
    // Since species is a private Animal parameter we can't access it from Cat,
    // but we can initialize our cat using the Animal parameterized constructor,
    // passing cat as the species argument
    Cat(): Animal("cat")  { }
    unsigned short int remainingLives() { return nLives; }
    void almostDie() { 
        if(nLives>1) {
            nLives -= 1;
            cout << "The cat almost died. Now it has " << nLives << " lives" << endl;
        } else {
            nLives=0;
            cout << "7 lives were spend. This time your cat really died" << endl;
        }
    }

};

/*
    --------------- Constructor Inheritance --------------------

    We can specify which super-class (parent class) constructor
    will be called when we create an instance of our child class.
    To acess the direct super class private attribuites we can use
    the constructor inheritance feature, passing the child class 
    instantiation arguments in to the direct super class on the 
    constructor. See the example bellow
*/

class Machine {
private:
    int id;
public:
    Machine() { cout << "Machine no-argument constructor called. " << endl; }
    Machine(int id): id(id) { cout << "Machine parameterized constructor called. " << endl; }
    void info() { cout << "ID: " << id << endl; }
}; 

class Vehicle: public Machine {
public:
    Vehicle() {cout << "Vehicle no-argument constructor called." << endl; }
    // Note that we are using the super class constructor to pass the private argument (id)
    // to the Vehicle instance
    Vehicle(int id): Machine(id) { cout << "Vehicle parameterized constructor called. " << endl; }
};

// Lets create another class level, in which the direct super class is Vehicle
class Car: public Vehicle {
public:
    Car() {cout << "Car no-argument constructor called." << endl; }
    // Note that we are using the super class constructor to pass the private argument (id)
    // to the Vehicle instance
    Car(int id): Vehicle(id) { cout << "Car parameterized constructor called. " << endl; }

};

int main() {

    Animal blub;
    blub.setName("Jingles");
    blub.printInfo();

    // Note that the child class cat inherits the setName method
    Cat mimi;
    mimi.setName("Mimi");
    mimi.printInfo();

    // Lets play around with the specific cat attribuites
    Cat badCat;
    while(badCat.remainingLives()!=0){
        cout << "The bad cat fell in a trap. " << endl;
        badCat.almostDie();
    }

    // Example on Constructor Inheritance
    cout << endl;
    cout << "---------------------------------------" << endl;
    cout << "------ Constructor Inhertiance --------" << endl;
    cout << "---------------------------------------" << endl;
    cout << endl;

    Car sandero(13423);
    sandero.info();


    return 0;
}