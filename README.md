# OCR testing nbdev environment
> Third attempt at working with nbdev.


This code can: (hopefully, when it's done.)
    1. Create images from text files. Use various fonts and sizes.
    2. Manipulate the images to simulate poor quality scans.
    3. Send images to Google, Amazon and Microsoft to OCR.
    4. Collect the results from each service.
    5. Calculate the error rate for each text and service.
    6. Show the differences between each OCR result and the orginal.

## Install

`pip install ocr_dev`

## How to use


Create text files to use. Save them in a folder. Point the code to that folder. Specify where to save the images and how to make them.
Specify adjustments to the images.
In order to send the images to any service you'll need an account with that service. The services are: Amazon Web Services Vision. Google Cloud Platform Read. Microsoft Azure OCR. Microsoft has a limited number of languages that it supports and if the text isn't in one of those then it won't return any results.

Specify which services to send the images.



```python
1+1
```




    2


