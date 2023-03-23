"""
lab 9
"""

class my_stat(): 
    def cal_sigma(self,m,n):
        result = 0
        for i in range(n, m+1):
            result = result +i
        return result
    
    def cal_pi(self,m, n):
        result = 1
        for i in range(n, m+1):
            result = result * i
        return result
        
    def cal_fact(self,m):
        if m==0:
            return 1
        else: 
            return m*self.cal_fact(m-1)
    
    def cal_perm(self,m,n):
        return self.cal_fact(m)/self.cal_fact(m-n)
    
            
        