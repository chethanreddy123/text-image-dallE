import streamlit as st
import numpy as np
import plotly.express as px

im = np.random.random((200, 200))

labels = {
        'x':"X Axis Title",
        'y':"X Axis Title" ,
        'color':'Z Label'      
        }
fig = px.imshow(im,aspect='equal',labels = labels)  

st.plotly_chart(fig)