from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_url
from agents.linkedin_lookup_agent import linkedin_lookup_url

if __name__ == "__main__":
    linkedin_url = linkedin_lookup_url(name="Eden Marco")
    summary_template = """ Given the information {information} of a person give me the following:
                        1. Give me a summary
                        2. Two interesting facts"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(prompt=summary_prompt_template, llm=llm)
    linkedin_data = scrape_linkedin_url(linkedin_url=linkedin_url)
    print(chain.run(information=linkedin_data))
