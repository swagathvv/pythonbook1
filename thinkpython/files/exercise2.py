import sys

def sed(pattern,replace,source,dest):
    try:
        fin=open(source,'r')
        fout=open(dest, 'w')
        for line in fin:
            line=line.replace(pattern,replace)
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print('something went wrong')

def main(name):
    pattern='pattern'
    replace='replace'
    source= name
    dest= name+ '.replaced'
    sed(pattern,replace,source,dest)

if __name__ == '__main__':
    main(*sys.argv)

