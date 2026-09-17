class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = {}
        def recur(s1_ind, s2_ind, s3_ind):
            if (s1_ind,s2_ind,s3_ind) in m:
                return m[(s1_ind,s2_ind,s3_ind)]
            if (s1_ind >= len(s1) and s2_ind >= len(s2) and s3_ind >= len(s3) ):
                m[(s1_ind,s2_ind, s3_ind)] = True
                return True
            elif s3_ind >= len(s3):
                m[(s1_ind,s2_ind, s3_ind)] = False
                return False
            elif s1_ind < len(s1) and s2_ind < len(s2) and s1[s1_ind] == s2[s2_ind] == s3[s3_ind]:
                a = recur(s1_ind+1, s2_ind, s3_ind+1)
                if a:
                    m[(s1_ind,s2_ind, s3_ind)] = True
                    return True

                b = recur(s1_ind, s2_ind+1, s3_ind+1)

                if b:
                    m[(s1_ind,s2_ind, s3_ind)] = True
                    return True
                
                
            elif s1_ind < len(s1) and s1[s1_ind] == s3[s3_ind]:
                a =  recur(s1_ind+1, s2_ind, s3_ind+1)
                m[(s1_ind,s2_ind, s3_ind)] = a

                return a
            elif  s2_ind < len(s2) and s2[s2_ind] == s3[s3_ind]:
                b =  recur(s1_ind, s2_ind+1, s3_ind+1)
                m[(s1_ind,s2_ind, s3_ind)] = b

                return b
            m[(s1_ind,s2_ind, s3_ind)] = False
            return False

        return recur(0,0,0)

        