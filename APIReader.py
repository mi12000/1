'''
Created on 2016-1-22

@author: Admin
'''
import xlrd,time,os,re
from KT_190E import Session_id


class APIReader(Session_id.Session_Id):
    def __init__(self,env='test'):
        Session_id.Session_Id.__init__(self)
        self.xfdc={}
        self.xf={}
        self.get_TEMP()
        self.TNAME=[]
        self.APINAME=''
        self.DATA=[]
        self.DATA2=[]
        self.DATA3=[]
        self.trainA={}
        self.trainB={}
        self.appdata=[]
        self.get_env(env)
        
    
    def get_TEMP(self,xfe=7):
        xfn=[]
        allfn=os.listdir('D:\\')
        for fn in allfn:
            if '.xlsx' in fn:
                try:
                    xfn.append(fn)
                except FileNameException as e:
                    print(e)
        for xn in range(len(xfn)):
            self.xfdc[xn]=xfn[xn]
            self.xf[xfn[xn]]=xn
        print(self.xfdc)
        print(self.xf)
        xlname=self.xfdc[int(xfe)]
        self.bk = xlrd.open_workbook('D:\\'+xlname)
        shxrange = range(self.bk.nsheets)
           
    def get_env(self,envv):
        self.time_man = time.strftime('%Y-%m-%d %H:%M:%S')
        if envv=='test' or envv=='TEST':
            self.appurl='https://test.madailicai.com/p2p/apps/router'
            self.BDATA={'appId':'ios-user','version':'1.0','deviceId':'50434028OEAOOB10','platform':'ios','channel':'baidu','appVersion':'1.7.1','osVersion':'9.3'}
            self.login_data_mine = {"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"12341234123","password":"qqqqqqqq"}
            self.login_data_unatd = {"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"12243191145","password":"qqqqqqqq"}
            self.login_data_sn2={}
            self.login_data_sn3={}
            self.login_data_sn4={}
            self.login_data_sn5={}
            self.login_data_sn6={"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"13524528707","password":"qwer1234"}
            self.testlink='http://test.madailicai.com/p2p/apps/router?'
        elif envv=='uat' or envv=='UAT':
            self.appurl='https://uat.madailicai.com/p2p/apps/router'
            self.BDATA={'appId':'ios-user','version':'1.0','deviceId':'50434028OEAOOB10','platform':'ios','channel':'baidu','appVersion':'1.7.1','osVersion':'9.3'}
            self.login_data_mine = {"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"12341234123","password":"qqqqqqqq"}
            self.login_data_unatd = {"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"19626980624","password":"qqqqqqqq"}
            self.login_data_sn2= {"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"17000001111","password":"aaaa1111"}
            self.login_data_sn3={"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"17000001112","password":"aaaa1111"}
            self.login_data_sn4={"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"17000001113","password":"aaaa1111"}
            self.login_data_sn5={"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"13167277837","password":"qwer1234"}
            self.login_data_sn6={"service":"oauth.token.get","appId":"ios-user","appVersion":"1.0","timestamp":self.time_man,"deviceId":"sandbox_device_88888888","platform":"IOS","channel":"appstore","appVersion":"1.0","osVersion":"1.8","version":"1.0","account":"13524528707","password":"qwer1234"}
            self.testlink='http://uat.madailicai.com/p2p/apps/router?'
        elif envv=='预生产' or envv=='pre' or envv=='PRE':
            self.appurl='https://p.madailicai.com/p2p/apps/router'
            self.BDATA={'appId':'ios-user','version':'1.0','deviceId':'50434028OEAOOB10','platform':'ios','channel':'baidu','appVersion':'1.7.1','osVersion':'9.3'}
            self.testlink='http://p.madailicai.com/p2p/apps/router?'
        elif envv=='online' or envv=='线上':
            self.appurl='https://www.madailicai.com/p2p/apps/router'
            self.BDATA={'appId':'ios-user','version':'1.0','deviceId':'50434028OEAOOB10','platform':'ios','channel':'baidu','appVersion':'1.7.1','osVersion':'9.3'}
            self.testlink='http://www.madailicai.com/p2p/apps/router?'
        return self.appurl
    
    def get_title(self,she):
        try:
            sh = self.bk.sheet_by_name(she)
        except:
            raise Exception(u'ERROR：%s not found in '%she)
        nrows = sh.nrows
        #print(self.shts)
        for rw in range(nrows):
            #self.TNAME.append(sh.cell_value(rw,0))
            if type(sh.cell_value(rw,0))==float:
                self.TNAME.append(str(int(sh.cell_value(rw,0))))
            elif sh.cell_value(rw,0)==None:
                self.TNAME.append('NOID')
            else:
                try:
                    self.TNAME.append(str(int(sh.cell_value(rw,0))))
                except:
                    self.TNAME.append(sh.cell_value(rw,0))
        if 'ID' in self.TNAME:
            self.TNAME.remove('ID')
        print(self.TNAME)
        return self.TNAME
    
    def get_sht(self):
        self.SHEETS=[]
        self.shts=self.bk.sheets()
        for she in self.shts:
            self.SHEETS.append(she.name)
        self.STNAME={}
        self.EMANTS={}
        self.xn=0
        for st in self.SHEETS:
            self.STNAME[self.xn]=st
            self.EMANTS[st]=self.xn
            self.xn+=1
        
    def rd_data(self,sheet):
        self.mktime()
        self.PDATA={}
        self.MDATA={}
        self.VDATA=[]
        self.P={}
        self.C=''
        self.BDATA['timestamp']=self.tm
        try:
            sh = self.bk.sheet_by_name(sheet)
        except:
            raise Exception(u'ERROR：%s not found in '%sheet)
        nrows = sh.nrows
        ncols = sh.ncols
        print ("获取数据：%d列,%d行" %(ncols,nrows))
        for row in range(nrows):
            if row ==0:
                continue
            else:
                self.DATA3.append(sh.cell_value(row,2))
                if sh.cell_value(row,1)=='':
                    self.APINAME='NONAME'
                else:
                    self.APINAME=sh.cell_value(row,1)
                self.DATA3.append(self.APINAME)
                try:
                    self.P=eval(sh.cell_value(row,4))
                except:
                    self.P={}
                self.PDATA=dict(dict(self.BDATA,**eval(sh.cell_value(row,3))),**self.P)
                for sin in eval(sh.cell_value(row,3)).keys():
                    if sin=='session':
                        self.PDATA['session']=self.myid
                    elif sin=='session1':
                        self.PDATA['session']=self.unatd
                        del self.PDATA['session1']
                    elif sin=='session2':
                        self.PDATA['session']=self.sn2id
                        del self.PDATA['session2']
                    elif sin=='session3':
                        self.PDATA['session']=self.sn3id
                        del self.PDATA['session3']
                    elif sin=='session4':
                        self.PDATA['session']=self.sn4id
                        del self.PDATA['session4']
                    elif sin=='session5':
                        self.PDATA['session']=self.sn5id
                        del self.PDATA['session5']
                    elif sin=='session6':
                        self.PDATA['session']=self.sn6id
                        del self.PDATA['session6']
                    
                self.DATA3.append(self.PDATA)
                try:
                    int(sh.cell_value(row,5))
                except:
                    self.C=sh.cell_value(row,5)
                else:
                    if int(sh.cell_value(row,5))==0:
                        self.C='0000'
                    else:
                        self.C=(4-len('%s'%(int(sh.cell_value(row,5)))))*'0'+str(int(sh.cell_value(row,5)))
                self.VDATA.append(self.C)
                self.VDATA.append(sh.cell_value(row,6))
                if sh.cell_value(row,7) == '':
                    self.VDATA.append('')
                else:
                    try:
                       self.FDS(sh.cell_value(row,7))
                    except:
                        print(sh.cell_value(row,7))
                        print('格式不对')
                    else:
                        self.VDATA.append(self.FD)
                self.DATA3.append(self.VDATA)
                for vd in self.DATA3:
                    self.DATA.append(vd)
                self.trainA[str(int(sh.cell_value(row,0)))]=self.DATA
                self.appdata.append(self.trainA)
                self.DATA=[]
                self.VDATA=[]
                self.DATA3=[]
                #self.DATA2=[]
        #print(self.APINAME)
        #print(self.DATA)
        #print(self.trainA)
        #print('appdata:%s'%self.appdata)
        #print(self.trainB)
    def FDS(self,fd):
        self.fd=fd
        flag4=True
        flag5=True
        flag6=True
        while flag4:
            self.fd=re.sub('false','False',self.fd)
            if 'false' in self.fd:
                flag4=True
            else:
                flag4=False
        while flag5:
            self.fd=re.sub('true','True',self.fd)
            if 'true' in self.fd:
                flag5=True
            else:
                flag5=False
        while flag6:
            self.fd=re.sub('null','None',self.fd)
            if 'null' in self.fd:
                flag6=True
            else:
                flag6=False
        self.FD=eval(self.fd)
           
        
            #print(apd.values()[0]['session'])
    def badass(self,vfnum):
        self.vfnum=vfnum
        if  vfnum==3:
            print('你太笨了，我走了.')
            self.kg=False
            self.ekg=False
        else:
            self.vfnum+=1
        return self.vfnum
        
    def ask_me(self,id,sheet,no=1):
        self.furl=''
        self.xdata={}
        self.ydata={}
        self.rd_data(sheet)
        self.nm=''
        for apdta in self.appdata:
            for k,v in apdta.items():
                if k==id:
                    self.ydata=v[2]
                    self.xdata=v[3]
        self.mk_sign(self.ydata,no)
        self.furl=self.appurl+'?'+self.link
        

    
    
if __name__=='__main__':
    #APIReader().get_TEMP(1)
    APIReader().rd_data('充值取现类')
    #APIReader().ask_me('7','充值取现类')
    #APIReader().get_title('用户中心')