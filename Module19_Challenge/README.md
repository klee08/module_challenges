# MODULE 19. Cryptocurrency Wallet
Send the transaction to the Ganache blockchain as Fintech Finder Customer by doing followings:
Cryptocurrency Wallet
* STEP1: Generate a new Ethereum account instance by using your mnemonic seed phrase (which you created earlier in the module).
* STEP2: Fetch and display the account balance associated with your Ethereum account address.
* STEP3: Calculate the total value of an Ethereum transaction, including the gas estimate, that pays a Fintech Finder candidate for their work.
* STEP4: Digitally sign a transaction that pays a Fintech Finder candidate, and send this transaction to the Ganache blockchain.
* STEP5: Review the transaction hash code associated with the validated blockchain transaction.
_____________________________________________________
# README ANSWERS - SCREEN SHOTS
1.To launch the Streamlit application, type `streamlit run fintech_finder.py`.
![RUN_SCREEN](https://github.com/klee08/module_challenges/blob/main/Module19_Challenge/Images/0_run.png)

2. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you and Click the Send Transaction button to sign and send the transaction with your Ethereum account information. If the transaction is successfully
communicated to Ganache, validated, and added to a block, a resulting transaction hash code will be written to the Streamlit application sidebar.
![SEND_TRANACTION](https://github.com/klee08/module_challenges/blob/main/Module19_Challenge/Images/2_send_wage_hash_generated.png)

3. Navigate to the Ganache accounts tab and locate your account (index 0).and Take a screenshot of the address, balance, and transaction (TX) count.
- BEFORE TRANSACTION:
- ![MY ACCOUNT_BEFORE](https://github.com/klee08/module_challenges/blob/main/Module19_Challenge/Images/1_before_transfer.png)
- AFTER TRANSACTION:
- ![MY ACCOUNT_BEFORE](https://github.com/klee08/module_challenges/blob/main/Module19_Challenge/Images/3_4ETH_deducted.png)

4.  Navigate to the Ganache transactions tab and locate the transaction. Click the transaction and take a screenshot of it.
- ![TRANSCTION_RECORD](https://github.com/klee08/module_challenges/blob/main/Module19_Challenge/Images/4_TRANSACTION_RECORD.png)

_____________________________________________________
# Technologies
- Web3.py: A Python library for connecting to and performing operations on Ethereum-based blockchains.
- ethereum-tester: A Python library that provides access to the tools we’ll use to test Ethereum-based applications.
- mnemonic: A Python implementation for generating a 12- or 24-word mnemonic seed phrase based on the BIP-39 standard.
- bip44: A Python implementation for deriving hierarchical deterministic wallets from a seed phrase based on the BIP-44 standard.
- Ganache: A program that allows you to quickly set up a local blockchain, which you can use to test and develop smart contracts.
  
# Installation Guide
For this project modeule: we need the following dependencies:
- pip install web3==5.17
- pip install eth-tester==0.5.0b3
- pip install mnemonic
- pip install bip44
- Install Ganache: Follow the instructions on the Ganache download page to download and install this tool on your local machine.
# Usage
- To run this project: type `streamlit run fintech_finder.py' from terminal

# Required libaray: 
# Import required libraries
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account
from crypto_wallet import get_balance
from crypto_wallet import send_transaction

# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
