#include <stdio.h>
#include <string.h>

// Function to perform Vigenere encryption
void vigenereEncrypt(char plaintext[], char key[]) {
    int plaintextLen = strlen(plaintext);
    int i, keyLen = strlen(key);

    for (i = 0; i < plaintextLen; i++) {
        if (plaintext[i] >= 'A' && plaintext[i] <= 'Z') {
            plaintext[i] = 'A' + (plaintext[i] - 'A' + key[i % keyLen] - 'A') % 26;
        }
    }
}

// Function to perform Vigenere decryption
void vigenereDecrypt(char ciphertext[], char key[]) {
    int ciphertextLen = strlen(ciphertext);
    int i, keyLen = strlen(key);

    for (i = 0; i < ciphertextLen; i++) {
        if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z') {
            ciphertext[i] = 'A' + (ciphertext[i] - 'A' - key[i % keyLen] + 'A' + 26) % 26;
        }
    }
}

int main() {
    char fullName[100];
    char key[20];

    printf("Enter your full name (UPPERCASE): ");
    fgets(fullName, sizeof(fullName), stdin);

    // Remove the newline character from the name
    fullName[strcspn(fullName, "\n")] = '\0';

    printf("Enter the encryption key (UPPERCASE): ");
    fgets(key, sizeof(key), stdin);

    // Remove the newline character from the key
    key[strcspn(key, "\n")] = '\0';

    printf("Original name: %s\n", fullName);

    // Encryption
    vigenereEncrypt(fullName, key);
    printf("Encrypted name: %s\n", fullName);

    // Decryption
    vigenereDecrypt(fullName, key);
    printf("Decrypted name: %s\n", fullName);

    return 0;
}

