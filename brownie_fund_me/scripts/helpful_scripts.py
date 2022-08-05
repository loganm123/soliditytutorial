from brownie import network, config, accounts

def get_account():
    #if we're on dev network use first default account
    if network.show_active() == "development":
        return accounts[0]
        #otherwise use our rinkeby account
    else:
        return accounts.add(config["wallets"]["from_key"])