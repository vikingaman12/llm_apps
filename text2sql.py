import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = "your_google_api_key_here"

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Create a prompt template
prompt_template = """
You are an expert in converting natural language queries to SQL. 
Given the following natural language query, generate the corresponding SQL query.

Natural language query: {query}

Table schema:
{schema}

SQL query:
"""

prompt = PromptTemplate(
    input_variables=["query", "schema"],
    template=prompt_template
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Function to convert natural language to SQL
def natural_language_to_sql(natural_language_query, table_schema):
    result = chain.run(query=natural_language_query, schema=table_schema)
    return result.strip()

# Example usage
table_schema = """
employees
- id (int, primary key)
- name (varchar)
- department (varchar)
- salary (int)
- hire_date (date)
"""

natural_language_query = "Show me the names and salaries of all employees in the sales department who earn more than $50,000, ordered by their hire date, and limit the results to 10."

sql_query = natural_language_to_sql(natural_language_query, table_schema)
print(f"Natural Language Query: {natural_language_query}")
print(f"Generated SQL Query: {sql_query}")