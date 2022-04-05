#importing my modules
import csv
import pandas as pd

#read csv file 
election = pd.read_csv("C:\\Users\\Owner\\Desktop\\GT-VIRT-DATA-PT-03-2022-U-LOL\\Homeworks\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv")

#total amount of votes 
total_votes = len(election)

#total list of canidates 
candidates= election.groupby('Candidate')
candidates.first()

#total number of votes each candiate won
Stockham_result = election[election['Candidate'] == "Charles Casper Stockham"]
Stockham_result2 = len(Stockham_result)


DeGette_result = election[election['Candidate'] == 'Diana DeGette'] 
DeGette_result2 = len(DeGette_result)


Doane_result = election[election['Candidate'] == 'Raymon Anthony Doane']
Doane_result2= len(Doane_result)


#total percentage for each candidate 
Stockham_precentage = (round((Stockham_result2 / total_votes) * 100, 3))
DeGette_precentage = (round((DeGette_result2/total_votes) *100, 3))
Doane_precentage = (round((Doane_result2/total_votes)* 100, 3))

#To find out the winner
total_precentages = [(Stockham_precentage),(DeGette_precentage), (Doane_precentage)]

winner= max(total_precentages)





print('Election Results')

print('----------------------')

print('Total Votes:', total_votes)

print('-------------------')

print(f'Charles Casper Stockham: {Stockham_precentage}% ({Stockham_result2})' )

print(f'Diana DeGette: {DeGette_precentage}% ({DeGette_result2})')

print(f'Raymon Anthony Doane: {Doane_precentage}% ({Doane_result2})')

print('--------------------------')

if winner == Stockham_precentage:
    print('Winner: Charles Casper Stockham')
elif winner == DeGette_precentage:
    print('Winner: Diana DeGette')
elif winner == Doane_precentage:
    print('Winner: Raymon Anthony Doane')

print('----------------')

