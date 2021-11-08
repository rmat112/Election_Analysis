# Election_Analysis

## Overview of Election Audit
The Colorado Board of Elections is conducting an election audit of a recent congressional election and is requesting the information below
1. The total number of votes cast.
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote
Click here to view the Python script ( )

## Resources
- Data Source: election_results.csv
- Software: Python 3.9, Visual Studio Code Version: 1.62.0

## Election Audit Results
The analysis of the election show that:
- There were a total of 369,711 votes cast in this congressional election.
- The county results were as follows:
  - Voter turnout in Jefferson County was 38,855 votes which was 10.5% of total votes.
  - Voter turnout in Denver County was 306,055 votes which was 82.8% of total votes. 
  - Voter turnout in Arapahoe County was 24,801 votes which was 6.7% of total votes.
- The largest voter turnout was seen in Denver County.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the total votes and 85,213 votes.
  - Dana DeGette received 73.8% of the total votes and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the total votes and 11,606 votes.
  - The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 votes.

##### Below is a screenshot of results printed to terminal
![terminal_output](https://github.com/rmat112/Election_Analysis/blob/main/analysis/terminal_output.png)


##### Below is a screenshot of results printed to a text file "election_analysis.txt"
![Textfile_output](https://github.com/rmat112/Election_Analysis/blob/main/analysis/Textfile_output.png)

## Election Audit Summary
This script proved to be very useful for the analysis of results of this congressional election. With the help of this script we were able to calculate total number of votes. We were able to find out the voter turnout in each County and total votes per county as a percentage. Last, but not the least, we were able to find results of the election by calculating total number of votes per candidate as a number and as percentage, which ultimately helped us declare the final winner.<br/> 

For any other election this script will be equally or more useful in the following ways:
1. When there are not just three, but several counties involved and several candidates involved, the script will still work and provide accurate results.
2. This script can also be modified to include the results by City. This will need collecting more data about the city for each Ballot ID. This type of information can assist the candidates in future elections by giving them an idea about which way voters lean in each city. 
