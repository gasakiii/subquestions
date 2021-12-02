import os
import sys
import numpy as np
from PIL import Image, ImageDraw
import cv2
import matplotlib.pyplot as plt


# imgpath = '/Users/uchiga/Documents/220114/image/Shukan/'
# txtpath = '/Users/uchiga/Desktop/testimage/1true/'
# savepath = '/Users/uchiga/Documents/220114/image/Shukan2/'

textSSIMs = [95, 90, 85]
imgnums = [1,2,4,6,15,17,20,27,28,32]
count = 0

if __name__ == "__main__":
    args = sys.argv
    try:
        qid = int(args[1])
    except:
        print("Please input questionnaire ID.")
        exit()

    max_id = 16
    if (qid < 0) or (qid > max_id):
        print("ID must be 1 - %d"%(max_id))
        exit()

    img_dir = "imgs"
    txt_dir = "region"
    res_name = 'result_'+str(qid)+'.txt'

    with open(res_name, 'a') as f:
        f.write(str(qid) + '\n')
        
    for textSSIM in textSSIMs:
        for imgnum in imgnums:
            imgname = str(textSSIM) + '_' + str(imgnum) + '.png'
            if os.path.exists(os.path.join(img_dir, imgname)):

                txtname = 'res_img_'+str(imgnum)+'.txt'
                with open(os.path.join(txt_dir, txtname)) as f:
                    lines = f.readlines()

                xy = np.zeros(4)
                for z, line in enumerate(lines):
                    count += 1
                    for i in range(4):
                        xy[i] = int(line.split(',')[i])

                    gray = cv2.imread(os.path.join(img_dir, imgname),cv2.IMREAD_GRAYSCALE)
                    gray_three = cv2.merge([gray,gray,gray])

                    cv2.rectangle(gray_three, (int(xy[0])-2, int(xy[1])-2), (int(xy[0])+int(xy[2])+2, int(xy[1])+int(xy[3])+2), (255,0,0))

                    fig = plt.figure()
                    plt.imshow(gray_three)
                    # plt.tight_layout()
                    plt.pause(0.01)

                    while True:
                        print("+--------------------------------------------------")        
                        print('| 5点 ： 全て問題なく読める')
                        print('| 4点 ： 概ね読めるが、一部読みづらい文字がある')
                        print('| 3点 ： 一部読めない文字がある')
                        print('| 2点 ： 大半が読めない')
                        print('| 1点 ： 全く読めない')
                        print("+--------------------------------------------------")        
                        val = input("{} / 93 :Put your score >> ".format(count))
                        if int(val)>=1 and int(val)<= 5:
                            with open(res_name, 'a') as f:
                                f.write(val + '\n')
                            break
                        else:
                            print('****** Please Input score 1~5 *******')
                            continue

                    plt.close()

    print('\n')
    print("+-----------------------------------------")
    print('| This question is completed!')
    print("| Your answer is saved in 'result_{}.txt'.".format(qid))
    print("| Please submit your answer to this URL:")
    print("| URL")
    print("| Thank you very much for your cooperation!!")
    print("+-----------------------------------------")


