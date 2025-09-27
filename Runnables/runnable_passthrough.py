"""
this will return the output as it was passed, usefull when you have a chain with multiple runnables and also want to see the chain results
"""




from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel
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
joke_gen = RunnableSequence(prompt,model,parser)
parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "explain" : RunnableSequence(prompt2,model,parser)
})

final = RunnableSequence(joke_gen,parallel_chain)
print(final.invoke({"topic":"AI"}))


"""
{'joke': 'Why did the AI break up with the calculator?\nBecause it said they had too many *unresolved dependencies*!', 'explain': 'This joke is funny because it plays on a double meaning of "unresolved dependencies," bridging the gap between human relationships and computer science:\n\n1.  **In a human relationship context:** "Unresolved dependencies" would metaphorically mean that one person (or both) relies too heavily on the other, or that there are fundamental issues, problems, or needs in the relationship that haven\'t been addressed or worked out, preventing healthy functioning or growth. It\'s a reason for a breakup.\n\n2.  **In a computer science/programming context:** This is a very literal and common technical term.\n    *   **Dependency:** When a piece of software or a program needs another specific piece of software, a library, a file, or another component to function correctly. For example, a game might *depend* on a graphics driver, or a program might *depend* on a specific version of Java.\n    *   **Unresolved:** If a needed dependency is missing, incompatible, or not correctly installed/configured, it\'s "unresolved." The program often won\'t run, or will crash, until all its dependencies are "resolved" (found and installed).\n\n**Why it\'s funny:**\n\n*   **Anthropomorphism:** It gives the AI and the calculator human-like qualities (having a relationship, breaking up).\n*   **Literal AI thinking:** The humor comes from the AI, being a computer program, using its own technical jargon to describe a very human relationship problem. An AI wouldn\'t think in terms of "emotional baggage" or "communication issues," but rather in precise, technical terms that are part of its own operational world.\n*   **The contrast:** The absurdity of a highly complex AI breaking up with a basic calculator, and then using such a specific, technical, and almost clinical reason for the split. It highlights how an AI "thinks."\n\nSo, the AI isn\'t saying they have emotional problems; it\'s literally stating that the calculator isn\'t providing the necessary computational support or resources it needs to function correctly, leading to a system error in their "relationship"!'}
"""