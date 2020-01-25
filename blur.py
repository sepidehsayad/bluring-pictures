import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import signal


def get_picture_convert_to_gray(): #because matplotlib just take a png, we can convert png to bmp(gray scale) with this fucntion

    fname = 'download.png' # name of picture
    image = Image.open(fname).convert("L")
    old_pic_pix = np.asarray(image)
    
    plt.imshow(old_pic_pix, cmap='gray', vmin=0, vmax=255) 
    plt.show()         
    return old_pic_pix



def get_mask_from_input():
    rows = int(input("Enter the number of rows : "))
    columns = int(input("Enter the number of columns : "))
    print("Enter",rows*columns,"number :(Enter 1 number then press enter)")
    row, col = (rows,columns)
    mat = [[int(input()) for i in range(col)] for j in range(rows)]
    
    print("mask: ",mat)
    
    return mat

def conv(arr,mask):
    sm=[]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sm+=[arr[i][j]*mask[i][j]]
    q=0
    for i in sm :
       q+=i
    return q


def slice_(old_pic_pix,mask):
    num=len(mask)
    rows, cols = (len(old_pic_pix)-num,len(old_pic_pix[0])-num)
    arr2 = [[0 for i in range(cols)] for j in range(rows)]
    arr = [[0 for i in range(num)] for j in range(num)]
    xs=old_pic_pix

    for i in range(0,len(old_pic_pix)-num):
       for k in range(0,len(old_pic_pix[i])-num):
            for j in range(num):
                n=0
                for z in range(k,k+num):
                    arr[j][n]=xs[j+i][z]
                    n+=1
                    
            temp =conv(arr,mask)
            arr2[i][k]=int((temp)/(num*num))
            arr = [[0 for i in range(num)] for j in range(num)]
    #print(arr2)
    return arr2

oldpix=get_picture_convert_to_gray()
kernel=get_mask_from_input()
print("first you see a orginal picture then you see a blur picture :)")
b=slice_(oldpix,kernel)
plt.imshow(b, cmap='gray', vmin=0, vmax=255)
plt.show()


