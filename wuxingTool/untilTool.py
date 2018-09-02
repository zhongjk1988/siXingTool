# -*- coding: utf-8 -*- 
from collections import Counter
import string
class Tool ():

    list_0 = [0,3,6,9]
    list_1 = [1,4,7]
    list_2 = [2,5,8]

    def __init__(self):
        pass

    def Get_CheckBoxValue(self,getLabel):
        if getLabel == "0":
            return 0
        if getLabel == "1":
            return 1
        if getLabel == "2":
            return 2
        if getLabel == "3":
            return 3
        if getLabel == "4":
            return 4
        if getLabel == "5":
            return 5
        if getLabel == "6":
            return 6
        if getLabel == "7":
            return 7
        if getLabel == "8":
            return 8
        if getLabel == "9":
            return 9
    def Get_HouErHeWeiBool(self,list,killHouEr):
        if killHouEr in list:
            return False
        else:
            return True

    ####################################################################################
    # kill 2 码 直接杀二码
    def Kill_ErMa_m(self,list,qian,bai,shi,ge):
        erma1 = 0
        if str(qian) in list:
            erma1 = erma1 + 1
        if str(bai) in list:
            erma1 = erma1 + 1
        if str(shi) in list:
            erma1 = erma1 + 1
        if str(ge) in list:
            erma1 = erma1 + 1
        return erma1
        
    #kill 2 码 保留头尾
    def Kill_ErMa_NoTou_m(self,list,bai,shi,ge):
        erma1 = 0
        if str(bai) in list and str(shi) in list:
            erma1 = erma1 + 1
        if str(shi) in list and str(ge) in list:
            erma1 = erma1 + 1
        return erma1

        
    #kill 2 码 不包含对子和头尾二码相连
    def Kill_ErMa_NoTouSuan_m(self,list,bai,shi,ge):
        erma1 = 0
        if str(bai) in list and str(shi) in list and bai != shi:
            erma1 = erma1 + 1
        if str(shi) in list and str(ge) in list and shi != ge:
            erma1 = erma1 + 1
        return erma1

     #kill 2 码 保留双
    def Kill_ErMa_NoShuang_m(self,list,bai,shi,ge):
        erma1 = 0
        if str(bai) in list and str(shi) in list and bai != shi:
            erma1 = erma1 + 1
        if str(shi) in list and str(ge) in list and shi != ge:
            erma1 = erma1 + 1
        if str(bai) in list and str(ge) in list and bai != ge:
            erma1 = erma1 + 1
        return erma1

    #kill 2 码
    def Kill_ErMa_Bool(self,list,qian,bai,shi,ge,baoLiuTouWei_s,baoLiuTouWei,baoLiuShuang):

        if(baoLiuShuang):
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_NoShuang_m(data_list,bai,shi,ge)
                    if num >= 1:
                        return False
        elif baoLiuTouWei_s:
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_NoTouSuan_m(data_list,bai,shi,ge)
                    if num >= 1:
                        return False
        elif baoLiuTouWei:
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_NoTou_m(data_list,bai,shi,ge)
                    if num >= 1:
                        return False
        else:
            if list:
                for data_list in list:
                    num = self.Kill_ErMa_m(data_list,qian,bai,shi,ge)
                    if num >= 2:
                        return False
        return True
    #####################################################################################
    #kill 3 码
    def Kill_SanMa_m(self,list,qian,bai,shi,ge):
        erma1 = 0
        if str(qian) in list:
            erma1 = erma1 + 1
        if str(bai) in list:
            erma1 = erma1 + 1
        if str(shi) in list:
            erma1 = erma1 + 1
        if str(ge) in list:
            erma1 = erma1 + 1
        return erma1

    #判断是否有同码
    def isTongMa(self,ertongyishsang_boot,qian,bai,shi,ge):
        list = []
        list.append(qian)
        list.append(bai)
        list.append(shi)
        list.append(ge)

        for data in list:
            num = list.count(data)
            if ertongyishsang_boot:
                if(num >=2):
                    return True
            else:
                if(num >=3):
                    return True
        return False

    def Kill_SanMa_Bool(self,list,ertongyishsang_boot,qian,bai,shi,ge):
        if list:
            for data_list in list:
                num = self.Kill_SanMa_m(data_list,qian,bai,shi,ge)
                #if num >= 3 and not self.isTongMa(ertongyishsang_boot,qian,bai,shi,ge):
                if num >= 3 :
                    return False
            return True
        else:
            return True

    def getData_list(self,mlist)->list:
        qian = ""
        bai = ""
        shi = ""
        ge = ""
        bast_list = []

        if mlist:
            for data_list in mlist:
                if len(data_list) == 4:
                    qian = list(data_list)[0]
                    bai = list(data_list)[1]
                    shi = list(data_list)[2]
                    ge = list(data_list)[3]
                    bast_list.append(qian+bai+shi)
                    bast_list.append(qian+shi+ge)
                    bast_list.append(bai+shi+ge)
                    bast_list.append(qian+bai+ge)
        return bast_list

    #####################################################################################

    def get_012(self,num):
        if num in self.list_0:
            return 0
        if num in self.list_1:
            return 1
        if num in self.list_2:
            return 2

    #kill 012
    def Kill_012_Bool(self,kill_012_Dict,qian,bai, shi, ge):
        #wan_012 = self.get_012(wan)
        qian_012 = self.get_012(qian)
        bai_012 = self.get_012(bai)
        shi_012 = self.get_012(shi)
        ge_012 = self.get_012(ge)
        data_012 = str(qian_012) +str(bai_012) + str(shi_012) + str(ge_012)
        if data_012 in kill_012_Dict:
            return False
        else:
            return True
    ######################################################################
    def DaDiPinJie_Bool(self,daDiPinJie_Dict,flog,qian,bai,shi,ge):
        if daDiPinJie_Dict:
            for data in daDiPinJie_Dict:
                if len(data) == 2:
                    if data[0] == str(shi) and data[1] == str(ge):
                        return not flog
                if len(data) == 3:
                    if data[0] == str(bai) and data[1] == str(shi) and data[2] == str(ge):
                        return not flog
                if len(data) == 4:
                    if data[0] == str(qian) and data[1] == str(bai) and data[2] == str(shi) and data[3] == str(ge):
                        return not flog
            return flog
        else:
            return True
    ####################三胆#################################################
    def DanMa_Bool(self,danMa_list,liangDan,bai,shi,ge):
        if len(danMa_list) == 0:
            return True
        if liangDan:
            num = 0
            if bai in danMa_list:
                num = num + 1
            if shi in danMa_list:
                num = num + 1
            if ge in danMa_list:
                num = num + 1
            if num >=2:
                return True
            else:
                return False
            pass
        else:
            if bai in danMa_list or shi in danMa_list or ge in danMa_list:
                return True
            else:
                return False
    #######################五胆###############################################
    def DanMa_Bool(self,danMa_list,liangDan,wan,qian,bai,shi,ge):
        if len(danMa_list) == 0:
            return True
        if liangDan:
            num = 0
            if wan in danMa_list:
                num = num +1
            if qian in danMa_list:
                num = num +1
            if bai in danMa_list:
                num = num + 1
            if shi in danMa_list:
                num = num + 1
            if ge in danMa_list:
                num = num + 1
            if num >=2:
                return True
            else:
                return False
            pass
        else:
            if wan in danMa_list or qian in danMa_list or bai in danMa_list or shi in danMa_list or ge in danMa_list:
                return True
            else:
                return False
    #######################四胆###############################################
    def DanMa_Bool(self,danMa_list,liangDan,qian,bai,shi,ge):
        if len(danMa_list) == 0:
            return True
        if liangDan:
            num = 0
            if qian in danMa_list:
                num = num +1
            if bai in danMa_list:
                num = num + 1
            if shi in danMa_list:
                num = num + 1
            if ge in danMa_list:
                num = num + 1
            if num >=2:
                return True
            else:
                return False
            pass
        else:
            if qian in danMa_list or bai in danMa_list or shi in danMa_list or ge in danMa_list:
                return True
            else:
                return False
    #杀和值
    def Kill_hezhi_Bool(self,kill_hezhi_list,wan,qian,bai,shi,ge):
        num = wan+qian+bai+shi+ge
        if str(num) in kill_hezhi_list:
            return False
        else:
            return True
    #杀和值4码
    def Kill_hezhi_Bool(self,kill_hezhi_list,qian,bai,shi,ge):
        num = qian+bai+shi+ge
        if str(num) in kill_hezhi_list:
            return False
        else:
            return True
    #5码豹子
    def Kill_xingtai_Bool(self,AAAAA_boot,AAABB_boot,baozhi_boot,wan,qian,bai,shi,ge):
        print(AAAAA_boot)
        if baozhi_boot:
            if wan == qian and wan == bai and wan == shi and wan == ge:
                return False
        if AAABB_boot:
            list = []
            data = Counter([wan,qian,bai,shi,ge]).values()
            for i in data:
                list.append(i)
            if len(list) >= 2: 
                if (list[0] == 3 and list[1] == 2) or (list[0] == 2 and list[1] == 3):
                    return False
            
        return True
    #4码豹子
    def Kill_xingtai_Bool(self,AAAAA_boot,AAABB_boot,baozhi_boot,qian,bai,shi,ge):
        if baozhi_boot:
            if qian == bai and qian == shi and qian == ge:
                return False
        if AAABB_boot:
            list = []
            data = Counter([qian,bai,shi,ge]).values()
            for i in data:
                list.append(i)
            if len(list) >= 2: 
                if (list[0] == 3 and list[1] == 2) or (list[0] == 2 and list[1] == 3):
                    return False
        if AAAAA_boot:
            list = []
            list.append(qian)
            list.append(bai)
            list.append(shi)
            list.append(ge)
            for i in list:
                if list.count(i) >= 3:
                    return False
        return True
