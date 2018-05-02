// This file contains the basics of C++ syntax

#include <iostream>
#include <climits>
#include <iomanip>

using namespace std;

int main() {
    // ----------------------------- Variable Types ----------------------------
    // integers have a memory limit
    // We can see those limits using the limits library

    cout << "The maximum int value is: " << flush;
    cout << INT_MAX << endl;

    cout << "The minimum int value is: " << flush;
    cout << INT_MIN << endl;
    cout << endl;

    // For integers above or bellow these limits we can use long int
    // To save memory we can use short int, but that is limited small numbers

    long int x = 1315553334;
    short int y = 144;

    // we can chech how much memory space a variable or a type uses with the sizeof()
    // built in function
    cout << "X is: " << x << " and it's size is: " << sizeof(x) << endl;
    cout << "Y is: " << x << " and it's size is: " << sizeof(y) << endl;
    
    cout << "A normal integer has a size of: " << sizeof(int) << endl;

    // if we know that we're only storing positive numbers we can use unsigned ints

    unsigned int idValue = 142393;
    cout << idValue << " the memory size is the same as int: " << sizeof(idValue);
    cout << endl;

    // Decimal numbers are called float
    float myHeight = 1.73;

    // A float number can be printed in two forms: fixed notation or scientific notation
    // We need to include the iomanip library to make use of the fixed or scientific 
    // keywords in the cout statement
    cout << fixed << myHeight << " is my height in meters." << flush;
    cout << "It uses: " << sizeof(myHeight) << " bytes of memory" << endl;

    // note that we can use only a certain amount of precision in your decimal numbers
    // we can set the precision using the setprecision function

    cout << setprecision(2) << myHeight << endl;

    // You must match the precision with the memory allocation for a variable
    // Note that forcing a high precision in a 4 byte float would produce garbage
    // up to a certain digit
    cout << setprecision(32) << myHeight << endl;

    // We can use a double instead of a float to store decimal point numbers with 
    // more precision. We can use long double for even more precision
    double piValue = 3.1415926535;
    long double highPrecisionPi = 3.14159265358979323;

    cout << setprecision(10) << flush;
    cout << "The value of pi is: " << piValue << " with: " << sizeof(piValue) << " bytes" << endl;
    cout << setprecision(14) << flush;
    cout << "The value of pi is: " << highPrecisionPi << " with: " << sizeof(highPrecisionPi) << " bytes" << endl;

    // for very big or very small numbers we can use scientific notation
    float astroConstant = 1432574.764;
    cout << setprecision(6) << scientific << astroConstant << endl;

    // Other build in types
    // Boolean: bool, only true or false values
    // in C true is rendered to 1 and false to 0
    bool amAwsome = true;
    cout << amAwsome << endl;

    // char, single character in the ASCII set, with only 1byte (128 possible values)
    // you can assign a number and it would correspond to the ASCII character for that number
    // Use singe quotes '' to define a char
    char anyChar = 'c';
    char numChar = 102; 
    cout << anyChar << "  " << numChar << endl <<endl;

    // we can use an int statement to "cast" a char into the corresponding integer
    cout << "The 'c' character coorespond to the number: " << (int)anyChar << endl;  

    // to use special characters we can use the wchar_t (wide char), that uses 2 bytes
    // we need to cast it as char to see the actual character
    wchar_t specialChar = 'í';
    cout << (char)specialChar << " has a size of: " << sizeof(wchar_t) << endl;

    // -------------- Conditionals: If, Elif, Else and Switch Statements --------------
    
    // Conditional statements allow checking some boolean expression and executing code
    // based on the result of the expression (if it is true or false)
    // If statement:
    // let's print a funny sentence if the user types the write password
    string password = "123456";
    // also, lets have a magical keyword that prints some crazy text
    string magicalKey = "porcupine";
    cout << "Type the correct password: " << flush;

    string userString;
    cin >> userString;

    // comparison operators:
    // == equality
    // != inequality
    // > greater than
    // < less than
    // >= or <= greater/less or equal than
    // use && to concatenate conditions (condition1 AND condition2)
    // use || to execute if at least one condition is met (condition1 OR condition2)

    if(userString == password) {
        cout << "Banging your head against a wall burns 150 kcalories an hour..." << endl;
    }
    else if(userString == magicalKey) {
        cout << "HaHA!! You found the most amazing easteregg ever!!! Congratulations!!" << endl;
    }
    else {
        cout << "Wrong password... " << endl;
    }

    // Switch Statement
    // case we have many conditions to check we can use switch case statements
    cout << "Type a number from 0 to 100: " << flush;
    int number;
    cin >> number;
    switch (number) {
        case 0:
            cout << "You lose! You typed 0" << endl;
            break;
        case 1:
            cout << "You lose! You typed 1" << endl;
            break;
        case 4:
            cout << "You lose! You typed 4" << endl;
            break;
        case 42:
            cout << "Yes!! That is the Secret of the Universe!! :-)" << endl;
            break;
        default:
            cout << "You are doomed... Muahahahaha" << endl;
    }
    cout << flush;


    // Comparing floats: not a trivial thing
    float rndValue = 1.1;
    if(rndValue == 1.1) {
        cout << "Equal" << endl;
    }
    else {
        cout << "Not Equal! How Crazy is that, hum? haha" << endl;
    }

    // To compare floats we need to check if the differente between then is less than a certain
    // value, according to the precision required
    if(rndValue-1.1 < 0.001){
        cout << "Close enought" << endl;
    }
    else {
        cout << "Not really... The value minus 1.1 is greater than 0.001" << endl;
    }

    // we can define a boolean variable to store a certain condition:
    // in case we have a complicated condition, with many logical operators (&&, ||)
    bool condition = (4 != 3) && (10 > 9);

    // ------------------------- Loops: Repeating Blocks of Code ---------------------
    // while loop: it will execute the code inside until the condition is not met anymore
    short int iterator = 0;
    while(iterator<=20) {
        cout << "Condition is true, iterator value is: " << iterator << endl;
        // we can update the value of the iterator increasing it by 1 using:
        iterator++; // the same as: iterator = iterator + 1;
    }

    // do while loop: it will execute the code inside at least one time, and than check
    // the condition in the end to figure if the loop will continue
    do {
        cout << "It is not checking the condition, yet" << endl;
    } while(false);

    // we can do that to promp for a password, repeating until the condition is met
    string input;
    password = "helloworld";
    do {
        cout << "Type the correct password: " << flush;
        cin >> input;
        if(input != password) {
            cout << "Access denied!" << endl;
        }
    } while (input != password);

    cout << "Password correct, you may come in! :)" << endl;

    // Now, the MOST IMPORTANT TYPE OF LOOP: .......
    // The amazing for loop!!  :)  :)  ;-)
    // Haha, for loops execute a certain amount of times
    // We define how many times it will execute upon calling the statement
    // The syntax is like the following: for(variable;condition;update variable) {code to execute}
    for(int i=0;i<10;i++){
        // the loop will execute 10 times
        // we can check our iterator i in every loop step
        // i is a local variable that only works in the context of the for loop
        cout << "Counting " << i << endl;
    }

    // Break and Continue
    // We can exit a loop using the break statement
    // we can continue to the next operation using the statement continue
    int i = 0;
    while(true){
        if(i == 3){
            break;
        }
        i++;
    }
    for(int i=0;i<10;i++){
        //lets skip the 5, going to the next iteration if the condition is met
        if(i == 5){
            continue;
        }
        cout << i << endl;
    }

    // ------------- Arrays: Storing Multiple Elements in a Variable -------------
    // we need to specify the size of the array beforehand
    // also, we need to tell what kind of variable the array would be storing
    int myArray[10] = {1,2,3,4,5,6,7,8,9,10};
    // the index starts at 0, so the last index in this case would be 9, not 10!
    myArray[0] = 23;
    myArray[9] = 41;
    // we can iterate through the array and print its values
    for(int i=0; i<10; i++){
        cout << "Array value is: "<< myArray[i] << endl;
    }
    
    // we can initialize an empy array using empy curly brackets
    int otherArray[10] = { };

    // also, you don't need to set the size if you are initializing the elements
    string fruits[] = {"Apple", "Banana", "Orange"};

    // C++ doesn't show you an error if you try to access values out of the
    // index of your array, it will print whatever is stored in that part of memory, or simply crash
    // cout << "This is not a fruit... " << fruits[4] << endl;

    // MultiDimentional Arrays:
    // First brackets indicates the rows and the second the columns
    // Each element of a multidimentional array would be an array
    string animals[2][3] = {
        {"fox", "dog", "cat"},
        {"chicken", "eagle", "crow"}
    };

    // We will use a nested loop to print those values
    for(int i=0; i<2; i++) {
        for(int j=0; j<3; j++) {
            cout << "Row: " << i << " Column: " << j << flush;
            cout << " Animal: " << animals[i][j] << endl;
        }
    }

    // lets print it like a table:
    for(int i=0; i<2; i++) {
        for(int j=0; j<3; j++) {
            cout << (i+1)*(j+1) << " - " << animals[i][j] << "\t" << flush;
        }
        cout << endl;
    }

    // Array Size:
    // We can use the sizeof function to get the number of bytes that an array is using
    // We now, from the type of the array, how many bytes one element uses
    // So, dividing the total size by the element size we know how many elements
    // an array has
    int values[] = {1,5,4,3,2,76,9,6,4,3,4,5,6,8,9,2,1,2,3,5};
    unsigned int numElements = sizeof(values)/sizeof(int);

    cout << "=============================" << endl;
    cout << "The array has: " << numElements << " elements" << endl;
    // when iterating through the array we can use the number of elements
    for(int i=0; i < numElements; i++){
        cout << values[i] << " " << flush;
    }
    cout << endl;


    return 0;

}
