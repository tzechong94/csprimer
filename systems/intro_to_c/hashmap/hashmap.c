#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STARTING_BUCKETS 8
#define MAX_KEY_SIZE 32 // TODO remove this constraint

// an array of linkedlist
typedef uint32_t Hash;

typedef struct Node {
  char *key;
  void *value;
  Hash hash;
  struct Node *next; // address to the next node
} Node;

typedef struct Hashmap {
  Node **buckets;
  int num_buckets;
} Hashmap;

Hashmap* Hashmap_new (void) {
  Hashmap *h = (Hashmap *)malloc(sizeof(Hashmap));
  // calloc is zeroed out
  h->buckets = calloc(STARTING_BUCKETS, sizeof(Node));
  h->num_buckets = STARTING_BUCKETS;
  return h;
};

void Hashmap_free(Hashmap *h) {
  // TODO free all the node including string copies
  Node *prior, *n;
  for (int i = 0; i < h->num_buckets; i++) {
    n = h->buckets[i];
    while (n!= NULL){
      prior = n;
      n = n->next;
      free(prior->key);
      free(prior);
    }
  }
  free(h->buckets);
  free(h);
};

Hash djb2(const char *s) {
  int32_t h = 5381;
  char ch;
  while ((ch = *s++))
    h = ((h << 5) + h) + ch; // faster than multiplication
  return h;
}

void Hashmap_set(Hashmap *h, char *key, void* value){
  //TODO HANDLE COLLISION
  // Node* n = malloc(sizeof(Node));
  // n->key = strdup(key); // key points to the entire string (duplicate string)
  // // *key pionts to a single character (the first char of the string)
  // n->value = value;
  // n->hash = djb2(key);
  // h->buckets[n->hash % h->num_buckets]->next = n;
  // get hashkey first
  Hash hash = djb2(key);
  int i = hash % h->num_buckets;
  Node *n = h->buckets[i];

  while (n != NULL) {
    if (n->hash == hash && strncmp(key, n->key, MAX_KEY_SIZE) == 0) {
      n->value = value;
      return;
    }
    n = n->next;
  }

  n = malloc(sizeof(Node));
  n->key = strdup(key);
  n->value = value;
  n->hash = hash;
  n->next = h->buckets[i];
  h->buckets[i] = n;  
  // initialise new node
  // Node* new_node = malloc(sizeof(Node));
  // new_node->key = strdup(key);
  // new_node->value = value;
  // new_node->hash = hashkey;
  // new_node->next = NULL;
  // Node* existing_node = h->buckets[hashkey % h->num_buckets];
  // // check if bucket is empty
  // if (existing_node == NULL) {
  //   h->buckets[hashkey % h->num_buckets]= new_node;
  // } else {
  //   // if not empty, traverse linked list to check for an existing key or to insert at the end
  //   Node* prev = NULL;
  //   while (existing_node != NULL) {
  //     if (strncmp(existing_node->key, key, MAX_KEY_SIZE) == 0) {
  //       // key exists, update value
  //       existing_node->value = value;
  //       return;
  //     }
  //     prev = existing_node;
  //     existing_node = existing_node->next;
  //   }
  //   // key does not exist, insert the new node at the end of the list
  //   prev->next = new_node;
  // }
  // if no, next points to new node
  // if yes, existing node next points to new node
  
};

void* Hashmap_get(Hashmap *h, char *key){
  // TODO handle collision
  Hash hash = djb2(key);
  Node * n = h->buckets[hash % h->num_buckets]; 

  while (n != NULL) {
      if (n->hash == hash && strncmp(n->key, key, MAX_KEY_SIZE) == 0) {
        return n->value;
      } 
      n = n->next;
  //returns a node, get value from node
  }// value over null is segfault
  return NULL;
}

void Hashmap_delete(Hashmap *h, char *key) {
  Hash hash = djb2(key);
  int i = hash % h->num_buckets;
  Node *prior = NULL;
  Node * n = h->buckets[i]; 

  while (n != NULL) {
    if (n->hash == hash && strncmp(n->key, key, MAX_KEY_SIZE) == 0){
      if (prior == NULL) {
        h->buckets[i] = n->next;
      } else {
        prior->next = n->next;
      }
      free(n->key);
      free(n);
      return;
    }
    prior = n;
    n = n->next;
  }
  // if (h->buckets[hash % h->num_buckets] != NULL && strcmp(n->key, key) == 0){
  //   free(h->buckets[i]); // free the node
  //   h->buckets[i] = NULL;
  // }
  // TODO if there's nothing there, free NULL. only free if not null.
}


int main() {
  Hashmap *h = Hashmap_new();

  // basic get/set functionality
  int a = 5;
  float b = 7.2;
  Hashmap_set(h, "item a", &a);
  Hashmap_set(h, "item b", &b);
  assert(Hashmap_get(h, "item a") == &a);
  assert(Hashmap_get(h, "item b") == &b);

  // using the same key should override the previous value
  int c = 20;
  Hashmap_set(h, "item a", &c);
  assert(Hashmap_get(h, "item a") == &c);

  // basic delete functionality
  Hashmap_delete(h, "item a");
  // // printf("%p", Hashmap_get(h, "item a"));
  assert(Hashmap_get(h, "item a") == NULL);

  
  // // handle collisions correctly
  // // note: this doesn't necessarily test expansion
  // int i, n = STARTING_BUCKETS * 10, ns[n];
  // char key[MAX_KEY_SIZE];
  // for (i = 0; i < n; i++) {
  //   ns[i] = i;
  //   sprintf(key, "item %d", i);
  //   Hashmap_set(h, key, &ns[i]);
  // }
  // for (i = 0; i < n; i++) {
  //   sprintf(key, "item %d", i);
  //   assert(Hashmap_get(h, key) == &ns[i]);
  // }
  

  Hashmap_free(h);
  /*
     stretch goals:
     - expand the underlying array if we start to get a lot of collisions
     - support non-string keys
     - try different hash functions
     - switch from chaining to open addressing
     - use a sophisticated rehashing scheme to avoid clustered collisions
     - implement some features from Python dicts, such as reducing space use,
     maintaing key ordering etc. see https://www.youtube.com/watch?v=npw4s1QTmPg
     for ideas
     */
  printf("ok\n");
}
