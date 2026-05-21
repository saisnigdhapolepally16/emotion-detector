"""
Flask server for emotion detector.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotion route.
    """

    text_to_analyze = request.args.get(
        'textToAnalyze'
    )

    response = emotion_detector(
        text_to_analyze
    )

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render main page.
    """

    return """
    <html>
        <body>
            <h1>Emotion Detector</h1>

            <form action="/emotionDetector">

                <input
                    type="text"
                    name="textToAnalyze"
                    placeholder="Enter text"
                >

                <input
                    type="submit"
                    value="Analyze"
                >

            </form>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
