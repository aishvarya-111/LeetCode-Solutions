class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res = ""
        for i in s:
            if i == "]":
                sub = ""
                while st[-1]!= '[':
                    sub=st.pop()+sub
                st.pop()
                num = ""
                while st and st[-1].isdigit():
                    num=st.pop()+num
                sub=sub*int(num) 
                st.append(sub)
                
            else:
                st.append(i)
        return "".join(st)
        