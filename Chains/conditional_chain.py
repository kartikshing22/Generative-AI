"""
this chain used for conditional based chain, where next chain depends on previous output of chain/LLm.
"""


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Return sentiment of the revFeedback")
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="clssify the sentiment of the following feedback text into positive or negitive \n{feedback} \n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

classifier_chain = prompt | model | parser2


prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback \n {feedback}",
    input_variables= ["feedback"]
)
prompt3 = PromptTemplate(
    template="write an appropriate response to this negitive feedback \n {feedback}",
    input_variables= ["feedback"]
)

branch_main = RunnableBranch(
    (lambda x:x.sentiment == "positive",prompt2 | model | parser),      #if
    (lambda x:x.sentiment == "negitive",prompt3 | model | parser),      #elif
    RunnableLambda(lambda x:"coud not found sentiment")                 #else
)

chain = classifier_chain | branch_main
result = chain.invoke({"feedback":"This is good game"})
print(result)
chain.get_graph().print_ascii()


"""
Here are a few options, ranging in tone and formality. Choose the one that best fits your brand/context:

**Option 1: Concise & Professional**

> Thank you so much for your positive feedback! We truly appreciate you taking the time to share your kind words.

**Option 2: Warm & Appreciative**

> That's wonderful to hear! We're so grateful for your positive feedback – it truly motivates us to continue delivering the best possible experience.

**Option 3: Team-Oriented**

> Thank you for your fantastic feedback! We're thrilled to know you had such a positive experience. Our team works hard to ensure satisfaction, and your comments are incredibly rewarding.

**Option 4: Slightly More Formal**

> We sincerely appreciate your positive feedback. Thank you for taking the time to share your thoughts; it's always encouraging to hear when we've met or exceeded expectations.

**Remember to:**

*   **If you have specific details** from the feedback (e.g., "I loved the new feature," or "The customer service was excellent"), you can personalize it by adding: "We're especially glad you enjoyed [specific detail]."
*   **If it's about a specific person:** "We'll be sure to pass your kind words on to [Name/Team]."
*   **Adjust the tone** to match your usual communication style.
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
+------------------------+ 
| ChatGoogleGenerativeAI | 
+------------------------+ 
             *             
             *             
             *             
 +----------------------+  
 | PydanticOutputParser |  
 +----------------------+  
             *             
             *             
             *             
        +--------+         
        | Branch |         
        +--------+         
             *             
             *             
             *             
     +--------------+      
     | BranchOutput |      
     +--------------+      
"""