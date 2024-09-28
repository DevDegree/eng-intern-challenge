class HashTable {
  constructor() {
    this.table = {};
  }

  set(key, value) {
    this.table[key] = value;
  }

  get(key) {
    return this.table[key];
  }
}

module.exports = HashTable;
