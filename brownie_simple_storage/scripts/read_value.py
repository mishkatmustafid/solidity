from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[0]
    # go take the index thats one less than the length
    print(simple_storage.retrieve())


def main():
    read_contract()
