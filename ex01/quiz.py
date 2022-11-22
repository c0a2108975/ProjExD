import random
import datetime
def shutudai(qa_list):
    qa = random.choice(qa_list)
    print("問題："+qa["q"])
    return qa["a"]

def kaitou(ans):
    st=datetime.datetime.now()
    ans = input("答えるんだ:")
    ed = datetime.datetime.now()
    if ans in ans_list:
        print("正解")
    else:
        print("出直してこい")
    
    print("解答時間："+str((ed-st).seconds)+"秒")


if __name__== "__main__":
    qa_list=[{"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]},
             {"q":"カツオ妹の名前は？","a":["ワカメ","わかめ"]},
             {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]},]

    ans_list=shutudai(qa_list)
    kaitou(ans_list)














"""import random
import datetime
def shutudai():
    quiz=["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    masuo_ans=["マスオ","ますお"]
    wakame_ans=["ワカメ","わかめ"]
    tarao_ans=["甥","おい","甥っ子","おいっこ"]
    st =datetime.datetime.now()
    mondai = random.choice(quiz)
    if mondai == quiz[0]:
        return 1
    elif mondai ==quiz[1]:
        return 2
    else:
        return 3
    print(mondai)
def kaitou():
    ans = input("答えるんだ：")
    if sutudai() == 1:
        if ans in masuo_ans:
            print("正解!!")
        else:
            print("出直してこい")

    if sutudai() == 2:
        if ans in wakame_ans:
            print("正解!!")

        else:
            print("出直してこい")

    if sutudai() == 3:
        if ans in tarao_ans:
            print("正解!!")

        else:
            print("出直してこい")
    ed = datetime.datetime.now()
    print(str((ed-st).seconds)+"秒")
def main():
    shutudai()
    kaitou()"""