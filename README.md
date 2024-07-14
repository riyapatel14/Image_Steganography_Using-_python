# Image Steganography: Hiding Text in an Image

This repository contains a Python script for hiding a secret message within an image using steganography. The script allows you to encode a message into an image and decode it later, using a password for added security.

## Features

- Encode a secret message into an image
- Decode the hidden message from the image
- Password-protected decryption
- Verification of successful encoding

## How It Works

The script uses the following steps:

1. **Encoding the Message:**
   - The length of the message is first encoded into the image.
   - Each character of the message is then encoded into the image pixels by converting characters to their ASCII values.

2. **Decoding the Message:**
   - The length of the message is decoded first to determine how many characters to extract.
   - The encoded characters are extracted from the image pixels and converted back to their original form.



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
