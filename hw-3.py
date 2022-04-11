import datetime
import hashlib


class Block():

    def __init__(self, height, timestamp, tx, nonce, prev_blockhash=""):
        m = hashlib.sha256()
        self.height = height
        self.timestamp = timestamp
        self.tx = tx
        self.nonce = nonce
        self.prev_blockhash = prev_blockhash
        self.curr_blockhash = m
        self.hash_block()

    def __repr__(self) -> str:
        return f'[height: {self.height}, timestamp: {self.timestamp}, tx: {self.tx}, nonce: {self.nonce}, prev_block: {self.prev_blockhash}] with hash "{self.curr_blockhash.hexdigest()}"'

    def hash_block(self) -> str:
        self.curr_blockhash.update(
            f"{self.height}{self.timestamp}{self.tx}{self.nonce}{self.prev_blockhash}".encode())
        return self.curr_blockhash.hexdigest()


class Blockchain:

    def __init__(self):
        self.block_list = []
        self.genesis_block = None

    def create_genesis_block(self, tx, nonce, timestamp=datetime.datetime.utcnow()) -> Block:
        """
        Produce el bloque cero.

        El bloque cero tiene solo una particularidad: no tiene un
        hash de bloque previo. Fuera de eso, es exactamente igual
        a cualquier otro bloque.
        """

        genesis_block = Block(0, timestamp, tx, nonce)

        print("Creating genesis block")
        return genesis_block

    def add_block(self, block: Block):
        """
        Agrega el bloque a la cadena de bloques.
        """
        print(
            f'Added block #{block.height} with hash "{block.curr_blockhash.hexdigest()}"')
        self.block_list.append(block)

    def create_block(self, timestamp, tx, nonce, prev_blockhash) -> Block:
        new_block = Block(len(self.block_list), timestamp,
                          tx, nonce, prev_blockhash)
        print(
            f'Preparing new block {new_block}')
        return new_block

    def start_blockchain(self):
        genesis_block = self.create_genesis_block(
            "This is the genesis block", 0)
        self.add_block(genesis_block)


blockchain = Blockchain()
blockchain.start_blockchain()
for i in range(10):
    new_block = blockchain.create_block(datetime.datetime.utcnow(
    ), f"This is block number {i}", 0, blockchain.block_list[-1].curr_blockhash.hexdigest())
    blockchain.add_block(new_block)
