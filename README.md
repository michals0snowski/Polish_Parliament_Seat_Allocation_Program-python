Polish Parliament Seat Allocation Program

This program implements the D'Hondt method to allocate seats in the Polish Parliament based on election results.
Usage

    Run the program.
    Enter the total number of parties and committees that obtained over 5% and 7% of the votes, respectively, in the elections.
    Provide the name of each party or committee and the number of votes they received in the elections.
    The program will allocate seats in the parliament based on the D'Hondt method and display the results.

How It Works

The program takes input on the number of parties and committees and the corresponding votes they received. It then creates a decreasing sequence of electoral quotients for each party or committee. Next, it sorts the quotients in reverse order and selects the top 460 unique values, representing the number of seats in the parliament. Finally, it allocates seats to each party or committee based on the selected quotients.
Example

Suppose there are three parties:

    Party A: 1,000,000 votes
    Party B: 800,000 votes
    Party C: 600,000 votes

The program will allocate seats based on the proportion of votes each party received, using the D'Hondt method.
License

This program is licensed under the MIT License.
