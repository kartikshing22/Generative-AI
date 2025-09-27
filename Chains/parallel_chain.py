from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="generate short and simple notes from the following text \n{text}",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="generate 5 short question and answers from the following text \n{text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document \n notes ->{notes} \n Quiz -> {quiz}",
    input_variables=["notes","quiz"]
)


parallel_chain = RunnableParallel({
    "notes" : prompt | model | parser,
    "quiz" :  prompt2 | model2 | parser
})

merge_chain = prompt3 | model | parser 
chain = parallel_chain | merge_chain


text = """
                What is Django Middleware

                Middleware in Django is like a set of tools that help in handling requests and responses. It’s a simple system that allows developers to make changes to how Django takes in information or sends out responses on a global level. Each part of the middleware has its own job or function.
                2. Think of middleware in Django like a pipeline that requests and responses flow through. Each part of this pipeline, represented by a middleware class, has a specific job or adds extra features to the web application. For example, middleware can handle authentication, deal with cookies, or enforce security rules.

                Example of Some Predefined Django Middleware

                SecurityMiddleware
                Helps in enforcing various security features, such as setting HTTP headers for security, like Content Security Policy (CSP).
                AuthenticationMiddleware
                Adds the user object to the request based on the current session. It allows easy access to the authenticated user in views
                SessionMiddleware
                Manages user sessions by storing session data on the server side and sending a session ID to the client through a cookie.
                How Django Middleware works

                Imagine Django middleware as a helpful bridge connecting the web server and your view functions (the parts of your web application that handle specific tasks). It’s like a traffic cop that manages both incoming requests and outgoing responses.

                When someone interacts with your website, their request goes through Django middleware before reaching your actual web page (view functions). The middleware consists of different classes that you set up in your application’s settings. It’s like a series of checkpoints that the request has to pass through

                Now, let’s break down how Django middleware works into two main stages:

                Request Processing
                When a user makes a request (like clicking on a link or submitting a form), Django middleware processes it first. It can perform various tasks like checking for security measures, handling sessions, or adding extra information to the request.
                Response Processing
                After your view functions have generated a response (like showing a web page), Django middleware again steps in. It can modify the response before it goes back to the user, adding headers, compressing content, or performing other tasks.
                """
result = chain.invoke({
    "text" : text
})


print(result)
chain.get_graph().print_ascii()


"""
Here's a consolidated document merging the notes and quiz questions/answers into a single, comprehensive overview of Django Middleware:

---

## Django Middleware: Concepts & Functionality

Django Middleware is a fundamental component of the Django web framework, designed to handle requests and responses on a global level. It provides a powerful mechanism to modify or enhance the request/response cycle across your entire application.

### What is Django Middleware?

*   **A Set of Tools:** Middleware can be thought of as a collection of tools that help in processing incoming requests and outgoing responses.
*   **Global Impact:** It allows for global changes to how Django processes information, affecting all requests and responses that pass through it.
*   **A Pipeline:** Effectively, middleware acts like a pipeline through which requests and responses flow. Each part of this pipeline has a specific job or function, such as managing authentication, enforcing security, or handling user sessions.

### How Django Middleware Works

Middleware functions as a bridge between the web server and your Django view functions. It manages both incoming requests and outgoing responses and is configured as classes within your application's settings.

Django middleware operates in two main stages:

1.  **Request Processing:**
    *   When a user makes an incoming request, Django middleware processes it *before* it reaches any view functions.
    *   During this stage, middleware can perform crucial tasks like checking for security measures, handling user authentication, or initiating/managing user sessions.

2.  **Response Processing:**
    *   After your view functions have generated a response, Django middleware steps in to process it *before* it is sent back to the user.
    *   In this stage, middleware can modify the outgoing response. This might involve adding HTTP headers (e.g., for security), compressing content, or performing other final adjustments before the response is delivered to the client.

### Examples of Predefined Middleware

Django comes with several built-in middleware classes that provide essential functionalities:

*   **SecurityMiddleware:**
    *   Helps in enforcing various security features across your application.
    *   This includes setting important HTTP headers for security, such as `X-Content-Type-Options`, `X-Frame-Options`, and `Content Security Policy` (CSP).

*   **AuthenticationMiddleware:**
    *   Responsible for adding the `user` object to the request.
    *   This makes the authenticated user's information readily available to your view functions, allowing you to build user-specific logic.

*   **SessionMiddleware:**
    *   Manages user sessions.
    *   It typically stores session data on the server-side and uses a client-side cookie to identify and link the user's browser to their specific session data.

---
                +---------------------------+             
                | Parallel<notes,quiz>Input |             
                +---------------------------+             
                     **               **                  
                  ***                   ***               
                **                         **             
    +----------------+                +----------------+  
    | PromptTemplate |                | PromptTemplate |  
    +----------------+                +----------------+  
             *                                 *          
             *                                 *          
             *                                 *          
+------------------------+              +------------+    
| ChatGoogleGenerativeAI |              | ChatOpenAI |    
+------------------------+              +------------+    
             *                                 *          
             *                                 *          
             *                                 *          
    +-----------------+               +-----------------+ 
    | StrOutputParser |               | StrOutputParser | 
    +-----------------+               +-----------------+ 
                     **               **                  
                       ***         ***                    
                          **     **                       
               +----------------------------+             
               | Parallel<notes,quiz>Output |             
               +----------------------------+             
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