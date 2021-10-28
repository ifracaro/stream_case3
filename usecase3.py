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
    st.markdown('<div style="text-align:center"><span class="JTALK_1">J</span><span class="JTALK_2">AKALA // per Iren</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center"><p class="big-font">Smistamento automatico di email</p></div>', unsafe_allow_html=True)  
    st.write('\n\n\n')



df1 = pd.DataFrame(np.array([['Voltura', '0.68'], ['Sales Process', '0.31'], ['Change Offer', '0.01']]), columns=['classe', 'probabilità'], index = None)
df2 = pd.DataFrame(np.array([['Nome Cognome', 'Bruna Rossi']]), columns = ['dati personali', 'valori'])

df3 = pd.DataFrame(np.array([['Proved Payment', '0.83'], ['Payment Method', '0.12'], ['Payment Extension', '0.05']]), columns = ['classe', 'probabilità'], index = None)
df4 = pd.DataFrame(np.array([['Numero fattura', '0000002160085673']]), columns = ['dati personali', 'valori'])

df5 = pd.DataFrame(np.array([['Request Claim', '0.97'], ['Refund', '0.02'], ['Change Offer', '0.01']]), columns = ['classe', 'probabilità'], index = None)
df6 = pd.DataFrame(np.array([['Numero pratica', '03299532'], ['Nome Cognome', 'Franca Gallina'], ['Indirizzo', 'Via degli Albanesi 11/17 16148 Genova']]), columns = ['dati personali', 'valori'])

df7 = pd.DataFrame(np.array([['Refund', '0.68'], ['Request Claim', '0.30'], ['Proved Payment', '0.02']]), columns = ['classe', 'probabilità'], index = None)
df8 = pd.DataFrame(np.array([['Numero fattura', '502001905884'], ['Nome Cognome', 'Rebolino Federica'], ['id account', '10102553043'], ['codice contratto', '00910012']]), columns = ['dati personali', 'valori'])



## esempio A

if example == 'Email A':

    st.write('\n\n\n')
    st.write("DATA RICEZIONE EMAIL: '2021-02-06'")
    st.write('Buongiorno,  vi rimando il documento compilato che mi avete mandato su mia richiesta allo scopo di richiedere il cambio di intestazione per fatturazione TARI a Bruna Rossi (mia mamma). Mio papà è deceduto in dicembre quindi mia mamma risulta intestataria delle bollette e unica domiciliata in casa. \n\nPer qualsiasi richiesta ulteriore vi chiedo di scrivere a questa mail. \n\nCordiali saluti, \n\nStefania Contesini')

    but1, but2, but3, but_4, but_5 = st.columns(5)
    if (but3.button("RUN")):
        gif_runner = st.image('https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif')
        time.sleep(3)
        gif_runner.empty()
        st.write('\n\n\n')
        
        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)

        kpi1_col, kpi2_col = st.columns(2)
    
        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Voltura </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df1)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Informazioni personali estratte </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df2)
        
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Presenza ricicli: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="med"> <b> NO </b></p></div>', unsafe_allow_html=True)

       # kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
      #  kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
       # kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Inviata a: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Voltura team </b></p></div>', unsafe_allow_html=True)
        



## esempio  B

if example == 'Email B':

    st.write('\n\n\n')
    st.write("DATA RICEZIONE EMAIL: '2021-02-26'")
    st.write('Buongiorno,\n\nho effettuato un bonifico tramite home banking della fattura  n°0000002160085673 in data 05-02-2021.\nAd oggi sul portale di Iren questa bolletta risulta ancora da pagare.\nPotete controllare?\n\n\n\n\nGrazie.\n\nCordiali saluti,\n\nChiara Belicchi')
    

    but1, but2, but3, but4, but5 = st.columns(5 )
    if (but3.button("RUN")):
        gif_runner2 = st.image('https://media.giphy.com/media/l46Cq6Bro9CsP149q/giphy.gif')
        time.sleep(3)
        gif_runner2.empty()
        st.write('\n\n\n')
        

        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)
        kpi1_col, kpi2_col = st.columns(2)

        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Proved Payment </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df3)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Informazioni personali estratte </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df4)

        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Presenza ricicli: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="med"> <b> NO </b></p></div>', unsafe_allow_html=True)

        
        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
       # kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Inviata a: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Proved Payment team </b></p></div>', unsafe_allow_html=True)



## email C

if example == 'Email C':
    
    st.write('\n\n\n')
    st.write("DATA RICEZIONE EMAIL: '2021-02-25'")
    st.write("Ad oggi, dopo l'invio di tre mail, non ho avuto alcun riscontro sull'avanzamento della pratica che faticosamente mi è stata identificata dal call center come 03299532.\nReitero la richiesta di essere contattato al più presto per comprendere come procedere e in che tempi.\n\nSaluti, \n\nCarlo Bima\n\n---------- Messaggio originale ---------- \n\nDa: carlo.bima@libero.it\n\nA: 'servizioclienti@gruppoiren.it' <servizioclienti@gruppoiren.it>\n\nData: 13/01/2021 13:03\n\nOggetto: Fwd: Franca Gallina - contratto Via degli Albanesi 11/17 16148 Genova\n\n\n\nInvio alla vostra attenzione per la terza volta la documentazione. Dal 5 gennaio che ho ricevuto mail di presa in carico dalla casella postale clienti, non ho avuto alcun riscontro e solo risposte molto lacunose dal vostro call center.\n\nTrovo la situazione scandalosa.\n\nAl momento devo far rientrare mia madre di 92 anni dall'ospedale e sono in enorme difficoltà a causa di IREN per l'assoluta incertezza sui tempi di attivazione della fornitura.\n\nVi chiedo di procedere con la pratica e di darmi un pronto riscontro appena possibile.\n\nCordiali saluti,\n\nCarlo Bima")

    but1, but2, but3, but4, but5 = st.columns(5)
    if (but3.button("RUN")):
        gif_runner = st.image('https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif')
        time.sleep(3)
        gif_runner.empty()
        st.write('\n\n\n')
 
        
        st.markdown('<div style="text-align:left"><p class="big-font">Results</p></div>', unsafe_allow_html=True)
        kpi1_col, kpi2_col = st.columns(2)

        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> Request Claim </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font">  Scoring table </div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df5)
        kpi1_col.markdown('<div style="text-align:left"><p class="medium-font"> <b> Informazioni personali estratte </b></p></div>', unsafe_allow_html=True)
        kpi1_col.dataframe(df6)

        kpi1_col.markdown('<div style="text-align:right"><p class="medium-font"> <b> Presenza ricicli: </b></p></div>', unsafe_allow_html=True)
        kpi1_col.markdown('<div style="text-align:right"><p class="med"> <b> SI </b></p></div>', unsafe_allow_html=True)

        
        original1 = Image.open('MicrosoftTeams-image.png')
        kpi2_col.image(original1, width=40)
       # kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Inviata a: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Request Claim team </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
       # kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        original2 = Image.open('warning.PNG')
        kpi2_col.image(original2, width = 80)




if example == 'Email D':
    
    st.write('\n\n\n')
    st.write("DATA RICEZIONE EMAIL: '2021-05-01'")
    st.write("Buongiorno,\n\nVi inoltro nuovamente mail, già inviatavi in data 13 aprile e della quale non ho ricevuto, come di consueto, la risposta automatica con l’indicazione del nr pratica assegnato. In attesa di vostro cortese riscontro, porgo cordiali saluti.\n\nFederica Rebolino\n\nmartedì 13 aprile 2021, 09:03 +0200 da Roberto e Federica <rebo.ricc@libero.it>:\n\nBuongiorno,\n\nVi riporto i dati per ottenere il rimborso di € 43,29 relativi alla fattura nr 502001905884 del 12/10/2020 scadenza il 2/11/2020, intestata a REBOLINO FEDERICA, nr cliente 10102553043, contratto nr. 00910012, in quanto pagata due volte. In attesa di vostro riscontro, porgo cordiali saluti.\n\nFederica Rebolino")

    but1, but2, but3, but4, but5 = st.columns(5)
    if (but3.button("RUN")):
        gif_runner = st.image('https://media.giphy.com/media/Qw4X3Fsf0N1VqFFUiBi/giphy.gif')
        time.sleep(3)
        gif_runner.empty()
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
       # kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="medium-font"> <b> Inviata a: </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown('<div style="text-align:center"><p class="med"> <b> Refund team </b></p></div>', unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        #kpi2_col.markdown("<p>&nbsp;</p>",  unsafe_allow_html=True)
        original2 = Image.open('warning.PNG')
        kpi2_col.image(original2, width = 70)
 
