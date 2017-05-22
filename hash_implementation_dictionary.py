class myDatabase:

    def __init__(self, size) :

        # 1. Create a dictionary using curly brackets.
        # Dictionary is a hash that is already implemented in python.
        # It's faster to use a dictionary than a list.

        self.myData = {}

    def put(self, key, value) :

        # 2. Store (key, value) in dictionary

        self.myData[key] = value


    def get(self, key) :
        # 3. Return value stored at location key. If there's no value accordingly, return -1

        if self.myData[key] != -1 :
            return self.myData[key]
        else :
            return -1

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
