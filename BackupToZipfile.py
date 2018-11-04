import zipfile,os
os.chdir('D:\\manish')

folder=os.path.abspath('D:\\manish')
number=1
while True:
    zipfilename=os.path.basename(folder)+'_'+str(number)+'.zip'
    if not os.path.exists(zipfilename):
        break
    number=number+1
print('creating %s...'%(zipfilename))
backupzip=zipfile.ZipFile(zipfilename,'w')
for foldername,subfolders,filenames in os.walk(folder):
    print('Adding files in %s...'%(foldername))
    backupzip.write(foldername)
    for filename in filenames:
        newBase =os.path.basename(folder)+'_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue
        backupzip.write(os.path.join(foldername,filename))
backupzip.close()
