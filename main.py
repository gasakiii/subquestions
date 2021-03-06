import os
import sys
import numpy as np
from PIL import Image, ImageDraw
import cv2
import matplotlib.pyplot as plt

textSSIMs = [95, 90, 85]
imgnums = [1,2,4,6,15,17,20,27,28,32]
count = 0
imgcount = 0

if __name__ == "__main__":
    args = sys.argv
    try:
        qid = int(args[1])
    except:
        print("Please input questionnaire ID.")
        exit()

    max_id = 17
    if (qid < 0) or (qid > max_id):
        print("ID must be 1 - %d"%(max_id))
        exit()

    img_dir = 'original_imgs'
    txt_dir = 'region'
    res_name = 'result_'+str(qid)+'.txt'
    
    if os.path.exists(res_name):
        os.remove(res_name)

    with open(res_name, 'a') as f:
        f.write(str(qid) + '\n')
        
    for textSSIM in textSSIMs:
        for imgnum in imgnums:
            imgname = str(textSSIM) + '_' + str(imgnum) + '.png'
            imgcount += 1
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
                        print("| image  {} / 30, number of text region {} / {}".format(imgcount, z+1, len(lines)))
                        print("+--------------------------------------------------")        
                        print('| 5??? ??? ???????????????????????????')
                        print('| 4??? ??? ?????????????????????????????????????????????????????????')
                        print('| 3??? ??? ?????????????????????????????????')
                        print('| 2??? ??? ?????????????????????')
                        print('| 1??? ??? ??????????????????')
                        print("+--------------------------------------------------")        
                        val = input("Put your score >> ")
                        try:
                            if int(val)>=1 and int(val)<= 5:
                                with open(res_name, 'a') as f:
                                    f.write(imgname + ' ' + str(z+1) + ' ' + val + '\n')
                                break
                            else:
                                print('****** Please Input score 1~5 *******')
                                continue
                        except:
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


