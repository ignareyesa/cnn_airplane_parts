import os
import datetime

URL_DRIVE = "drive/MyDrive/TFM/"

IMAGE_PATH = URL_DRIVE + "preparation/in/images/"
VIDEO_INPUT_PATH = URL_DRIVE + "videos/"

MODEL_VERSION="vgg16"
NUMBER_VERSION = "1.0"
FINE_TUNING = False

MODEL_PATH = URL_DRIVE + "output/" + MODEL_VERSION + "/"
ACTUAL_PATH = MODEL_PATH + NUMBER_VERSION + "/"
NON_FINETUNING_PATH = ACTUAL_PATH + "normal/"
FINETUNING_PATH = ACTUAL_PATH + "finetuning/"

if FINE_TUNING:
  OUTPUT_PATH = FINETUNING_PATH
  LOG_DIR = URL_DRIVE + "logs/fit/" + MODEL_VERSION + "-" + NUMBER_VERSION + "-normal"

else: 
  OUTPUT_PATH = NON_FINETUNING_PATH
  LOG_DIR = URL_DRIVE + "logs/fit/" + MODEL_VERSION + "-" + NUMBER_VERSION + "-fine_tuned"


PLOT_PATH = OUTPUT_PATH + "plots"
VIDEO_OUTPUT_PATH = OUTPUT_PATH + "videos/"

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
  os.mkdir(OUTPUT_PATH)
except:
  pass

try: 
  os.mkdir(PLOT_PATH)
except:
  pass

try:
  os.mkdir(VIDEO_OUTPUT_PATH)
except:
  pass