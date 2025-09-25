from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="I love programming.")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)


'''
[SystemMessage(content='You are a helpful assistant that translates English to French.', additional_kwargs={}, response_metadata={}),
HumanMessage(content='I love programming.', additional_kwargs={}, response_metadata={}), 
AIMessage(content="J'adore la programmation.", additional_kwargs={}, response_metadata={})]
'''