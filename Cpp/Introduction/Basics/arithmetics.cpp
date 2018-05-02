// Basic operations in c++

#include <iostream>
using namespace std;

/*
    Basic Operators:
    + : addition;
    - : subtraction;
    * : multiplication;
    / : division;
    % : mod operator (returns the rest of division);
    += : increments the variable by a certain amount (a += 3 => a = a + 3);
    -= : subtracts the variable by a certain amount;
    *= : updates the variable by a multiplicative factor (a *= 3 => a = a * 3);
    /= : updates the variable by a divisive factor (a /= 3 => a = a / 3);

    The mathematics operation precedence rules are applied!
    We can use round brackets () to specify the order of operations
    Ex:
        (4+3)*5 != 4+3*5
*/

int main() {

    // Note on division: if a and b are integers the operation a/b will return an
    // integer (the rest of the division will be ignored)
    // To have decimal point division we can cast an integer variable into a float/double
    int a = 7;
    int b = 3;
    double c = a/b;
    cout << "Division result before casting into double: " << c << endl;

    // if one of the variable is a double or float the division will return a decimal point number
    c = (double)a/b;

    cout << "Division result after casting into double: " << c << endl;

    // The mod operator gets the remainder of a division
    int d = a % b;
    cout << d << endl;

    return 0;
}