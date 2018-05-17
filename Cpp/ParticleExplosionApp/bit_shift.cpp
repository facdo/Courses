/*
    -------------------------- Bit Shifting ------------------------------------

    The color for a pixel is specified by 4 bytes, or 4 chars.
    One for each color, red, green, blue and one for the alpha value.

    We need to be able to set each RGBA value individually and then reassign it
    to an unsigned int, which is the format that SDL works with.

    In this tutorial we will be covering how to do that using biit shift operations.

    We will be using these operations for seting our pixels in our Screen class

*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Lets define each value in a char, using hexadecimal numbers
    unsigned char alpha = 0xFF;
    unsigned char red = 0x0A;
    unsigned char green = 0x33;
    unsigned char blue = 0x3B;

    // This combination would yield the color 0xFF0A333B

    // our color is defined as an int
    unsigned int color = alpha;

    // using iomanip library we can see the int value in hexadecimal
    cout << hex << color << endl;

    // The real value of the int is 0x000000FF, but the zeros in the left are
    // ignored. To enable the view of this digits we will set the width of the 
    // displayed variable and also fill the blanks with the character '0'
    cout << setfill('0') << setw(8) << hex << color << endl;

    // Now we can see how bit shift operations works. The << operator shiifts the bits to the left
    // To shift it in one byte we can shift 8 bits (each 2 hex digits corresponds to 1 byte)
    color <<= 8; // The same as: color = color << 8;

    cout << setfill('0') << setw(8) << hex << color << endl;

    // We can add each RGBA char to the int and shift it by 1 byte to get the desired result
    color = 0;
    color += alpha;
    color <<= 8;
    color += red;
    color <<= 8;
    color += green;
    color <<= 8;
    color += blue;

    cout << setfill('0') << setw(8) << hex << color << endl;
    // see that the resulting color is exactly the one we wanted: 0xFF0A333B

    return 0;
}