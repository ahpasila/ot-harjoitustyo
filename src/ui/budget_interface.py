from entities.budget import Budget
from datetime import date

class BudgetInterface:
    def __init__(self):
        self.__budget = Budget()  

    def information(self):
        print("Käyttöliittymä")
        print("1 - Anna budjettijakson alku- ja loppupvm")
        print("2 - Lisää uusi tulo")
        print("3 - Lisää uusi meno")
        print("4 - Tulosta tulot")
        print("5 - Tulosta menot")
        print("6 - Lopeta")
    
    def execute(self):
        self.information()
        while True:
            givenValue=input("Anna luku: ")
            if (givenValue == "1"):
                begDateEntry = input("Anna alkupäivämäärä (muotoa VVVV-KK-PP): ")
                begYear,begMonth,begDay = map(int, begDateEntry.split('-'))
                self.__budget.set_beginningDate(begYear, begMonth, begDay)
                endDateEntry = input("Anna loppupäivämäärä (muotoa VVVV-KK-PP): ")
                endYear,endMonth,endDay = map(int, endDateEntry.split('-'))
                self.__budget.set_endDate(endYear, endMonth, endDay)
            elif (givenValue == "2"):
                incomeName=input("Anna tulon nimi: ")
                income=input("Anna tulon suuruus: ")
                self.__budget.add_income(incomeName, income)
            elif (givenValue == "3"):
                expenseName=input("Anna menon nimi: ")
                expense=input("Anna menon suuruus: ")
                self.__budget.add_expense(expenseName, expense)
            elif (givenValue == "4"):
                self.__budget.printing_test_income()
            elif (givenValue == "5"):
                self.__budget.printing_test_expense()
            elif (givenValue == "6"):
                break
            else:
                print("Virheellinen arvo")

appInterface = BudgetInterface()
appInterface.execute()
