
# Smart Contract Proxy

This is program for showing how to use proxies for creating smart contract that can be updateable. This is useful for cases where the programmer or community wants to upgrade some functionalities in smart contract and as you know, the blockchain cannot be edited.

## Prerequisites
Please install or have installed the below program:

- [Python and pip](https://nodejs.org/en/download/)
- [nodejs and npm](https://nodejs.org/en/download/)

## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```
Or, if that doesn't work, via pipx
```bash
pip install --user pipx
pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
2. Clone this repo
```
# open your terminal
git clone https://github.com/codebestia/smart-contract-proxy.git
cd smart-contract-proxy
```

3. [Install ganache-cli](https://www.npmjs.com/package/ganache-cli)

```bash
npm install -g ganache-cli
```
If you want to be able to deploy to testnets, do the following. 

4. Set your environment variables

Set your `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). 

You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/). 


Create a .env file in the contract directory and add your environment variables to the `.env` file:

```
export PRIVATE_KEY=<PRIVATE_KEY>
```
> DO NOT SEND YOUR KEY TO GITHUB
> If you do that, people can steal all your funds. Ideally use an account with no real money in it. 


Then, make sure your `brownie-config.yaml` has:

```
dotenv: .env
```




## Usage/Examples

1. Compile the smart contracts
```
brownie compile
```
2. Deploy and Interaction
for local ganache chain
```
brownie run scripts/deploy.py
```
for testnet
```
brownie run scripts/deploy.py --network sepolia
```
