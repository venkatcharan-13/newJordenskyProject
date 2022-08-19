from time import sleep
import time
import requests
import json
from databaseConfig import dbservice


db = dbservice()


CLIENT_ID='1000.4MRW467CKK6O6JU5QMQQSDC4VVVJFL'
CLIENT_SECRET='4ca8f47df3add19f6e78f70078964362413ca3fe9e'
REDIRECT_URL='http://www.zoho.in/books'
REFRESH_TOKEN=''


# def generateAuthToken():
#     URL_FOR_REFRESHTOKEN='https://accounts.zoho.com/oauth/v2/token?refresh_token={REFRESH_TOKEN}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&redirect_uri=http://www.zoho.in/books&grant_type=refresh_token'
#     response_for_token=requests.post(URL_FOR_REFRESHTOKEN)
#     response_data = response_for_token.content
#     auth_token = json.loads(response_data)['access_token']
#     return auth_token

def fetchingAccount(accounts_data,idOfClient):
    for account in accounts_data:
        account['client_id']=idOfClient
        db.add_record('accounts_zohoaccount', input_data=account)
    print('done accounts')


def fetchTransactions(accounts_data,ORGANIZATION_ID,HEADER,response_for_accounts):
    account_ids_dict = {}
    URL_FOR_TRANSACTIONS = f"https://books.zoho.in/api/v3/chartofaccounts/transactions?organization_id={ORGANIZATION_ID}&per_page=500&account_id="
    for account in accounts_data:
        account_ids_dict[account['account_id']] = account['parent_account_id']

    transactions_dict = {}
    c = 1
    for account_id in account_ids_dict:
        response_for_transaction= requests.get(URL_FOR_TRANSACTIONS + account_id, headers=HEADER)
        print(response_for_accounts.status_code, c, account_id)
        c += 1
        transaction_data = response_for_transaction.content
        transaction_data = json.loads(transaction_data)['transactions']
        transactions_dict[account_id] = transaction_data

    for account_id in transactions_dict:
        if transactions_dict[account_id] == []:
            continue
        for transaction in transactions_dict[account_id]:
            transaction['parent_account_id'] = account_ids_dict[account_id]
            db.add_record('accounts_zohotransaction', input_data=transaction)
    print('done transactions')


def fetchingCompleteDetails(organisactionID,idOfClient):
    ORGANIZATION_ID =  organisactionID
    URL_FOR_ACCOUNTS = f"https://books.zoho.in/api/v3/chartofaccounts?organization_id={ORGANIZATION_ID}&showbalance=true"
    AUTH_TOKEN = '1000.f8f246857ea9622e0923669bc54a7da3.3b5998689c14d0f06d7872da902082f6' 
    # AUTH_TOKEN=generateAuthToken()
    HEADER = {
        'Authorization': f'Zoho-oauthtoken {AUTH_TOKEN}'
    }

    response_for_accounts = requests.get(URL_FOR_ACCOUNTS, headers=HEADER)
    accounts_data = response_for_accounts.content
    accounts_data = json.loads(accounts_data)['chartofaccounts']

    fetchingAccount(accounts_data,idOfClient)
    fetchTransactions(accounts_data,ORGANIZATION_ID,HEADER,response_for_accounts)
    print('completed')



# fetchingCompleteDetails(60014631936,2)


# Uncomment below foor loop in case of accounts
# for account in accounts_data:
#     db.add_record('accounts_zohoaccount', input_data=account)

#Comment this part when fetching accounts 
# account_ids_dict = {}
# for account in accounts_data:
#     account_ids_dict[account['account_id']] = account['parent_account_id']

# transactions_dict = {}
# c = 1
# for account_id in account_ids_dict:
#     response_for_transaction= requests.get(URL_FOR_TRANSACTIONS + account_id, headers=HEADER)
#     print(response_for_accounts.status_code, c, account_id)
#     c += 1
#     transaction_data = response_for_transaction.content
#     transaction_data = json.loads(transaction_data)['transactions']
#     transactions_dict[account_id] = transaction_data
    # time.sleep(3)

#Comment below part for accounts
# for account_id in transactions_dict:
#     if transactions_dict[account_id] == []:
#         continue
#     for transaction in transactions_dict[account_id]:
        
#         transaction['parent_account_id'] = account_ids_dict[account_id]
#         db.add_record('accounts_zohotransaction', input_data=transaction)