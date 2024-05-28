from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import JSONLoader
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()


class EMarketResponseApp:

    customer_id = None

    def __init__(self, customer_id):
        self.customer_id

    def get_llm(self):
        return OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.0)

    def get_LLM_chain(self, prompt_template=None):
        if prompt_template is None:
            raise ValueError("Prompt template is not supported")
        return LLMChain(llm=self.get_llm(), prompt=prompt_template)

    def lang_detect(self, question):
        """ add basic question """
        sentence_class_prompt_str = "Teniendo en cuenta la siguiente lista de idiomas (ingles, español, portugues), indique el idioma en el cual esta elaborada la siguiente sentencia {sentence}. Responda en formato JSON donde el lenguaje este almacenado en la key 'lang'"
        sentence_class_prompt = PromptTemplate.from_template(
            sentence_class_prompt_str)
        chain = self.get_LLM_chain(prompt_template=sentence_class_prompt)
        response = chain.invoke({"sentence":question})
        """ add json parser """
        print(response)

        """ add json parser """
        """ business logic """

    def check_sentence_syntax_question_concordance(self, sentence):
        sentence_class_prompt_str = "Puedes decir si la siguiente oracion es una pregunta ? tenga en cuenta que no es necesario el uso de signos de admiracion {sentence}"
        sentence_class_prompt = PromptTemplate.from_template(
            sentence_class_prompt_str)
        chain = self.get_LLM_chain(prompt_template=sentence_class_prompt)
        response = chain.invoke({"sentence":sentence})
        """ add json parser """
        print(response)

    def check_if_sentence_could_be_resolve(self, sentence):
        sentence_class_prompt_str = "Puedes decir si la siguiente oracion es una respuesta ? tenga en cuenta que no es necesario el uso de signos de admiracion {sentence}"
        sentence_class_prompt = PromptTemplate.from_template(
            sentence_class_prompt_str)
        chain = self.get_LLM_chain(prompt_template=sentence_class_prompt)
        response = chain.invoke({"sentence":sentence})
        """ add json parser """
        print(response)

instanceEMarketApp = EMarketResponseApp('123')

#instanceEMarketApp.lang_detect("Give me the initial values of EV market sells in USA?")
#instanceEMarketApp.check_sentence_syntax_question_concordance("Cual es el precio de oferta de energia en el mercado de USA?")
#instanceEMarketApp.check_sentence_syntax_question_concordance("voy por las mañanas al gimnasion sin falta")
