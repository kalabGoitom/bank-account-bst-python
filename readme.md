# 🏦 Bank Account Management System (BST)

A menu-driven **Bank Account Management System** built in Python using a **Binary Search Tree (BST)** as the core data structure. Built as a course project for a Data Structures class.

---

## 📌 Overview

Traditional banking systems that store records in unsorted lists suffer from slow search, update, and delete operations as customer count grows. This project solves that by organizing all account records in a Binary Search Tree, where each node represents one customer — enabling efficient `O(log n)` operations on average.

---

## 🌳 Data Structure

A **Binary Search Tree** is used where:

- Each **node** holds: `account_number`, `name`, and `balance`
- The **account number** is the BST key
- Left subtree nodes have smaller account numbers; right subtree nodes have larger ones
- **In-order traversal** produces accounts sorted by account number

```
         1005 (David)
        /             \
  1002 (Bob)       1007 (Carol)
  /        \
1001       1003
(Alice)   (Eva)
```

---

## ⚙️ Features

| #   | Operation                | Description                                              |
| --- | ------------------------ | -------------------------------------------------------- |
| 1   | **Create Account**       | Insert a new customer account into the BST               |
| 2   | **Search Account**       | Find an account by account number                        |
| 3   | **Deposit Money**        | Add funds to an existing account                         |
| 4   | **Withdraw Money**       | Deduct funds (with balance validation)                   |
| 5   | **Update Account**       | Modify customer name or balance                          |
| 6   | **Delete Account**       | Remove an account using BST deletion logic               |
| 7   | **Display All Accounts** | Show all accounts in sorted order via in-order traversal |
| 8   | **Exit**                 | Safely terminate the program                             |

---

## 🛡️ Error Handling

- Duplicate account number on creation
- Account not found during search, deposit, withdraw, update, or delete
- Insufficient balance during withdrawal
- Negative deposit/withdrawal amounts
- Invalid input types (non-integer account numbers, non-numeric amounts)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required — uses only the Python standard library

### Run the program

```bash
git clone https://github.com/your-username/bank-account-bst-python.git
cd bank-account-bst-python
python bank_account_bst.py
```

Five sample accounts are pre-loaded on startup so you can demo all operations immediately.

---

## 🖥️ Sample Output

```
╔════════════════════════════════════════════╗
║    BANK ACCOUNT MANAGEMENT SYSTEM (BST)   ║
╠════════════════════════════════════════════╣
║  1. Create Account                        ║
║  2. Search Account                        ║
║  3. Deposit Money                         ║
║  4. Withdraw Money                        ║
║  5. Update Account                        ║
║  6. Delete Account                        ║
║  7. Display All Accounts (Sorted)         ║
║  8. Exit                                  ║
╚════════════════════════════════════════════╝

  Enter choice (1-8): 2

-- Search Account --
  Account Number : 1003

  Account Found:
  Account No : 1003
  Name       : Alice Johnson
  Balance    : $5,000.00
```

---

## 📁 Project Structure

```
bank-account-bst-python/
│
├── bank_account_bst.py   # Main source file (BST + menu interface)
└── README.md
```

---

## 🧠 Concepts Demonstrated

- Binary Search Tree construction and traversal
- Recursive insertion, search, and deletion
- In-order traversal for sorted output
- BST deletion (three cases: leaf, one child, two children)
- Object-oriented design with `AccountNode` and `BankBST` classes
- Input validation and error handling

---

## 📚 Course Info

**Course:** Data Structures  
**Level:** Undergraduate  
**Language:** Python

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
