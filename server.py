"""Serve the emotion analysis web application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_analyzer

app = Flask("Emotion Analyzer")


@app.route("/emotionDetector")
def emotion_detector():
    """Analyze the supplied text and display its emotion scores."""
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_analyzer(text_to_analyse)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid input ! Try again."

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Display the application's home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    