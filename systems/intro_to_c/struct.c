#include <stdio.h>


struct user {
    int age; //4 byte
    short postcode; // 4byte (2 byte + padding)
    char* name; // 8byte
};

int main() {
    struct user u = {25, 10000, "Bob"};
    struct user u2 = { 17, 20000, "Alice"};

    struct user * p = &u2;

    printf("%s is %d years old\n", u.name, u.age);
    printf("%s is %d years old\n", (*p).name, (*p).age);

    printf("%p %p %p %p\n", &u, &(u.age), &(u.postcode), &(u.name));

    struct user users[2] = {
        {1, 10000, "foo"},
        {2, 10001, "bar"}
    };

    printf("One struct is %lu bytes \n", sizeof(struct user));
    printf("%s is %d years old\n", users[1].name, users[1].age);
    printf("users array is at %p, \"%s\") is located at %p\n", users, &users[1].name);
    printf("ok\n");
}

// struct is a kind of variable for grouping and referencing convenience