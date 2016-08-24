import os
import time
print(os.getcwd())
metadata=os.stat("Files.py")
print(metadata)
print(time.localtime(metadata.st_mtime))
print("")