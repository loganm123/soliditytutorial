from brownie import FundMe
from scripts.helpful_scripts import get_account
import os

# 5:15:13


def deploy_fund_me():
    account = get_account()
    # state change to blockchain means we need an account
    fund_me = FundMe.deploy({"from": account})
    # prints address of deployed fund_me to rinkeby
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
