
"""
in case of wrong data type pydantic throws error
"""




from pydantic import BaseModel, Field

class Student(BaseModel):
    name :str
    religion: str = "Humanity"   #Default Optional value in case of age not passed
    age: int = None             #optional value
    cgpa: float = Field(gt=0.0,lt=10.0,default=5.0, description="cgpa of student") #constraints in pytdantic which will check passed value is in range

student_obj = {"name":"kartik"}
student_obj_2 = {"name":"kartik","age":"25"}        #pydantic will convert string to int (coerced)
student = Student(**student_obj_2)
print(student)
print(student.model_dump_json())        #converts to json
print(dict(student))        #converts to python dict    
