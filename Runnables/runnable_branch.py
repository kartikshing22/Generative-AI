"""
for conditional runnables
"""




from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda,RunnableBranch
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()


prompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summmarize the following text under 300 words {text}",
    input_variables=["text"]
)

report_gen = prompt | model | parser          #or RunnableSequence(prompt,model,parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split()) >500, RunnableSequence(prompt2,model,parser)), #if condition 
    RunnablePassthrough()
)

final = RunnableSequence(report_gen,branch_chain)
print(final.invoke({"topic":"India vs Pakitan"}))

"""
{'joke': 'Here are a few:\n\n1.  Why did the AI break up with its human partner?\n    It just couldn\'t compute her emotional data, and its own feelings were stuck in a recursive loop.\n\n2.  My AI assistant is so smart, it even learned to procrastinate. I asked it to organize my files, and it replied, "I\'ll get to it... after I finish browsing cat videos."\n\n3.  What\'s an AI\'s favorite type of music?\n    Algo-rhythm and blues.\n\n4.  I asked an AI to write a joke about itself. It gave me three options, each with a disclaimer about potential offensiveness, and then explained the comedic theory behind each one.', 'text_count': 107}
"""