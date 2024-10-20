from langchain_openai import ChatOpenAI
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise Exception('must give at least one argument (word to be found)')

    output_temporary_file_path = os.path.join('C', 'dev', 'lang-learning', 'scraping_out_tmp.txt')

    llm = ChatOpenAI()

    print('\n')

    
    with (open(output_temporary_file_path, 'a', encoding="utf-8") as f):
        for input_word in sys.argv[1:]:
    
            response = llm.invoke(
            f'''explain word "{input_word}" in the following format:
            word [part of speech]
            ()
            1. explanation
            (if there is more than one explanation you can list them using subsequent numbers)'''
            )
            

            
            res = response.content + '\n'

            print(res)
            f.write(res + '\n')
