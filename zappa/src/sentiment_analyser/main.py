from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from textblob import TextBlob


app = FastAPI()


class TextInput(BaseModel):
    text: str


@app.post("/analyse-sentiment")
async def analyze_sentiment(input: TextInput):
    blob = TextBlob(input.text)
    sentiment = blob.sentiment
    print(sentiment.polarity)  # -1 (negative) to 1 (positive)
    label = "positive" if sentiment.polarity > 0 else "negative"
    return {"label": label, "polarity": sentiment.polarity}


handler = Mangum(app)
