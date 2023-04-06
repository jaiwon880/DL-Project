import streamlit as st
from ChoiceArea import GetSideBar
st.set_page_config(page_title="DL", layout="wide")

def test() : 
    return True if GetSideBar().result_sidebar() is None else False

def user_interface():
    st.title("뼈대 작업 중...")

    st.subheader("연결 성공 여부는? : ", test())

    image = ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]
    
    containers = [st.container() for i in range(len(image))]

    for i in range(len(image)) :
        with st.expander(f"사진_{i+1}"):
            st.image(image[i])

    # for i in range(len(image)) :
    #     with containers[i] : 
    #         st.image(image[i], width = 700)