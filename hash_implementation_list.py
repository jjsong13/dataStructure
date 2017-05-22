class myDatabase:

    def __init__(self, size) :
        # 1. Create a hashtable
        # (size = # of key, value tuples)
        # (initially all key, value are -1)
        self.myData = [(-1, -1) for i in range(size)]

    def put(self, key, value) :
        # 2. Pass key via hashFunction to get index
        index = self.hashFunction(key)

        # 4. Look at hashTable at index.
        # if key at index is -1, the space in hashtable is empty so add value to the location
        # but not -1, space is already filled so continue looking for empty spaces up to length of hashtable -1
        for i in range(len(self.myData)):
            if self.myData[index][0] == -1 :
                self.myData[index] = (key,value)
                return
            else :
                index = (index+1)%(len(self.myData))

    def get(self, key) :
        # 5. Pass key via hashFunction to get index
        index = self.hashFunction(key)
        # 6. If key at index equals the key given, return the value at index
        # Else continue looking for the key in hashtable that equals key given and return the value
        # If empty space is found before finding an equal key in hashtable, value is not present in hashtable
        for i in range(len(self.myData)):
            if self.myData[index][0] == key:
                return self.myData[index][1]
            if self.myData[index][0] == -1:
                return -1

            index = (index+1)%(len(self.myData))

        return -1

    def hashFunction(self, key) :
        # 3. Create a hashFunction, i.e. returns the remainder of key when
        # divided by the length of hashtable
        return key%(len(self.myData))

def main():
    db = myDatabase(100)

    db.put(1, 3)
    db.put(2, 7)
    db.put(3, 8)
    db.put(403, 9)

    print(db.get(3))
    print(db.get(403))


if __name__ == "__main__":
    main()
