import random

people = ['Fred', 'Sue', 'Harry', 'Lisa']
our_verbs = ['likes', 'knows', 'detests', "doesn't like"]


def random_sentence(subjects, verbs, complements):
  subject = random.choice(subjects)
  verb = random.choice(verbs)
  complement = random.choice(complements)
  return subject + ' ' + verb + ' ' + complement + '.'

def sentence ():
  return random_sentence(people, our_verbs, people)

print sentence()  
