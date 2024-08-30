import sys

def isEnglish(message: str) -> bool:
    for char in message:
        if (char != 'O' or char != '.'):
            return False
    
    return True
    
if __name__ == "__main__":
    message = sys.argv[1]
    print(message)
    
