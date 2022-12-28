// This contains the solution to the third examples in the pointer tutorial

#include <stdio.h>
#include <assert.h>

// function declaration
void correctBankMixup(float *a, float *b);

int main()
{
    // no swap necessary
    float a = 5;
    float b = 3;
    correctBankMixup(&a, &b);
    
    // test 1, ensuring no swap necessary
    assert(a == 5);
    assert(b == 3);
    
    // test 2, swap necessary
    a = -2;
    
    // ensuring swapped
    correctBankMixup(&a,&b);
    
    // will yield error if your solution is incorrect
    assert(a == 3);
    assert(b == -2);
    
    return 0;
}

// function implementation
void correctBankMixup(float *a, float *b)
{
    // Initializing temporary variable maintain value of a
    float temp_value = 0;
    
    // If account balance improper, swapping values of a and b
    if(*a <= 0)
    {
        // storing value of data referenced by a so not lost
        temp_value = *a;
        
        // swapping
        *a = *b;
        *b = temp_value;
    }
}
