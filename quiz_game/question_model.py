class Question:
    def __init__(self,text,ans):
        self.text=text
        self.ans=ans

new_q=Question("adf","False")
print(new_q.text)
print(new_q.ans)