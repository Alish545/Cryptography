#include <stdio.h>
#include <string.h>

// Function to encrypt a character using Caesar Cipher
char encryptChar(char ch, int key) {
    if (ch >= 'A' && ch <= 'Z') {
        return 'A' + (ch - 'A' + key) % 26;
    }
    return ch;
}

// Function to decrypt a character using Caesar Cipher
char decryptChar(char ch, int key) {
    if (ch >= 'A' && ch <= 'Z') {
        return 'A' + (ch - 'A' - key + 26) % 26;
    }
    return ch;
}

int main() {
    char fullName[100];
    int key, i;

    printf("Enter your full name(ALL IN UPPERCASE): ");
    fgets(fullName, sizeof(fullName), stdin);

    printf("Enter the encryption key: ");
    scanf("%d", &key);

    printf("Original name: %s", fullName);

    // Encryption
    for (i = 0; i < strlen(fullName); i++) {
        fullName[i] = encryptChar(fullName[i], key);
    }
    printf("Encrypted name: %s", fullName);

    // Decryption
    for (i = 0; i < strlen(fullName); i++) {
        fullName[i] = decryptChar(fullName[i], key);
    }
    printf("Decrypted name: %s", fullName);

    return 0;
}
