# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source election_results.csv
- Software: Python 3.7, Visual Studio Code 1.70.1

## Summary
The analysis of the election shows that:
- There were "x" votes cast in the election.
- The candidates were:
    - Candidate 1
    - Candidate 2
    - Candidate 3
- The candidate results were:
    - Candidate 1 received "x%" of the vote and "y" number of votes.
    - Candidate 2 received "x%" of the vote and "y" number of votes.
    - Candidate 3 received "x%" of the vote and "y" number of votes.
- The winner of the election was:
    - Candidate (1, 2, or 3), who received "x%" of the vote and "y" number of votes.

## Challenge Overview

For this challenge assignment, we had to add to the code that we developed through the course as materials described above. In addition to the candidate data that the course materials walked us through reading from the source .csv file and writing results to a .txt file, we had to add an analysis of the data for each county that participated in the election. This was a similar process, and the steps to complete it for the county-based data were analogous to the steps outlined above for candidate-based data:

1. Because the candidate data had already calculated the total votes cast, we did not need to repeat this step for the county data as it was already in the code.
2. We got a complete list of the counties which participated in the election.
3. We calculated the total number of votes that were cast in each participating county.
4. We calculated the percentage of total votes that were cast in each participating county.
5. We determined which county that participated in this election had the highest voter turnout.

## Challenge Summary
### Election-Audit Results

- Total votes cast: 369,711
    - Relevant code used:
    ```
    total_votes = 0
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        for row in file_reader:
            total_votes += 1
    ```
        
- Votes by county: Jefferson: 10.5% (38,385), Denver: 82.8% (306,055), Arapahoe: 6.7% (24,801)
    - Relevant code used:
    ```
    county_options = []
    county_votes = {}
    
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        headers = next(file_reader)
        for row in file_reader:
            total_votes = total_votes + 1
            county_name = row[1]
            if county_name not in county_options:
                county_options.append(county_name)
                county_votes[county_name] = 0
            county_votes[county_name] += 1
        
        for county_name in county_votes:
            county_votecount = county_votes.get(county_name)
            votecount_percentage = float(county_votecount) / float(total_votes) * 100
            county_results = (
                f"{county_name}: {votecount_percentage:.1f}% ({county_votecount:,})\n")
        ```

- County with most votes: Denver
    - Relevant code used:
    ```
    largest_turnout = ""
    turnout_votes = 0
    turnout_percentage = 0
            
            if (county_votecount > turnout_votes) and (votecount_percentage > turnout_percentage):
                turnout_votes = county_votecount
                largest_turnout = county_name
                turnout_percentage = votecount_percentage
            ```
            
- Votes by candidate: Charles Casper Stockham: 23.0% (85,213), Diana DeGette: 73.8% (272,892), Raymon Anthony Doane: 3.1% (11,606)
    - Relevant code used:
    ```
    candidate_options = []
    candidate_votes = {}
    
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        headers = next(file_reader)
        for row in file_reader:
            total_votes = total_votes + 1
            candidate_name = row[2]
            if candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
            
        for candidate_name in candidate_votes:
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")         
    ```

- Election winner: Diana DeGette: 73.8% (272,892)
    - Relevant code used:
    ```
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    
            if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
     ```

### Election-Audit Summary
