import os


# def trazilica():
#     for folderName, subfolders, filenames in os.walk('E:\\devanje'):
#         for subfolder in subfolders:
#             for filename in filenames:
#                 if filename == "fajl.txt":
#                     statinfo = os.stat(filename)
#                     return('FILE INSIDE ' + folderName + ': ' + filename + '\n' + 'File size: ' + statinfo)


# print(trazilica())
statinfo = os.stat("fajl.txt")
print(statinfo)
