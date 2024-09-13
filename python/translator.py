# Description: This script will take a message and convert it to/from braille into plaintext.

# Name:         decode
# Purpose:      Decodes a message from braille to plaintext
# Parameters:   i - a string containing the braille message
# Returns:      a string containing the decoded message
def decode(i: str):
    decoded_msg = str()
    return decoded_msg

# Name:         encode
# Purpose:      Encodes a message from plaintext to braille
# Parameters:   i - a string containing the plaintext message
# Returns:      a string containing the encoded message
def encode(i: str):
    encoded_msg = str()
    return encoded_msg

if __name__ == '__main__':
    import sys

    # parse input from first arg and store to msg
    if len(sys.argv) < 2:
        print('Please provide a message to convert to/from braille into plaintext. Usage: python translator.py <msg>')
        exit(1)
    if len(sys.argv) > 2:
        msg: str = sys.argv[1:].join(' ')
    else:
        msg: str = sys.argv[1]
    # Check if the message contains only 0 or o
    if not all(c in '0o' for c in msg):
        # message is a plaintext message
        print(encode(msg))
    else:
        # message is a braille message
        print(decode(msg))
