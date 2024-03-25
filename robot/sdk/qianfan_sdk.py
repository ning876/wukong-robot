
# 通过环境变量传递（作用于全局，优先级最低）
import os
import qianfan
os.environ["QIANFAN_ACCESS_KEY"] = "c03972d35c6f48ae88baf088e5397d19"
os.environ["QIANFAN_SECRET_KEY"] = "3655435a6ff44c509086590e4a19df38"

def one_cycle_dialog(query,model_name,stream=False):

    chat_comp = qianfan.ChatCompletion()
    # 调用默认模型，即 ERNIE-Bot-turbo
    resp = chat_comp.do(messages=[{
        "role": "user",
        "content": query
    }],model=model_name,stream=stream)
    if stream==True:
        for r in resp:
            print(r.body.get('result',''))
    else:
        print(resp.body.get('result','无法回答！'))

###多轮对话


def more_cycle_dialog(query,model_name,stream=False):
    chat_comp = qianfan.ChatCompletion()

    # 下面是一个与用户对话的例子
    msgs = qianfan.Messages()
    if query!='':
        msgs.append(query)
    while True:
        if query!="":
            resp = chat_comp.do(messages=msgs,model=model_name,stream=stream)
            output = resp.body.get('result','无法回答！')
            print(output) # 模型的输出
            msgs.append(resp)            # 追加模型输出
            query=""
        else:
            msgs.append(input("输入："))         # 增加用户输入
            resp = chat_comp.do(messages=msgs,model=model_name,stream=stream)
            output = resp.body.get('result','无法回答！')
            print(output) # 模型的输出
            msgs.append(resp)            # 追加模型输出

if __name__ == "__main__":
    model_name='Yi-34B-Chat'
    query='请帮我介绍一下长城汽车' #长城汽车和古建筑长城有什么关联
    #query=""
    #one_cycle_dialog(query,model_name,True)
    more_cycle_dialog(query,model_name)