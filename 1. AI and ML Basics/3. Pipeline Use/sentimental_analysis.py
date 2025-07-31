import transformers
from transformers import pipeline

pipe = pipeline("sentimental-analysis")
pipe("The weather is looking good, seems that there will be no rain")
