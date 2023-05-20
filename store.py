import pandas as pd
class Store():
    def __init__(self):
        self.d = pd.read_csv(
            'C:/Users/LENOVO/Desktop/Ap/project 1/warehouse.csv')

    def Order(self, wares: list):     # shows goods and takes order and add the order to ware list #
        for i in self.d.index:
            if self.d.loc[i, 'number'] > 0:      # shows available goods #
                print(
                    f"{i+1}.({self.d.loc[i , 'number']}){self.d.loc[i , 'name']} {self.d.loc[i , 'price']}")
            else:
                print(f"{i+1}.{self.d.loc[i , 'name']}  unavailable")
        o = eval(input("please choose the good you want: "))
        n = eval(input("please choose the number you want: "))

        # checks if the chosen number of a good be in warehouse #
        if self.d.loc[o-1, 'number'] >= n:
            self.d.loc[o-1, 'number'] -= n  # update number of showable list
            s = input("Wich size do you want?(M,L,XL) ")
            print("\nthe goods added to your cart successfuly:)")
            l = [self.d.loc[o-1, 'name'], self.d.loc[o-1, 'price'], n]
            wares.append(l)
        else:
            print("Oops! the number you want is not available")
        return wares

    def cart(wares):  # shows all chosen goods and let to add more
        # dataframe of wares
        dw = pd.DataFrame(wares, columns=['name', 'price', 'number'])
        print(f"\n{dw}\n")
        print("Choose an option to continue!")
        o = input("1.Back to store\n2.Payment\n")
        return o
