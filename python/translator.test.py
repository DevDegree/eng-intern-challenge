import unittest
import subprocess

class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        #command = ["python3", "translator.py", "Abc", "123", "xYz"]   cannot find
        ##command = ["python3", "C:/PersonalGIT/eng-intern-challenge/python/translator.py", "Abc", "123", "xYz"]
        command = ["python3", "C:/PersonalGIT/Fork'd-eng-intern-challenge/eng-intern-challenge/python/translator.py", "Abc", "123", "xYz"]
       # C:\PersonalGIT\Fork'd-eng-intern-challenge\eng-intern-challenge\python

        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Expected output without the newline at the end
      #  expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO\n"

        
        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)

if __name__ == '__main__':
    unittest.main()

# cd "C:/PersonalGIT/Fork'd-eng-intern-challenge/eng-intern-challenge/python"
# run with  python "C:/PersonalGIT/Fork'd-eng-intern-challenge/eng-intern-challenge/python/translator.py" "Abc 123 xYz"
#if no output then open a new terminal window (to avoidd term session issues) and make sure python version still appears:   python --version
# here are the output tests running as expected:
# PS C:\PersonalGIT\eng-intern-challenge> python --version
# Python 3.10.1
# PS C:\PersonalGIT\eng-intern-challenge> cd "C:/PersonalGIT/Fork'd-eng-intern-challenge/eng-intern-challenge/python"
# PS C:\PersonalGIT\Fork'd-eng-intern-challenge\eng-intern-challenge\python> python "C:/PersonalGIT/Fork'd-eng-intern-challenge/eng-intern-challenge/python/translator.py" "Abc 123 xYz"
# O.....O.O...OO...........O.OOO..O...O.OOOO......OO..OOOO.OOOO..OOO
# PS C:\PersonalGIT\Fork'd-eng-intern-challenge\eng-intern-challenge\python> 

# needed help from chat GPT on this one!