import os
import cv2

img = cv2.imread("Tree.jpg")
msg = input("Enter secret message: ")
password = input("Enter Password: ")

# Initialize dictionaries
d = {}
c = {}

for i in range(256):  # Use range(256) to cover all byte values
    d[chr(i)] = i
    c[i] = chr(i)  # Reverse mapping from integer to character

n, m, z = 0, 0, 0

# Encoding the message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

cv2.imwrite("Encryptedimage.jpg", img)
os.startfile("Encryptedimage.jpg")

message = ""
n, m, z = 0, 0, 0

pas = input("Enter password for decryption: ")

# Decoding the message from the image
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Wrong password, Secret nai dikhega tujhe")
