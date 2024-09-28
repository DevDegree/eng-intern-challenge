import subprocess
from custom_test_cases import TESTS

def runTests():
  english = ""
  braille = ""
  for test in TESTS:
    english = test["english"]
    braille = test["braille"]
    # eng to braille first
    # Command to run translator.py script
    command = ["python3", "translator.py"] + english.split(' ')
    # Run the command and capture output
    result = subprocess.run(command, capture_output=True, text=True)
    
    
    # Strip any leading/trailing whitespace from the output and compare
    output = result.stdout.strip()
    if output != braille:
      print("TEST FAILED english to braille")
      print(english)
      print(braille)
      print(output)
      print(result.stderr)
    else:
      print("yay")

    # braille to eng
    # Command to run translator.py script
    command = ["python3", "translator.py", braille]
    # Run the command and capture output
    result = subprocess.run(command, capture_output=True, text=True)

    
    # Strip any leading/trailing whitespace from the output and compare
    output = result.stdout.strip()
    if output != english:
      print("TEST FAILED braille to english")
      print(braille)
      print(english)
      print(output)
      print(result.stderr)
    else:
      print("yay")
if __name__ == '__main__':
  runTests()