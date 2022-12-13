import os,sys
from uuid import uuid4
from statr import *
from compile import CompileCpp
from sandbox import SandBoxRun
from comparison import ComParisonAns
class CPprgCPP(CompileCpp,SandBoxRun,ComParisonAns):
    BASE_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),"temp")
    def mkstemp(self,suffix,text,tt=None):
        t=str(uuid4())
        ttt=0
        if text:
            ttt=open(os.path.join(self.BASE_DIR,t+suffix),"w+",encoding="utf-8")
        else:
            ttt=open(os.path.join(self.BASE_DIR,t+suffix),"wb+")
        if tt!=None:
            ttt.write(tt)
        ttt.close()
        return os.path.join(self.BASE_DIR,t+suffix)
    def readfile(self,path):
        t=open(path,"r")
        tt=t.read()
        t.close()
        return tt
    def delout(self):
        if(os.path.exists(self.fname_in)):
            os.remove(self.fname_in)
        if(os.path.exists(self.fname_out)):
            os.remove(self.fname_out)
        if(os.path.exists(self.fname_ans)):
            os.remove(self.fname_ans)
        if(os.path.exists(self.fname_file)):
            os.remove(self.fname_file)
        if(os.path.exists(self.fname_efile)):
            os.remove(self.fname_efile)
    def run(self,stdin,stdans,stdfile):
        try:
            self.fname_in=self.mkstemp(suffix=".in",text=True,tt=stdin)
            self.fname_out=self.mkstemp(suffix=".out",text=True,tt="")
            self.fname_ans=self.mkstemp(suffix=".ans",text=True,tt=stdans)
            self.fname_file=self.mkstemp(suffix=".cpp",text=True,tt=stdfile)
            self.fname_efile=os.path.join(self.BASE_DIR,str(uuid4())+".exe")
            if self.compile(self.fname_file,self.fname_efile,sys.stdout)!=0:
                self.delout()
                return CE
            t=0
            t=self.runPrg(None,self.fname_efile,self.fname_in,self.fname_out)
            if t==1:
                self.delout()
                return TLE
            elif t==2:
                self.delout()
                return MLE
            elif t==3:
                self.delout()
                return RE
            t=self.comparison(stdans,self.readfile(self.fname_out))
            if t==-1:
                self.delout()
                return WA
            elif t==1:
                self.delout()
                return PC
            elif t==2:
                self.delout()
                return OLE
            self.delout()
            return AC
        except Exception as e:
            self.delout()
            return UKE
t=open("I:\\exe\\python\\pythonOJSandbox\\temp\\KAJjKAJj.cpp")
tt=t.read()
t.close()
print(CPprgCPP().run("5 12","17",tt).chinese)