#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define HASH_SIZE 10000

typedef struct Node{
    int value;
    int count;
    struct Node* next;
} Node;

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int hash(int value) {
    return abs(value) % HASH_SIZE;
}

Node* hash_table[HASH_SIZE] = {NULL};

void increment_count(int value) {
    int index = hash(value);
    Node* current = hash_table[index];

    // search for existing value
    while (current != NULL) {
        if (current->value == value) {
            current->count++;
            return;
        }
        current = current->next;
    }
    // value not fount 
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;
    new_node->count = 1;
    new_node->next = hash_table[index];
    hash_table[index] = new_node;
}

int get_count(int value) {
    int index = hash(value);
    Node* current = hash_table[index];

    while (current != NULL) {
        if (current->value == value) {
            return current->count;
        }
        current = current->next;
    }
    return 0;
}

void free_hash_table() {
    for (int i = 0; i < HASH_SIZE; i++) {
        Node* current = hash_table[i];
        while (current != NULL) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
}

int main() {
    FILE *file = fopen("../input.txt", "r");    
    int capacity = 100;
    int *arr1 = NULL; 
    int *arr2 = NULL; 
    int count = 0; 

    if (file == NULL) {
        printf("Error opening file!");
        return 1; 
    }
    // initial memory allocation
    arr1 = malloc(capacity * sizeof(int));
    arr2 = malloc(capacity * sizeof(int));

    if (arr1 == NULL || arr2 == NULL) {
        printf("Memory allocation failed!");
        return 1;
    }

    while (fscanf(file, "%d %d", &arr1[count], &arr2[count]) == 2){
        count++;
        // if we need more space 
        if (count >= capacity) {
            capacity *= 2;
            int *temp1 = realloc(arr1, capacity * sizeof(int));
            int *temp2 = realloc(arr2, capacity * sizeof(int));

            if (temp1 == NULL || temp2 == NULL) {
                printf("Memory reallocation failed!\n");
                free(arr1);
                free(arr2);
                return 1;
            }

            arr1 = temp1;
            arr2 = temp2; 
        }
    }

    qsort(arr1, count, sizeof(int), compare);
    qsort(arr2, count, sizeof(int), compare);
    
    int distance = 0;  
    for (int i = 0; i < count; i++) {
        distance += abs(arr1[i] - arr2[i]);
    } 

    printf("Part 1 - Total distance: %d\n", distance);

    int similarityScore = 0;
    for (int i = 0; i < count; i++) {
        increment_count(arr2[i]);
    }

    int numberCount = 0;
    for (int i = 0; i < count; i++) {
        numberCount = get_count(arr1[i]);
        similarityScore += (arr1[i] * numberCount); 
    }

    printf("Part 2 - Similarity score: %d\n", similarityScore);
    
    // clean up 
    free(arr1);
    free(arr2);
    fclose(file); 
    return 0;
}