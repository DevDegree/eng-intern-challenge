import React, { useState } from 'react'


const brailleMap = {

    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛',
    'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝',
    'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥',
    'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', ' ': ' ', ',': '⠂',
    '.': '⠲', '?': '⠦', '!': '⠖'
  
}

//function to translate to braille
const translateToBraille = (text) =>{
    return text
    .toLowerCase()
    .split('')
    .map(char => brailleMap[char] || char) // falls back to original if not in the map
    .join('')
}


const Mycomponent = () => {
    const [inputText, setInputText] = useState('')
    const [result, setResult] = useState('')

    //Handle input text change
    const  handleChange = (e) =>{
      const text = e.target.value;
      setInputText(text)
      setResult(translateToBraille(text))
    }
  return (
    <div className='flex justify-center items-center w-full h-screen bg-custom-gradient'>
      <div className='border w-[500px] p-4 rounded-md bg-blue-100'>
      <h1 className='text-2xl font-bold text-center'>Braille Translator</h1>
      <div className='text-center text-xl mt-8'>Word Input</div>
      <input
        type='text'
        value={inputText}
        placeholder='Write text to translator'
        onChange={handleChange}
        className='outline-none px-2 py-2 border rounded-md w-full'
      />
        <div className='mt-8 text-xl text-center'>Braille Output</div>
      <p className='text-2xl border'>{result}</p>
      </div>
    </div>
  )
}

export default Mycomponent