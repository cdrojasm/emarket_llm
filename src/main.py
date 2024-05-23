from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import JSONLoader

class EMarketResponseApp:
    def __init__(self, customer_id ):
        self.customer_id
        
    def get_LLM_chain(self):
        pass
        
    def lang_detect(self, question):
        """ add basic question """
        sentence_class_prompt_str = "Teniendo en cuenta la siguiente lista de idiomas (ingles, español, portugues), indique el idioma en el cual esta elaborada la siguiente sentencia {sentence}"
        sentence_class_prompt = PromptTemplate.from_template(sentence_class_prompt_str)
        """ add invoke """
        """ add json parser """    
        """ business logic """
        
    def check_sentence_syntax_question_concordance(self):
        sentence_class_prompt_str = "Teniendo Puedes detectar el idioma en el cual se encuentra la siguiente pregunta."
        
        
    