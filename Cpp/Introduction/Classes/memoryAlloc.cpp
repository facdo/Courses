/*
    --------------------- Memory Allocation ------------------------

    Content:
        - new operator with arrays
        - arrays with functions
        - exercise on how to iterate through an array of objects and set
        the attribuites based on a array of chars

*/

#include <iostream>
#include <sstream>

using namespace std;

// Class to help understanding the concepts of memory allocation with object arrays
class Device {
private:
    string type = "";
    unsigned int size[2] = {0,0};
public:
    Device() { cout << "New device created" << endl; };
    ~Device() { cout << "Device destroyed" << endl; };
    void setType(string type) {
        this->type = type;
     };
    void setSize(unsigned int *size) {
        this->size[0] = size[0];
        this->size[1] = size[1];
    };
    void printInfo() {
        cout << "Device: " << type << "; size: " << size[0] << " by " << size[1] << endl;
    };

};

int main() {
    
    // test the class functionality
    Device chip;
    chip.setType("microcontroller");
    unsigned int size[] = {230,410}; 
    chip.setSize(size);
    chip.printInfo();

    cout << endl;
    cout << "-------------------------------------------" << endl;
    cout << endl;

    // ---------------- Memory Allocation ------------
    // We can use the new operator to create an array of objects
    Device *pChip = new Device[27];

    char alpha[] = "abcdefghijklmnopqrstuvxwyz";
    cout << sizeof(alpha) << endl;
    
    // lets iterate over pChip and set a alphabet letter as type for each instance
    for(int i=0; i<sizeof(alpha)-1; i++, pChip++) {
        // We need to create a stringStream because we can't concatenate
        // char in a string
        stringstream aux;
        aux << "Verum-";
        aux << alpha[i];
        string type = aux.str();
        pChip->setType(type);
        pChip->printInfo();
    }

    // Let's take the pChip pointer back to the first element, so we can delete
    // the entire array
    pChip -= 26;


    // to delete an array we have to use []
    delete [] pChip;


    return 0;
}