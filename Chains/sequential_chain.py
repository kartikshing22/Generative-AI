from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(
    template="generate 5 intresting things about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a 2 line summary on {text}",
    input_variables=["text"]
)
model = ChatOpenAI()

user_input = input("Enter a topic: ")
parser = StrOutputParser()

chain = prompt | model | parser | prompt2 | model | parser

result = chain.invoke({"topic":user_input})

print(result)
chain.get_graph().print_ascii()


"""
Enter a topic: sql
SQL, a standardized language for managing databases, allows for querying, updating, deleting, and inserting data efficiently.
With support from popular database systems, SQL offers powerful set-based operations for creating complex structures and analyzing data.
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +------------+       
      | ChatOpenAI |       
      +------------+       
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +------------+       
      | ChatOpenAI |       
      +------------+       
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
"""