from typing import List


class Reorder:
    def reorderLogFiles(self, logs:List[str])->List[str]:
        letters, digits=[],[]
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return letters + digits

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
reorder = Reorder()
print(reorder.reorderLogFiles(logs)) 
# Expected output: ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
