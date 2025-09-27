from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(
    template="generate 5 intresting things about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()
chain = prompt | model | parser

chain.get_graph().print_ascii()     #it will print flow of chain
result = chain.invoke({"topic":"captial of india Delhi"})
print(result)
