import streamlit as st
from PIL import Image
import wave
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

import altair as alt

import re

img_logo = Image.open('logo.png')
white_img = Image.open('white.PNG')

header = st.container()
play = st.container()
kpi = st.container()

st.markdown("""
<style>
.JTALK_1 {font-size:40px !important; font-family: arial black;color: #B41E3C}
.JTALK_2 {font-size:40px !important; font-family: arial black;color: #002060}
.big-font {font-size:30px !important; font-family: arial black;color: #002060}
.medium-font {font-size:18px !important; font-family: arial black;color: #002060}
.small-font {font-size:18px !important; font-family: arial;color: #000000}
.med {font-size: 18px !important; font-family: arial black;color: #000000}
</style>
""", unsafe_allow_html=True)

st.sidebar.image(img_logo, width = 180)
example = st.sidebar.selectbox("Select a file ", ['', 'Email A', 'Email B', 'Email C', 'Email D'])

with header:
    st.markdown('<div style="text-align:center"><span class="JTALK_1">J</span><span class="JTALK_2">AKALA </span></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center"><p class="big-font">Automatic email sorting</p></div>', unsafe_allow_html=True)  
    st.write('\n\n\n')



df1 = pd.DataFrame(np.array([['Transfer', '0.88'], ['Sales Process', '0.09'], ['Change Offer', '0.03']]), columns=['class', 'probability'], index = None)
df2 = pd.DataFrame(np.array([['Name Surname', 'BXXX RXXX']]), columns = ['personal data', 'values'])

df3 = pd.DataFrame(np.array([['Proved Payment', '0.83'], ['Payment Method', '0.12'], ['Payment Extension', '0.05']]), columns = ['class', 'probability'], index = None)
df4 = pd.DataFrame(np.array([['Numero fattura', '0000002160085673']]), columns = ['personal data', 'values'])

df5 = pd.DataFrame(np.array([['Request Claim', '0.97'], ['Refund', '0.02'], ['Change Offer', '0.01']]), columns = ['class', 'probability'], index = None)
df6 = pd.DataFrame(np.array([['Numero pratica', '03299532'], ['Name Surname', 'FXXX GXXX'], ['Address', 'Via degli Albanesi 11/17 16148 Genova']]), columns = ['personal data', 'values'])

df7 = pd.DataFrame(np.array([['Refund', '0.68'], ['Request Claim', '0.30'], ['Proved Payment', '0.02']]), columns = ['classe', 'probabilità'], index = None)
df8 = pd.DataFrame(np.array([['Bill number', '502001905884'], ['Name Surname', 'RXXX FXXX'], ['id account', '10102553043'], ['Contract code', '00910012']]), columns = ['personal data', 'values'])



## esempio A

if example == 'Email A':

    st.write('\n\n\n')
    but1, but2, but3, but_4, but_5 = st.columns(5)

    if not (but3.button("RUN")):
        st.image('AA.PNG')

    else:
        gif_runner = st.image('https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif')
        time.sleep(3)
        gif_runner.empty()

        st.image('AA1.PNG')
        st.write('\n\n\n')
        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)

        kpi1_col, kpi2_col = st.columns(2)
    
        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Transfer </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df1)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Personal information extracted </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df2)  
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Recycle: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="med"> <b> NO </b></p></div>', unsafe_allow_html=True)


        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Send to: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Transfer team </b></p></div>', unsafe_allow_html=True)
        



## esempio  B

if example == 'Email B':

    st.write('\n\n\n')
    but1, but2, but3, but4, but5 = st.columns(5)

    if not (but3.button("RUN")):
            st.image('BB.PNG')

    else:
        gif_runner2 = st.image('https://media.giphy.com/media/l46Cq6Bro9CsP149q/giphy.gif')
        time.sleep(3)
        gif_runner2.empty()

        st.image('BB1.PNG')
        st.write('\n\n\n')
        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)

        kpi1_col, kpi2_col = st.columns(2)

        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Proved Payment </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df3)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Personal information extracted </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df4)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Recycle: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="med"> <b> NO </b></p></div>', unsafe_allow_html=True)

        
        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Send to: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Proved Payment team </b></p></div>', unsafe_allow_html=True)



## email C

if example == 'Email C':
    
    st.write('\n\n\n')
    but1, but2, but3, but4, but5 = st.columns(5)

    if not (but3.button("RUN")):
        st.image('CC.PNG')

    else:
        gif_runner = st.image('https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif')
        time.sleep(3)
        gif_runner.empty()

        st.image('CC1.PNG')
        st.write('\n\n\n')
        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)
        kpi1_col, kpi2_col = st.columns(2)

        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Request Claim </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df5)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Personal information extracted </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df6)
        kpi1_col.markdown('<div style="text-align:right"><p class="medium-font"> <b> Recycle: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> SI </b></p></div>', unsafe_allow_html=True)

        
        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Send to: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Request Claim team </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        original2 = Image.open('warning.PNG')
        kpi2_col.image(original2, width = 80)




if example == 'Email D':
    
    st.write('\n\n\n')
    but1, but2, but3, but4, but5 = st.columns(5)

    if not (but3.button("RUN")):
        st.image('DD.PNG')

    else:
        gif_runner = st.image('https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif')
        time.sleep(3)
        gif_runner.empty()

        st.image('DD1.PNG')
        st.write('\n\n\n')
        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)
        kpi1_col, kpi2_col = st.columns(2)

        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Refund </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df7)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Informazioni personali estratte </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df8)
        kpi1_col.markdown('<div style="text-align:right"><p class="medium-font"> <b> Presenza ricicli: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> SI </b></p></div>', unsafe_allow_html=True)

        
        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Inviata a: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Refund team </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        original2 = Image.open('warning.PNG')
        kpi2_col.image(original2, width = 70)
 
