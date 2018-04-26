// Here we have our class functions declaration

#include <iostream>

// We need to include our class header
#include "Person.h"

using namespace std;


// Here we define our class constructor, with the variables and methods
// that must be called when an object of that class is created
Person::Person() {
    cout << "New person created!" << endl;
}

// Alternative constructor to set the name and age
Person::Person(std::string name, unsigned short int age) {
    // We use the keyword this to avoid variable name confusion
    // this->variable specifies that it is a class variable
    this->name = name;
    this->age = age;
}

// Alternative constructor to set the name only, using Constructor Initialization List
// Recommended method for writing a constructor. We can pass as many arguments as we want
// separating then with commas, ','
// Since the constructor only initialize those variables it doesn't need any code inside
// the curly brackets
Person::Person(std::string name): name(name) {}

// Here we put the destructor definition
Person::~Person(){
    cout << "Person destroyed" << endl;
}
// We have a special syntax to indicate that these functions are related to the 
// Person class
void Person::introduction() {
    cout << "Hello, my name is "<< name << endl;
}

void Person::greeting() {
    if(goodMood){
        cout << "Hello, how are you doing?" << endl;
    } else {
        cout << "Hi..." << endl;
    }
    
}

void Person::goodbye() {
    cout << "Goodbye, see you next time." << endl;
}

void Person::setGoodMood(bool isGoodMood) {
    if(isGoodMood) {
        goodMood = true;
    } else {
        goodMood = false;
    }
}

void Person::setAge(unsigned short int newAge) {
    age = newAge;
}

unsigned short int Person::getAge() {
    return age;
}

