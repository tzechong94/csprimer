#include <stdio.h>

// int main()
// {
//     printf("hello, world\n");
//     return 0;
// }

/*print Fahrenheit-Celsius table
    for fahr = 0, 20,... , 3000
*/

int main() {
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    prinf("Celsius to Fahrenheit Conversion Table\n");
    fahr = lower;
    while (fahr <= upper) {
        celsius = 5.0/9.0 * (fahr - 32);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }

    /*
    int fahr;

    for (fahr = 300; fahr >= 0; fahr = fahr - 20)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
    */
    return 0;
}

// variables must be decalred before the yare used, usually at the beginning of the functino
/// before any executable statements. type, list of variables etc
