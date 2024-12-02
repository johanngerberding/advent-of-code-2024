#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

#define MAX_LINE_LENGTH 1024

int countLines(FILE *file) {
    int lines = 0;
    char ch;
    while (!feof(file)) {
        ch = fgetc(file);
        if (ch == '\n') {
            lines++;
        }
    }
    rewind(file);
    return lines + 1;
}

int countNumbers(char *line) {
    int count = 0; 
    char *temp = strdup(line);
    char *token = strtok(temp, " ");
    while (token != NULL) {
        count++;
        token = strtok(NULL, " ");
    }
    free(temp);
    return count;
}

int validateLine(int **numbers, int row, int cols) {
    int direction; 
    int diff = numbers[row][1] - numbers[row][0];
    if (diff == 0) {
        return -1;
    } else if (diff > 0){
        // increase 
        direction = 0;
    } else {
        // decrease
        direction = 1;
    }
    for (int i = 1; i < cols; i++) {
        int diff = numbers[row][i] - numbers[row][i - 1];
        if (direction == 0) {
            if (diff <= 0 || diff > 2) return 0; 
        } else {
            if (diff >= 0 || diff < -2) return 0;
        } 
    }  
    return 1;
}


int main() {
    FILE *file = fopen("./input.txt", "r");
    
    if (file == NULL) {
        printf("Cannot open file.");
        return 1;
    }

    // count total lines 
    int rows = countLines(file);

    // allocate array of pointers 
    int **numbers = malloc(rows * sizeof(int));
    // number of cols per row 
    int *cols = malloc(rows * sizeof(int));
    
    // read file line by line 
    int row = 0;
    char line[MAX_LINE_LENGTH];
    while (fgets(line, MAX_LINE_LENGTH, file)) {
        // remove newline if present
        line[strcspn(line, "\n")] = 0;
        cols[row] = countNumbers(line);

        // allocate array for this row
        numbers[row] = malloc(cols[row] * sizeof(int));
        // parse numbers from line 
        char *token = strtok(line, " ");
        int col = 0;
        while (token != NULL && col < cols[row]) {
            numbers[row][col] = atoi(token);
            token = strtok(NULL, " ");
            col++;
        } 
        row++;
    } 
    fclose(file);    

    
    int valid;
    // now do stuff
    for (int i = 0; i < rows; i++) {
        valid = validateLine(numbers, i, cols);
        if (valid) {
            printf("Line %d is valid", i);
        }
    }

    // free memory
    for (int i = 0; i < rows; i++) {
        free(numbers[i]);
    }
    free(numbers);
    return 0;
}