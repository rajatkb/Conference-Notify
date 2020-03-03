import re
import random as r
import timeit

class Uuid:
    """
        url {{string}}: url used in class
    """
    def __init__(self,url):
        self.url = url    
    """
         remove punctuation from string and compress string
         eg www.google.com-> wwwgooglecom -> w3g1o2g1l1e1c1o1m1
    """
    def clean_and_compress(self):
            value = re.sub('[^A-Za-z0-9]','',self.url)+'#'
            res=''
            j=0
            while(j<len(value)-1):
                c=1
                while(value[j]==value[j+1]):
                    c+=1
                    j+=1
                res+=str(value[j])+str(c)
                j+=1
            return res
    """
        convert it to hexadecimal format
    """
    def toHex(self,string):
        lst = []
        for ch in string:
            hv = hex(ord(ch)).replace('0x', '')
            if len(hv) == 1:
                hv = '0'+hv
            lst.append(hv)
        return ''.join(lst)
    """
        genrate unique ID
    """
    def generate_uuid(self):
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uuid_format = [8, 4, 4, 4, 12]
        for n in uuid_format:
            for i in range(0,n):
                random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
            if n != 12:
                random_string += '-'
        return self.toHex(self.clean_and_compress())+"-"+random_string

#   Testing purpose
#if __name__ ==  "__main__":
#    start = timeit.timeit()
#    collision_list=[]
#    collision=0
#    i=0
#    with open("domain.txt",'r') as f:
#        list_of_domain = f.readlines()
#        for x in list_of_domain:
#            x = Uuid(x).generate_uuid()
#            if x not in collision_list:
#                print(x)
#                collision_list.append(x)
#            else:
#                collision+=1
#            i+=1
#    end = timeit.timeit()
#    print("test results "+str(i)+" cases:")
#    print("number of collision: ",collision)    
    
    
#output:
#    test results 10000 cases:
#    number of collision:  0
#    
    
    
    