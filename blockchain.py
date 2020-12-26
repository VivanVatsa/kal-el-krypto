from hashlib import sha256
from typing import ChainMap


def updatehash(*args):
    # for arg in args:
    #     print(arg)
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode("utf-8"))

    return h.hexdigest()


print(updatehash("hello world", "hello wow"))


class Block:
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(self.previous_hash, self.number, self.data,
                          self.nonce)

    def __str__(self):
        return str(
            "Block #: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %
            (self.number, self.hash(), self.previous_hash, self.data,
             self.nonce))


class Blockchain:
    difficulty = 4

    def __init__(self, chain=[]):
        self.chain = chain

    # this is for adding a new block in blockchain
    # just appending a list to a dictionary

    def add(self, block):
        self.chain.append({
            "hash": block.hash(),
            "previous": block.previous_hash,
            "number": block.number,
            "data": block.data,
            "nonce": block.nonce,
        })

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].get('hash')
        except IndexError:
            pass

        while True:
            if block.hash([:4]) == "0" * difficulty:
                self.add(block)
                break

            else:
                block.nonce +=1


def main():
    blockchain = Blockchain()
    database = ["hello world", "what's up", "hello", "bye"]

    num = 0
    for data in database:
        num += 1
        blockchain.mine(BLock)
    # block = Block("hello world", 1)
    # print(block)


if __name__ == "__main__":
    main()
