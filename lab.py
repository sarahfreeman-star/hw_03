import random

'''
For each of the 6 functions below:
    Create a high level comment pattern.
    3 of these patterns should be explaining why you support a particular presidential candidate,
    and 3 of these patterns should be attacking a presidential candidate that you don't like.
    The patterns should be between 2-5 sentences each.
    
    Select at least 5 words/phrases from the pattern.
    For each word/phrase, create a list of at least 4 other words/phrases that can be substituted for the selected word/phrase without changing the pattern's meaning.
    Use the random.choice function to randomly select which word/phrase you're going to use,
    and then concatenate the results together into a single coherent comment.
To submit your lab, generate 10000 randomly generated comments and upload them to sakai.
'''

def generate_comment_0():
    pattern = "Maybe Benedict Cumberbatch should be president. A superhero will make our nation better."
    word_dict = {'Maybe':['Perhaps','Conceivably','Mayhap','Perhance'],'should be':['has to be','must be','is going to be','is going to become'],
                'superhero':['hero','savior','warrior','lionheart'],'nation':['country','kingdom','empire','realm'],'better':['superior','greater','finer','stronger']}
    to_replace = random.choice(list(word_dict.keys()))
    new_word = random.choice(word_dict[to_replace])
    comment = pattern.replace(to_replace,new_word)
    return comment

def generate_comment_1():
    pattern = "Benedict Cumberbatch will do things no president ever has. He will destroy Thanos, catch criminals, and bring the avengers back."
    word_dict = {'Benedict Cumberbatch':['Sherlock','Holmes','Dr. Strange','Alan Turing'],'president':['leader','head of state','commander in chief','POTUS'],
                'destroy':['demolish','wreck','shatter','finish'],'catch':['imprison','find','convict','end'], 'criminals':['bad people','law breakers','evil people','cruel people']}
    to_replace = random.choice(list(word_dict.keys()))
    new_word = random.choice(word_dict[to_replace])
    comment = pattern.replace(to_replace,new_word)
    return comment

def generate_comment_2():
    pattern = "Sherlock for president! He is very intelligent and will make America safer and more efficient."
    word_dict = {'very':['really','extremely','incredibly','super'],'intelligent':['clever','smart','bright','brilliant'],
                'America':['USA','US','United States','the land of the brave'],'safer':['a less dangerous place','secure','peaceful','ordered'], 'efficient':['effective','productive','fruitful','potent']}
    to_replace = random.choice(list(word_dict.keys()))
    new_word = random.choice(word_dict[to_replace])
    comment = pattern.replace(to_replace,new_word)
    return comment


def generate_comment_3():
    pattern = "Superman is a weak superhero and cannot control reality. We need someone who can control reality to lead us."
    word_dict = {'weak':['fragile','feeble','incompetent','indisposed'],'control':['manipulate','transcend','modify','alter'],'need':['want','desire','must have','should elect'],
                'someone':['a president','a leader','a POTUS','a king'],'lead':['guide','pilot','conduct','show us the way']}
    to_replace = random.choice(list(word_dict.keys()))
    new_word = random.choice(word_dict[to_replace])
    comment = pattern.replace(to_replace,new_word)
    return comment

def generate_comment_4():
    pattern = "Superman could not defeat Lex Luthor by himself. Do you think he is strong enough to lead a nation by himself?"
    word_dict = {'defeat':['exterminate','execute','kill','eliminate'],'Lex Luthor':['Jesse Einberg','Mark Zuckerberg','J. Daniel Atlas','Columbus'],'think':['believe','reckon','feel','imagine'],
                'by himself':['alone','without help','independently','without support'],'strong enough':['fit','capable','skilled','powerful']}
    to_replace = random.choice(list(word_dict.keys()))
    new_word = random.choice(word_dict[to_replace])
    comment = pattern.replace(to_replace,new_word)
    return comment

def generate_comment_5():
    pattern = "Superman doesn't understand the human condition. He might turn into a tyrant and might threaten to destroy humanity"
    word_dict = {'Superman':['Peter Parker','Henry Cavill','Tom Holland','Christopher Reeve'],'understand':['comprehend','conceptualize','empathize','sense'],'tyrant':['dictator','monarch','despot','autocrat'],
                'destroy':['decimate','demolish','ruin','wreck'],'turn':['become','transform','convert','develop into']}
    to_replace = random.choice(list(word_dict.keys()))
    new_word = random.choice(word_dict[to_replace])
    comment = pattern.replace(to_replace,new_word)
    return comment

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    possible_choices = [generate_comment_0(), generate_comment_1(), generate_comment_2(), generate_comment_3(), generate_comment_4(), generate_comment_5()]
    selected_function = random.choice(possible_choices)
    return selected_function

##UNCOMMENT TO GENERATE 10000 COMMENTS
#with open('output.txt', 'w') as output_file: 
#    pass
#output_file = open("output.txt", "w")
#for i in range(0,10000):
#        output_file.write("Sentence #"+str(i+1)+' = '+ generate_comment()+'\n')
#output_file.close()
