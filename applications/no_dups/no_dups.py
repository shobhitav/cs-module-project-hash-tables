def no_dups(s):
    count={}
    new_string_list=s.split()
    
    if s=="" :
        count[s]=1
        dict_list=list(count.keys())
        return dict_list

         
    else:    
        for str in new_string_list :
            
            if str in count:
                count[str]+=1
            else:
                count[str]=1 

    # print(count)
    dict_list=list(count.keys())
    return dict_list   
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))