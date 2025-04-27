import transformers
from transformers import pipeline

pipe = pipeline("sentimental-classifixation")
pipe("The weather is looking good, seems that there will be no rain")
