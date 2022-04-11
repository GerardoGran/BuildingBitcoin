import hashlib


class Block():

    def __init__(self, height, timestamp, tx, nonce, prev_blockhash):
        m = hashlib.sha256()
        self.height = height
        self.timestamp = timestamp
        self.tx = tx
        self.nonce = nonce
        self.prev_blockhash = prev_blockhash
        self.curr_blockhash = m

    def hash_block(self) -> str:
        self.curr_blockhash.update(
            f"{self.height}{self.timestamp}{self.tx}{self.nonce}{self.prev_blockhash}".encode())
        return self.curr_blockhash.hexdigest()


height = 0
timestamp = '2021-02-25 11:59:59.134365'
tx = 'Alice, Bob, 10'
nonce = 0
# Hash de bytes(0) utilizando SHA-256
prev_blockhash = '3af366504b556c3802248387ee16eb51ffee5ba52906bae95f0eff7ea454218e'
hash = "c340ad4ab9ab5fb5043586cc9523330d690ba9e0b08c3a909a4438ce3232515f"

test_block = Block(height, timestamp, tx, nonce, prev_blockhash)

assert test_block.hash_block() == hash
