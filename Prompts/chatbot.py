from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_history = [SystemMessage(content="You are a helpful AI assistant."),
    ]

while True:
    user_input = input("User: ")
    
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)


'''
---------------result without messages----------------
User: hi
AI:  Hello! How can I assist you today?
User: which country is leading AI technology?
AI:  As of now, the United States and China are considered to be the leaders in artificial intelligence (AI) technology. The United States has been a pioneer in AI research and development, with companies like Google, Microsoft, and IBM leading the way. China, on the other hand, has been investing heavily in AI and has made significant advancements in areas like facial recognition technology and AI-powered surveillance systems. Other countries like Japan, South Korea, and the United Kingdom are also making strides in AI technology.


User: how south korea?
AI:  South Korea is considered a significant player in the field of artificial intelligence (AI) technology. The country has a strong tech industry and government support for AI research and development. South Korean companies like Samsung, LG, and SK Telecom are actively investing in AI technologies and incorporating them into their products and services.
Additionally, South Korea has been focusing on developing AI-powered solutions for various industries, including healthcare, finance, transportation, and robotics. The country also hosts several AI research institutes and organizations that are dedicated to advancing AI technology.
Overall, South Korea's strong technological infrastructure, government support, and innovative companies make it a key player in the global AI landscape.

---------------result with messages----------------
'''