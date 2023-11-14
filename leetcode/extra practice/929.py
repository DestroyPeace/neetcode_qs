List = list 

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []

        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")[0]
            local.replace(".", "")


            if f"{local.replace('.', '')}@{domain}" not in res:
                res.append(f"{local.replace('.', '')}@{domain}")

        return len(res)
    
test = Solution()
print(test.numUniqueEmails(emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

        
