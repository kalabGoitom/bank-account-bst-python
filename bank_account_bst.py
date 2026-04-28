"""
Bank Account Management System
Course: Data Structures
Data Structure Used: Binary Search Tree (BST)
Language: Python
"""

# ─────────────────────────────────────────────
#  Node class — one customer account per node
# ─────────────────────────────────────────────
class AccountNode:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number   # int  — BST key
        self.name           = name             # str
        self.balance        = balance          # float
        self.left           = None
        self.right          = None

    def __str__(self):
        return (f"  Account No : {self.account_number}\n"
                f"  Name       : {self.name}\n"
                f"  Balance    : ${self.balance:,.2f}")


# ─────────────────────────────────────────────
#  BST class — all tree operations live here
# ─────────────────────────────────────────────
class BankBST:

    def __init__(self):
        self.root = None

    # ── helpers ──────────────────────────────
    def _insert(self, node, acc_no, name, balance):
        """Recursively insert; raises ValueError on duplicate."""
        if node is None:
            return AccountNode(acc_no, name, balance)
        if acc_no == node.account_number:
            raise ValueError(f"Account {acc_no} already exists.")
        elif acc_no < node.account_number:
            node.left  = self._insert(node.left,  acc_no, name, balance)
        else:
            node.right = self._insert(node.right, acc_no, name, balance)
        return node

    def _search(self, node, acc_no):
        """Return node or None."""
        if node is None:
            return None
        if acc_no == node.account_number:
            return node
        elif acc_no < node.account_number:
            return self._search(node.left,  acc_no)
        else:
            return self._search(node.right, acc_no)

    def _min_node(self, node):
        """Leftmost node in a subtree — used during deletion."""
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node, acc_no):
        """Recursively delete; returns updated subtree root."""
        if node is None:
            raise ValueError(f"Account {acc_no} not found.")
        if acc_no < node.account_number:
            node.left  = self._delete(node.left,  acc_no)
        elif acc_no > node.account_number:
            node.right = self._delete(node.right, acc_no)
        else:
            # Node found — three cases
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Two children: replace with in-order successor
            successor       = self._min_node(node.right)
            node.account_number = successor.account_number
            node.name       = successor.name
            node.balance    = successor.balance
            node.right      = self._delete(node.right, successor.account_number)
        return node

    def _inorder(self, node, results):
        """In-order traversal → sorted by account number."""
        if node:
            self._inorder(node.left, results)
            results.append(node)
            self._inorder(node.right, results)

    # ── public operations ────────────────────

    def create_account(self, acc_no, name, balance):
        """Insert a new account into the BST."""
        if not isinstance(acc_no, int) or acc_no <= 0:
            raise ValueError("Account number must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.root = self._insert(self.root, acc_no, name.strip(), balance)
        print(f"\n✔ Account {acc_no} created successfully.")

    def search_account(self, acc_no):
        """Find and display an account."""
        node = self._search(self.root, acc_no)
        if node is None:
            raise ValueError(f"Account {acc_no} not found.")
        return node

    def deposit(self, acc_no, amount):
        """Add money to an account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        node = self.search_account(acc_no)
        node.balance += amount
        print(f"\n✔ Deposited ${amount:,.2f} to Account {acc_no}.")
        print(f"  New balance: ${node.balance:,.2f}")

    def withdraw(self, acc_no, amount):
        """Deduct money if balance is sufficient."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        node = self.search_account(acc_no)
        if amount > node.balance:
            raise ValueError(
                f"Insufficient funds. Available balance: ${node.balance:,.2f}"
            )
        node.balance -= amount
        print(f"\n✔ Withdrew ${amount:,.2f} from Account {acc_no}.")
        print(f"  New balance: ${node.balance:,.2f}")

    def update_account(self, acc_no, new_name=None, new_balance=None):
        """Update name and/or balance of an account."""
        node = self.search_account(acc_no)
        if new_name and new_name.strip():
            node.name = new_name.strip()
        if new_balance is not None:
            if new_balance < 0:
                raise ValueError("Balance cannot be negative.")
            node.balance = new_balance
        print(f"\n✔ Account {acc_no} updated successfully.")

    def delete_account(self, acc_no):
        """Remove an account from the BST."""
        self.root = self._delete(self.root, acc_no)
        print(f"\n✔ Account {acc_no} deleted successfully.")

    def display_all(self):
        """Print all accounts in sorted order (in-order traversal)."""
        accounts = []
        self._inorder(self.root, accounts)
        if not accounts:
            print("\n  (No accounts found.)")
            return
        print(f"\n{'─'*40}")
        print(f"  {'ALL ACCOUNTS (sorted by account number)'}")
        print(f"{'─'*40}")
        for a in accounts:
            print(a)
            print(f"{'─'*40}")


# ─────────────────────────────────────────────
#  Input helpers
# ─────────────────────────────────────────────
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ⚠ Please enter a valid integer.")

def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            return val
        except ValueError:
            print("  ⚠ Please enter a valid number.")


# ─────────────────────────────────────────────
#  Menu-driven interface
# ─────────────────────────────────────────────
def print_menu():
    print("""
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
╚════════════════════════════════════════════╝""")

def run():
    bank = BankBST()

    # Pre-load a few sample accounts so the tree is not empty on first run
    samples = [
        (1003, "Alice Johnson",   5000.00),
        (1001, "Bob Smith",       1200.50),
        (1007, "Carol Williams", 18000.00),
        (1005, "David Brown",     3400.75),
        (1002, "Eva Martinez",    9500.00),
    ]
    for acc, name, bal in samples:
        bank.create_account(acc, name, bal)
    print("\n  (Sample accounts loaded.)")

    while True:
        print_menu()
        choice = input("  Enter choice (1-8): ").strip()

        try:
            if choice == "1":
                print("\n-- Create Account --")
                acc_no  = get_int("  Account Number : ")
                name    = input("  Customer Name  : ")
                balance = get_float("  Initial Balance: $")
                bank.create_account(acc_no, name, balance)

            elif choice == "2":
                print("\n-- Search Account --")
                acc_no = get_int("  Account Number : ")
                node   = bank.search_account(acc_no)
                print(f"\n  Account Found:\n{node}")

            elif choice == "3":
                print("\n-- Deposit Money --")
                acc_no = get_int("  Account Number : ")
                amount = get_float("  Amount to Deposit: $")
                bank.deposit(acc_no, amount)

            elif choice == "4":
                print("\n-- Withdraw Money --")
                acc_no = get_int("  Account Number : ")
                amount = get_float("  Amount to Withdraw: $")
                bank.withdraw(acc_no, amount)

            elif choice == "5":
                print("\n-- Update Account --")
                acc_no   = get_int("  Account Number : ")
                new_name = input("  New Name (leave blank to skip): ").strip()
                nb_input = input("  New Balance (leave blank to skip): $").strip()
                new_bal  = float(nb_input) if nb_input else None
                bank.update_account(
                    acc_no,
                    new_name  if new_name  else None,
                    new_bal
                )

            elif choice == "6":
                print("\n-- Delete Account --")
                acc_no = get_int("  Account Number : ")
                confirm = input(f"  Confirm delete account {acc_no}? (yes/no): ")
                if confirm.lower() == "yes":
                    bank.delete_account(acc_no)
                else:
                    print("  Deletion cancelled.")

            elif choice == "7":
                bank.display_all()

            elif choice == "8":
                print("\n  Thank you for using the Bank System. Goodbye!\n")
                break

            else:
                print("  ⚠ Invalid choice. Please enter a number between 1 and 8.")

        except ValueError as e:
            print(f"\n  ✘ Error: {e}")
        except Exception as e:
            print(f"\n  ✘ Unexpected error: {e}")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    run()
