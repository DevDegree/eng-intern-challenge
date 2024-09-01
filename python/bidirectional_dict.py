class BidirectionalDict:
    def __init__(self):
        self.key_to_value = {}
        self.value_to_key = {}

    def add(self, key, value):
        if key in self.key_to_value or value in self.value_to_key:
            raise ValueError("Duplicate key or value")
        self.key_to_value[key] = value
        self.value_to_key[value] = key
        
    def get(self, key):
        return self.key_to_value.get(key, None)
    
    def get_by_value(self, value):
        return self.value_to_key.get(value, None)
    
    def __repr__(self):
        return("BidirectionalDict(key_to_value=" + str(self.key_to_value) + ", value_to_key=" + str(self.value_to_key)+ ")")