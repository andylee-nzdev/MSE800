import sqlite3

CREATE_CUSTOMER_TABLE = '''
    CREATE TABLE IF NOT EXISTS Customer (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT,
        first_name TEXT,
        last_name TEXT,
        address TEXT
    )
'''

CREATE_ACCOUNT_TABLE = '''
    CREATE TABLE IF NOT EXISTS Account (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        balance REAL,
        currency_code TEXT,
        FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
    )
'''

CREATE_PAYMENT_TABLE = '''
    CREATE TABLE IF NOT EXISTS Payment (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        payment_method TEXT,
        payment_date TEXT,
        amount REAL,
        FOREIGN KEY (account_id) REFERENCES Account(account_id)
    )
'''

CREATE_CURRENCY_TABLE = '''
    CREATE TABLE IF NOT EXISTS Currency (
        currency_code TEXT PRIMARY KEY,
        country TEXT,
        currency_name TEXT,
        symbol TEXT,
        exchange_rate REAL
    )
'''

CREATE_EMPLOYEE_TABLE = '''
    CREATE TABLE IF NOT EXISTS Employee (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT,
        role TEXT
    )
'''

CREATE_EXCHANGE_TRANSACTION_TABLE = '''
    CREATE TABLE IF NOT EXISTS Exchange_Transaction (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        currency_code TEXT,
        from_account INTEGER NOT NULL,
        to_account INTEGER NOT NULL,
        employee_id INTEGER,
        FOREIGN KEY (currency_code) REFERENCES Currency(currency_code),
        FOREIGN KEY (from_account) REFERENCES Account(account_id),
        FOREIGN KEY (to_account) REFERENCES Account(account_id),
        FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
    )
'''

def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute(CREATE_CUSTOMER_TABLE)
    cursor.execute(CREATE_ACCOUNT_TABLE)
    cursor.execute(CREATE_PAYMENT_TABLE)
    cursor.execute(CREATE_CURRENCY_TABLE)
    cursor.execute(CREATE_EMPLOYEE_TABLE)
    cursor.execute(CREATE_EXCHANGE_TRANSACTION_TABLE)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("All tables created successfully.")
