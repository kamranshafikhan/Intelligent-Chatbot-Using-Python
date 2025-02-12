import nltk
import nltk.corpus
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem import PorterStemmer
from string import punctuation

# Natural Language Toolkit(nltk) is a 3rd party library that has been imported into this program
# corpus is a massive amount of large data sets within nltk

ps = PorterStemmer()  # Created an object ps for stemming of words



def stemming_file_data(listsent):   #stem all the even numbered sentences in the database
    i=0
    while i<len(listsent):
        str = ''
        b = word_tokenize(listsent[i])
        for words in b:
            c = ps.stem(words)
            str+= ' '+ c   
        listsent[i] = str
        i+=2
    return listsent

def list_to_string(answer_list):   # required for converting a given list into string
    str=""
    for i in answer_list:
        str +=" " + i
    return str

file = open("data.txt","r",encoding='utf8') 
file = file.read()
list_file = sent_tokenize(file)
list_stem = stemming_file_data(list_file)



# Here includes the classes starting from
'''
class A: the functions in this class tokenise the user input, then removes stopwords and then turn the remaining
words into a list, and then also stem the words in the list.
'''

class A:


    def __init__(self,user_question):
        self.user_question = user_question
    
    def intrepet_user_question(self):
        keywords = ['if','and','not','or','for','while','do']
        words = word_tokenize(self.user_question)
        un_words = set(stopwords.words('english'))
        un_words = list(un_words)
        filter_words = []
        for x in keywords:
            if x not in un_words:
                filter_words.append(x)
                
        filtered_keywords = []
        for w in words:
            if w not in filter_words:
                y = ps.stem(w)
                filtered_keywords.append(y)
        return filtered_keywords

'''  
ClassB: this class is an inherited class of class A(child class of A), and contains code to perform the function of
removing any punctuation from the tokenised words in the list.
'''
        
class B(A):
    def __init__(self,keyword_list):
        self.keyword_list = keyword_list
        self.file = list_stem

    def punctuation_remover(self):
        new_list = []
        for a in self.keyword_list:
            if a not in punctuation:
                new_list.append(a)
        return new_list

class C(B):

    def question_database_matching(self):
        
        
        i=0
        matches=0
        misses=100
        a = []
        while(i<len(self.file)):
            testbit = 0
            missbit = 0

            for w in self.keyword_list:
                if w in self.file[i]:
                    testbit+=1

            for k in self.file[i]:
                if k not in self.keyword_list:
                    missbit+=1
        
            if testbit >matches:
                matches=testbit
                misses = missbit
                a = self.file[i+1]
            elif testbit == matches and matches !=0:
                if missbit<misses:
                    misses = missbit
                    a = self.file[i+1]
            i+=2   
        return a
        


class D(C):
    def __init__(self,compound_question):
        self.compound_question = compound_question
        
       

    def comp_question(self):
        j = 0
        i = 0
        offset = 0
        while i < len(self.compound_question):
            if self.compound_question[i] == 'and':
                offset =i
            i+=1
        pronouns = ["it","its","their","theirs","they","them"]
        pronoun_test = False
        for y in pronouns:
            if y in self.compound_question:
                pronoun_test = True
        part1 = []
        part2 = []

        while j < offset:
            part1.append(self.compound_question[j])
            if pronoun_test:
                part2.append(self.compound_question[j])
            j+=1
        k = offset + 1
        while k < len(self.compound_question):
            part2.append(self.compound_question[k])
            k+=1
        return part1,part2
       

class E(D):

    def __init__(self):
        super().__init__(user_question)
        super().__init__(keyword_list)
        self.file = list_stem






print("\n\n\n\nHello! My name is Prime Bot")
print("I am an intelligent chatbot and i can answer questions related to c++")
query = input("Enter your question: ")
while True:
    
    obj1 = A(query)
    a1 = obj1.intrepet_user_question()
    obj2 = B(a1)
    a2 = obj2.punctuation_remover()
    obj3 = C(a2)
    a3 = obj3.question_database_matching()
 
    
    if 'and' in query:
        query = word_tokenize(query)
        obj4 = D(query)
        a4 = obj4.comp_question()
        a5 = list(a4)
        user_question = " "
        keyword_list = []
        obj5 = E()
        a = 0
        while a < len(a5):
            a6 = list_to_string(a5[a])
            obj5.user_question = a6
            a7 = obj5.intrepet_user_question()
            obj5.keyword_list = a7
            a8 = obj5.punctuation_remover()
            obj5.keyword_list = a8
            a9 = obj5.question_database_matching()
            comp_ans = a9
            print(comp_ans)
            a +=1
    elif a3 == []:
        print ("Sorry either the programmer is not smart enough or you have asked an invalid question")
    else:
        print("computer>> " + a3)


    query = input("Enter another question: ")
    
        

       

    

    

