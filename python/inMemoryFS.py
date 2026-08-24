# 

# Binary Tree -> 

# Node
    # Each node can have a dict with inner directories
    # At that node we can have a dictionary of files - name/content

class Node:
    def __init__(self):
        self.subdirs = {}
        self.files = {}

class FileSystem:
    def __init__(self):
        self.root = Node() # This is /
    
    def ls(self, path):
        pathParts = path.split('/')
        dest = pathParts[-1]
        curr = self.root
        
        for p in pathParts[1:-1]:
            curr = curr.subdirs[p]
        
        if dest in curr.files:
            return [dest]
        else:
            if dest:
                curr = curr.subdirs[dest]
                
            everything = list(curr.files.keys()) + list(curr.subdirs.keys())
            everything.sort()
            
            return everything
        # If path is a file return a list containing only that file name
        # If path is a directory reeturn all files and directories direxcly inside it
        # Results myst be lexigraphically sorted
    
    def mkdir(self, path):
        pathParts = path.split('/')
        curr = self.root
        
        for p in pathParts[1:]:
            if p not in curr.subdirs:
                curr.subdirs[p] = Node()
                
            curr = curr.subdirs[p]
        # creates the directory at path + any intermediates
    
    def addContentToFile(self, filePath, content):
        pathParts = filePath.split('/')
        file = pathParts[-1]
        curr = self.root
        
        for p in pathParts[1:-1]:                
            curr = curr.subdirs[p]
        
        if file not in curr.files:
            curr.files[file] = content
        else:
            curr.files[file] += content
        # if file does not exist create it with content
        # if it doesnt exist - append content
        
    def readContentFromFile(self, filePath):
        pathParts = filePath.split('/')
        file = pathParts[-1]
        curr = self.root
                
        for p in pathParts[1:-1]:                
            curr = curr.subdirs[p]
            
        return curr.files[file]
        # Retrun the file's content
        
    # Paths are absolute and begin with /
    # Paths dont end with / except / itself
    # names LC only
    # no duplicate file/directories
    # All operations use valid paths
    