import unittest
import subprocess


class TestTranslator(unittest.TestCase):
    def test_output(self):
        # Command to run translator.py script
        command = ["python3", "translator.py", "Abc", "123", "xYz"]

        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Expected output without the newline at the end
        expected_output = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"

        # DEBUGGING
        # chunked_expected = "\n".join(
        #     [expected_output[i : i + 6] for i in range(0, len(expected_output), 6)]
        # )
        # chunked_result = "\n".join(
        #     [
        #         result.stdout.strip()[i : i + 6]
        #         for i in range(0, len(result.stdout.strip()), 6)
        #     ]
        # )
        # for expected, res in zip(chunked_expected.split(), chunked_result.split()):
        #     print(expected, res)

        # Strip any leading/trailing whitespace from the output and compare
        self.assertEqual(result.stdout.strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
