from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.area, self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice != None and "" : 
            return self.plus_index(self.df[self.df['시, 군'] == self.choice])
            
        elif self.address != None :
            # return self.plus_index(self.df[self.df['글램핑장'].str.contains(self.address).reset_index(drop=True)])
            return self.plus_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))])

        else : return None

    def plus_index(self, result):
        result.reset_index(drop=True)
        result.index += 1 
        return result

    def result_function(self) : return self.choice_address(), self.choice, self.address