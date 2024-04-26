import os
import json
import logging
from typing import List, Dict

from src.logger import Logger, log_time
class EmotionDataProcessor:
    """
    A class to process emotion data and divide it into separate files based on emotion.
    """

    def __init__(self, data_path: str = './data/emotion_data.json', output_dir: str = './data/divided'):
        """
        Initialize EmotionDataProcessor with data path and output directory.

        Args:
            data_path (str): Path to the emotion data JSON file.
            output_dir (str): Directory to store divided emotion entries.
        """
        self.data_path = data_path
        self.output_dir = output_dir
        self.logger = Logger("EmotionDataProcessor", see_time=True, console_log=True, level=logging.INFO)

        os.makedirs(self.output_dir, exist_ok=True)

    @log_time
    def load_data(self) -> List[Dict[str, str]]:
        """
        Load emotion data from JSON file.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing emotion entries.
        """
        try:
            with open(self.data_path, 'r') as f:
                text = f.read()
                text = text.splitlines()
            data = [json.loads(line) for line in text]
            return data
        except FileNotFoundError:
            self.logger.log_message("File not found. Please provide the data.", level=logging.ERROR)
            assert False, "\n\nFile not found. Please provide the data. \nAsk Ashad for the data."
        except Exception as e:
            self.logger.log_message(f"Error loading data: {str(e)}", level=logging.ERROR)
            return []

    def divide_data_by_emotion(self, data: List[Dict[str, str]]) -> None:
        """
        Divide the emotion data into separate files based on emotion.

        Args:
            data (List[Dict[str, str]]): List of dictionaries containing emotion entries.
        """
        emotions_dict = {}
        for entry in data:
            emotion = entry['emotion']
            if emotion not in emotions_dict:
                emotions_dict[emotion] = []
            prompt = entry['prompt']
            response = entry['response']
            emotions_dict[emotion].append({'prompt': prompt, 'response': response})

        for emotion, entries in emotions_dict.items():
            filename = os.path.join(self.output_dir, f"{emotion}_entries.json")
            with open(filename, 'w') as file:
                json.dump(entries, file, indent=4)
                self.logger.log_message(f"{len(entries)} entries written to {filename}")

if __name__ == "__main__":
    processor = EmotionDataProcessor()
    data = processor.load_data()
    processor.divide_data_by_emotion(data)
