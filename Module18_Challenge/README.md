# MODULE 18. PyChain Ledger
build a blockchain-based ledger system with a user-friendly web interface. 
This ledger should allow partner banks to conduct financial transactions (i.e.) transfer money between senders and receivers) 
and to verify the integrity of the data in the ledger.
* Step 1: # Create a Record Data Class
* Step 2: # Modify the Existing Block Data Class to Store Record Data
* Step 3: # Add Relevant User Inputs to the Streamlit Interface
* Step 4: # Test the PyChain Ledger by Storing Records
_____________________________________________________
# README ANSWERS
1. PyChain - Our Blockchain-based ledger System User-friendly web insterface
- Streamlit run pychain.py
![RUN_SCREEN](https://github.com/klee08/module_challenges/blob/main/Module18_Challenge/Resources/image1.PNG)

2. Enter values for the sender, receiver, and amount, and then click the "Add Block" button. 
e.g. Test Input:  
- Sender: Ken Lee
- Receiver: Kris Hansen
- Amount: 15000

3. Verify the block contents and hashes in the Streamlit drop-down menu.
Take a screenshot of the Streamlit application page, which should detail a blockchain that consists of multiple blocks. 
- The PyChain Ledger Record List - Added the above input (new record) to the list successfully
![LEDGER_LIST](https://github.com/klee08/module_challenges/blob/main/Module18_Challenge/Resources/image2.PNG)

4. Test the blockchain validation process by using the web interface.
Take a screenshot of the Streamlit application page, which should indicate the validity of the blockchain
- Block Inspector - Validated the transaction details thru block inspector
![INSPECTOR](https://github.com/klee08/module_challenges/blob/main/Module18_Challenge/Resources/image3.PNG)
![VALIDATOR](https://github.com/klee08/module_challenges/blob/main/Module18_Challenge/Resources/image4.PNG)

_____________________________________________________
# Technologies
## 1. Blockchain is a technology that records and shares data over a network, such as the internet (decentralized)
-  Shared Accounting with Digital Ledgers: Data class (dataclass) is used to create a block in our blockchain and digital ledger
-  Improved Data Integrity with Hashing (hashlib)
## 2. Streamlit application turns Python scripts into shareable web apps - a user-friendly webpage interface for a blockchain.
  
# Installation Guide
For this project modeule: we need the following dependencies:
  pip install streamlit

# Usage
To run this project load the jupyter notebook forecasting_net_prophet.ipynb and run.
Required libaray: 
# Import required libraries
import streamlit as st
from datetime import datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import hashlib

# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
