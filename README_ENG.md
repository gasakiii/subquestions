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
By copying this repository, you can use python to display the image and enter the score on the terminal.


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

## Experimental procedure
When you are ready, you can start the evaluation experiment by running the following command

```
$ python main_ENG.py {id}
```

When you run the command, you will see an image with the specified text area surrounded by a red frame, and the following text on the terminal.

<p align="center">
  <img width="240" height="320" src="https://github.com/gasakiii/subquestions/blob/main/temp_img/85_1_1.png">
</p>

```
+--------------------------------------------------
| image 1 / 30, number of text regions 1 / 3
+--------------------------------------------------
| 5 : all readable without problems
| 4 : Generally readable, but some text is difficult to read.
| 3 : Some of the text is unreadable.
| 2 : Most of the text is unreadable.
| 1 : Not readable at all
+--------------------------------------------------
Put your score >> 
````

```
image 1 / 30, number of text regions 1 / 3
```

The image is the current number of images, and the number of text regions is the current number of text regions in the image.

The number of text regions represents the number of text regions in the current image. Enter a score for each text region surrounded by a red frame, according to the given score.

Enter a score from 1-5 and press Enter to move on to the next text region or image.


## How to submit

Once you have answered all the questions for all the images, a file "result_{id}.txt" will be generated in the directory.

Send this to the following link

https://www.dropbox.com/request/MQjqFRoDhzmkvg3zbL7u

Thank you very much for your cooperation!

