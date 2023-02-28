import streamlit as st
from PIL import Image

st.markdown('###  :chart_with_upwards_trend: <font color=#016169>自动化报表（R/PYTHON+EXCEL）</font>',unsafe_allow_html=True)

# import os
# st.write(os.getcwd())
col1, col2,col3= st.columns(3)
with col1:
    st.markdown('#####  <font color=#016169>周度行情数据</font>',unsafe_allow_html=True)
    image = Image.open('./pages/周度行情数据.png')
    st.image(image, caption='每日统计销售接单情况、供应链各环节生产情况，提示是否达标及与目标差距')
    
    st.markdown('----')
    
    st.markdown('#####  <font color=#016169>订单进度表</font>',unsafe_allow_html=True)
    image = Image.open('pages/订单进度表.png')
    st.image(image, caption='收集每笔应收、应付的预计收付日期，得出往后每天预计的资金缺口，便于催促收款及调整生产计划')

    
    

with col2:   
    st.markdown('#####  <font color=#016169>日报表</font>',unsafe_allow_html=True)
    image = Image.open('./pages/日报表.png')
    st.image(image, caption='每日统计销售接单情况、供应链各环节生产情况，提示是否达标及与目标差距')
    
    st.markdown('----')
    
    st.markdown('#####  <font color=#016169>仓差</font>',unsafe_allow_html=True)
    image = Image.open('./pages/仓差.png')
    st.image(image, caption='每日统计销售接单情况、供应链各环节生产情况，提示是否达标及与目标差距')

with col3:
    st.markdown('#####  <font color=#016169>资金收支预算平衡表</font>',unsafe_allow_html=True)
    image = Image.open('pages/资金收支预算平衡表.png')
    st.image(image, caption='收集每笔应收、应付的预计收付日期，得出往后每天预计的资金缺口，便于催促收款及调整生产计划')
    
    st.markdown('----')
    
    st.markdown('#####  <font color=#016169>资金计划表</font>',unsafe_allow_html=True)
    image = Image.open('pages/资金计划表.png')
    st.image(image, caption='收集每笔应收、应付的预计收付日期，得出往后每天预计的资金缺口，便于催促收款及调整生产计划')
