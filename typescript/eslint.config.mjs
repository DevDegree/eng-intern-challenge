import globals from 'globals';
import pluginJs from '@eslint/js';
import shopifyEslintPlugin from '@shopify/eslint-plugin';
import tseslint from 'typescript-eslint';


export default [
  {files: ['**/*.{js,mjs,cjs,ts}']},
  {languageOptions: {globals: globals.browser}},
  pluginJs.configs.recommended,
  ...shopifyEslintPlugin.configs.es5,
  ...tseslint.configs.recommended,
  {
    rules: {
      'id-length': 'off',
    },
  },
];
