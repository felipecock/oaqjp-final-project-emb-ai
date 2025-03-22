"""
This script defines the Flask server for the Emotion Detection App.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetectionApp")


@app.route("/")
def home():
    """
    Function for the home page of the Emotion Detection App.

    Returns:
        str: The HTML content for the home page.
    """

    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_app():
    """
    Function for running emotion detection using the Emotion Predict function of the
    Watson NLP Library.

    Returns:
        str: A plain text response containing the emotion analysis results.
    """

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Call the emotion_detector function from the EmotionDetection package
    result = emotion_detector(text_to_analyze)

    # Format the result as a string
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the result as a JSON response
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
