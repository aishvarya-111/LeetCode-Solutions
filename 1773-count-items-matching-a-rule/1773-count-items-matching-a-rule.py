class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        z = list(zip(*items))
        if ruleKey == "type":
            return z[0].count(ruleValue)
        elif ruleKey == "color":
            return z[1].count(ruleValue)
        else:
            return z[2].count(ruleValue)