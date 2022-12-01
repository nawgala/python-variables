import os
print(os.environ.keys())
list = list(os.environ.keys())
print(list)

print(os.environ.get('JAVA_HOME'))