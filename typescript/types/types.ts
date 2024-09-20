import {brailleDictionary, modifyiers, numbersDictionary} from '../utils/constants';

export type NumberChar = keyof typeof numbersDictionary

export type EnglsihChar = keyof typeof brailleDictionary | NumberChar

export type ModifyiersChar = typeof modifyiers [keyof typeof modifyiers]

export type BrailleChar =
| typeof brailleDictionary [keyof typeof brailleDictionary]
| ModifyiersChar
