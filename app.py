import streamlit as st
from streamlit_option_menu import option_menu as om
import mysql.connector as ms
import pandas as pd
import main
from random import random
st. set_page_config(layout="wide")
st.header(':seedling: Agri Connect ', divider='green')
st.caption('_powered by Envisioners_')
db=ms.connect(host='localhost',user='root',password='root',database='agriconnect')
cur=db.cursor()

with st.sidebar:

    
    sel=om(
        menu_title=None,
        options=['Home','Sign-up','Log in','Stock Requirements','Purchase','Your Activity'],
        menu_icon='arrow_downward',
        default_index=0,
       # orientation='horizontal',
    )
if sel=='Home':
    main.home()
elif sel=='Sign-up':
    main.register()
elif sel=='Log in':
    main.login()
elif sel=='Stock Requirements':
    main.order()
elif sel=='Purchase':
    main.buy()
elif sel=='Your Activity':
    main.cart()
