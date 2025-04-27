import transformers
from transformers import pipeline

pipe = pipeline("text-classifixation")
pipe("The weather is looking good, seems that there will be no rain")
