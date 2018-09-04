from blockchain import Blockchain

#Initiates blockchain

def generate_blocks(number_of_blocks):
    # """
    # input: number_of_blocks: int
    # output: hash of final block: str
    #
    # Given a number of blocks return the output after x amount of block as a string. Input blocks are EMPTY
    # """

    # instantiate the blockchain class to create the gensis block
    bc_data = Blockchain()

    # Since the test case would be testing on the number of blocks in the chain
    # a loop is needed such that it would iterate until it match the number of
    # counts of block required, which is 5 and 10

    # Terminating condition is set to 1. Reverse iteration
    while number_of_blocks != 1:
        # Calling the mine method would automatically generate new block with the parent block's hash been supply in.
        # To get the parent block is to call the "get_current_block" method which return the latest block in the chain
        bc_data.mine(bc_data.get_current_block())

        # After hashing of the new block with the previous block hash, decrease count
        number_of_blocks -= 1

    # Return the hash of the latest block by calling the same method again "get_current_block", follow by access the
    # block attributes, "hash" in this case
    return bc_data.get_current_block().hash

