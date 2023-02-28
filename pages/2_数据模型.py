import streamlit as st
from PIL import Image

st.subheader('数据模型')

col1, col2,col3= st.columns(3)
with col1:
    st.write('价格对比模型')
    image = Image.open('./pages/价格对比模型.jpg')
    st.image(image, caption='每日统计销售接单情况、供应链各环节生产情况，提示是否达标及与目标差距')


with col2:   
    st.write('条件计价模型')
    image = Image.open('pages/订单进度表.png')
    st.image(image, caption='收集每笔应收、应付的预计收付日期，得出往后每天预计的资金缺口，便于催促收款及调整生产计划')

with col3:
    st.write('选址模型')
    image = Image.open('pages/资金收支预算平衡表.png')
    st.image(image, caption='收集每笔应收、应付的预计收付日期，得出往后每天预计的资金缺口，便于催促收款及调整生产计划')

