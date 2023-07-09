from pyknp import KNP

knp = KNP()
line = "運転をするのが初めてな私でも、安心して目的地まで到着できた。"
#"免許取り立ての人が多いイメージ"
#"運転が初めてな私でも、安心して目的地まで到着できた。"
#"日本の新しいスポーツが好きな彼女は友達と遊ぶ"#二回
#"階段がかなりあるので足腰が弱い人にはきついかもです."
#最後までいくと1300段あるので無理だったからお守りがほしかったので売り場までは頑張っていきました。そこまでで700段近くありました。次の日は筋肉痛で足がパンパンになったけどいい運動になったかな"

result = knp.parse(line)
print(result.draw_tag_tree())

target = "<SM-主体>"
list_1 = []

for bnst in result.bnst_list():#このforはtargetを探すコード
    parent_x = bnst.parent
    child_rep = bnst.midasi #mrph_list()は形態素で取得、
    
    if parent_x == None:
        pass
    else:
        parent_1 = parent_x.fstring#fstringで意味マーカを取得
        if target in parent_1:#feture(parent_1)に人("<SM-主体>")が含まれてたら下記のコードを実行。人に係っている単語を探していくのが下記のコード
            print(parent_x.midasi)
            for i in result.bnst_list():#人に係っている単語を取得するfor
                if i.midasi == parent_x.midasi:
                    print(child_rep,">>>",parent_x.midasi)
                    print(child_rep + parent_x.midasi)#childは「好きな」
                    list_1.append(child_rep)
                    new = list_1
                    for s in result.bnst_list():#二回目
                        parent_2 = s.parent
                        japan = ""
                        if parent_2 == None:
                            pass
                        else:
                            parent_2x = parent_2.midasi
                            child_rep2 = s.midasi
                            if parent_2x == child_rep:
                                print(child_rep2,">>>",parent_2x)
                                print(child_rep2 + parent_2x)
                                text_3 = child_rep2 + parent_2x
                                list_1.append(text_3)
                                for d in result.bnst_list():
                                    parent_3 = d.parent
                                    if parent_3 == None:
                                        pass
                                    else:
                                        parent_3x = parent_3.midasi
                                        child_rep3 = d.midasi
                                        if parent_3x == child_rep2:
                                            print(child_rep3,">>>",parent_3x)
                                            print(japan + child_rep3 + parent_3x + parent_2x,"japan + chiled_rep3 + parent_3x + parent_2x")
                                            text_1 = japan + child_rep3 + parent_3x + parent_2x
                                            japan = ""
                                            print(child_rep3 + parent_3x + parent_2x,"japan + chiled_rep3 + parent_3x + parent_2x")
                                            text_2 = child_rep3 + parent_3x + parent_2x
                                            if text_1 == text_2:
                                            #一緒だったら追加しないコードを記載
                                                list_1.append(text_1)
                                            else:
                                                list_1.append(text_2)
                                                list_1.append(text_1)
                                            

                                            japan = child_rep3
                                            
 
                                                        
print(list_1)
print("a")



            #print("1:",list_1)
    #どうにしかして同じ箇所に係っている所が二個以上あれば取りたい
                
                    




                

