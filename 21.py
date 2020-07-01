
sentence_list = []
formatted_statement = ''
while True:
    statment = input('Say something: ')
        
    if statment != 'e':
        sentence_list.append(statment)

    elif statment == 'e':
        for sentence in sentence_list:
            if sentence.lower().startswith(('how','when','where','is','do','why')):
                formatted_statement = formatted_statement + sentence.capitalize() + '? '
            else:
                formatted_statement = formatted_statement + sentence.capitalize() + '. '
                
        #e
        #print(sentence_list)
        print(formatted_statement)
        break