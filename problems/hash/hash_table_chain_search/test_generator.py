from lib.testgen import TestSet
from lib.random import seed, randint
import random

seed(42)

words = ["Alarm", "Arena", "Service", "Enemy", "Canvas",
             "Sort", "Experiment", "Mine", "General", "Winter",
             "Performance", "Control", "Cooking", "Creation",
             "Basket", "Hearing", "Roll", "Rule", "Spending",
             "Luck", "Scene", "Tooth", "Administration", "Panel",
             "Attack", "Commander", "Engine", "Pitch", "Payment",
             "Hell", "Honor", "Limit", "Poem", "Family", "Check",
             "Chart", "Income", "Mortgage", "Writer", "Designer",
             "Collapse", "Corruption", "Blade", "Heat", "Beauty",
             "Memory", "Portfolio", "Effectiveness", "Priest",
             "Village", "Rifle", "Text", "Square", "Counterpart",
             "End", "Factor", "Implementation", "Scandal", "Subject",
             "Disaster", "Ceremony", "Pitcher", "Store", "Position",
             "Restriction", "Pipe", "Ice", "Comedy", "Abuse", "Businessman",
             "Banking", "Era", "Driver", "Steel", "Place", "Maker", "Log",
             "String", "Announcement", "Hold", "Officer", "Work", "Planning",
             "Combination", "Pump", "Standard", "Substance", "Emotion", "Laughter",
             "Fraud", "Magic", "Celebration", "Compromise", "Snow", "Food",
             "Pleasure", "Limitation", "Telephone", "Blood", "Clinic"]
print(words)
def question(word):
    return '{}\n'.format(word)

def answer(bol):
    return '{}\n'.format(bol)

#положительные тесты
ranlist = random.choices(words, k=10)

tests = TestSet()
for word in ranlist:
    tests.add(question(word), answer(True))

#случайные тесты
for i in range(5):
    s = ''
    s_len = randint(1, 13)

    for j in range(s_len):
        char_ord = randint(ord('A'), ord('z'))
        s += chr(char_ord)  
    tests.add(question(s), answer(s in set(words)))
