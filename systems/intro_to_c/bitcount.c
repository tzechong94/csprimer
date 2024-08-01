#include <assert.h>
#include <stdio.h>


int bitcount(unsigned n) {
    int count = 0;

    while (n) {
    //     count += n & 0x01;
    //     n >>= 1;
        n &= (n - 1);
        // same as n = n & (n - 1)
        count++;
    }
    return count;

}

// x &= (x-1) rightmost bit deleted 0 turns into 1




int main() {
    assert(bitcount(0) == 0); //0b0
    assert(bitcount(1)== 1); //0b1
    assert(bitcount(3) == 2); //0b11
    assert(bitcount(8) == 1); //0b1000

    assert(bitcount(0xffffffff) == 32);
    printf("OK\n");
}

