/**
 * K two-way mapping data structure.
 * (Incomplete as it is unnecessary for the problem)
 */
export class BidirectionalMap<K, V> {
  private forwardMap: Map<K, V> = new Map();
  private reverseMap: Map<V, K> = new Map();

  /**
   * @param iterable Iterable list of key-value pairs.
   */
  constructor(iterable?: Iterable<readonly [K, V]> | null) {
    if (iterable === undefined || iterable === null) {
      return;
    }
    for (let [ a, b ] of iterable) {
      if (this.forwardMap.has(a) || this.reverseMap.has(b)) {
        throw new Error('Repeated key / value.');
      }
      this.forwardMap.set(a, b);
      this.reverseMap.set(b, a);
    }
  }

  /**
   * @returns Returns a value element from the BidirectionalMap object given its paired key.
   */
  public getValue(key: K): V | undefined {
    return this.forwardMap.get(key);
  }

  /**
   * @returns Returns a key element from the BidirectionalMap object given its paired value.
   */
  public getKey(value: V): K | undefined {
    return this.reverseMap.get(value);
  }

  /**
   * @returns Returns true if value is in BidirectionalMap object.
   */
  public hasValue(value: V): boolean {
    return this.reverseMap.has(value);
  }

  /**
   * @returns Returns true if key is in BidirectionalMap object.
   */
  public hasKey(key: K): boolean {
    return this.forwardMap.has(key);
  }
}