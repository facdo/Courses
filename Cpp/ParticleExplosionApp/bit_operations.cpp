/*
    -------------------------- Bit Shifting ------------------------------------

    The color for a pixel is specified by 4 bytes, or 4 chars.
    One for each color, red, green, blue and one for the alpha value.

    We need to be able to set each RGBA value individually and then reassign it
    to an unsigned int, which is the format that SDL works with.

    In this tutorial we will be covering how to do that using biit shift operations.

    We will be using these operations for seting our pixels in our Screen class


    ------------------------- Bitwise AND Operation -----------------------------

    To retrieve the individual RGBA color values from the 32bit color integer we 
    can use the bitwise and operation, done using the '&' character. It takes the 
    bit intersection between two values. Ex: 0x45001F00 & 0xF000FF00 = 0x40001F00
    So we use a mask, composed of 0s and Fs, to get bit portions that we want. 
    The mask with hexadecimal values F and 0 corresponds to the binary 11111111, 
    and 00000000 numbers.

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

    // Bitwise AND: the & operator, retrieveing the red, green and blue
    cout << "Retrieving the individual colors! Bitwise AND." << endl;
    int r_red = (color & 0x00FF0000) >> 16;
    int r_green = (color & 0x0000FF00) >> 8;
    int r_blue = (color & 0x000000FF);

    cout << "Red: " << r_red << endl;
    cout << "Green: " << r_green << endl;
    cout << "Blue: " << r_red << endl;

    return 0;
}