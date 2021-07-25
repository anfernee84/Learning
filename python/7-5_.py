import re
def capital_text(s):
    punc_filter = re.compile('([.!?;]\s*)')
    split_with_punctuation = punc_filter.split(s)
#    print(split_with_punctuation)
    for i,j in enumerate(split_with_punctuation):
        if len(j) > 1:
            split_with_punctuation[i] = j[0].upper() + j[1:]
    text = ''.join(split_with_punctuation)
    return text
    
print(capital_text("privet! kak tvoi dela?chto delzrsh?"))    
    
        
    
        
    
    
        
            
            
                
            
                
        
    