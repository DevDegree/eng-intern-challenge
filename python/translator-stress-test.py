import random
import unittest
import subprocess

def generate_string(length):
    """
    Generate a random string of the given length
    """
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", k=length))
    
def generate_number(length):
    """
    Generate a random number of the given length
    """
    return str(random.randint(0, 10 ** length))

class TestTranslator(unittest.TestCase):
    def test_output(self):
        for i in range(100):
            string = generate_string(random.randint(1, 10))
            number = generate_number(random.randint(1, 10))
            
            command = ["python3", "translator.py", string, number]
            
            # Run the command and capture output
            e2b = subprocess.run(command, capture_output=True, text=True)
            
            e2b = e2b.stdout.strip()
            
            # Expected output without the newline at the end
            b2e = subprocess.run(["python3", "translator.py", e2b], capture_output=True, text=True).stdout.strip()
            
            original_string = string + " " + number
            # Strip any leading/trailing whitespace from the output and compare
            self.assertEqual(b2e, original_string)

if __name__ == '__main__':
    unittest.main()
