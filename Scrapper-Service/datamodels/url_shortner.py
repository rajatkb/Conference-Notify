import re
import math

class Url_To_Id():
    
    def __init__(self,url):
        '''
            [url_to_id class]
            Used for genration of the unique ID
            
            Arguments:
                __url(String): it is store the url
                __mapping(string): it is used for mapping the number to string
                __char_mapping(dictionary): it is used for mapping each character to its numeric value
        '''
        self.__url = url
        self.__mapping = self.genrate_Sequence()
        self.__char_mapping = self.genrate_map()
        self.__n = len(self.__mapping)
        '''
            it is used to genrate mappping string
            __mapping: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
            
        '''
    def genrate_Sequence(self):
        res=[]
        for i in range(26):
            res.append(chr(i+97))
        for i in range(26):
            res.append(chr(i+65))
        for i in range(10):
            res.append(chr(i+48))
        return res
    '''
        It is used for dividing large string number
        eg: 1123452344323 / 100 = 11234523443
    '''
    def longDivision(self,number, divisor):
        
        if(int(number)>=0 and int(number) <= self.__n ):
            return number
        
        ans = "";  
        idx = 0;  
        temp = ord(number[idx]) - ord('0'); 
        while (temp < divisor): 
            temp = (temp * 10 + ord(number[idx + 1])-ord('0')); 
            idx += 1; 
        idx +=1;  
        
        while ((len(number)) > idx):  
            ans += chr(math.floor(temp // divisor) + ord('0'));  
            temp = ((temp % divisor) * 10 + ord(number[idx])-ord('0')); 
            idx += 1; 
        ans += chr(math.floor(temp // divisor) + ord('0')); 
        if (len(ans) == 0):  
            return "0";  
        else: 
            return ans;  
        '''
            It is used to calculate the modulus of number
            eg: 1123423423423 % 10 =3
        '''
    def longmod(self,number, divisor):
        res = 0
        for i in range(0, len(number)): 
            res = (res * 10 + int(number[i])) % divisor; 
        return res 
    '''
        It is used to genrate mapping dictionary alphabet to numeric value
        ef  dict = {'a':1,'b',2,........}
    '''
    def genrate_map(self):
        dct={}
        for i in range(len(self.__mapping)):
            dct[self.__mapping[i]]=i+1
        return dct
    
    '''
        It will convert url to numeric mapping
        eg: 
            step 1)
                www.google.cm  :- wwwgooglecom
                
            step 2)
                wwwgooglecom :-  232323715157125313
            
            step 3)
                232323715157125313:- vWXh2rXck
    '''
    def hash_string(self,text):
        unique_id = ''
        for i in range(len(text)):
            unique_id+=str(self.__char_mapping[text[i]])
#        print(unique_id)
        result=''
        while(int(unique_id)> self.__n):
            result += self.__mapping[self.longmod(unique_id,self.__n)]
            unique_id = self.longDivision(unique_id,self.__n)
        if(result==''):
            return self.__mapping[self.longmod(unique_id,self.__n)]
        return result
    
    '''
        URL:   https://www.amazon.in/hfc/mobileRecharge?ref_=apay_pc_qc_rech
        UNIQUE_ID:  qlmeuCU94uSKsIEcG5AmVYHjqdWipCwz2en5Yxp
    '''    
    def getKey(self):
        text = re.sub("[^A-Za-z0-9]",'',self.__url)
#        print(text)
        return self.hash_string(text)

#if __name__ == "__main__":
#    print(Url_To_Id("www.google.cm").getKey())
#    
#    
#


