from chatterbot.logic import LogicAdapter

class MyLogicAdapter (LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

        self.drug_names = kwargs.get('drugNames')
        self.drug_urls = kwargs.get('drugURLS')
        self.drug_dictionary = kwargs.get('drugDictionary')
    
    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement

        for word in input_statement.text:
            if word in self.drug_names:
                return Statement('Here is some information on', word, ': ', self.drug_dictionary[word])

        return str(self.chatbot.get_response(input_statement))

'''
chatbot = ChatBot('Health Bot',
                  logic_adapters = [
                      {
                          'import_path' : 'custom_adapter.MyLogicAdapter',
                          'drugDictionary' : drugDictionary,
                          'drugNames' : drugNames,
                          'drugURLS' : drugURLS
                      }
                  ]
            )
'''