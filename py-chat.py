from chat import ChatClient
from init import load_env

def main():
    client = ChatClient()
    while True:
        user_input = input("> ")
        if user_input == "exit":
            break
        try:
            ai_response = client.chat(user_input)
            print(f"AI : {ai_response}")
        except Exception as e:
            print(f"Error happened: {e}")

if __name__ == '__main__':
    load_env()
    main()