"""
to build sequintial chainswe use runnable sequence
"""




from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Explain joke - {joke}",
    input_variables=["joke"]
)
chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)
print(chain.invoke({"topic":"AI"}))