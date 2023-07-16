class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        
        n, m = len(req_skills), len(people)
        skill_idx = {v : i for i, v in enumerate(req_skills)}
        dp = { 0: [] }
        for i, p in enumerate(people):
            Cur_skill = 0
            for skill in p:
                if skill in skill_idx:
                    Cur_skill |= 1 << skill_idx[skill]
            for prev, need in dict(dp).items():
                Comb = prev | Cur_skill
                if Comb == prev: continue
                if Comb not in dp or len(dp[Comb]) > len(need) + 1:
                    dp[Comb] = need + [i]
        return dp[(1 << n) - 1]
        

# Follow me on instagram for more my instagram id is - @codewithsomesh
