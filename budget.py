class Budget:
    def __init__(self, budgetID, totalAmount):
        self.budgetID = budgetID
        self.totalAmount = totalAmount
        self.spentAmount = 0.0

    def addExpense(self, amount):
        self.spentAmount += amount

    def getRemainingBudget(self):
        return self.totalAmount - self.spentAmount
