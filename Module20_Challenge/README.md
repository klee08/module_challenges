# MODULE 20. Solidity JointSavings smart contract.
To automate the creation of joint savings accounts, create a Solidity smart contract that accepts two user addresses
* Step 1: Create a Joint Savings Account Contract in Solidity
* Step 2: Compile and Deploy Your Contract in the JavaScript VM
* Step 3: Interact with Your Deployed Smart Contract
_____________________________________________________
# README ANSWERS - Execution_Results
1.Test the deposit functionality of your smart contract by sending the following amounts of ether. After each transaction, use the contractBalance function to verify that the funds were added to your contract:
![SET_ACCOUNT](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Set_Account.png)
- Transaction 1: Send 1 ether as wei.
![TRANSACTION_1](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Transaction1_Send1_ether_as_wei.png)
- Transaction 2: Send 10 ether as wei.
![TRANSCATION_2](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Transaction2_Send10_ether_as_wei.png)
- Transaction 3: Send 5 ether
![TRANSACTION_3](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Transaction3_Send5ether.png)

2. Once you’ve successfully deposited funds into your contract, test the contract’s withdrawal functionality by withdrawing 5 ether into
- Withdrawing 5 ether into accountOne
![WITHDRAW_5](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Withdraw_5_ether_into_Account1.png)
- Withdrawing 10 ether into accountTwo
![WITHDRAW_10](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Withdraw_10_ether_into_Account2.png)
- use the lastToWithdraw to verify tthe address
![VERIFY_ADDRESS](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/lastToWithdraw.png)
- use the lastWithdrawAmount to verify the amount
![VERIFY_AMOUNT](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/lastWithdrawAmount.png)
- After each transaction, use the contractBalance function to verify that the funds were withdrawn from your contract
![CONTACT_BALANCE](https://github.com/klee08/module_challenges/blob/main/Module20_Challenge/Execution_Results/Contact_balance.png)

_____________________________________________________
# Technologies
- Used Remix IDE to build and test Solidity smart contracts
https://remix.ethereum.org/  
# Usage
- To run this project: https://remix.ethereum.org/ > upload joint_savings.sol > compile and deploy
(“Deploy & Run Transactions” pane, and then make sure that “JavaScript VM” is selected as the environment)

# Reference: 
- Ethereum Unit Converter: https://eth-converter.com/
- create new, dummy addresses on the Vanity-ETH: https://vanity-eth.tk/

# Contributers
Ken Lee
Columbia FinTech BootCamp
# Licence
Open source project, made for educational purposes only
