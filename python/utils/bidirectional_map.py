import json

class BidirectionalMap:
    """
    map that stores mappings between keys and values and allows 
    access from either side.
    """

    def __init__(self, data):
        self.forward_map = data
        self.reverse_map = {v: k for k, v in data.items()}

    def add(self, key, value):
        if key in self.forward_map:
            raise ValueError(f"Key {key} already exists.")
        if value in self.reverse_map:
            raise ValueError(f"Value {value} already exists.")
        
        self.forward_map[key] = value
        self.reverse_map[value] = key

    def get_value(self, key):
        if key not in self.forward_map:
            raise KeyError(f"Key {key} not found.")
        return self.forward_map.get(key)

    def get_key(self, value):
        if value not in self.reverse_map:
            raise KeyError(f"Value {value} not found.")
        return self.reverse_map.get(value)
