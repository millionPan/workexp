# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:50:28 2023

@author: Administrator
"""

import streamlit as st
import numpy as np
import pandas as pd
import datetime
import os

#import streamlit.components.v1 as components
# from pyecharts.charts import *
# from pyecharts.globals import ThemeType
# from pyecharts import options as opts
# from pyecharts.commons.utils import JsCode

#全局配置
st.set_page_config(
    page_title="million",    #页面标题
    page_icon=":rainbow:",        #icon:emoji":rainbow:"
    layout="wide",                #页面布局
    initial_sidebar_state="auto"  #侧边栏
)


###标题
st.title('行情数据分享 ')

col1, col2,col3, col4= st.columns([3,4,3,3])
with col1:
    st.markdown('#### :telephone_receiver: 13690646481')
    #st.markdown('#### :telephone_receiver: <font color=#016169>13690646481</font>',unsafe_allow_html=True)
with col2: 
    st.markdown('#### :e-mail:809251311@qq.com')  
   
with col3:
    st.markdown('#### :mortar_board:暨南大学')
with col4:   
    st.markdown('#### :book:经济统计学')
    
    
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

import streamlit_echarts



fn = """
    function(params) {
        if(params.name.length == 1)
            return '';
        return params.name + ' : ' + params.value ;
    }
    """


def new_label_opts():
    return opts.LabelOpts(formatter=JsCode(fn), position="center",color="#016169")
def new_Tooltip_opts():
    return opts.TooltipOpts(formatter=JsCode(fn))

skillpie = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(["R ", "1"], [80, 20])],
        center=["25%", "25%"],
        radius=[35, 60],
        label_opts=new_label_opts(),
       
    )
    .add(
        "",
        [list(z) for z in zip(["PYTHON", "2"], [60, 40])],
        center=["50%", "25%"],
        radius=[35, 60],
        label_opts=new_label_opts(),
        
    )
    .add(
        "",
        [list(z) for z in zip(["AxureRP", "3"], [60, 40])],
        center=["75%", "25%"],
        radius=[35, 60],
        label_opts=new_label_opts(),
        
    )

    .add(
        "",
        [list(z) for z in zip(["PPT", "4"], [75, 25])],
        center=["25%", "75%"],
        radius=[35, 60],
        label_opts=new_label_opts(),
       
    )
    .add(
        "",
        [list(z) for z in zip(["EXCEL", "5"], [85, 15])],
        center=["50%", "75%"],
        radius=[35, 60],
        label_opts=new_label_opts(), 
       
    )
    .add(
        "",
        [list(z) for z in zip(["Endraw", "6"], [85, 15])],
        center=["75%", "75%"],
        radius=[35, 60],
        label_opts=new_label_opts(), 
       
    )
    .set_colors([ "#016169","#F2F2F2"])
    
    .set_global_opts(
        title_opts=opts.TitleOpts(title="software"),
        tooltip_opts=new_Tooltip_opts(),
        legend_opts=opts.LegendOpts(
            is_show=False
        ),
    )

)

streamlit_echarts.st_pyecharts(
    skillpie,
    theme=ThemeType.VINTAGE
)





     
     
     