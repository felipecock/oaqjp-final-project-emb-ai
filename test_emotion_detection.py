"""
This file contains the unit tests for the emotion_detection function from EmotionDetection package.
The function takes a string as input and returns the dominant emotion in the string as output.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    This class contains the unit tests for the emotion_detector function.
    """

    def test_emotion_detector(self):
        """
        This function tests the emotion_detector function from EmotionDetection package.
        """

        # Test case for joy emotion:
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

        # Test case for anger emotion:
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

        # Test case for disgust emotion:
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

        # Test case for sadness emotion:
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

        # Test case for fear emotion:
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


unittest.main()
