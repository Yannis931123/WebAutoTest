slang_dic = {"觉醒年代": "AAA", "YYDS": "永远的神", "双减": "教育部政令"}

query_dic = input("请输入你想查询的词语：")
if query_dic in slang_dic:
    print("您查询的" + query_dic + "的含义如下：")
    print(slang_dic[query_dic])
else:
    print("您查询的" + query_dic + "未收录")
    print("当前已经收录的词条数量为" + str(len(slang_dic)) + "条")
