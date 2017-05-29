"""
Batch processing the Japanese sentences parsing.
The results will be stored in a dir. 
If the dir is not settled, the program will new one automatically.
"""
import os
import MeCab
def fenci(argv,path) :
    #the dir saving the results of the parsing
    sFilePath = './segfile'
    if not os.path.exists(sFilePath) : 
        os.mkdir(sFilePath)
    #reading the documents
    filename = argv
    f = open(path+filename,'r+')
    file_list = f.read()
    f.close()
    
    #using MeCab parsing
    seg_list = MeCab.Tagger()
    seg_list = seg_list.parse(file_list)

    #dealing with the space and the line break
    result = []
    for seg in seg_list :
        seg = ''.join(seg.split())
        if (seg != '' and seg != "\n" and seg != "\n\n") :
            result.append(seg)

    #the result save with the space
    f = open(sFilePath+"/"+filename+"-seg.txt","w+")
    f.write(' '.join(result))
    f.close()
