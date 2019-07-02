class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        li = []
        
        for i in range(0, len(emails)):
            email = emails[i]
            emailAtIndex = email.index("@")
            emailLocalName = email[:emailAtIndex].replace(".", "")
            
            if "+" in email:
                emailPlusIndex = emailLocalName.index("+")
                emailLocalName = emailLocalName[:emailPlusIndex]
            
            emailDomainName = email[emailAtIndex:]
            email = emailLocalName + emailDomainName
            
            if email not in li:
                li.append(email)
                
        return len(li)
        
