import os
from zai import ZhipuAiClient

class ChatClient:
    Client = None
    Model: str = ""
    Temperature: float = 0.0
    Do_sample = False
    Top_p = 0.0
    Stream = False
    Messages = []
    Responses = []

    def __init__(self, model: str ="glm-4.6", temperature: float =0.6, do_sample=False, top_p=0.9, stream=False):
        self.Client = ZhipuAiClient(api_key=os.getenv("AI_API_KEY"))
        self.Model = model
        self.Temperature = temperature
        self.Do_sample = do_sample
        self.Top_p = top_p
        self.Stream = stream
        self.__init_messages__()

    def __init_messages__(self):
        self.Messages = [
            {
                "role": "system",
                "content": "你是一个有用的AI助手。"
            }
        ]

    def __append_message__(self, role: str, message: str):
        self.Messages.append({"role": role, "content": message })

    def __append_response__(self, response):
        self.Responses.append(response)

    def chat(self, message: str) -> str:
        self.__append_message__("user", message)
        response = self.Client.chat.completions.create(
            model=self.Model,
            temperature=self.Temperature,
            do_sample=bool(self.Do_sample),
            top_p=self.Top_p,
            stream=bool(self.Stream),
            messages = self.Messages
        )
        ai_response = response.choices[0].message.content
        self.__append_response__(ai_response)
        self.__append_message__("assistant", ai_response)
        return ai_response
    def print_responses(self):
        for response in self.Responses:
            print(response)

    def print_messages(self):
        for message in self.Messages:
            print(message)