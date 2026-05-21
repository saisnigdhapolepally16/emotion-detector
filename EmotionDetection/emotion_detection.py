"""
Emotion detection module.
"""


def emotion_detector(text_to_analyse):
    """
    Mock emotion detector function.
    """

    text = text_to_analyse.lower()

    if text.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if "glad" in text or "happy" in text:
        dominant = "joy"

    elif "mad" in text or "angry" in text:
        dominant = "anger"

    elif "disgusted" in text:
        dominant = "disgust"

    elif "sad" in text:
        dominant = "sadness"

    elif "afraid" in text or "fear" in text:
        dominant = "fear"

    else:
        dominant = "joy"

    emotions = {
        'anger': 0.02,
        'disgust': 0.01,
        'fear': 0.05,
        'joy': 0.88,
        'sadness': 0.04,
        'dominant_emotion': dominant
    }

    return emotions