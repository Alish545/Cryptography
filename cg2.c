#include <stdio.h>
#include <string.h>

#define SIZE 3 // Size of the key matrix

// Function to perform matrix multiplication
void matrixMultiply(int key[SIZE][SIZE], int input[SIZE], int result[SIZE]) {
	int i, j;
    for (i = 0; i < SIZE; i++) {
        result[i] = 0;
        for (j = 0; j < SIZE; j++) {
            result[i] += key[i][j] * input[j];
        }
        result[i] %= 26; // Assuming only uppercase letters
    }
}

int main() {
    char fullName[100];
    int i, j, key[SIZE][SIZE] = {{6, 24, 1}, {13, 16, 10}, {20, 17, 15}}; // Example key matrix
    int encrypted[SIZE], decrypted[SIZE];

    printf("Enter your full name (UPPERCASE): ");
    fgets(fullName, sizeof(fullName), stdin);

    // Remove the newline character from the name
    fullName[strcspn(fullName, "\n")] = '\0';

    printf("Original name: %s\n", fullName);

    // Encryption
    for (i = 0; i < strlen(fullName); i += SIZE) {
        int input[SIZE] = {0};
        for (j = 0; j < SIZE; j++) {
            if (i + j < strlen(fullName)) {
                input[j] = fullName[i + j] - 'A';
            }
        }
        matrixMultiply(key, input, encrypted);

        for (j = 0; j < SIZE; j++) {
            printf("%c", encrypted[j] + 'A');
        }
    }
    printf("\n");

    // Decryption (assuming the key is invertible)
    // You need to calculate the inverse of the key matrix and use it here

    return 0;
}

