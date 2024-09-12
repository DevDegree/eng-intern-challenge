//Space and time complexity. Let n be the length of the input text
//Space complexity: O(n) - storage of input string length n. output of string length n
//Time complexity: O(n) - single for loops that span over the length of the input text

'use strict'

class TwoWayMap {
    #map1
    #map2

    // Requires 2 completely unique arrays of same length (no common elements in either)
    // Thus works for 2 distinct alphabets of same length
    constructor(arr1, arr2) {
        this.#map1 = new Map()
        this.#map2 = new Map()
        for(let i = 0; i < arr1.length; i++) {
            this.#map1.set(arr1[i], arr2[i])
            this.#map2.set(arr2[i],arr1[i])
        }
    }

    getValueFor(key){
        let value = this.#map1.get(key)
        if (value === undefined){
            value = this.#map2.get(key)
        }

        return (value === undefined) ? null : value
    }
}

class EnglishBrailleTranslator {
    #letterMap
    #numberMap   

    constructor() {
        this.#letterMap = new TwoWayMap(EnglishBrailleTranslator.letterArray(),EnglishBrailleTranslator.letterArrayBraille())
        this.#numberMap = new TwoWayMap(EnglishBrailleTranslator.numberArray(),EnglishBrailleTranslator.numberArrayBraille())
    }

    translate(text) {
        //Determine if string is braille or not 
        //O(n)
        let isBraille = true
        let i = 0
        let brailleSymbolArr = [] //store 6 char sequences 
        let brailleSymbol = ""
    
        while(isBraille && i < text.length) {
            if(text[i] !== '.' && text[i] !== 'O') {
                isBraille = false
            }
    
            brailleSymbol += text[i]
            i++
    
            if(i % 6 === 0) {
                brailleSymbolArr.push(brailleSymbol)
                brailleSymbol = ""
            } 
        }
    
        if(isBraille) {
            this.brailleToEnglish(brailleSymbolArr)
        } else {
            this.englishToBraile(text)
        }
    }

    brailleToEnglish(brailleSymbolArr) {
        let englishText = ''
        let numberMode = false
        let capitalMode = false
        let toAppend = ''
        

        for(let i = 0; i < brailleSymbolArr.length; i++) {
            let key = brailleSymbolArr[i]

            if(key === EnglishBrailleTranslator.capitalFollows()){
                capitalMode = true
            } else if(key === EnglishBrailleTranslator.numberFollows()) {
                numberMode = true
            } else if (key === EnglishBrailleTranslator.space()) {
                numberMode = false
                englishText += ' '
            } else if(numberMode && (toAppend = this.#numberMap.getValueFor(key)) !== null) {
                englishText += toAppend
            } else if((toAppend = this.#letterMap.getValueFor(key)) !== null && !numberMode) { //must encounter a space to disable number mode
                capitalMode ? englishText += toAppend.toUpperCase() : englishText += toAppend
            }
        }

        console.log(englishText)
    }

    englishToBraile(text) {
        let brailleText = ''
        let numberMode = false

        for(let i = 0; i < text.length; i++) {
            let key = text[i]
            let lowerCaseKey = key.toLowerCase()
            let toAppend = ''

            if((toAppend = this.#numberMap.getValueFor(lowerCaseKey)) !== null) {
                if(!numberMode){
                    brailleText += EnglishBrailleTranslator.numberFollows()
                    numberMode = true
                } 

                brailleText += toAppend

            } else if((toAppend = this.#letterMap.getValueFor(lowerCaseKey)) !== null){
                if(toAppend === EnglishBrailleTranslator.space()) {
                    numberMode = false
                }
                if (!numberMode) { //must be out of number mode to write from the alphabet
                    if(key === key.toUpperCase() && key != ' '){
                        brailleText += EnglishBrailleTranslator.capitalFollows()
                    }

                    brailleText += toAppend
                }
            } 
        }

        console.log(brailleText)
    }

    // Array containing English possibilities
    static letterArray() { return [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z',
            ' '
        ]
    }
    
    // Array containing Braille representations as strings. Order matched letter array
    static letterArrayBraille() { return [
            'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..', 
            'O...O.', 'O.O.O.', 'OO..O.', 'OO.OO.', 'O..OO.', 'OOO.O.', 'OOOOO.', 'O.OOO.', '.OO.O.', '.OOOO.', 
            'O...OO', 'O.O.OO', '.OOO.O', 'OO..OO', 'OO.OOO', 'O..OOO',
            '......' 
        ]
    }

    // Array containing all sigle digit numbers. 
    static numberArray() { return [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
        ]
    }

    // Array containing braille representation of sinlge digit numbers. Order matched number array
    static numberArrayBraille() { return [
            'O.....', 'O.O...', 'OO....', 'OO.O..', 'O..O..', 'OOO...', 'OOOO..', 'O.OO..', '.OO...', '.OOO..'
        ]
    }

    static numberFollows() {
        return '.O.OOO'
    }

    static capitalFollows() {
        return '.....O'
    }

    static space() {
        return '......'
    }
}

let translator = new EnglishBrailleTranslator()
let input = process.argv.slice(2).join(" ")
translator.translate(input)

