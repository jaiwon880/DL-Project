from SideBar import GetSideBar
from Data import GetData

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

class GetResult:
    def __init__(self) -> None:
        self.df, \
        self.area, \
        self.direction = GetSideBar().choice_result_sidebar()

        self.total, \
        self.gapyeong, \
        self.pocheon = GetData().create_price()
        
        self.image_path = ["https://i.imgur.com/qZJvwRB.png", \
                            "https://i.imgur.com/Bgv83pb.png", \
                            "https://i.imgur.com/QGxbZJa.png"]

    def handle_df(self, df) :
        if df is not None :
            df = df.drop_duplicates(subset=['name'], keep='first')
            df.sort_values(by='ranking', ascending=False, inplace=True)
            df = df[['name', 'ranking']].reset_index(drop=True)
            df.index.name = "🏆 순위"
            df = df.rename(columns={'name': '🏕️ 업체명', 'ranking': '⭐ 별점'})
            df.index += 1
            return df
            
        else : return None

    def choice_result_df(self) : 
        return self.handle_df(self.df) if self.df is not None else None

    def get_result(self) : 
        return self.choice_result_df(), self.area, self.direction

    def hadle_price(self) : 
        if self.direction == "전체" : return self.total, self.image_path[0]
        elif self.direction == "가평군" : return self.gapyeong, self.image_path[1]
        elif self.direction == "포천시" : return self.pocheon, self.image_path[2]
        else : return None, None

    def get_price(self):
        df, image_path = self.handle_price()

        if df and image_path is not None :
            keyword = pd.DataFrame(df["importance"][:11]).transpose()

            fig, ax = plt.subplots(figsize=(10, 8))
            df.plot(kind="barh", ax=ax)

            st.image(image_path)
            st.pyplot(fig)
            st.write(keyword)
        else : st.write("충분하지 않다!!!!!!!!!!!!!!!!!!!!!!!!!!")