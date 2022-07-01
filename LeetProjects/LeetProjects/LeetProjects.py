sentence = "mqzedwtwcdopqehzhcbphiwqpnmlmyzabqpfvigmyborlzcasgivklcuwbiilohvzysfmodeefagnmkexnaridkgxrhzedlsitbsetaofosptvcklkaqxasrcbmlabvwhzmwdglfkmqkkqdxucbwsizgiuchgeptmgslrvxzgaunoiifnlsltubxlbfnsxvyzhuqszvebvtcqurwnacsfavoupiqmbfwmuyingsfwbernknanqpyxkocstdtbxymvrdecnyffhipwlhyonvbrlqicdomgexguyvldoeazagmwxrnxwzifrcklotrbuoqiefotlkevubpguuicvgucupegeswtcgzubzihqtfvhxdrxxnudiccqhtqucoogpdekbosxacfvtlmvqowvwqteimsisnqvxikonvspfkheruovqmkbfnefqtduynoqydkmgopwwtloshegflixsihomiccfofgqbghqxxsyuedgdnahaqbazhxxtsfbadwxaxhcnxwspmkxwbazqxpkrghoegwbiblwwkmgzbymsvmnrebgrzkpwunxtkruuenxguckaxqmvkstdkexlvaslalfwxivrswhgrvhknzwcmueqqlxgkklbmefchcdtxqcwarkvwwqulfmofnsvmrbxxlsaiqnzxrsffapqwpllndqnsmbgseaeipmrthgwrnrplgufzwahkzxhckzidiokttoclvvmowtreafspznomsouqzttspvoxtkzmxacnmxhzfhhtyrbgeroloeoncpikhktfmfhueahppzeekfaqvtslivpvlmuskdzrofdtgpnmpfflsymkggpraulvpffkbfvrxdhirubsidzfwvwbriifntgdmkuodwhkbmqxkkagcooitylwqgxqvmnoultivwpmilorbtwpcxzgbtxpzhqhuqhzmtqyfpbinmktabcwisquhn"

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        co = 0
        for i in alph:
            exist = i in sentence
            if(exist == True):
                co = 1
            else:
                return False
        if(co == 1):
            return True

sol = Solution()
print(sol.checkIfPangram(sentence))