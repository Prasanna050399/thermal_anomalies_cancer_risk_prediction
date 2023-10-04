#BGR
import cv2
import matplotlib.pyplot as plt
import numpy as np
coordinates = list()
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (255, 255, 255), 2)
        coordinates.append((y,x))
        print(x, y, img[y][x])
        cv2.imshow('image',img)
        cv2.waitKey()
        


#full_images = ["001.png", "002.png", "003.png", "004.jpg", "005.jpg", "006.jpg", "007.jpg", "008.jpg", "009.jpg", "010.jpg", "011.jpg", "012.jpg", "013.jpg", "014.jpg", "015.jpg"]
#images = ["001_res.png", "002_res.png", "003_res.png", "004_res.png", "005_res.png", "006_res.png", "007_res.png", "008_res.png", "009_res.png", "010_res.png", "011_res.png", "012_res.png", "013_res.png", "014_res.png", "015_res.png"]
images = ["001.png", "002.png", "003.png", "004.jpg", "005.jpg", "006.jpg", "007.jpg", "008.jpg", "009.jpg", "010.jpg", "011.jpg", "012.jpg", "013.jpg", "014.jpg", "015.jpg", "016.jpg", "017.jpg", "018.jpg", "019.jpg", "020.jpg", "021.jpg", "022.jpg", "023.jpg", "024.jpg", "025.jpg", "026.jpg", "027.png", "028.png", "029.png", "030.png", "031.png"]
for i in images[15:]:
    # read the image
    img = cv2.imread(i)
    img = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LANCZOS4)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',click_event)
    cv2.waitKey(0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    #plt.show()
    cv2.destroyAllWindows()
    #print(coordinates)
    coor = coordinates.pop()

    image = cv2.imread(i)
    image = cv2.resize(image, (640, 480), interpolation = cv2.INTER_LANCZOS4)
    img_enhanced = cv2.detailEnhance(image, sigma_s=10, sigma_r=0.15)
    # convert to RGB
    img = cv2.cvtColor(img_enhanced, cv2.COLOR_BGR2RGB)
    
    #img = cv2.imread('home.jpg')
    Z = img.reshape((-1,3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 8
    ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    #res2 = cv2.cvtColor(res2, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(res2, cv2.COLOR_RGB2GRAY)
    #for i in range(gray.shape[0]):
    #    for j in range(gray.shape[1]):
    #        r,g,b = res2[i][j][0],res2[i][j][1],res2[i][j][2]
    #        if g>r and g>b:
    #            #if r-b > r*50/100:
    #            #    val = 0.3*r + 0.1*g + 0.2*b
    #            #elif b-r > b*50/100:
    #            #    val = 0.2*r + 0.1*g + 0.3*b
    #            #else:
    #            #    val = 0.3*r + 0.59*g + 0.11*b
    #            val = 0.3*r + 0.59*g + 0.11*b
    #        else:
    #            val = 0.2*r + 0.1*g + 0.2*b
    #        #val = 0.1*res2[i][j][0] + 0.6*res2[i][j][1] + 0.1*res2[i][j][2]
    #        gray[i][j] = val

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            #val = -0.1*res2[i][j][0] + 0.7*res2[i][j][1] + 0.1*res2[i][j][2]
            #if val < 0 :
            #    val = 0
            #if val > 255:
            #    val = 255
            #val = 0.1*res2[i][j][0] + 0.7*res2[i][j][1] + 0.1*res2[i][j][2]
            val = 0.1*res2[i][j][0] + 0.6*res2[i][j][1] + 0.1*res2[i][j][2]           
            gray[i][j] = val

    
    x,y = coor
    avg = 0

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            #print(i,j)
            avg += gray[i][j]
    avg /= 9

    pixel = list()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if gray[i][j] > 0 :
                pixel.append((i,j))


    position = list()
    #thresh = 15
    #while len(position)==0 and thresh>10:
    for x,y in pixel:
        temp = avg - gray[x][y]
        if temp > avg*15/100:
            #image[x][y] = [100,100,100]
            position.append((x,y))
    #    thresh -= 1
    #    print(thresh,len(position))
    #print(position)
    for x,y in position:
        if image[x][y][0] < image[x][y][2]:
            #red
            image[x][y] = [100,100,200]
        elif image[x][y][0] > image[x][y][2]:
            #blue
            image[x][y] = [200,100,100]

##    for i in range(image.shape[0]):
##        for j in range(image.shape[1]):
##            if image[i][j][0] >= 200 and image[i][j][1] >= 200 and image[i][j][2] >= 200:
##                image[i][j] = [100,100,200]
    #cv2.imshow('res',res2)
    cv2.imshow('result', image)
    cv2.imshow('gray',gray)
    #cv2.imshow('res2',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    ans = input('do you want to continue?(y/n) ')
    if ans == 'n' or ans == 'N':
        break
