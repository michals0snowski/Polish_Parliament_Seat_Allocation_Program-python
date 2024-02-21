# getting the number of comitees and votes given party won in the elections
comitees_no = input(f"Podaj łączną ilość partii i komitetów, które w wyborach zdobyły odpowiednio ponad 5% i 7% głosów: ")
comitees_no = int(comitees_no)
votes = {}

for i in range(comitees_no):
    x = str(input(f"Podaj nazwę partii, lub komitetu: "))     
    y = int(input(f"Podaj ilość głosów, którą partia ta (bądź komitet) zdobyła w wyborach: "))
    votes[x] = y

# Creating a decreasing sequence of electoral quotients of a given committee    
candidates = {}
seats = 460

for key, value in votes.items():
    candidates[key] = [value]
    n = 2
    for i in range(seats): 
        candidates[key] += [value / n]
        n += 1

# Flattening the lists and sort them in reverse order
all_values = sorted([value for sublist in candidates.values() for value in sublist], reverse=True)

# taking the top 460 (the number of seats in parliment) unique values
top_460_values = sorted(set(all_values), reverse=True)[:460]

# initialize the result dictionary
result = {}

# Iterate over the original dictionary
for key, values in candidates.items():
    top_values_for_key = [value for value in top_460_values if value in values]
    result[key] = top_values_for_key[:460]

print("\n")
for key in result.keys():
    print(f"{key.upper()} dostanie {len(result[key])} miejsc w sejmie.")