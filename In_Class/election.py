import matplotlib.pyplot as plt

choices = {'Lewandowski': 0, 'Zajak': 0, 'Taromir': 0, 'Kwiataski':0 }

def vote(candidates, numVotes):
    print("Please choose one of the following candidates: ")
    for i, candidate in enumerate(candidates, start=1):
        print(f"{i}. {candidate}")
    for i in range(numVotes):
        x = int(input("Enter your choice: "))
        candidate = list(candidates.keys())[x-1]
        candidates[candidate] += 1
    return candidates

# def plot(results):
#     names = list(results.keys())
#     votes = list(results.values())
#     plt.bar(range(len(results)), votes, tick_label=names)
#     return(plt.show())

plot = plt.bar(list(choices.keys()), list(choices.values()))
        
votes = vote(choices, 6)
