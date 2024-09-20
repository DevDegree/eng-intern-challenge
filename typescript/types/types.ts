import {brailleDictionary, modifyiers} from '../utils/constants';

export type EnglsihChar = keyof typeof brailleDictionary

export type ModifyiersChar = typeof modifyiers [keyof typeof modifyiers]

export type BrailleChar =
| typeof brailleDictionary [keyof typeof brailleDictionary]
| ModifyiersChar
