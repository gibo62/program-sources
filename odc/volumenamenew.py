import win32api
print (win32api.GetVolumeInformation("D:\\")[0])
