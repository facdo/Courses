#ifndef PERSON_H_
#define PERSON_H_

#include <string>

// Here we put our class definition with the prototypes for the class functions
class Person {
// With the private keyword we state that the variables and methods are only accessible
// internally in the class
private:
    // This variable can only be set and altered by the class methods
    bool goodMood;
    // Sometimes it is useful to put class atribuites as private and then
    // define a Seter and a Geter function to write set/write and to get/read
    // those atribuites
    unsigned short int age;


// With the public keyword we state that these functions are accessible outside the class context
// (in a main function, for instance)
public:
    // A special method, called construction, is always runned when the class is
    // instaciated
    // The constructor must have the class name and it doesn't have a return type
    Person();
    // We can have a constructor overloading by declaring another constructor
    // that receives some input parameters
    // We can have as many constructors as we like, as long they have different
    // parameters
    Person(std::string name, unsigned short int age);
    // Another constructor
    Person(std::string name);
    // We can have variable associated with the data related to that person
    // These variable can be accessed in the class methods (functions) to alter 
    // its behaviour
    std::string name;
    
    // Here we put our public class methods
    void introduction();
    void greeting();
    void goodbye();
    void setGoodMood(bool isGoodMood);
    void setAge(unsigned short int newAge);
    unsigned short int getAge();

    // We can have another special method that does the opposite of a constructor,
    // a destructor method. It is like the constructor but with a ~ before the name
    ~Person();
};

#endif