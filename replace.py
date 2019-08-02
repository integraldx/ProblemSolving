import sys

importedHeaders = set()

def PrintNewFile(filePath : str):
    f = open(filePath, 'r')
    for s in f.readlines(99999):
        if s.startswith("#include "):
            s = s[9:]
            if s.startswith("\""):
                s = s.strip("\"\n")
                if not importedHeaders.__contains__(s):
                    importedHeaders.add(s)
                    PrintNewFile(s)
            else:
                s = s.strip("<>\n")
                if not importedHeaders.__contains__(s):
                    importedHeaders.add(s)
                    print("#include <" + s + ">")
        else:
            print(s.strip("\n\r"))

filePath = input()
PrintNewFile(filePath)