import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def cutting() : 
    return st.markdown("---")

def set_page() : 
    return st.set_page_config(page_title="for Doksan Seo teacher", page_icon="🏕️", layout="wide", \
                                initial_sidebar_state="expanded")

def set_background():
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/PSeW0pm.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)


def start_background() : 
    return st.markdown("""<style>
                        .main {
                            background-image: url('https://i.imgur.com/idnsDBs.gif');
                            background-size: cover;
                        }
                        </style> """, unsafe_allow_html=True)

def title_ment(area, direction) : 
    return st.markdown(f"<div style='background-color: green; \
                        padding: 10px; color: white; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{area} {direction} \
                        </div>", unsafe_allow_html=True)

def print_direction(direction) : 
    return st.markdown(f"<div style='background-color: green; \
                        padding: 10px; color: white; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{direction} \
                        </div>", unsafe_allow_html=True)

def refactoring() : 
    ment = "사용자 에게 도출될 키워드 리뷰 카운드(%별 수), 업체 사진(image), 객실 정보(info) 등은 한글 화 진행 중 추후 리팩토링.."
    return st.markdown(f"<div style='background-color: white; \
                        padding: 10px; color: green; font-size: 48px;\
                        font-weight: bold; display: inline-block;'> \
                        👉{ment} \
                        </div>", unsafe_allow_html=True)

def sidebar_print_df(df) :
    return st.write("업체가 충분하지 않거나 없습니다.") if len(df) < 10 else st.write("# Best!"), st.dataframe(df.head(), width=600), \
                                                                            st.write("# Worst!"), st.dataframe(df.tail(), width=600)

def total_load():
    total = pd.read_csv("DL_Project/Data_csv/total.csv",index_col =0, encoding="utf-8")

    total_ranking_keyword = pd.DataFrame(total['importance'][:11]).transpose()

    fig, ax = plt.subplots(figsize=(10, 8))
    total.plot(kind='barh', ax=ax)

    return st.image("https://i.imgur.com/qZJvwRB.png"), st.pyplot(fig), st.write(total_ranking_keyword)

def gapyeong_load():
    gapyeong = pd.read_csv("DL_Project/Data_csv/gapyeong.csv",index_col =0, encoding="utf-8")

    gapyeong_ranking_keyword = pd.DataFrame(gapyeong['importance'][:11]).transpose()

    fig1, ax = plt.subplots(figsize=(10, 8))
    gapyeong.plot(kind='barh', ax=ax)

    return st.image("https://i.imgur.com/Bgv83pb.png"), st.pyplot(fig1), st.write(gapyeong_ranking_keyword)

def pocheon_load():
    pocheon = pd.read_csv("DL_Project/Data_csv/pocheon.csv",index_col =0, encoding="utf-8")

    pocheon_ranking_keyword = pd.DataFrame(pocheon['importance'][:11]).transpose()

    fig2, ax = plt.subplots(figsize=(10, 8))
    pocheon.plot(kind='barh', ax=ax)

    return st.image("https://i.imgur.com/QGxbZJa.png"), st.pyplot(fig2), st.write(pocheon_ranking_keyword)