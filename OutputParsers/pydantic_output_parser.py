
"""
structure output parser enforce schema but does not do the data validation,
response from LL will come in the structure we define but it does nor contains the data validation
"""


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
class person(BaseModel):
    name : str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City name of the person belongs to")

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(template="generate the name and age and city of a fictional {place} person\n {format_instruction}",
               input_variables=['place'],
               partial_variables={'format_instruction':parser.get_format_instructions()})

chain = template | model| parser
result = chain.invoke({"place":"Nepali"})
print(result)

#name='Shreya Rai' age=25 city='Kathmandu'