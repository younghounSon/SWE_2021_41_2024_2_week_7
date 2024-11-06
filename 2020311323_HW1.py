import sys
import random
import math

    
    
if __name__ == '__main__':
    
    stnum = sys.argv[0]
    stnum2=stnum[:10]
    
    casenum = sys.argv[1]
    util = sys.argv[2]
    iedd = sys.argv[3]
    f=open('./output/'+stnum2+'_'+casenum+'_'+util+'_'+iedd+'.txt','w')
    
    for i in range(100):
        usum=float(0)
        writestr = casenum+' '+util+' '+iedd
        sumU=float(util)
        utilnum=[]
        for k in range(1,int(casenum)):
            nextU=sumU*math.pow(random.random(),1/(int(casenum)-k))
            utilnum.append(sumU-nextU)
            sumU=nextU
        utilnum.append(sumU)
        for j in range(int(casenum)):
            a=random.randint(100,1000)
            b=round(a*utilnum[j])
            usum+=b/a
            
            writestr=writestr+' '+str(a)+' '+str(b)+' '
            if(iedd=='0'):
                writestr=writestr+str(a)
            else:
                writestr=writestr+str(random.randint(b,a))
                
        
        
        f.write(writestr+'\n')
    
    f.close()

       
   
   
   
   
   
   
    