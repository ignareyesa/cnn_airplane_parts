import os
import datetime

URL_DRIVE = "drive/MyDrive/TFM/"

IMAGE_PATH = URL_DRIVE + "preparation/in/images/"

MODEL_VERSION="vgg16"
NUMBER_VERSION = "1.0"

MODEL_PATH = URL_DRIVE + "output/" + MODEL_VERSION + "/"
ACTUAL_PATH = MODEL_PATH + NUMBER_VERSION + "/"

OUTPUT_PATH = ACTUAL_PATH
LOG_DIR = URL_DRIVE + "logs/fit/" + MODEL_VERSION + "-" + NUMBER_VERSION
PLOT_PATH = ACTUAL_PATH + "plots"

TEST_SIZE_SPLIT=0.20


LOSS_LABEL = "categorical_crossentropy"
LOSS_BOUNDINGBOX = "mean_squared_error"
LOSS_WEIGHT = float(1.0)
INIT_LR = 1e-4
MODEL_METRICS = ["accuracy"]
NUM_EPOCHS = 25
BATCH_SIZE = 32


#True if you want to print the summaries of the model
PRINT_SUMMARY = False
try:
  os.mkdir(MODEL_PATH)
except:
  pass
  
try:
  os.mkdir(ACTUAL_PATH)
except:
  pass

try: 
  os.mkdir(PLOT_PATH)
except:
  pass