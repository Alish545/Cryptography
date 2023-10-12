# Additive Constants
K = [
    0x428A2F98D728AE22, 0x7137449123EF65CD, 0xB5C0FBCFEC4D3B2F, 0xE9B5DBA58189DBBC,
    0x3956C25BF348B538, 0x59F111F1B605D019, 0x923F82A4AF194F9B, 0xAB1C5ED5DA6D8118,
    0xD807AA98A3030242, 0x12835B0145706FBE, 0x243185BE4EE4B28C, 0x550C7DC3D5FFB4E2,
    0x72BE5D74F27B896F, 0x80DEB1FE3B1696B1, 0x9BDC06A725C71235, 0xC19BF174CF692694,
    0xE49B69C19EF14AD2, 0xEFBE4786384F25E3, 0x0FC19DC68B8CD5B5, 0x240CA1CC77AC9C65,
    0x2DE92C6F592B0275, 0x4A7484AA6EA6E483, 0x5CB0A9DCBD41FBD4, 0x76F988DA831153B5,
    0x983E5152EE66DFAB, 0xA831C66D2DB43210, 0xB00327C898FB213F, 0xBF597FC7BEEF0EE4,
    0xC6E00BF33DA88FC2, 0xD5A79147930AA725, 0x06CA6351E003826F, 0x142929670A0E6E70,
    0x27B70A8546D22FFC, 0x2E1B21385C26C926, 0x4D2C6DFC5AC42AED, 0x53380D139D95B3DF,
    0x650A73548BAF63DE, 0x766A0ABB3C77B2A8, 0x81C2C92E47EDAEE6, 0x92722C851482353B,
    0xA2BFE8A14CF10364, 0xA81A664BBC423001, 0xC24B8B70D0F89791, 0xC76C51A30654BE30,
    0xD192E819D6EF5218, 0xD69906245565A910, 0xF40E35855771202A, 0x106AA07032BBD1B8,
    0x19A4C116B8D2D0C8, 0x1E376C085141AB53, 0x2748774CDF8EEB99, 0x34B0BCB5E19B48A8,
    0x391C0CB3C5C95A63, 0x4ED8AA4AE3418ACB, 0x5B9CCA4F7763E373, 0x682E6FF3D6B2B8A3,
    0x748F82EE5DEFB2FC, 0x78A5636F43172F60, 0x84C87814A1F0AB72, 0x8CC702081A6439EC,
    0x90BEFFFA23631E28, 0xA4506CEBDE82BDE9, 0xBEF9A3F7B2C67915, 0xC67178F2E372532B,
    0xCA273ECEEA26619C, 0xD186B8C721C0C207, 0xEADA7DD6CDE0EB1E, 0xF57D4F7FEE6ED178,
    0x06F067AA72176FBA, 0x0A637DC5A2C898A6, 0x113F9804BEF90DAE, 0x1B710B35131C471B,
    0x28DB77F523047D84, 0x32CAAB7B40C72493, 0x3C9EBE0A15C9BEBC, 0x431D67C49C100D4C,
    0x4CC5D4BECB3E42B6, 0x597F299CFC657E2A, 0x5FCB6FAB3AD6FAEC, 0x6C44198C4A475817,
]

# Initial Hash Values
HASH_VALUE = [
    0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1,
    0x510E527FADE682D1, 0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179,
]


# SHA-512 Functions
# Ch(e, f, g) function used in SHA-512 compression
def Ch(e, f, g):
    return (e & f) ^ (~e & g)

# Maj(a, b, c) function used in SHA-512 compression
def Maj(a, b, c):
    return (a & b) ^ (a & c) ^ (b & c)

# Right rotate function
def rotr(x, n):
    return (x >> n) | (x << (64 - n))

# Constants and functions used in SHA-512 compression
def summation_a(a):
    return rotr(a, 28) ^ rotr(a, 34) ^ rotr(a, 39)

def summation_e(e):
    return rotr(e, 14) ^ rotr(e, 18) ^ rotr(e, 41)

def sigma_0(word):
    return rotr(word, 1) ^ rotr(word, 8) ^ (word >> 7)

def sigma_1(word):
    return rotr(word, 19) ^ rotr(word, 61) ^ (word >> 6)

# Modular addition of two 64-bit values
def addition_modulo_2_64(value):
    return value % (2**64)

# Pad the message to the required format for SHA-512
def pad_message(message):
    # Append '1' bit followed by zeros to the message
    message += b"\x80"

    # Ensure the message length is a multiple of 1024 bits (128 bytes)
    while len(message) % 128 != 112:
        message += b"\x00"

    # Calculate and append the message length (in bits)
    message += (8 * len(message)).to_bytes(16, "big")
    print(len(message))
    return message

# Divide the message into 1024-bit blocks
def divide_to_blocks(message):
    blocks = []
    for i in range(0, len(message), 128):
        blocks.append(message[i : i + 128])

    return blocks

# Initialize the message schedule W
W = [0] * 80

# SHA-512 Compression Function
def compression_function(message):
    global HASH_VALUE

    a, b, c, d, e, f, g, h = HASH_VALUE

    # Prepare the message schedule W
    for t in range(16):
        W[t] = int.from_bytes(message[t * 8 : (t + 1) * 8], byteorder="big")

    # Calculate the rest of the message schedule using sigma functions
    for t in range(16, 80):
        W[t] = sigma_1(W[t - 2] + W[t - 7]) + sigma_0(W[t - 15] + W[t - 16])

    # Compression Loop
    for t in range(80):
        T1 = h + (Ch(e, f, g) + summation_e(e) + K[t] + W[t])
        T2 = summation_a(a) + Maj(a, b, c)

        h = g
        g = f
        f = e
        e = addition_modulo_2_64(d + T1)
        d = c
        c = b
        b = a
        a = addition_modulo_2_64(T1 + T2)

    # Update the intermediate hash values
    HASH_VALUE[0] = addition_modulo_2_64(HASH_VALUE[0] + a)
    HASH_VALUE[1] = addition_modulo_2_64(HASH_VALUE[1] + b)
    HASH_VALUE[2] = addition_modulo_2_64(HASH_VALUE[2] + c)
    HASH_VALUE[3] = addition_modulo_2_64(HASH_VALUE[3] + d)
    HASH_VALUE[4] = addition_modulo_2_64(HASH_VALUE[4] + e)
    HASH_VALUE[5] = addition_modulo_2_64(HASH_VALUE[5] + f)
    HASH_VALUE[6] = addition_modulo_2_64(HASH_VALUE[6] + g)
    HASH_VALUE[7] = addition_modulo_2_64(HASH_VALUE[7] + h)

# Main code

# Input the message to be hashed
message = input("Enter a message: ").encode("utf-8")

# Pad the message and divide it into blocks
padded_message = pad_message(message)
blocks = divide_to_blocks(padded_message)

# Print the message length in bits
message_length = 8 * len(message)
print(f"Message Length: {message_length} bits")

# Perform SHA-512 hashing on each block
for block in blocks:
    compression_function(block)

# Convert and print the final SHA-512 hash
final_hash = "".join(format(h, "016x") for h in HASH_VALUE)
print(f"SHA-512 Hash: {final_hash}")