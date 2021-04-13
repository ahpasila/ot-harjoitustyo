from datetime import date

class Budget:
    def __init__(self):
        self.__beginnigDate = date.today()
        self.__endDate = date.today()
        self.__allIncomes = {}
        self.__allExpenses = {}

    def set_beginningDate(self, begYear: int, begMonth: int, begDay: int):
        self.__beginningDate=date(begYear,begMonth,begDay)

    def set_endDate(self, endYear: int, endMonth: int, endDay: int):
        self.__endDate=date(endYear,endMonth,endDay)

    def add_income(self, incomeName: str, income: int):
        self.__allIncomes[incomeName] = []
        self.__allIncomes[incomeName].append(income)

    def add_expense(self, expenseName: str, expense: int):
        self.__allExpenses[expenseName] = []
        self.__allExpenses[expenseName].append(expense)

    def printing_test_income(self):
        print("Tulot ajalla",self.__beginnigDate,"-",self.__endDate)
        incomeItems = self.__allIncomes.items()
        for item in incomeItems:
            print(item)
        
    def printing_test_expense(self):
        print("Menot ajalla",self.__beginnigDate,"-",self.__endDate)
        expenseItems = self.__allExpenses.items()
        for item in expenseItems:
            print(item)
