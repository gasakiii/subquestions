# Subjective evaluation experiment on the text area of an image
## Purpose
Nowadays, images are widely used for communication due to the spread of smart phones and social networking services.
However, due to their large size, images must be compressed before they can be used for communication.
When compressing images, it is necessary to maintain high quality in the text area, which is considered to be the most important part of the image.
However, objective evaluation is not sufficient to determine the readability of text.

Therefore, we would like to ask you to make a subjective evaluation of the quality of text areas in an image.

I know you are busy, but I would appreciate it if you could help me.

There are 30 images in total, and 93 text areas. It should take about 10 minutes to complete.

## Repository contents
By copying this repository, you can use python to display images.

You will be asked to answer the evaluation values using a google form.

We recommend that you use your phone or tablet to answer the questions using the google form, while viewing and evaluating the images on your PC.

↓Click here for the answer form↓.

URL

## Preparing the programme
It is recommended to run the image display locally. The program runs in python3.

First, you can put this repository locally by running the following command

```
$ git clone https://github.com/gasakiii/subquestions.git
```

Next, go to the directory you copied (subquestions) and install the necessary packages with the following commands. (Skip if you don't need them)

```
$ cd subquestions
$ pip install -r requirements.txt
```

## 画像表示方法
When you are ready, you can start your evaluation experiment by running the following command

```
$ python main_ENG.py
```

When you run it, you will see an image and the following text on your terminal.
