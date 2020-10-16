# Object detection using haar cascades

This is a tool to help you train your model to detect objects in an image/video using haar cascades

### Steps to follow

- Grab a 50*50 jpg image and name it "image.jpg"
- Execute 1-createsamples
- Execute 2-vec
- Execute 3-training (it will take a while to complete depending on you machine specs)
- Execute 4-conv it will convert the training data into an xml file
- to test your xml file rename it to test.xml and execute test.py

> Please note that this tool is not suitable for face detection as the images in "neg" folder have people in them so unless you want the tool to succeed at detecting faces you have to change the content of that folder with other 100*100 negative images of your choice