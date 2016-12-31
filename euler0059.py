# XOR decryption
#
# Published on Friday, 19th December 2003, 10:00 am; Solved by 28322; Difficulty rating: 5%
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import csv;
import sys;
import time;

start_time = time.time();

FILENAME_CIPHER = "p059_cipher.txt";
FILENAME_WORDS = "words.txt";
ORD_a = ord('a');
ORD_z = ord('z');
ORD_SPACE = ord(' ');

common_words = [];

def decrypt(cipher_text_list, key):
    plain_text = "";
    common_word_count = 0;
    length = len(cipher_text_list);
    # The average length of an English word is about 5 characters, so the expected number of spaces is about length / (5 + 1 for the space).
    # Make the minimum half of that to allow for anomalous cases.
    space_count_min = (length / 6) / 2;
    key_index = 0;
    space_count = 0;
    for i in range(length):
        byte = int(cipher_text_list[i]) ^ key[key_index];
        key_index = (key_index + 1) % 3;
        if byte == ORD_SPACE:
            space_count += 1;
        plain_text += chr(byte);
    if space_count >= space_count_min:
        words = plain_text.split(' ');
        for word in words:
            if word in common_words:
                common_word_count += 1;
    return (plain_text, common_word_count);

common_word_count_max = 0;
argmax_key = None;
argmax_plain_text = None;

with open(FILENAME_WORDS) as word_file:
    for word in word_file:
        common_words.append(word[:-1]);

with open(FILENAME_CIPHER) as cipher_file:
    reader = csv.reader(cipher_file, delimiter = ',');
    for cipher_text_list in reader:
        for key0 in range(ORD_a, ORD_z + 1):
            for key1 in range(ORD_a, ORD_z + 1):
                for key2 in range(ORD_a, ORD_z + 1):
                    key = [key0, key1, key2];
                    plain_text, common_word_count = decrypt(cipher_text_list, key);
                    if common_word_count > common_word_count_max:
                        common_word_count_max = common_word_count;
                        argmax_key = key;
                        argmax_plain_text = plain_text;
                        print common_word_count_max, argmax_key;
print;
print argmax_plain_text;
print;
ascii_sum = 0;
for char in argmax_plain_text:
    ascii_sum += ord(char);
print "ascii_sum = %d." % ascii_sum;

print "Execution time = %f seconds." % (time.time() - start_time);
