import unittest
import subprocess

def test_output():
    command = ["python3", "translator.py", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."]
    
    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("input: " + " ".join(command[1:]))
        # Expected output without the newline at the end
        expected_output = "Abc 123"
        
        # Strip any leading/trailing whitespace from the output and compare
        print("result:")
        print(result.stdout.strip())
        print("expected:")
        print(expected_output)

        # Compare result and expected output
        if result.stdout.strip() == expected_output:
            print("Test passed!")
        else:
            print("Test failed. Output doesn't match expected.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running translator.py: {e}")
        print(f"stderr: {e.stderr}")
    except FileNotFoundError:
        print("translator.py not found. Please ensure the file exists and is in the correct location.")


if __name__ == '__main__':
    test_output()

