<?php
class Braille
{
    const CONTROL_CAPITAL = 'capital';
    const CONTROL_SPACE = 'space';
    const CONTROL_NUMBER = 'number';

    const e_maps = [
        'a' => 'O.....',
        'b' => 'O.O...',
        'c' => 'OO....',
        'd' => 'OO.O..',
        'e' => 'O..O..',
        'f' => 'OOO...',
        'g' => 'OOOO..',
        'h' => 'O.OO..',
        'i' => '.OO...',
        'j' => '.OOO..',

        '1' => 'O.....',
        '2' => 'O.O...',
        '3' => 'OO....',
        '4' => 'OO.O..',
        '5' => 'O..O..',
        '6' => 'OOO...',
        '7' => 'OOOO..',
        '8' => 'O.OO..',
        '9' => '.OO...',
        '0' => '.OOO..',

        'k' => 'O...O.',
        'l' => 'O.O.O.',
        'm' => 'OO..O.',
        'n' => 'OO.OO.',
        'o' => 'O..OO.',
        'p' => 'OOO.O.',
        'q' => 'OOOOO.',
        'r' => 'O.OOO.',
        's' => '.OO.O.',
        't' => '.OOOO.',
        'u' => 'O....O',
        'v' => 'O.O..O',
        'w' => '.OOO.O',
        'x' => 'OO..OO',
        'y' => 'OO.OOO',
        'z' => 'O..OOO',

        self::CONTROL_CAPITAL => '.....O',
        self::CONTROL_NUMBER => '.O.OOO',
        self::CONTROL_SPACE => '......',
    ];

    const numberMaps=[
        'O.....' => '1',
        'O.O...' => '2',
        'OO....' => '3',
        'OO.O..' => '4',
        'O..O..' => '5',
        'OOO...' => '6',
        'OOOO..' => '7',
        'O.OO..' => '8',
        '.OO...' => '9',
        '.OOO..' => '0',
    ];
    
    const letterMaps = [
        'O.....' => 'a',
        'O.O...' => 'b',
        'OO....' => 'c',
        'OO.O..' => 'd',
        'O..O..' => 'e',
        'OOO...' => 'f',
        'OOOO..' => 'g',
        'O.OO..' => 'h',
        '.OO...' => 'i',
        '.OOO..' => 'j',
        'O...O.' => 'k',
        'O.O.O.' => 'l',
        'OO..O.' => 'm',
        'OO.OO.' => 'n',
        'O..OO.' => 'o',
        'OOO.O.' => 'p',
        'OOOOO.' => 'q',
        'O.OOO.' => 'r',
        '.OO.O.' => 's',
        '.OOOO.' => 't',
        'O....O' => 'u',
        'O.O..O' => 'v',
        '.OOO.O' => 'w',
        'OO..OO' => 'x',
        'OO.OOO' => 'y',
        'O..OOO' => 'z',

        '.....O' => self::CONTROL_CAPITAL,
        '.O.OOO' => self::CONTROL_NUMBER,
        '......' => self::CONTROL_SPACE,
    ];

    private static function isBraille(string $source): bool
    {
        return preg_match('/^[O.]+$/', $source) && strlen($source) % 6 == 0;
    }

    public static function numberToBraille(string $source ='123'): string{
        $target = '';
        $isFirstNumber = false;

        foreach (str_split($source) as $char) {
            //1
            if (is_numeric($char)) {
                if (!$isFirstNumber) {
                    $target .= self::e_maps[self::CONTROL_NUMBER];   
                }
                $target .= self::e_maps[$char];
                $isFirstNumber = true;
            } elseif ($char == ' ') {
                $isFirstNumber = false;
                $target .= self::e_maps[self::CONTROL_SPACE];
            }
        }
        return $target;   // numner_control_123
        //numner_control1numner_control2 _3 _2 _3/

    }

    private static function toBraille(string $source): string
    {
        $target = '';
        $isFirstNumber = false;
        foreach (str_split($source) as $char) {
            if (ctype_upper($char)) {
                $target .= self::e_maps[self::CONTROL_CAPITAL];
                $target .= self::e_maps[strtolower($char)];
            } else if (is_numeric($char)) {
                if (!$isFirstNumber) {
                    $target .= self::e_maps[self::CONTROL_NUMBER];
                }
                $target .= self::e_maps[$char];
                $isFirstNumber = true;
            } elseif ($char == ' ') {
                $isFirstNumber = false;
                $target .= self::e_maps[self::CONTROL_SPACE];
            } else {
                $target .= self::e_maps[$char];
            }
        }
        return $target;
    }

    private static function toEnglish(string $source): string
    {
        $target = '';


        return $target;
    }

    public static function translator(string $source): string
    {
        return self::isBraille($source) ? self::toEnglish($source) : self::toBraille($source);
    }
}
