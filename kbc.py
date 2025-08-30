qlist=["""International Literacy Day is observed on:
A) Sep 8
B) Nov 28
C) May 2
D) Sep 22""",

"""Lakshadweep’s language is:
A) Tamil
B) Hindi
C) Malayalam
D) Telugu""",

"""Kumbh Mela is held every 12 years at:
A) Ujjain, Puri, Prayag, Haridwar
B) Prayag, Haridwar, Ujjain, Nasik
C) Prayag, Haridwar, Nasik, Kashi
D) Ujjain, Prayag, Rameshwaram, Haridwar""",

"""Bahubali festival relates to which religion?
A) Islam
B) Hinduism
C) Buddhism
D) Jainism""",


"""World Standards Day falls on:
A) June 26
B) Oct 14
C) Nov 15
D) Dec 2"""
]
ans=["a","c","b","d","b"]
amount=[2000,4000,6000,8000,10000]
winamt=0
for i in range(0,len(qlist)):
    print(qlist[i])
    answer=input("Enter option: ")
    if(answer.lower()==ans[i]):
        print("Congrats! correct answer")
        print(f"You are winning :{amount[i]} ")
        winamt=winamt+amount[i]
        continue
    else:
        print("OOPS! wrong answer:")
        print(f"you win: Rs.{winamt}")
        break


