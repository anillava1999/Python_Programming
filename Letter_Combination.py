'''

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution(object):
    def letterCombinations(self, digits):
        input_digit = digits
        input_calc = []
        string_store = []
        di = {2 : "abc",3 : "def", 4 : "ghi",5 : "jkl",6 : "mno",7 : "pqrs",8 : "tuv",9 : "wxyz",}



        for i in input_digit:
            input_calc.append(int(i))
            
        #print(input_calc)
        for j in input_calc:
            if j in di:
                #print(j)
                #print(di.get(j))
                string_store.append(di.get(j))

        result_list = []
        lk = 0
        len_st = len(string_store)
        for a in range(len(string_store)):
            for s in string_store[a]:
                print(s)
                index_check = 0
                if  len_st >= a+2 :
                    for g in string_store[a+1]:
                        result = s+g
                        lk = len(string_store[a+1])
                        result_list.append(result)
                    index_check +=1
                    continue
        if len(input_digit) == 1:
            out_list = list(di[int(input_digit)])
            return out_list
        else:
            return result_list
        
