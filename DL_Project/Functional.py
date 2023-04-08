from ChoiceArea import GetSideBar
from Data import GetData

class GetResult:
    def __init__(self) -> None:
        self.df = GetData().result_data()
        self.area, self.choice, self.address = GetSideBar().result_sidebar()

    def choice_address(self) : 
        if self.choice is not None and "" : return self.handle_index(self.df[self.df['시, 군'] == self.choice])
        elif self.address is not None : return self.handle_index(self.df[(self.df['시, 군'] == self.choice) & (self.df['글램핑장'].str.contains(self.address))])
        else : return None

    def handle_index(self, data):
        data = data.iloc[:, 2:].sort_values('평점', ascending=False).reset_index(drop=True)
        data.index += 1

        if data.empty : data.loc[0] = ["-"] * len(data.columns)
        return data

    def result_function(self) : return self.choice_address(), self.area, self.choice, self.address

    # 테스트 끝나면 위에 지울 것
    # def result_function(self) : return self.choice_address()