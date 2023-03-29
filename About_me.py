# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:50:28 2023

@author: Administrator
"""

import streamlit as st 

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
st.markdown('### <font color=#016169>潘兆欣</font>',unsafe_allow_html=True)



 
from pyecharts import options as opts

from pyecharts.globals import ThemeType

import streamlit_echarts
#print(streamlit_echarts.__version__)

from pyecharts.charts import Bar,Grid


tab1, tab2, tab3,tab4= st.tabs(["个人简介", "自动化报表","数据模型", "系统设计"])
with tab1:
    st.markdown('#### <font color=#016169>基本信息</font>',unsafe_allow_html=True)
    col1, col2,col3, col4, col5= st.columns([3,4,3,3,3])
    with col1:
        st.markdown('###### :telephone_receiver: 13690646481')
        #st.markdown('#### :telephone_receiver: <font color=#016169>13690646481</font>',unsafe_allow_html=True)
    with col2: 
        st.markdown('###### :e-mail:809251311@qq.com')  
       
    with col3:
        st.markdown('###### :mortar_board:暨南大学')
    with col4:   
        st.markdown('###### :book:经济统计学')
    with col5:   
        st.markdown('###### :round_pushpin:广东 佛山')    
        
        

    # st.markdown('\n')   
    st.markdown('----')
    
    st.markdown('#### <font color=#016169>工作技能</font>',unsafe_allow_html=True)
    col1, col2= st.columns([6,5])
    with col1:
        st.markdown("""
        +  熟练使用办公软件：Excel（公式、数据透视表）、PPT、Word
        +  熟练掌握R、PYTHON：连接数据库、自动化报表、网页爬虫、echarts
        +  能用Endraw、AxureRP9梳理流程图、绘制系统开发界面图
        +  微信公众平台管理、内容编辑、发送推文
        +  通过CET-6，具有良好的英语阅读能力""")
 
    with col2:
        l1=['Endraw','AxureRP9','PPT','PYTHON','R','EXCEL']
        l2=[60,65,70,75,80,85]
        skillbar = (
            Bar()
            .add_xaxis(l1)
            .add_yaxis("",l2,color="#016169")
            .reversal_axis()
            
            .set_series_opts(label_opts=opts.LabelOpts(color="#016169",font_weight="bold",position="right"))
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10,color="#016169",font_weight="bold")),
                
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show= False)),
                # title_opts=opts.TitleOpts(
                #     is_show = False,
                #     #title="工作技能",
                #     #title_textstyle_opts=opts.TextStyleOpts(font_size=22,color="#016169",font_weight="bold")
                #     ),
                legend_opts=opts.LegendOpts(
                    is_show=False
                ),)  
        )
        
        grid=Grid()
        grid.add(skillbar,grid_opts=opts.GridOpts(pos_left='30%',pos_top='8%',pos_bottom='0%'))
        
        streamlit_echarts.st_pyecharts(
            grid,height="125px",
            theme=ThemeType.VINTAGE
        )
        
    st.markdown('----')
    
    st.markdown('#### <font color=#016169>获奖情况</font>',unsafe_allow_html=True)
    st.markdown('###### 2017-2018 暨南大学优秀学生奖学金×2',unsafe_allow_html=True)
    
with tab2:
   st.markdown('####  R/PYTHON + EXCEL/PPT')
   col1, col2,col3= st.columns(3)
   with col1:
       st.markdown('#####  <font color=#016169>周度行情数据</font>',unsafe_allow_html=True)
       image = './pages/周度行情数据.png'
       st.image(image,caption='')
       st.markdown("""
                   每周定期从网页**采集行业数据**（运价指数、汇率、镍价、铁矿石、铬铁价、各牌号不锈钢价格及社会库存），
                   自动编制图表并**输出PPT和图片**，以便把握行业波动，为公司**制定采购和销售策略**提供数据支持
                   """,unsafe_allow_html=True)
       
       st.markdown('----')
       
       st.markdown('#####  <font color=#016169>订单进度表</font>',unsafe_allow_html=True)
       image = 'pages/订单进度表.png'
       st.image(image, caption='')
       st.markdown("""
                    每天定期从不同岗位**收集并读取工作表**（销售明细、采购、配货、排产、验收、回款），
                    以销售订单为单位**输出各环节进度**，以便业务员向客户同步订单进度、供应链推进下一环节、财务落实应收，
                    完成订单的**全周期监管**
                    """,unsafe_allow_html=True)
       
       

   with col2:   
       st.markdown('#####  <font color=#016169>日报表</font>',unsafe_allow_html=True)
       image = './pages/日报表.png'
       st.image(image, caption='')
       st.markdown("""
                    每日统计销售接单情况、供应链各环节生产情况，
                    提示是否达标及与**目标差距**,
                    让管理员每日**监控公司运营**情况
                    """,unsafe_allow_html=True)
                    
       st.markdown('----')
       
       st.markdown('#####  <font color=#016169>仓差</font>',unsafe_allow_html=True)
       image = './pages/仓差.png'
       st.image(image, caption='')
       st.markdown("""
                    每日统计各牌号不锈钢库存及采购基价、销售未交货及销售基价，
                    提示**仓差情况**【可售库存数+在途可售库存（已订货未交货）-未采购量】,
                    让操盘手结合价格趋势判断采购及销售策略和时机
                    """,unsafe_allow_html=True)
                    
                
   with col3:
       st.markdown('#####  <font color=#016169>资金收支预算平衡表</font>',unsafe_allow_html=True)
       image = 'pages/资金收支预算平衡表.png'
       st.image(image, caption='')
       st.markdown("""
                   对于**资金紧张**型企业，资金安排者可以关注**资金积压**点和资金缺口，尽快疏通调度。\n
                    【流动资产】银行存款、预付账款、应收账款（货款+订金）、存货、未处理采购客诉\n
                    【流动负债】应付账款（货款+订金）、预收账款、其他应付款、未处理销售客诉
                    """,unsafe_allow_html=True)
                    
       st.markdown('----')
       
       st.markdown('#####  <font color=#016169>资金计划表</font>',unsafe_allow_html=True)
       image = 'pages/资金计划表.png'
       st.image(image, caption='')
       st.markdown("""
                    收集每笔应收、应付的预计收付日期，得出往后每天预计的资金缺口，便于催促收款及调整生产计划
                    """,unsafe_allow_html=True)
                    
with tab3:
   col1, col2= st.columns(2)
   with col1:
       st.markdown('#####  <font color=#016169>价格对比模型</font>',unsafe_allow_html=True)
       image = './pages/价格对比模型.jpg'
       st.image(image, caption='')
       st.markdown("""
                    已预设各产地的加价逻辑，采购员每天只需录入实时**基础价格**即可得出各产地各规格的产品价格，
                    方便其挑选**价格最优**的产地，节约采购成本，提高订单利润。
                    """,unsafe_allow_html=True)
                    

   with col2:  
       st.markdown('#####  <font color=#016169>条件计价模型</font>',unsafe_allow_html=True)
       image = 'pages/条件计价模型.png'
       st.image(image, caption='')
       st.markdown("""
                    已预设各工序的加价逻辑，业务员每天只需录入定制**订单要求**即可得出产品价格，
                    方便其快速计算价格并提供给客户，提高订单**转化率**。
                    """,unsafe_allow_html=True)
                    
   


with tab4:
    col1, col2= st.columns(2)
    with col1:
        st.markdown("""#####  流程管理、需求文档、测试、优化 (Endraw + AxureRP9)""")
        st.markdown("""#####  对接信息部同事提起功能需求、日常bug反馈处理及优化方案""")
        
        st.markdown("""
                    #####  <font color=#016169>*报价系统</font>
                    ###### 项目描述：公司对接客户的阵地，提高报价效率和客户体验，为供应链提供统一订单数据
                    
                   """,unsafe_allow_html=True)
        st.markdown("""  
                    完成4版H5/小程序重构、上线、维护、迭代\n
                    + 负责工作：梳理定制化产品报价逻辑并转化为公式、优化合同模板（电子章电子签名）、建立合同审批、修改、取消流程\n
                    + 模块包括：每日基价、现货库存、定制产品报价、购物车、地址管理、合同列表
                    """,unsafe_allow_html=True)
        
        st.markdown("---")
            
        st.markdown("""
                    #####  <font color=#016169>*供应链系统</font>
                    ###### 项目描述：公司内部高效运转的关键，自动生成凭证单据，形成岗位之间数据流转闭环
                    
                    """,unsafe_allow_html=True)
        st.markdown("""  
                    7个月完成33个界面上线\n
                    + 负责工作：梳理供应链各岗位作业表格、单据凭证、字段对应关系、数据流动方向、单据审批流程及开发进度跟进\n
                    + 模块包括：销售订单、采购订单、采购报货明细、库存管理（调仓、转货）、
                            配货、排产（排产模型：自动生成工序描述）、成品验收、交货管理、客诉管理（采购+销售）、
                            支出申请、财务收款单、款项分配、财务应收应付报表
                    
                    """,unsafe_allow_html=True)
                    
        st.markdown("---")

    with col2:
        image = 'pages/报货明细界面设计图.png'
        st.image(image, caption='基于Antdesign的报货明细界面设计图')
        
        image = 'pages/供应链系统.png'
        st.image(image, caption='系统架构图')


     
     
     