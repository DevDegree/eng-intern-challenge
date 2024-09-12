import sys

def main():
    if len(sys.argv) <1:
        print("Please input at least 1 word")
        sys.exit(1)
    
    concatenated_words = ''
    
    for i in range(1,len(sys.argv)):
        print(i)
        print('we concat')
        print(sys.argv[i])
        # Concatenate the words
        concatenated_words += str(sys.argv[i])

    # Print the result
    print(concatenated_words)

if __name__ == "__main__":
    main()