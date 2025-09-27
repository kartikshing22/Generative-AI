"""
to build parallel chains we use runnable parallel,
it will take a dictionary as input , and runs runnables parallely. 
returns dictionary
"""




from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

prompt = PromptTemplate(
    template="generate a tweeet about {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Generate a linkedin post about - {topic}",
    input_variables=["topic"]
)
chain = RunnableParallel({
    "tweet": RunnableSequence(prompt,model,parser),
    "linkedin": RunnableSequence(prompt2,model,parser)
})
result = chain.invoke({"topic":"AI"})
print(result)


"""
{'tweet': 'Here are a few options, choose your favorite!\n\n**Option 1 (Whimsical & Gentle):**\nOur clever little AI friends are busy behind the scenes, sprinkling digital stardust on new ideas. ✨ So much gentle potential blooming! 🌸 #AI #TechMagic\n\n**Option 2 (Sweet & Curious):**\nWatching AI learn and grow, like a tiny digital sprout reaching for the sun. ☀️ What wonders will it help us imagine next? #AI #FutureIsSweet\n\n**Option 3 (Dreamy & Helpful):**\nAI, our quiet digital helper, is dreaming up possibilities and lending a tiny hand to big ideas. So cozy! ☕🧠 #AI #Innovation', 'linkedin': "Here are a few options for a LinkedIn post about AI, choose the one that best fits your immediate focus or audience!\n\n---\n\n**Option 1: Focusing on Opportunity & Adaptation**\n\n🚀 The pace of AI innovation is breathtaking, and it's no longer just a futuristic concept – it's here, reshaping industries, redefining job roles, and unlocking unprecedented possibilities.\n\nIgnoring it isn't an option. Instead, the question becomes: how are we integrating AI into our strategies, and what skills are we building to thrive in this new landscape?\n\nI believe the real power of AI lies in augmenting human capabilities, freeing us up for more strategic, creative, and empathetic work.\n\nWhat's one way AI has already impacted your work or industry? Or, what's a skill you're focusing on to stay ahead? Let's discuss! 👇\n\n#AI #ArtificialIntelligence #FutureOfWork #Innovation #DigitalTransformation #Upskilling #TechTrends\n\n---\n\n**Option 2: Focusing on Practical Application & Productivity**\n\n✨ AI isn't just for tech giants anymore. From automating mundane tasks to providing deeper insights, AI tools are becoming indispensable across every sector.\n\nThink about the hours saved on data analysis, content generation, personalized customer service, or even just smarter scheduling. The real power lies in augmenting human capabilities, allowing us to focus on the 'why' and the 'how,' rather than just the 'what.'\n\nWhat's one AI tool or application that has genuinely boosted your productivity or problem-solving recently? Share your go-to! 🤖📈\n\n#AItools #Productivity #Innovation #WorkSmarter #TechForGood #FutureIsNow #Efficiency\n\n---\n\n**Option 3: Focusing on Learning & Strategic Thinking**\n\n📚 The AI landscape is evolving at warp speed, and it can feel overwhelming to keep up. But staying informed and curious isn't just an advantage; it's a necessity.\n\nWhether you're a developer, a marketer, a leader, or an educator, understanding the *implications* of AI on your domain is critical. It's about asking the right questions: How can AI help us serve our customers better? Optimize our operations? Innovate our products? And what are the ethical considerations we must address?\n\nI'm constantly learning and adapting. What resources (books, courses, newsletters) are helping *you* navigate the world of AI? Let's build a collective learning list! 👇\n\n#AI #Learning #StrategicThinking #ProfessionalDevelopment #FutureReady #TechTrends #AIethics\n\n---\n\n**Remember to also consider adding:**\n*   A relevant image or short video if you have one.\n*   Tagging relevant connections or companies if appropriate."}
"""