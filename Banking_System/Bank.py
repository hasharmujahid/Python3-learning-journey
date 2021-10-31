import datetime


def date_time():
    return datetime.datetime.now()


class Account:
    bank_name = 'HBL'
    branch_name = 'CTN'

    def __init__(self, name, Total_balance, Age):
        self.Account_holder = name
        self.Total_account_balance = Total_balance
        self.Age = Age
        self.file = open(str(self.Account_holder) + ' Account logs.txt', 'a')

    def Adding_Money(self, New_ammount_To_Be_added):
        date = date_time()
        if New_ammount_To_Be_added >= 500:
            self.Total_account_balance += New_ammount_To_Be_added

            file_log = open(str(self.Account_holder) + ' Account logs.txt', 'a')
            file_log.write('[ ' + str(date) + '] ' + str(New_ammount_To_Be_added) + ' is added to your account \n ')
            file_log.close()

        else:
            print("Amount is negligible lest amount is 500 ")
            file_log = open(str(self.Account_holder) + ' Account logs.txt', 'a')
            file_log.write('[ ' + str(date) + '] ' + 'you attempted to add ' + str(
                New_ammount_To_Be_added) + ' in your account but acess was denined  \n ')
            file_log.close()

        return self.Total_account_balance

    def Widthdrawing_money(self, New_ammount_to_be_removed):
        date = date_time()
        if 500 <= New_ammount_to_be_removed <= self.Total_account_balance:
            self.Total_account_balance -= New_ammount_to_be_removed

            file_log = open(str(self.Account_holder) + ' Account logs.txt', 'a')
            file_log.write(
                '[ ' + str(date) + '] ' + str(New_ammount_to_be_removed) + ' is widthdrawed from your account \n ')
            file_log.close()
        else:
            print("Amount is negligible lest amount is 500 ")
            file_log = open(str(self.Account_holder) + ' Account logs.txt', 'a')
            file_log.write('[ ' + str(date) + '] ' + 'you attempted to widthdraw ' + str(
                New_ammount_to_be_removed) + ' in your account but acess was denined  \n ')
            file_log.close()
        return self.Total_account_balance

    def show_balance(self):
        print(f'{self.Account_holder} account balance is {self.Total_account_balance}')

    @classmethod
    def Changing_baranch(cls, New_Branch):
        cls.branch_name = New_Branch
        return cls.branch_name

    @classmethod
    def Changing_bank(cls, New_bank):
        cls.bank_name = New_bank
        return cls.bank_name

    @staticmethod
    def send_money(Account_1, Account_2):
        enter_amount = int(input("enter the money : "))
        date = date_time()
        if enter_amount < Account_1.Total_account_balance:
            Account_1.Total_account_balance -= enter_amount
            Account_2.Total_account_balance += enter_amount
            log_Account_1 = open(str(Account_1.Account_holder)+' Account logs.txt', 'a')
            log_Account_1.write('[ ' + str(date) + '] ' + 'you attempted to Send ' + str(
                enter_amount) + ' from your account to ' + str(
                Account_2.Account_holder) + 'Your new balance is '.format(Account_1.Total_account_balance) + '\n')
            log_Account_1.close()
            file_log_Account_2 = open(str(Account_2.Account_holder) + ' Account logs.txt', 'a')
            file_log_Account_2.write('[ ' + str(date) + '] ' + 'you recieved  ' + str(
                enter_amount) + ' from your  ' + str(
                Account_2.Account_holder) + ' Your new balance is '.format(Account_2.Total_account_balance) + '\n')
        else:
            print('You dont have enough balance in your account')


if __name__ == '__main__':
    Hashar = Account('Hashar', 3000, 18)
    Hashar.Adding_Money(9000)
    Hashar.show_balance()
    Hashar.Changing_bank("UBL")
    print(Hashar.bank_name)
    Tayyab = Account('Tayyab', 7000, 21)
    Tayyab.Adding_Money(2000)
    Tayyab.show_balance()

    Abdullah = Account('Abdullah', 6000, 13)
    Abdullah.Widthdrawing_money(200)
    Abdullah.show_balance()
    Abdullah.send_money(Abdullah, Hashar)
    Abdullah.show_balance()
    Hashar.show_balance()
