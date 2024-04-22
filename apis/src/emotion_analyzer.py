import os
from transformers import pipeline
from src.logger import Logger, log_time
import tensorflow as tf

class EmotionAnalyzer:
    @log_time
    def __init__(self, model_path: str = "SamLowe/roberta-base-go_emotions"):
        """
        Initialize the EmotionAnalyzer with a sentiment analysis pipeline and logger.

        Args:
            model_path (str): Path to the emotion analysis model. Default is the pre-trained model.
        """
        self.model_path = model_path
        self.emotion_pipeline_path = "./emotion_pipeline"
        os.makedirs(self.emotion_pipeline_path, exist_ok=True)
        
        if os.path.exists(os.path.join(self.emotion_pipeline_path, "config.json")):
            self.emotion_pipeline = pipeline(task="text-classification", model=self.emotion_pipeline_path, return_all_scores=True)
        else:
            self.emotion_pipeline = pipeline(task="text-classification", model=self.model_path, return_all_scores=True)
            self.emotion_pipeline.save_pretrained(self.emotion_pipeline_path)

    @log_time
    def analyze_response(self, text: str):
        """
        Analyze the emotion in the provided text response.

        Args:
            text (str): The text response to analyze.

        Returns:
            Tuple[str, float, str]: A tuple containing detected emotion, its score, and feedback.
        """
        result = self.emotion_pipeline(text)
        logger_all = Logger("all_results", see_time=True)
        logger_all.log_message(f"Detected emotions: {result}")
        
        emotions = [(emotion["label"], emotion["score"]) for emotion in result[0]]
        emotions = sorted(emotions, key=lambda x: x[1], reverse=True)
        
        return emotions
    
    def analyze_response_emotion(self, response: str) -> float:
        """
        Analyze the emotion in the provided text response.

        Args:
            emotion (str): The emotion to analyze.
            response (str): The text response to analyze.

        Returns:
            float: The score of the detected emotion.
        """
        emotions = self.analyze_response(response)
        if emotions:
            return emotions[0][0], emotions[0][1]
        return None, None

if __name__ == "__main__":
    analyzer = EmotionAnalyzer()
    user_input = "Thank you for your message. I will always strive to assist you with care, respect, and truth. I will provide you with the most useful and secure responses while avoiding any harmful, unethical, prejudiced, or negative content. My replies will always promote fairness and positivity.\nRegarding your question, love plays a crucial role in conflict management and resolution in family businesses. When conflicts arise in a family business, it is important to approach them with love and understanding. This means listening to each other's perspectives, seeking to understand their feelings and concerns, and working together to find solutions that benefit everyone involved.\nFamily businesses are unique in that they often involve personal relationships, and it can be challenging to separate business and personal issues. However, by approaching conflicts with love and understanding, family business owners can foster a positive and respectful work environment that promotes fairness and positivity.\nIn addition, effective communication is key to resolving conflicts in family businesses. By openly and honestly discussing issues and concerns, family business owners can work together to find solutions that meet everyone's needs. It is important to remember that conflicts are a natural part of any business, and by approaching them with love and understanding, family business owners can overcome them and build stronger, more resilient relationships."
    emotion, score = analyzer.analyze_response_emotion(user_input)
    print(emotion, score)
    # emotions = sorted(emotions, key=lambda x: x[1], reverse=True)
    # print("Detected Emotions:")
    # for emotion, score in emotions:
    #     print(emotion, "with a score of:", score)
