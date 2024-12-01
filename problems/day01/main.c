#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("/Users/johanngerberding/github/advent-of-code-2024/problems/day01/input.txt", "r");    
    int capacity = 10;
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
                printf("Memory reallocation failed!");
                free(arr1);
                free(arr2);
                return 1;
            }

            arr1 = temp1;
            arr2 = temp2; 
        }
    }

    // make sure the file reading works
    for (int i = 0; i < count; i++) {
        printf("arr1[%d]=%d, arr2[%d]=%d\n", i, arr1[i], i, arr2[i]);
    }




    // clean up 
    free(arr1);
    free(arr2);
    fclose(file); 
    return 0;
}