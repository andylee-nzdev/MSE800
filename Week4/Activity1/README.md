# Database Design for Currency Exchange

## Overview
This database is designed for a currency exchange and account management system. It consists of **6 tables** that work together to manage customers, accounts, payments, currency information, employees, and exchange transactions.



## Tables

### 1. **Customer** Table
**Columns:**
- `customer_id` (Primary Key) - Unique identifier for each customer
- `phone_number` - Customer's phone number
- `first_name` - Customer's first name
- `last_name` - Customer's last name
- `address` - Customer's physical address

**Justification:** This table stores core customer information. It is the foundation of the system and serves as the central entity from which all account relationships are derived. Every account and transaction in the system must be traceable back to a customer.



### 2. **Account** Table
**Columns:**
- `account_id` (Primary Key) - Unique identifier for each account
- `customer_id` (Foreign Key) - Links to the Customer table
- `balance` - Current balance in the account
- `currency_code` (Foreign Key) - Links to the Currency table

**Justification:** This table represents individual accounts owned by customers. Customers can have multiple accounts with different currencies. This table is essential to track account balances and maintain the relationship between customers and their financial holdings.


### 3. **Payment** Table
**Columns:**
- `payment_id` (Primary Key) - Unique identifier for each payment
- `account_id` (Foreign Key) - Links to the Account table
- `payment_method` - Method used for payment (e.g., credit card, bank transfer)
- `payment_date` - Date and time of the payment
- `amount` - Amount of the payment

**Justification:** This table records all payment transactions made from accounts. It provides an audit trail for financial activities and allows tracking of payment history, methods, and amounts for accounting and compliance purposes.


### 4. **Currency** Table
**Columns:**
- `currency_code` (Primary Key) - ISO currency code (e.g., USD, EUR, JPY)
- `country` - Country where the currency is used
- `currency_name` - Full name of the currency
- `symbol` - Currency symbol (e.g., $, €, ¥)
- `exchange_rate` - Current exchange rate (typically relative to a base currency)

**Justification:** This table maintains information about all supported currencies in the system. It is necessary to standardize currency codes, store exchange rates, and provide metadata about each currency. This enables the system to support multi-currency operations and conversions.


### 5. **Employee** Table
**Columns:**
- `employee_id` (Primary Key) - Unique identifier for each employee
- `first_name` - Employee's first name
- `last_name` - Employee's last name
- `phone_number` - Employee's phone number
- `role` - Employee's job role or title

**Justification:** This table stores employee information. Employees may be involved in processing exchange transactions and need to be tracked for accountability and audit purposes. This table provides a registry of all staff members in the organization.


### 6. **Exchange_Transaction** Table
**Columns:**
- `transaction_id` (Primary Key) - Unique identifier for each transaction
- `amount` - Amount exchanged
- `currency_code` (Foreign Key) - Links to the Currency table
- `from_account` (Foreign Key) - Links to the Account table (source account)
- `to_account` (Foreign Key) - Links to the Account table (destination account)
- `employee_id` (Foreign Key) - Links to the Employee table

**Justification:** This table records currency exchange transactions between accounts. It is critical for tracking multi-currency transfers, monitoring exchange activity, and maintaining a complete audit trail. The employee link enables tracking which staff member processed the exchange, supporting compliance and operational oversight.


## Database Relationships

```
Customer (1) ──────── (Many) Account
                           ├── Balance & Currency Info
                           └── (Many) Payment
                           └── (Many) Exchange_Transaction

Currency (1) ──────---- (Many) Account
                        (Many) Exchange_Transaction

Employee (1) ──────---- (Many) Exchange_Transaction

Exchange_Transaction:
  └── from_account → Account
  └── to_account → Account
  └── currency_code → Currency
  └── employee_id → Employee
```


## Summary

The 6-table structure provides:
- **Data Organization:** Clear separation of concerns (customers, accounts, payments, currencies, employees, transactions)
- **Referential Integrity:** Foreign key constraints ensure data consistency
- **Audit Trail:** Complete tracking of transactions and payments with employee accountability
- **Scalability:** Design supports multiple customers, accounts, currencies, and employees
- **Compliance:** Comprehensive record-keeping for financial and operational audits
