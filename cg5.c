#include <stdio.h>
#include <string.h>

// Function to perform Rail Fence encryption
void railFenceEncrypt(char *plaintext, int key) {
    int length = strlen(plaintext);
    char encrypted[length];
    int index = 0;
    int row, step1, step2, pos, flag;
    
    for (row = 0; row < key; row++) {
        step1 = (key - row - 1) * 2;
        step2 = row * 2;

        pos = row;
        flag = 0;

        if (row == 0 || row == key - 1) {
            while (pos < length) {
                encrypted[index++] = plaintext[pos];
                pos += (key - 1) * 2;
            }
        } else {
            while (pos < length) {
                encrypted[index++] = plaintext[pos];
                if (flag == 0) {
                    pos += step1;
                    flag = 1;
                } else {
                    pos += step2;
                    flag = 0;
                }
            }
        }
    }

    encrypted[index] = '\0';
    strcpy(plaintext, encrypted);
}

// Function to perform Rail Fence decryption
void railFenceDecrypt(char *ciphertext, int key) {
    int length = strlen(ciphertext);
    char decrypted[length];
    int index = 0;
    int row, step1, step2, pos, flag;

    for (row = 0; row < key; row++) {
        step1 = (key - row - 1) * 2;
        step2 = row * 2;

        pos = row;
        flag = 0;

        if (row == 0 || row == key - 1) {
            while (pos < length) {
                decrypted[pos] = ciphertext[index++];
                pos += (key - 1) * 2;
            }
        } else {
            while (pos < length) {
                decrypted[pos] = ciphertext[index++];
                if (flag == 0) {
                    pos += step1;
                    flag = 1;
                } else {
                    pos += step2;
                    flag = 0;
                }
            }
        }
    }

    decrypted[length] = '\0';
    strcpy(ciphertext, decrypted);
}

int main() {
    char fullName[100];
    int key;

    printf("Enter your full name: ");
    fgets(fullName, sizeof(fullName), stdin);

    printf("Enter the encryption key (number of rails): ");
    scanf("%d", &key);

    // Remove the newline character from the name
    fullName[strcspn(fullName, "\n")] = '\0';

    printf("Original name: %s\n", fullName);

    // Encryption
    railFenceEncrypt(fullName, key);
    printf("Encrypted name: %s\n", fullName);

    // Decryption
    railFenceDecrypt(fullName, key);
    printf("Decrypted name: %s\n", fullName);

    return 0;
}

