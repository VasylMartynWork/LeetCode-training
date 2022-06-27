st = "Myself2 Me1 I4 and3"
class Solution:
    def sortSentence(self, s: str) -> str:
        stri = s.split()
        st = ""
        i = 1
        while(i <= len(stri)):
            for el in stri:
                if(int(el[len(el) - 1]) == i):
                    st += el
                    st = st.replace(f'{i}', '')
                    if(i < len(stri)):
                        st += " "
            i += 1
        return st

sol = Solution()
print(sol.sortSentence(st))