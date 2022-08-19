from turtle import clear
import psycopg2

class dbservice:
    def __init__(self):
        self.connector = None
        self.dbcursor = None
        self.connect_db()
        #self.create_table()
    
    def connect_db(self):
        '''Connects to Postgresql Database'''

        self.connector = psycopg2.connect(database='jhl', user='postgres', password='pragna', host='127.0.0.1', port='5432')
        self.dbcursor = self.connector.cursor()

    def create_table(self):
        self.dbcursor.execute('''CREATE TABLE IF NOT EXISTS accounts_zohoaccount(
            account_id VARCHAR(100),
            account_name VARCHAR(100),
            account_code VARCHAR(20),
            account_type VARCHAR(100),
            description TEXT,
            is_user_created BOOLEAN,
            is_system_account BOOLEAN,
            is_active BOOLEAN,
            can_show_in_ze BOOLEAN,
            current_balance DECIMAL,
            parent_account_id VARCHAR(100),
            parent_account_name VARCHAR(100),
            depth INT,
            has_attachment BOOLEAN,
            is_child_present BOOLEAN,
            child_count VARCHAR(10),
            created_time VARCHAR(40),
            is_standalone_account BOOLEAN,
            last_modified_time VARCHAR(40),
            PRIMARY KEY (account_id)
        );''')

        self.dbcursor.execute('''CREATE TABLE IF NOT EXISTS accounts_zohotransaction(
            categorized_transaction_id VARCHAR(100),
            transaction_type VARCHAR(100),
            transaction_status VARCHAR(100),
            transaction_status_formatted VARCHAR(100),
            transaction_source VARCHAR(100),
            transaction_id VARCHAR(100),
            transaction_date DATE,
            transaction_type_formatted VARCHAR(100),
            account_id VARCHAR(100),
            parent_account_id VARCHAR(100),
            customer_id VARCHAR(100),
            payee VARCHAR(100),
            description TEXT,
            entry_number VARCHAR(100),
            currency_id VARCHAR(100),
            currency_code VARCHAR(20),
            debit_or_credit VARCHAR(20),
            offset_account_name VARCHAR(100),
            reference_number VARCHAR(100),
            debit_amount VARCHAR(40),
            credit_amount VARCHAR(40),
            fcy_debit_amount VARCHAR(40),
            fcy_credit_amount VARCHAR(40),
            reconcile_status VARCHAR(100),
            FOREIGN KEY (account_id) REFERENCES accounts_zohoaccounts(account_id) ON UPDATE CASCADE ON DELETE CASCADE
        );''')

        self.connector.commit()


    def add_record(self, table_name, input_data):
        if 'documents' in input_data:
            del input_data['documents']

        keys = list(input_data.keys())

        #Preparing Query
        table_data, table_values = '(', ' VALUES ('
        for i, x in enumerate(keys):
            if i != len(keys)-1:
                # table_values+=f'%({client_id})'
                table_values += f'%({x})s, '
                table_data += f'{x}, '
            else:
                table_values += f'%({x})s)'
                table_data += f'{x})'

        add_query = (f'INSERT INTO {table_name} ' + table_data + table_values)
        #Execute Query
        try:
            self.dbcursor.execute(add_query, input_data)
            self.connector.commit()
        except Exception as e:
            print(e)
