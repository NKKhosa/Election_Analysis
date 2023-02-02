# Election_Analysis

## Project Overview
An election audit was completed for the recent local congressional election for a Colorado Board of Elections employee.

The data we retrieved:
 1. The total number of votes cast
 2. The voter turnout of each county.
 3. The county with the highest voter turnout.
 4. A complete list of candidates who recieved votes
 5. The percentage of votes each candidate won
 6. The total number of votes each candidate won
 7. The winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.10.2, Visual Studio Code 1.64.2

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The counties in the election precinct were:
    - Jefferson
    - Denver
    - Arapahoe
- The turnout for each county compared to the total turnout was:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- The county with the highest turnout was:
    - Denver with 82.8% of the voter turnout and 306,055 number of votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham: 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette: 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane: 3.1% of the vote and 11,606 number of votes. 
- The winner of the election was:
    - Diana DeGette who recieved 73.8% of the vote and 272,892 number of votes.
    - 
![](https://github.com/NKKhosa/Election_Analysis/blob/main/Resources/election_results.png?raw=true)
## Election-Audit Summary

In the event of future elections, this script is highly versatile and can easily be modified to fit the needs of a new audit. 

Steps to re-use the script:
1. Add the new results file to the "Resources" folder, updating the input file. 
2. Change line 9 of the script:
     - file_to_load = os.path.join("Resources", "election_results.csv") to file_to_load = os.path.join("Resources", <"NEW_RESULTS_FILE.csv">)
3. Check the order of columns in the NEW_RESULTS_FILE.csv to make sure that the code in the for loop that is indexed in reference to the columns to assign values to the starter variables are correct. If the new dataset has a different arrangement, adjust the indexing of row[] to be accurate.
    - line 48: candidate_name = row[2] 
    - line 51: county_name = row[1]

By making these small adjusments, the code can now work through the input data and complete the audit of a new election.
