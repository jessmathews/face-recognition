import os
path="C:\\Users\\aksha\\OneDrive\\Desktop\\face_recognition\\FacialRecognition\\dataset"
images = os.listdir(path=path)
j=1
imagePaths = [os.path.join(path,f) for f in images]
for i in imagePaths:
    os.rename(i,path+"\\"+"User.6."+str(j)+".jpg")
    print(i)
    if j==200:
        break
    else:
        j=j+1
print("completed")