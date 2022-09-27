# Airplane Parts detection with Convolutional Neural Networks✈️🧠

Due to the need to develop an efficient and automatic technology for the detection of the in-flight refuelling pole of an MRTT, it is considered that an optimal way to achieve this knowledge is the construction of a neural network to detect the different parts of the aircraft.

This project proposes the creation from the first stage to the end of a convolutional neural network to detect the different parts of the aircraft.

This type of network has been selected due to the success it has had in recent history for similar tasks of detecting objects through images.

The project consisted of 4 distinct phases.

- Data collection
- Data preparation
- Model application
- Conclusions

![Image1](/images/prediction_img3.png?raw=true) ![Image2](/images/prediction_img1.png?raw=true) ![Image3](/images/prediction_img2.png?raw=true)

## Data collection and Data preparation📚
For this part, a total of 2000 aircraft images were collected from a Kaggle database. Subsequently, the different parts of the aircraft considered for the study have been labelled in each one of them
- Fuselage
- Rear part
- Engine
- Wings

The well-known LabelImg software has been used for labelling.

## Model application🔂 
Three models have been implemented. All of them start from the learning transfer of the VGG16 model on the "imagenet" dataset.
1. VGG16 without the fully connected layer.
2. VGG16 without the fully connected layer and with Data Augmentation
3. VGG16 with Fine-Tuning on the last convolutional block.

In the `training.ipynb` and `training_finetuning.ipynb` code, you can see the process followed and how the necessary transformations and adjustments to the model parameters are made in order to reach the best possible result.

## Conclusions📊
Below is a table with the results obtained for different metrics.
| Model | Accuracy | Precision | Recall |
| ------ | ------ | ------ | ------ |
| VGG16 | 0,283 | 0,284 | 0,283 |
| VGG16 + Data Augmentation | 0,349 | 0,417 | 0,349 |
| VGG16 + Data Augmentation + Fine-tuning | 0,340 | 0,459 | 0,340 |


As can be seen, the results are not quite what a proper model expects, as they are far from achieving good accuracy and other metrics. This is due to the fact that it is a dataset with a limited number of data and therefore tends to over-fitting, although a significant improvement can be seen by increasing the number of images using techniques such as Data-Augmentation.

There are two codes where prediction are performed: `prediction.ipynb` (images) and `videoprediction.ipynb` (video).

### DEMO
[![Video1](/images/predictvideo.gif)](https://github.com/ignareyesa/cnn_airplane_parts)

#### Future work🔨
1. Extend the image set: Reduce overfitting and increase accuracy.
2. Find the best model configuration: Test more models and adjust new hiperparameters.
3. Add new functionalities: Real-time image recognition and add new categories and aircraft parts.

---------------------------------------------------------------------------------------------------------------------

Ignacio Reyes Arboledas

**[Go back to website](https://ignacioreyesarboledas.tech/)** &#128522;
