# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from untilTool import Tool
import wx.xrc
import clipboard

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
    #定义工具类
    tool = Tool()
    #定义kill胆码列表
    killBaiWei_list = []
    killShiWei_list = []
    killGeWei_list = []
    #kill后三和尾列表
    kill_HouSanHeWei_list = []
    #kill后二和尾列表
    kill_HouErHeWei_list = []
    #胆码列表
    danMa_list = []
    #kill 二码
    kill_ErMa_Dict = []
    #kill 三码
    kill_SanMa_List = []
    ertongyishsang_boot = False
    #kill 012
    kill_012_Dict = []
    #大底拼接
    daDiPinJie_Dict = []
    daDiPinJie_flot = False
    daDiPinJie_num = 2
    
    #至少两胆
    liangDan = False
    #保留头尾
    baoLiuTouWei = False
    #保留头尾双
    baoLiuTouWei_s = False
    #保留头尾双
    baoLiuShuang = False
    #kill AAAAA
    AAAAA_boot = False
    AAABB_boot = False
    baozhi_boot = False
    #容错
    rongcuo_1_3_boot = False
    rongcuo_1_4_boot = False
    rongcuo_1_5_boot = False
    #容错列表
    rongcuo_wang = []
    rongcuo_qian = []
    rongcuo_bai = []
    rongcuo_shi = []
    rongcuo_ge = []
    #和值
    kill_hezhi_list = []
    #结果值
    result_list = []
    #转换成3码
    sanma_bool = False
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 839,634 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        gbSizer6 = wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        
        gb_DanMaBai = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_DanMaBai = wx.StaticText( self, wx.ID_ANY, u"杀百位", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_DanMaBai.Wrap( -1 )
        self.m_DanMaBai.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_DanMaBai.SetMinSize( wx.Size( 60,-1 ) )
        
        gb_DanMaBai.Add( self.m_DanMaBai, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_bai_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaBai.Add( self.m_bai_checkBox_9, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( gb_DanMaBai, 0, wx.EXPAND, 5 )
        
        gb_DanMaShi = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_DanMaShi = wx.StaticText( self, wx.ID_ANY, u"杀十位", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_DanMaShi.Wrap( -1 )
        self.m_DanMaShi.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_DanMaShi.SetMinSize( wx.Size( 60,-1 ) )
        
        gb_DanMaShi.Add( self.m_DanMaShi, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_shi_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaShi.Add( self.m_shi_checkBox_9, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( gb_DanMaShi, 0, wx.EXPAND, 5 )
        
        gb_DanMaGe = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_DanMaGe = wx.StaticText( self, wx.ID_ANY, u"杀个位", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_DanMaGe.Wrap( -1 )
        self.m_DanMaGe.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_DanMaGe.SetMinSize( wx.Size( 60,-1 ) )
        
        gb_DanMaGe.Add( self.m_DanMaGe, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_ge_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_DanMaGe.Add( self.m_ge_checkBox_9, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( gb_DanMaGe, 0, wx.EXPAND, 5 )
        
        self.m_cline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer22.Add( self.m_cline5, 0, wx.EXPAND |wx.ALL, 5 )
        
        gb_HouSanHeWei = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_HouSanHeWei = wx.StaticText( self, wx.ID_ANY, u"后三杀和尾", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_HouSanHeWei.Wrap( -1 )
        self.m_HouSanHeWei.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_HouSanHeWei.SetMinSize( wx.Size( 60,-1 ) )
        
        gb_HouSanHeWei.Add( self.m_HouSanHeWei, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_HouSanWei_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_HouSanHeWei.Add( self.m_HouSanWei_checkBox_9, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( gb_HouSanHeWei, 0, wx.EXPAND, 5 )
        
        b_HouErHeiWei = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_HouErHeWei = wx.StaticText( self, wx.ID_ANY, u"后二杀和尾", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_HouErHeWei.Wrap( -1 )
        self.m_HouErHeWei.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_HouErHeiWei.Add( self.m_HouErHeWei, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_HouErWei_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_HouErHeiWei.Add( self.m_HouErWei_checkBox_9, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_HouErHeiWei, 0, wx.EXPAND, 5 )
        
        self.m_cline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer22.Add( self.m_cline6, 0, wx.EXPAND |wx.ALL, 5 )
        
        b_DanMa = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_DanMa = wx.StaticText( self, wx.ID_ANY, u"胆码", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_DanMa.Wrap( -1 )
        self.m_DanMa.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_DanMa.SetMinSize( wx.Size( 60,-1 ) )
        
        b_DanMa.Add( self.m_DanMa, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_0 = wx.CheckBox( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_0, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_1, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_2, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_3, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_4, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_5, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_6, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_7, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_8, 0, wx.ALL, 5 )
        
        self.m_DanMa_checkBox_9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_DanMa.Add( self.m_DanMa_checkBox_9, 0, wx.ALL, 5 )
        
        self.m_ZhiShaoLianMa_checkBox = wx.CheckBox( self, wx.ID_ANY, u"至少两码", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_ZhiShaoLianMa_checkBox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
        
        b_DanMa.Add( self.m_ZhiShaoLianMa_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_DanMa, 0, wx.EXPAND, 5 )
        
        self.m_cline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer22.Add( self.m_cline7, 0, wx.EXPAND |wx.ALL, 5 )
        
        b_kill_ErMa1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_BaoLiuTouWei_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保留头尾", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_BaoLiuTouWei_checkBox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_kill_ErMa1.Add( self.m_BaoLiuTouWei_checkBox, 0, wx.ALL, 5 )
        
        self.m_BaoLiuTouWeiSuan_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保留头尾双", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_BaoLiuTouWeiSuan_checkBox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_kill_ErMa1.Add( self.m_BaoLiuTouWeiSuan_checkBox, 0, wx.ALL, 5 )

        self.m_BaoLiushuang_checkBox = wx.CheckBox( self, wx.ID_ANY, u"保留双", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_BaoLiushuang_checkBox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_kill_ErMa1.Add( self.m_BaoLiushuang_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_kill_ErMa1, 0, wx.EXPAND, 5 )
        
        b_kill_ErMa2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_Kill_ErMa = wx.StaticText( self, wx.ID_ANY, u"杀二码", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_Kill_ErMa.Wrap( -1 )
        self.m_Kill_ErMa.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_Kill_ErMa.SetMinSize( wx.Size( 60,-1 ) )
        
        b_kill_ErMa2.Add( self.m_Kill_ErMa, 0, wx.ALL, 5 )
        
        self.m_Kill_ErMa_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Kill_ErMa_textCtrl.SetMinSize( wx.Size( 150,-1 ) )
        
        b_kill_ErMa2.Add( self.m_Kill_ErMa_textCtrl, 0, wx.ALL, 5 )

        self.m_Kill_SanMa = wx.StaticText( self, wx.ID_ANY, u"杀三码", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Kill_SanMa.Wrap( -1 )
        self.m_Kill_SanMa.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_Kill_SanMa.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        
        b_kill_ErMa2.Add( self.m_Kill_SanMa, 0, wx.ALL, 5 )

        self.m_Kill_SanMa_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Kill_SanMa_textCtrl.SetMinSize( wx.Size( 150,-1 ) )
        
        b_kill_ErMa2.Add( self.m_Kill_SanMa_textCtrl, 0, wx.ALL, 5 )

        self.m_ertong_checkBox = wx.CheckBox( self, wx.ID_ANY, u"二同以上", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_kill_ErMa2.Add( self.m_ertong_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_kill_ErMa2, 0, wx.EXPAND, 5 )
        
        b_kill_012 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_Kill_012_Text = wx.StaticText( self, wx.ID_ANY, u"杀012", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_Kill_012_Text.Wrap( -1 )
        self.m_Kill_012_Text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_Kill_012_Text.SetMinSize( wx.Size( 60,-1 ) )
        
        b_kill_012.Add( self.m_Kill_012_Text, 0, wx.ALL, 5 )
        
        self.m_Kill_012_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_Kill_012_textCtrl.SetMinSize( wx.Size( 400,-1 ) )
        
        b_kill_012.Add( self.m_Kill_012_textCtrl, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_kill_012, 0, wx.EXPAND, 5 )
        
        b_kill_hezhi = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_kill_hezhi_Text = wx.StaticText( self, wx.ID_ANY, u"杀和值", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_kill_hezhi_Text.Wrap( -1 )
        self.m_kill_hezhi_Text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_kill_hezhi_Text.SetMinSize( wx.Size( 60,-1 ) )
        
        b_kill_hezhi.Add( self.m_kill_hezhi_Text, 0, wx.ALL, 5 )
        
        self.m_kill_hezhi_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_kill_hezhi_textCtrl.SetMinSize( wx.Size( 400,-1 ) )
        
        b_kill_hezhi.Add( self.m_kill_hezhi_textCtrl, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_kill_hezhi, 0, wx.EXPAND, 5 )
        
        self.m_cline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer22.Add( self.m_cline10, 0, wx.EXPAND |wx.ALL, 5 )
        
        b_kill_xingtai = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_kill_xingtai_Text = wx.StaticText( self, wx.ID_ANY, u"杀形态", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_kill_xingtai_Text.Wrap( -1 )
        self.m_kill_xingtai_Text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_kill_xingtai_Text.SetMinSize( wx.Size( 60,-1 ) )
        
        b_kill_xingtai.Add( self.m_kill_xingtai_Text, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_kill_xingtai, 0, wx.EXPAND, 5 )
        
        b_kill_xingtai_box = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_kill_baozhi_checkBox = wx.CheckBox( self, wx.ID_ANY, u"杀豹子", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_kill_xingtai_box.Add( self.m_kill_baozhi_checkBox, 0, wx.ALL, 5 )
        
        self.m_4lian_checkBox = wx.CheckBox( self, wx.ID_ANY, u"AAAAA", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_kill_xingtai_box.Add( self.m_4lian_checkBox, 0, wx.ALL, 5 )
        
        self.m_kill_santong_checkBox = wx.CheckBox( self, wx.ID_ANY, u"AAABB", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_kill_xingtai_box.Add( self.m_kill_santong_checkBox, 0, wx.ALL, 5 )

        self.m_sanma_checkBox = wx.CheckBox( self, wx.ID_ANY, u"三码", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_kill_xingtai_box.Add( self.m_sanma_checkBox, 0, wx.ALL, 5 )
        
        self.m_ch_erma_checkBox84 = wx.CheckBox( self, wx.ID_ANY, u"转二码", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_kill_xingtai_box.Add( self.m_ch_erma_checkBox84, 0, wx.ALL, 5 )
        
        bSizer22.Add( b_kill_xingtai_box, 0, wx.EXPAND, 5 )
        
        gb_BUTTON = wx.BoxSizer( wx.HORIZONTAL )
        
        self.gb_SuoShui_BUTTON = wx.Button( self, wx.ID_ANY, u"缩水", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.gb_SuoShui_BUTTON, 0, wx.ALL, 5 )
        
        self.m_cp_button = wx.Button( self, wx.ID_ANY, u"复制", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.m_cp_button, 0, wx.ALL, 5 )
        
        self.m_clean_button = wx.Button( self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.m_clean_button, 0, wx.ALL, 5 )

        self.m_ZhuShuDatatextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gb_BUTTON.Add( self.m_ZhuShuDatatextCtrl, 0, wx.ALL, 5 )
        
        bSizer22.Add( gb_BUTTON, 0, wx.EXPAND, 5 )
        
        b_Result = wx.BoxSizer( wx.VERTICAL )
        
        self.m_result_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_result_textCtrl.SetMinSize( wx.Size( 500,150 ) )
        
        b_Result.Add( self.m_result_textCtrl, 0, wx.ALL, 5 )
        
        
        bSizer22.Add( b_Result, 1, wx.EXPAND, 5 )
        
        
        gbSizer6.Add( bSizer22, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
        
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer33 = wx.BoxSizer( wx.VERTICAL )
        
        b_rongcuo = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rongcuo_13_checkBox = wx.CheckBox( self, wx.ID_ANY, u"1-3容错", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo.Add( self.m_rongcuo_13_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_14_checkBox = wx.CheckBox( self, wx.ID_ANY, u"1-4容错", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo.Add( self.m_rongcuo_14_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_15_checkBox = wx.CheckBox( self, wx.ID_ANY, u"1-5容错", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo.Add( self.m_rongcuo_15_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer33.Add( b_rongcuo, 0, wx.EXPAND, 5 )
        
        self.m_cline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer33.Add( self.m_cline8, 0, wx.EXPAND|wx.ALL, 5 )
        
        b_rongcuo_wan = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rongcuo_wang_da_checkBox = wx.CheckBox( self, wx.ID_ANY, u"万位大", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_wan.Add( self.m_rongcuo_wang_da_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_wang_xiao_checkBox = wx.CheckBox( self, wx.ID_ANY, u"万位小", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_wan.Add( self.m_rongcuo_wang_xiao_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer33.Add( b_rongcuo_wan, 0, wx.EXPAND, 5 )
        
        b_rongcuo_qian = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rongcuo_qian_da_checkBox = wx.CheckBox( self, wx.ID_ANY, u"千位大", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_qian.Add( self.m_rongcuo_qian_da_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_qian_xiao_checkBox = wx.CheckBox( self, wx.ID_ANY, u"千位小", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_qian.Add( self.m_rongcuo_qian_xiao_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer33.Add( b_rongcuo_qian, 0, wx.EXPAND, 5 )
        
        b_rongcuo_bai = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rongcuo_bai_da_checkBox = wx.CheckBox( self, wx.ID_ANY, u"百位大", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_bai.Add( self.m_rongcuo_bai_da_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_bai_xiao_checkBox = wx.CheckBox( self, wx.ID_ANY, u"百位小", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_bai.Add( self.m_rongcuo_bai_xiao_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer33.Add( b_rongcuo_bai, 0, wx.EXPAND, 5 )
        
        b_rongcuo_shi = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rongcuo_shi_da_checkBox = wx.CheckBox( self, wx.ID_ANY, u"十位大", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_shi.Add( self.m_rongcuo_shi_da_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_shi_xiao_checkBox = wx.CheckBox( self, wx.ID_ANY, u"十位小", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_shi.Add( self.m_rongcuo_shi_xiao_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer33.Add( b_rongcuo_shi, 0, wx.EXPAND, 5 )
        
        b_rongcuo_ge = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_rongcuo_ge_da_checkBox = wx.CheckBox( self, wx.ID_ANY, u"个位大", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_ge.Add( self.m_rongcuo_ge_da_checkBox, 0, wx.ALL, 5 )
        
        self.m_rongcuo_ge_xiao_checkBox = wx.CheckBox( self, wx.ID_ANY, u"个位小", wx.DefaultPosition, wx.DefaultSize, 0 )
        b_rongcuo_ge.Add( self.m_rongcuo_ge_xiao_checkBox, 0, wx.ALL, 5 )
        
        
        bSizer33.Add( b_rongcuo_ge, 0, wx.EXPAND, 5 )
        
        self.m_cline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer33.Add( self.m_cline9, 0, wx.EXPAND |wx.ALL, 5 )
        
        b_DaDiPinJie = wx.BoxSizer( wx.VERTICAL )
        
        self.m_DaDiPinJie_Text = wx.StaticText( self, wx.ID_ANY, u"大底拼接", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_DaDiPinJie_Text.Wrap( -1 )
        self.m_DaDiPinJie_Text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_DaDiPinJie_Text.SetMinSize( wx.Size( 60,-1 ) )
        
        b_DaDiPinJie.Add( self.m_DaDiPinJie_Text, 0, wx.ALL, 5 )
        
        self.m_DaDiPinJie_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.m_DaDiPinJie_textCtrl.SetMinSize( wx.Size( 250,250 ) )
        
        b_DaDiPinJie.Add( self.m_DaDiPinJie_textCtrl, 0, wx.ALL, 5 )

        bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_pinjie_flot_checkBox = wx.CheckBox( self, wx.ID_ANY, u"反集", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_pinjie_flot_checkBox, 0, wx.ALL, 5 )

        self.m_erma_pinjie_checkBox = wx.CheckBox( self, wx.ID_ANY, u"二码", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_erma_pinjie_checkBox, 0, wx.ALL, 5 )
        
        self.m_sanma_pinjie_checkBox81 = wx.CheckBox( self, wx.ID_ANY, u"三码", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_sanma_pinjie_checkBox81, 0, wx.ALL, 5 )
        
        self.m_sima_pinjie_checkBox = wx.CheckBox( self, wx.ID_ANY, u"四码", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer25.Add( self.m_sima_pinjie_checkBox, 0, wx.ALL, 5 )
        
        
        b_DaDiPinJie.Add( bSizer25, 1, wx.EXPAND, 5 )
        
        
        bSizer33.Add( b_DaDiPinJie, 1, wx.EXPAND, 5 )
        
        
        bSizer23.Add( bSizer33, 1, wx.EXPAND, 5 )
        
        
        gbSizer6.Add( bSizer23, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
        
        
        self.SetSizer( gbSizer6 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_bai_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_bai_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMaBai_OnCheckBox )
        self.m_shi_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_shi_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMaShi_OnCheckBox )
        self.m_ge_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_ge_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMaGe_OnCheckBox )
        self.m_HouSanWei_checkBox_0.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_1.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_2.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_3.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_4.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_5.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_6.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_7.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_8.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouSanWei_checkBox_9.Bind( wx.EVT_CHECKBOX, self.Kill_HouSanHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_0.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_1.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_2.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_3.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_4.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_5.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_6.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_7.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_8.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_HouErWei_checkBox_9.Bind( wx.EVT_CHECKBOX, self.Kill_HouErHeWei_OnCheckBox )
        self.m_DanMa_checkBox_0.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_1.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_2.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_3.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_4.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_5.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_6.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_7.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_8.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_DanMa_checkBox_9.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_ZhiShaoLianMa_checkBox.Bind( wx.EVT_CHECKBOX, self.DanMa_OnCheckBox )
        self.m_kill_baozhi_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_xingtai_OnCheckBox )
        self.m_4lian_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_xingtai_OnCheckBox )
        self.m_kill_santong_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_xingtai_OnCheckBox )
        self.gb_SuoShui_BUTTON.Bind( wx.EVT_BUTTON, self.OnButtonClick )
        self.m_cp_button.Bind( wx.EVT_BUTTON, self.OnButtonClick )
        self.m_clean_button.Bind( wx.EVT_BUTTON, self.OnButtonClick )
        self.m_rongcuo_13_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_OnCheckBox )
        self.m_rongcuo_14_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_OnCheckBox )
        self.m_rongcuo_15_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_OnCheckBox )
        self.m_rongcuo_wang_da_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_wang_xiao_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_qian_da_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_qian_xiao_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_bai_da_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_bai_xiao_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_shi_da_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_shi_xiao_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_ge_da_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_rongcuo_ge_xiao_checkBox.Bind( wx.EVT_CHECKBOX, self.RongCuo_dan_OnCheckBox )
        self.m_BaoLiuTouWei_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_BaoLiu_OnCheckBox )
        self.m_BaoLiuTouWeiSuan_checkBox.Bind( wx.EVT_CHECKBOX, self.Kill_BaoLiu_OnCheckBox )
        self.m_BaoLiushuang_checkBox.Bind(wx.EVT_CHECKBOX,self.Kill_BaoLiu_OnCheckBox)
        
        self.m_ertong_checkBox.Bind( wx.EVT_CHECKBOX, self.OnChecBox_ertong )
        self.m_sanma_checkBox.Bind( wx.EVT_CHECKBOX, self.m_sanma_OnCheckBox )
        self.m_pinjie_flot_checkBox.Bind( wx.EVT_CHECKBOX, self.On_pinjie_flog_OnCheckBox )
        self.m_erma_pinjie_checkBox.Bind( wx.EVT_CHECKBOX, self.On_pinjie_flog_OnCheckBox )
        self.m_sanma_pinjie_checkBox81.Bind( wx.EVT_CHECKBOX, self.On_pinjie_flog_OnCheckBox )
        self.m_sima_pinjie_checkBox.Bind( wx.EVT_CHECKBOX, self.On_pinjie_flog_OnCheckBox )
        
    def __del__( self ):
        pass

    def Kill_rongcuo_Bool(self,rongcuo_1_5_boot,rongcuo_1_4_boot,rongcuo_1_3_boot,wan,qian,bai,shi,ge):
        if rongcuo_1_5_boot:
            if wan in self.rongcuo_wang or qian in self.rongcuo_qian or bai in self.rongcuo_bai or shi in self.rongcuo_shi or ge in self.rongcuo_ge:
                return True
            else:
                return False
        return True

    #4码容错
    def Kill_rongcuo_Bool(self,rongcuo_1_5_boot,rongcuo_1_4_boot,rongcuo_1_3_boot,qian,bai,shi,ge):
        if rongcuo_1_5_boot:
            if qian in self.rongcuo_qian or bai in self.rongcuo_bai or shi in self.rongcuo_shi or ge in self.rongcuo_ge:
                return True
            else:
                return False
        return True

    
    def clearData(self):
        #清空所有数据
        self.killBaiWei_list.clear()
        self.killShiWei_list.clear()
        self.killGeWei_list.clear()
        #清空后三和尾列表
        self.kill_HouSanHeWei_list.clear()
        #清空后二和尾列表
        self.kill_HouErHeWei_list.clear()
        #清空胆码列表
        self.danMa_list.clear()
        #清空kill 二码
        self.kill_ErMa_Dict.clear()
        #清空kill 三码
        self.kill_SanMa_List.clear()
        #清空kill 012
        self.kill_012_Dict.clear()
        #清空大底拼接
        self.daDiPinJie_Dict.clear()
        #清空至少两胆
        self.liangDan = False
        #清空保留头尾
        self.baoLiuTouWei = False
        #清空保留头尾双
        self.baoLiuTouWei_s = False
        #清空保留双
        self.baoLiuShuang = False

        #kill AAAAA
        self.AAAAA_boot = False
        self.AAABB_boot = False
        self.baozhi_boot = False
        #容错
        self.rongcuo_1_3_boot = False
        self.rongcuo_1_4_boot = False
        self.rongcuo_1_5_boot = False
        #容错列表
        self.rongcuo_wang.clear()
        self.rongcuo_qian.clear()
        self.rongcuo_bai.clear()
        self.rongcuo_shi.clear()
        self.rongcuo_ge.clear()
        #清空和值
        self.kill_hezhi_list.clear()
        #清空结果值
        self.result_list.clear()

    def Get_Result(self):
        #缩水前先清空数据
        #for wan in range(0,10):
            for qian in range(0,10):
                for bai in range(0,10):
                    #杀百位
                    if bai not in self.killBaiWei_list:
                        for shi in range(0,10):
                            #杀十位
                            if shi not in self.killShiWei_list:
                                for ge in range(0,10):
                                    #杀个位
                                    if ge not in self.killGeWei_list:
                                        #杀后二和尾
                                        killHouEr = (shi + ge) % 10
                                        #杀后三和尾
                                        killHouSan = (bai + shi + ge) % 10;

                                        killHouEr_bool = self.tool.Get_HouErHeWeiBool(self.kill_HouErHeWei_list,killHouEr)
                                        killHouSan_bool = self.tool.Get_HouErHeWeiBool(self.kill_HouSanHeWei_list,killHouSan)
                                        #杀二码
                                        killErMa_bool = self.tool.Kill_ErMa_Bool(self.kill_ErMa_Dict, qian, bai, shi, ge,self.baoLiuTouWei_s,self.baoLiuTouWei,self.baoLiuShuang)
                                        #杀三码
                                        killSanMa_bool = self.tool.Kill_SanMa_Bool(self.kill_SanMa_List,self.ertongyishsang_boot, qian,bai, shi, ge)
                                        #杀012
                                        #kill_012_bool = self.tool.Kill_012_Bool(self.kill_012_Dict,wan,qian, bai, shi, ge)
                                        kill_012_bool = self.tool.Kill_012_Bool(self.kill_012_Dict,qian, bai, shi, ge)
                                        #大底拼接
                                        daDiPinJie_bool = self.tool.DaDiPinJie_Bool(self.daDiPinJie_Dict,self.daDiPinJie_flot,qian,bai,shi,ge)
                                        #胆码
                                        #danMa_bool = self.tool.DanMa_Bool(self.danMa_list,self.liangDan,wan,qian,bai,shi,ge)
                                        danMa_bool = self.tool.DanMa_Bool(self.danMa_list,self.liangDan,qian,bai,shi,ge)
                                        #杀和值
                                        #kill_hezhi_bool = self.tool.Kill_hezhi_Bool(self.kill_hezhi_list,wan,qian,bai,shi,ge)
                                        kill_hezhi_bool = self.tool.Kill_hezhi_Bool(self.kill_hezhi_list,qian,bai,shi,ge)
                                        #杀形态
                                        #kill_xingtai_bool = self.tool.Kill_xingtai_Bool(self.AAAAA_boot,self.AAABB_boot,self.baozhi_boot,wan,qian,bai,shi,ge)
                                        kill_xingtai_bool = self.tool.Kill_xingtai_Bool(self.AAAAA_boot,self.AAABB_boot,self.baozhi_boot,qian,bai,shi,ge)
                                        #杀容错
                                        #kill_rongcuo_bool = self.Kill_rongcuo_Bool(self.rongcuo_1_5_boot,self.rongcuo_1_4_boot,self.rongcuo_1_3_boot,wan,qian,bai,shi,ge)
                                        kill_rongcuo_bool = self.Kill_rongcuo_Bool(self.rongcuo_1_5_boot,self.rongcuo_1_4_boot,self.rongcuo_1_3_boot,qian,bai,shi,ge)
                                        if killHouEr_bool and killHouSan_bool and killErMa_bool and kill_012_bool and daDiPinJie_bool and danMa_bool and kill_hezhi_bool and kill_xingtai_bool and kill_rongcuo_bool and killSanMa_bool:
                                            #s = str(wan)+str(qian)+str(bai) + str(shi) + str(ge)
                                            if self.sanma_bool:
                                                s = str(bai) + str(shi) + str(ge)
                                            elif self.m_ch_erma_checkBox84.IsChecked():
                                                s = str(shi) + str(ge)
                                            else:
                                                s = str(qian)+str(bai) + str(shi) + str(ge)
                                            if not s in self.result_list:
                                                self.result_list.append(s)

    # Virtual event handlers, overide them in your derived class
    def DanMaBai_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.killBaiWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.killBaiWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def DanMaShi_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.killShiWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.killShiWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def DanMaGe_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.killGeWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.killGeWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def Kill_HouSanHeWei_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.kill_HouSanHeWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.kill_HouSanHeWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()
    
    def Kill_HouErHeWei_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.kill_HouErHeWei_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        if cb.GetValue() == False:
            self.kill_HouErHeWei_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()

    def OnChecBox_ertong( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.ertongyishsang_boot = True
        if cb.GetValue() == False:
            self.ertongyishsang_boot = False
        event.Skip()

    def m_sanma_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if cb.GetValue() == True:
            self.sanma_bool = True
        if cb.GetValue() == False:
            self.sanma_bool = False
        event.Skip()
    
    def DanMa_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"至少两码"):
            if cb.GetValue() == True:
                self.liangDan = True
            else:
                self.liangDan = False
        else:
            if cb.GetValue() == True:
                self.danMa_list.append(self.tool.Get_CheckBoxValue(cb.GetLabel()))
            if cb.GetValue() == False:
                self.danMa_list.remove(self.tool.Get_CheckBoxValue(cb.GetLabel()))
        event.Skip()

    def Kill_BaoLiu_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"保留头尾"):
            if cb.GetValue() == True:
                self.baoLiuTouWei = True
            else:
                self.baoLiuTouWei = False
        if(cb.GetLabel() == r"保留头尾双"):
            if cb.GetValue() == True:
                self.baoLiuTouWei_s = True 
            else:
                self.baoLiuTouWei_s = False
        if(cb.GetLabel() == r"保留双"):
            if cb.GetValue() == True:
                self.baoLiuShuang = True
            else:
                self.baoLiuShuang = False
        event.Skip()
    def Kill_xingtai_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"杀豹子"):
            if cb.GetValue() == True:
                self.baozhi_boot = True
            else:
                self.baozhi_boot = False
        if(cb.GetLabel() == r"AAAAA"):
            if cb.GetValue() == True:
                self.AAAAA_boot = True
            else:
                self.AAAAA_boot = False
        if(cb.GetLabel() == r"AAABB"):
            if cb.GetValue() == True:
                self.AAABB_boot = True
            else:
                self.AAABB_boot = False
        event.Skip()
    def RongCuo_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"1-3容错"):
            if cb.GetValue() == True:
                self.rongcuo_1_3_boot = True
            else:
                self.rongcuo_1_3_boot = False
        if(cb.GetLabel() == r"1-4容错"):
            if cb.GetValue() == True:
                self.rongcuo_1_4_boot = True
            else:
                self.rongcuo_1_4_boot = False
        if(cb.GetLabel() == r"1-5容错"):
            if cb.GetValue() == True:
                self.rongcuo_1_5_boot = True
            else:
                self.rongcuo_1_5_boot = False
        event.Skip()
    
    def RongCuo_dan_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"万位大"):
            if cb.GetValue() == True:
                for i in range(5,10):
                    self.rongcuo_wang.append(i)
            else:
                for i in range(5,10):
                    self.rongcuo_wang.remove(i)
        if(cb.GetLabel() == r"万位小"):
            if cb.GetValue() == True:
                for i in range(0,5):
                    self.rongcuo_wang.append(i)
            else:
                for i in range(0,5):
                    self.rongcuo_wang.remove(i)
        if(cb.GetLabel() == r"千位大"):
            if cb.GetValue() == True:
                for i in range(5,10):
                    self.rongcuo_qian.append(i)
            else:
                for i in range(5,10):
                    self.rongcuo_qian.remove(i)
        if(cb.GetLabel() == r"千位小"):
            if cb.GetValue() == True:
                for i in range(0,5):
                    self.rongcuo_qian.append(i)
            else:
                for i in range(0,5):
                    self.rongcuo_qian.remove(i)
        if(cb.GetLabel() == r"百位大"):
            if cb.GetValue() == True:
                for i in range(5,10):
                    self.rongcuo_bai.append(i)
            else:
                for i in range(5,10):
                    self.rongcuo_bai.remove(i)
        if(cb.GetLabel() == r"百位小"):
            if cb.GetValue() == True:
                for i in range(0,5):
                    self.rongcuo_bai.append(i)
            else:
                for i in range(0,5):
                    self.rongcuo_bai.remove(i)
        if(cb.GetLabel() == r"十位大"):
            if cb.GetValue() == True:
                for i in range(5,10):
                    self.rongcuo_shi.append(i)
            else:
                for i in range(5,10):
                    self.rongcuo_shi.remove(i)
        if(cb.GetLabel() == r"十位小"):
            if cb.GetValue() == True:
                for i in range(0,5):
                    self.rongcuo_shi.append(i)
            else:
                for i in range(0,5):
                    self.rongcuo_shi.remove(i)
        if(cb.GetLabel() == r"个位大"):
            if cb.GetValue() == True:
                for i in range(5,10):
                    self.rongcuo_ge.append(i)
            else:
                for i in range(5,10):
                    self.rongcuo_ge.remove(i)
        if(cb.GetLabel() == r"个位小"):
            if cb.GetValue() == True:
                for i in range(0,5):
                    self.rongcuo_ge.append(i)
            else:
                for i in range(0,5):
                    self.rongcuo_ge.remove(i)
        
        event.Skip()

    def On_pinjie_flog_OnCheckBox( self, event ):
        cb = event.GetEventObject() 
        if(cb.GetLabel() == r"反集"):
            if cb.GetValue() == True:
                self.daDiPinJie_flot = True
            if cb.GetValue() == False:
                self.daDiPinJie_flot = False
        if cb.GetLabel() == r"二码":
            if cb.GetValue() == True:
                self.daDiPinJie_num = 2
            if cb.GetValue() == False:
                self.daDiPinJie_num = 2
        if cb.GetLabel() == r"三码":
            if cb.GetValue() == True:
                self.daDiPinJie_num = 3
            if cb.GetValue() == False:
                self.daDiPinJie_num = 2
        if cb.GetLabel() == r"四码":
            if cb.GetValue() == True:
                self.daDiPinJie_num = 4
            if cb.GetValue() == False:
                self.daDiPinJie_num = 2
        event.Skip()
    
    def OnButtonClick( self, event ):
        cb = event.GetEventObject() 
        if cb.GetLabel() == r"缩水":

            #缩水前先获取输入的值
            self.kill_ErMa_Dict = str(self.m_Kill_ErMa_textCtrl.GetValue()).split(" ")
            self.kill_012_Dict = str(self.m_Kill_012_textCtrl.GetValue()).split(" ")
            self.kill_hezhi_list = str(self.m_kill_hezhi_textCtrl.GetValue()).split(" ")
            self.kill_SanMa_List = str(self.m_Kill_SanMa_textCtrl.GetValue()).split(" ")
            self.kill_SanMa_List = self.tool.getData_list(self.kill_SanMa_List)
            #获取和值
            
            #获取大底的数据并赋值给列表，去除换行符
            num = 0
            add_data = ""
            for data in str(self.m_DaDiPinJie_textCtrl.GetValue()):
                if data.isdigit():
                    num = num +1
                    add_data = add_data + data
                    #
                    if num == self.daDiPinJie_num:
                        num = 0
                        self.daDiPinJie_Dict.append(add_data)
                        add_data = ""
            #####################################################################
            #缩水前先清空结果
            self.result_list.clear()
            self.Get_Result()
            self.m_result_textCtrl.SetValue(str(self.result_list).replace(r'[',"").replace(r']',"").replace("'",""))
            self.m_ZhuShuDatatextCtrl.SetValue(str(len(self.result_list)))

        if cb.GetLabel() == r"清空":
            #清空杀百位
            self.m_bai_checkBox_0.SetValue(False)
            self.m_bai_checkBox_1.SetValue(False)
            self.m_bai_checkBox_2.SetValue(False)
            self.m_bai_checkBox_3.SetValue(False)
            self.m_bai_checkBox_4.SetValue(False)
            self.m_bai_checkBox_5.SetValue(False)
            self.m_bai_checkBox_6.SetValue(False)
            self.m_bai_checkBox_7.SetValue(False)
            self.m_bai_checkBox_8.SetValue(False)
            self.m_bai_checkBox_9.SetValue(False)
            #清空杀十位
            self.m_shi_checkBox_0.SetValue(False)
            self.m_shi_checkBox_1.SetValue(False)
            self.m_shi_checkBox_2.SetValue(False)
            self.m_shi_checkBox_3.SetValue(False)
            self.m_shi_checkBox_4.SetValue(False)
            self.m_shi_checkBox_5.SetValue(False)
            self.m_shi_checkBox_6.SetValue(False)
            self.m_shi_checkBox_7.SetValue(False)
            self.m_shi_checkBox_8.SetValue(False)
            self.m_shi_checkBox_9.SetValue(False)
            #清空杀个位
            self.m_ge_checkBox_0.SetValue(False)
            self.m_ge_checkBox_1.SetValue(False)
            self.m_ge_checkBox_2.SetValue(False)
            self.m_ge_checkBox_3.SetValue(False)
            self.m_ge_checkBox_4.SetValue(False)
            self.m_ge_checkBox_5.SetValue(False)
            self.m_ge_checkBox_6.SetValue(False)
            self.m_ge_checkBox_7.SetValue(False)
            self.m_ge_checkBox_8.SetValue(False)
            self.m_ge_checkBox_9.SetValue(False)
            #清空胆码
            self.m_DanMa_checkBox_0.SetValue(False)
            self.m_DanMa_checkBox_1.SetValue(False)
            self.m_DanMa_checkBox_2.SetValue(False)
            self.m_DanMa_checkBox_3.SetValue(False)
            self.m_DanMa_checkBox_4.SetValue(False)
            self.m_DanMa_checkBox_5.SetValue(False)
            self.m_DanMa_checkBox_6.SetValue(False)
            self.m_DanMa_checkBox_7.SetValue(False)
            self.m_DanMa_checkBox_8.SetValue(False)
            self.m_DanMa_checkBox_9.SetValue(False)
            #清空后三和尾
            self.m_HouSanWei_checkBox_0.SetValue(False)
            self.m_HouSanWei_checkBox_1.SetValue(False)
            self.m_HouSanWei_checkBox_2.SetValue(False)
            self.m_HouSanWei_checkBox_3.SetValue(False)
            self.m_HouSanWei_checkBox_4.SetValue(False)
            self.m_HouSanWei_checkBox_5.SetValue(False)
            self.m_HouSanWei_checkBox_6.SetValue(False)
            self.m_HouSanWei_checkBox_7.SetValue(False)
            self.m_HouSanWei_checkBox_8.SetValue(False)
            self.m_HouSanWei_checkBox_9.SetValue(False)
            #清空后二和尾
            self.m_HouErWei_checkBox_0.SetValue(False)
            self.m_HouErWei_checkBox_1.SetValue(False)
            self.m_HouErWei_checkBox_2.SetValue(False)
            self.m_HouErWei_checkBox_3.SetValue(False)
            self.m_HouErWei_checkBox_4.SetValue(False)
            self.m_HouErWei_checkBox_5.SetValue(False)
            self.m_HouErWei_checkBox_6.SetValue(False)
            self.m_HouErWei_checkBox_7.SetValue(False)
            self.m_HouErWei_checkBox_8.SetValue(False)
            self.m_HouErWei_checkBox_9.SetValue(False)
            #清空至少两码
            self.m_ZhiShaoLianMa_checkBox.SetValue(False)
            #清空保留头尾
            self.m_BaoLiuTouWei_checkBox.SetValue(False)
            #清空保留头尾双
            self.m_BaoLiuTouWeiSuan_checkBox.SetValue(False)
            #清空杀二码
            self.m_Kill_ErMa_textCtrl.Clear()
            #清空杀三码
            self.m_Kill_SanMa_textCtrl.Clear()
            #清空012
            self.m_Kill_012_textCtrl.Clear()
            #清空大底拼接
            self.m_DaDiPinJie_textCtrl.Clear()
            self.daDiPinJie_flot = False
            self.daDiPinJie_num = 2
            self.m_pinjie_flot_checkBox.SetValue(False)
            self.m_erma_pinjie_checkBox.SetValue(False)
            self.m_sanma_pinjie_checkBox81.SetValue(False)
            self.m_sima_pinjie_checkBox.SetValue(False)

            #清空结果
            self.m_result_textCtrl.Clear()
            #清空注数
            self.m_ZhuShuDatatextCtrl.Clear()
            #清空杀和值
            self.m_kill_hezhi_textCtrl.Clear()
            #清空形态
            self.m_kill_baozhi_checkBox.SetValue(False)
            self.m_4lian_checkBox.SetValue(False)
            self.m_kill_santong_checkBox.SetValue(False)
            #清空容错
            self.m_rongcuo_13_checkBox.SetValue(False)
            self.m_rongcuo_14_checkBox.SetValue(False)
            self.m_rongcuo_15_checkBox.SetValue(False)
            self.m_rongcuo_wang_da_checkBox.SetValue(False)
            self.m_rongcuo_wang_xiao_checkBox.SetValue(False)
            self.m_rongcuo_qian_da_checkBox.SetValue(False)
            self.m_rongcuo_qian_xiao_checkBox.SetValue(False)
            self.m_rongcuo_bai_da_checkBox.SetValue(False)
            self.m_rongcuo_bai_xiao_checkBox.SetValue(False)
            self.m_rongcuo_shi_da_checkBox.SetValue(False)
            self.m_rongcuo_shi_xiao_checkBox.SetValue(False)
            self.m_rongcuo_ge_da_checkBox.SetValue(False)
            self.m_rongcuo_ge_xiao_checkBox.SetValue(False)
            #清空后三转换
            self.m_sanma_checkBox.SetValue(False)

            #清空数据
            self.clearData()
        if cb.GetLabel() == r"复制":
            clipboard.copy(str(self.result_list).replace(r'[',"").replace(r']',"").replace("'",""))
        event.Skip()
    


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame2(None)
    frame.Show()
    app.MainLoop()


'''
            print("杀百位:"+str(self.killBaiWei_list)+r"\n")
            print("杀十位:"+str(self.killShiWei_list)+r"\n")
            print("杀个位:"+str(self.killGeWei_list)+r"\n")
            print("杀后三和尾:"+str(self.kill_HouSanHeWei_list)+r"\n")
            print("杀后二和尾:"+str(self.kill_HouErHeWei_list)+r"\n")
            print("胆码:"+str(self.danMa_list)+r"\n")
            print("至少两胆:"+str(self.liangDan)+r"\n")
            print("保留头尾:"+str(self.baoLiuTouWei)+r"\n")
            print("保留头尾双:"+str(self.baoLiuTouWei_s)+r"\n")
            print("杀二码:"+str(self.m_Kill_ErMa_textCtrl.GetValue()))
            print("杀012:"+str(self.m_Kill_012_textCtrl.GetValue()))
            print("杀和值:"+str(self.m_kill_hezhi_textCtrl.GetValue()))
            print("大底拼接:"+str(self.m_DaDiPinJie_textCtrl.GetValue()))
            print("豹子:"+str(self.baozhi_boot))
            print("AAAAA:"+str(self.AAAAA_boot))
            print("AAABB:"+str(self.AAABB_boot))
            print("容错1-3:"+str(self.rongcuo_1_3_boot))
            print("容错1-4:"+str(self.rongcuo_1_4_boot))
            print("容错1-5:"+str(self.rongcuo_1_5_boot))
            print("容错万位"+str(self.rongcuo_wang))
            print("容错千位:"+str(self.rongcuo_qian))
            print("容错百位:"+str(self.rongcuo_bai))
            print("容错十位:"+str(self.rongcuo_shi))
            print("容错个位:"+str(self.rongcuo_ge))
'''