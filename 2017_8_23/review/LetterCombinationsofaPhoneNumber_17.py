# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution(object):
    def letterCombinations(self, digits):
        """

        :param digits: str
        :return: List[str]
        """
        if not digits: return []
        dd = {"0":"0", "1":"1", "2":"abc","3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
              "8": "tuv", "9": "wxyz"}

        res = [""]
        for d in digits:
            tempStr = []
            for s in dd[d]:
                for string in res:
                    tempStr.append(string + s)
                res = tempStr
        return res