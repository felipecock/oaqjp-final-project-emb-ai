"""
This module contains the function for emotion detection using the Watson NLP Library.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Function for running emotion detection using the Emotion Predict function of the
    Watson NLP Library.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing the detected emotions and the dominant emotion.
    """

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=payload, headers=headers, timeout=10)

    if response.status_code in [400, 401, 403, 404, 500, 503, 504]:
        error_messages = {
            400: {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            },
            401: {
                "error_code": 401,
                "error_message": (
                    "The Watson NLP service is not authorized to access the "
                    "requested resource."
                ),
            },
            403: {
                "error_code": 403,
                "error_message": (
                    "The Watson NLP service is forbidden to access the "
                    "requested resource."
                ),
            },
            404: {
                "error_code": 404,
                "error_message": "The Watson NLP service is not available.",
            },
            500: {
                "error_code": 500,
                "error_message": (
                    "The Watson NLP service is currently unavailable. "
                    "Please try again later."
                ),
            },
            503: {
                "error_code": 503,
                "error_message": (
                    "The Watson NLP service is currently unavailable. "
                    "Please try again later."
                ),
            },
            504: {
                "error_code": 504,
                "error_message": (
                    "The Watson NLP service is taking too long to respond. "
                    "Please try again later."
                ),
            },
        }
        return error_messages[response.status_code]

    formatted_response = json.loads(response.text)

    if "emotionPredictions" not in formatted_response:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": "none",
        }

    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    emotions = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        **emotions,
        "dominant_emotion": dominant_emotion,
    }
