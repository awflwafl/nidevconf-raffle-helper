import csv
import random

with open('friday-quiz.csv', 'r') as f:
    reader = csv.reader(f)
    tickets = []

    # create a ticket for each correct answer or each point in the score
    for row in reader:
        person = row[0]
        score = int(row[1])
        correct_answers = int(row[2])

        print(row)

        for i in range(0, score):
            tickets.append(person)

    # select a random ticket
    print()
    print('Winner:', random.choice(tickets))
