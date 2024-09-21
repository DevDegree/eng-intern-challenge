import {brailleDictionary, modifyiers, numbersDictionary} from '../utils/constants';

export type NumberChar = keyof typeof numbersDictionary

export type NonNumberChar = keyof typeof brailleDictionary

export type EnglsihChar = NonNumberChar | NumberChar

export type ModifyiersChar = typeof modifyiers [keyof typeof modifyiers]

export type BrailleChar =
| typeof brailleDictionary [keyof typeof brailleDictionary]
| typeof numbersDictionary [keyof typeof numbersDictionary]
| ModifyiersChar
