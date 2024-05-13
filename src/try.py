# import textwrap
# from typing import List

# from IPython.display import Markdown

# import google.generativeai as genai

# from src.logger import Logger, log_time
# import os

# creds_path = "src/CREDS.py"
# assert os.path.isfile(creds_path), "\n\nsrc.CREDS is not present in the folder\n Ask Ashad for the file\n\n"

# from src.CREDS import GOOGLE_GEMINI_API_KEY

# if not GOOGLE_GEMINI_API_KEY or GOOGLE_GEMINI_API_KEY == "YOUR_API_KEY_HERE":
#     raise ValueError("Please set the GOOGLE_GEMINI_API_KEY in src.CREDS.py")

# class ContentGenerator:
#     """
#     A class to generate content based on a prompt using Google Gemini AI.
#     """

#     def __init__(self, api_key: str):
#         """
#         Initialize the ContentGenerator with the API key.

#         Args:
#             api_key (str): The API key for Google Gemini AI.
#         """
#         genai.configure(api_key=api_key)
#         self.logger = Logger("model", see_time=True)
#         self.model = genai.GenerativeModel("gemini-pro")
#         self.emotions = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise']
#         self.positive_emotions = ['admiration', 'amusement', 'approval', 'caring', 'curiosity', 'excitement', 'gratitude', 'joy', 'love', 'optimism', 'pride', 'realization', 'relief', 'surprise']
#         self.negative_emotions = ['anger', 'annoyance', 'confusion', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'fear', 'grief', 'nervousness', 'remorse', 'sadness']

        
#     @log_time
#     def generate_content(self, prompt: str, safety_settings: List[dict], max_tokens: int = 400) -> str:
#         """
#         Generate content based on the given prompt and safety settings.

#         Args:
#             prompt (str): Prompt for content generation.
#             safety_settings (List[dict]): Safety settings for content generation.

#         Returns:
#             str: Generated content.
#         """
#         self.logger.log_message(f"Generating content for prompt: {prompt}")
#         response = self.model.generate_content(
#             prompt,
#             generation_config=genai.types.GenerationConfig(
#                 candidate_count=1,
#                 stop_sequences=["x"],
#                 max_output_tokens=max_tokens,
#                 temperature=0.7,
#             ),
#             safety_settings=safety_settings,
#         )
#         generated_text = response.text
#         if response.candidates[0].finish_reason.name == "MAX_TOKENS":
#             generated_text += '...'
#             print('fin')
#         self.logger.log_message(f"Generated content: {generated_text}\n\n")
        
#         return generated_text

#     def handle_chat_history(self, prompt: str, chat_history: List[dict]) -> str:
#         """
#         Generate content based on the chat history.

#         Args:
#             chat_history (List[dict]): Chat history for content generation.

#         Returns:
#             str: Generated content.
#         """
#         if chat_history == []:
#             self.chat = self.model.start_chat(history=chat_history)
        
#         response = self.chat.send_message(prompt)
#         self.logger.log_message(f"Prompt: {prompt}")
#         self.logger.log_message(f"Response: {self.chat.history}")
#         return response.text
        
#     @staticmethod
#     def to_markdown(text: str) -> Markdown:
#         """
#         Convert plain text to Markdown format.

#         Args:
#             text (str): Plain text to be converted.

#         Returns:
#             Markdown: Markdown formatted text.
#         """
#         text = text.replace("•", "  *")
#         return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# if __name__ == "__main__":
#     safety_settings = [
#         {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
#         {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
#         {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
#         {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
#         {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
#     ]
#     generator = ContentGenerator(GOOGLE_GEMINI_API_KEY)
#     prompt = f"What is the meaning of life?"
#     generated_text = generator.handle_chat_history(prompt, [])
#     #generated_text = generator.generate_content(prompt, safety_settings)
    
#     print(generated_text)

import math

current_score = 6.3
answer = " ".join([str(i) for i in range(40)])
print(len(answer.split()))
current_score = current_score * math.log10(len(answer.split()))

print(current_score)