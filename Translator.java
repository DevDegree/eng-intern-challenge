import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Translator {

    private static final Map<String, String> brailleToEnglish = new HashMap<>();

    private static final Map<String, String> englishToBraille = new HashMap<>();

    static {
        brailleToEnglish.put("O.....", "a");
        brailleToEnglish.put("O.O...", "b");
        brailleToEnglish.put("OO....", "c");
        brailleToEnglish.put("OO.O..", "d");
        brailleToEnglish.put("O..O..", "e");
        brailleToEnglish.put("OOO...", "f");
        brailleToEnglish.put("OOOO..", "g");
        brailleToEnglish.put("O.OO..", "h");
        brailleToEnglish.put(".OO...", "i");
        brailleToEnglish.put(".OOO..", "j");
        brailleToEnglish.put("O...O.", "k");
        brailleToEnglish.put("O.O.O.", "l");
        brailleToEnglish.put("OO..O.", "m");
        brailleToEnglish.put("OO.OO.", "n");
        brailleToEnglish.put("O..OO.", "o");
        brailleToEnglish.put("OOO.O.", "p");
        brailleToEnglish.put("OOOOO.", "q");
        brailleToEnglish.put("O.OOO.", "r");
        brailleToEnglish.put(".OO.O.", "s");
        brailleToEnglish.put(".OOOO.", "t");
        brailleToEnglish.put("O...OO", "u");
        brailleToEnglish.put("O.O.OO", "v");
        brailleToEnglish.put(".OOO.O", "w");
        brailleToEnglish.put("OO..OO", "x");
        brailleToEnglish.put("OO.OOO", "y");
        brailleToEnglish.put("O..OOO", "z");
        brailleToEnglish.put(".....O", "capital");
        brailleToEnglish.put(".O.OOO", "number");
        brailleToEnglish.put("......", " ");
        
        for (Map.Entry<String, String> entry : brailleToEnglish.entrySet()) {
            if (!entry.getValue().equals("capital") && !entry.getValue().equals("number")) {
                englishToBraille.put(entry.getValue(), entry.getKey());
            }
        }
    }


    private static String translateBrailleToEnglish(String braille) {
        StringBuilder result = new StringBuilder();
        boolean isCapital = false;
        boolean isNumber = false;

        for (int i = 0; i < braille.length(); i += 6) {
            String symbol = braille.substring(i, i + 6);
            if (symbol.equals(".....O")) {
                isCapital = true;
            } else if (symbol.equals(".O.OOO")) { 
                isNumber = true;
            } else {
                String translated = brailleToEnglish.getOrDefault(symbol, "");
                if (isCapital) {
                    result.append(translated.toUpperCase());
                    isCapital = false;
                } else if (isNumber) {
                    result.append(translated);
                    isNumber = false;
                } else {
                    result.append(translated);
                }
            }
        }
        return result.toString();
    }

    private static String translateEnglishToBraille(String text) {
        StringBuilder result = new StringBuilder();

        for (char c : text.toCharArray()) {
            if (Character.isUpperCase(c)) {
                result.append(".....O"); // Capital Indicator
                result.append(englishToBraille.get(String.valueOf(c).toLowerCase()));
            } else if (Character.isDigit(c)) {
                result.append(".O.OOO"); // Number Indicator
                result.append(englishToBraille.get(String.valueOf(c)));
            } else {
                result.append(englishToBraille.get(String.valueOf(c)));
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter English or Braille string:");
        String input = scanner.nextLine();
        
        if (input.contains("O") || input.contains(".")) {

            System.out.println(translateBrailleToEnglish(input));
        } else {

            System.out.println(translateEnglishToBraille(input));
        }

        scanner.close();
    }
}
