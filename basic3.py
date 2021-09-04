mf = open(r'subtitles.txt', 'r+')
content = mf.read()

try:
    for i in range(len(content)):
        if (content[i]=='\n'):
            if(content[i-1] >= 'A' and content[i-1]<='Z') or (content[i-1] >= 'a' and content[i-1]<='z') or (content[i-1]=='.'):
                if( i+1<len(content) and content[i+1] >= '0' and content[i+1] <= '9'):
                    j=i+1
                    while( content[j]>='0' and content[j]<='9'):
                        j+=1
                    if( j< len(content)):
                        content = content[:i+1] + content[j:]
                        i -= (j-i)
                    else:
                        content = content[:i+1]
                        i-=2
 
finally:
    print(content)
    mf.seek(0)
    mf.write(content)
    mf.close()


