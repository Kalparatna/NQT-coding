'''
2. Minimum Team Selection to Cover Required Skills
Problem Statement:
You are given a list of required skills and a list of candidates, where each candidate has a subset of skills. Your task is to find the smallest possible team such that all required skills are covered.

You will be given:
1. Required skills list
2. Number of candidates (N)
3. Skillsets of N candidates

Return the indices of selected candidates forming the smallest team.

Example:
Input:
a b c d
4
a b
b c
c d
d
Output:
0 2

Input:
a b c
3
a
b c
c
Output:
0 1

'''

def smaller_sufficient_team(req_skills, people):
    from itertools import combinations

    required = set(req_skills)
    n = len(people)

    people_skills = [set(person) for person in people]
    min_team = list(range(n))

    for team_size in range(1, n+1):
        for team_indices in combinations(range(n), team_size):
            team_skills = set()
            for i in team_indices:
                team_skills|= people_skills[i]
            
            if required.issubset(team_skills):
                if len(team_indices) < len(min_team):
                    min_team = list(team_indices)
                break
        if len(min_team) <= team_size:
            break
    
    return min_team

if __name__ == "__main__":
    req_skills = input().strip().split()
    n  = int(input())
    people = [input().strip().split()for _ in range(n)]

    result =  smaller_sufficient_team(req_skills, people)
    print(" ".join(map(str, result)))
