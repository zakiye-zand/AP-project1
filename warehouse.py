import pandas as pd
class Warehouse:
    def __init__(self):

        self.d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')

    def Option(self):  # gets what user wants to do
        print("***Warehouse managment***\n")
        o = input("1.update list of goods\n2.print list of goods\n3.add good\n")
        return o

    # changes the warehouse file by name and *lost number of wares
    def auto_update(self, name, number):
        self.d.loc[(self.d['name'] == name), 'number'] -= number
        self.d.to_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv", index=False)
        pass

    # changes the warehouse file by name and  *new number of wares
    def Update(self, name, number: int):
        # d = pd.read_csv(
        # 'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')
        self.d.loc[(self.d['name'] == name), 'number'] = number
        self.d.to_csv(
            "C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv", index=False)
        pass

    def Manualy_update(self):  # Not automatic , this is how manager access for update

        o = input(
            "Choose update method\n1.csv file address \n2.enter the name and number of goods\n")

        if o == '2':
            name = input("enter the name\n")
            number = eval(input("enter the new number\n"))
            Warehouse.Update(name, number)
        elif o == '1':
            path = input("enter the path of csv file \n")
            d = pd.read_csv(path)
            for i in d.index:
                self.Update(d.iloc[i, 0], d.iloc[i, 1])
        else:
            print("not available option")

        pass

    def Output(self):  # saves an output of wares

        o = input("\n1.text output\n2.csv output\n")
        d = self.d[['code', 'number', 'wh.code']]
        if o == '1':
            path = 'c:/Users/LENOVO/Desktop/Ap/project 1/warehouse output.txt'
            with open(path, 'a') as f:
                d_string = d.to_string( index=False)
                f.write(d_string)
            print("Text file saved\n")
        elif o == '2':
            d.to_csv(
                "c:/Users/LENOVO/Desktop/Ap/project 1/warehouse output.csv", index=False)
            print("Csv file saved\n")

    def AddWare(self):
        whcode = eval(input("Enter warehouse code: \n"))
        name = input("Enter ware name: \n")
        code = eval(input("Enter ware code: \n"))
        number = eval(input("Enter ware number: \n"))
        price = input("Enter ware price: \n")
        self.d.loc[len(self.d.index)] = [whcode, name, code, number, price]
        self.d.to_csv(
            "c:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv", index=False)


