#include <stdio.h>

// int main()
// {
//     int c;

//     while ((c = getchar()) != EOF) {
//         printf("%d end of file",EOF);
//         printf("%d",(c = getchar()) != EOF);
//         putchar(c);
//         c = getchar();
//     }
//     return 0;
// }


// int main() {
//     printf("6\n");
//     return 0;
// }


// int main() {
//     // long nc;
//     // nc = 0;
//     // while (getchar() != EOF)
//     //     ++nc;
//     //     printf("%ld\n", nc);
//     double nc;
//     for (nc = 0; getchar() != EOF; ++nc)
//         ;
//     printf("%.0f\n", nc);
//     printf("Character count in float: %.0f\n", nc);
//     printf("Character count in integer: %d\n", (int)nc);
//     printf("Character count in hex: %X\n", (int)nc);

//     return 0;
// }

// int main() {
//     int c , nl;

//     nl = 0;
//     while ((c = getchar()) != EOF)
//         if (c == '\n')
//             ++nl;
//     printf("%d\n",nl);
// }

// word counting
// word is any sequence of characters that does not 
// contain a blank, tab or newline.

#define IN 1
# define OUT 0

/* count lines, words and characters in input*/

// main() {
// // state records whether the program is currently in 
// // a word or not
//     int c, nl, nw, nc, state;
//     state = OUT;
//     nl = nw = nc = 0;
//     while ((c = getchar()) != EOF) {
//         ++nc;
//         if (c == '\n') 
//             ++nl;
//         if (c == ' ' || c == '\n' || c == '\t') 
//             state = OUT;
//         else if (state == OUT) {
//             state = IN;
//             ++nw;
//         }
        
//     }
//     printf("%d %d %d\n", nl, nw, nc);
//  }

 // arrays

 // count digits, white space and others

 int main() {
    int c, i, nwhite, nother;
    int ndigit[10];

    nwhite = nother = 0;
    for (i = 0; i < 10; i++)
        ndigit[i] = 0;

    while ((c = getchar()) != EOF)
        if (c >= '0' && c<='9')
            ++ndigit[c-'0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;
    printf("digits = ");
    for (i = 0; i < 10; ++i)
        printf(" %d", ndigit[i]);
    printf(", white space = %d, other = %d\n", nwhite, nother);
    return 0;
}

int power(int m, int n);

main() {

    int i;
    for (i = 0; i< 10;++i)
        printf("%d %d %d\n", i, power(2,i), power(-3,i));
    return 0;
}

power(int base, int n) {
    int i, p;
    p = 1;
    for (i = 1; i <= n; ++i)
        p = p * base;
    return p;
}

/* a function definition has this form:
return-type function-name(parameter declarations, if any)
{
    declarations
    statements
}
*/

#define MAXLINE 1000

int getline(char line[], int maxline);
void copy(char to[], char from[]);

int main()
{
    int len;
    int max;
    char line[MAXLINE];
    char longest[MAXLINE];

    max = 0;
    while ((len=getline(line, MAXLINE)) >0)
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    if (max > 0)
        printf("%s", longest);
    return 0;
}

// read a line into s, return length
int getline(char s[], int lim) {
    int c,i;

    for (i =0; i<lim-1 && (c = getchar())!=EOF && c!='\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i]='\0';
    return i;
}

// copy from into to

void copy(char to[], char from[]) {
    int i;
    i = 0;
    while ((to[i] = from[i] != '\0'))
        ++i;
}
