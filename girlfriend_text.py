import itchat   # 记得安装这个库
import schedule # 记得安装这个库


def get_girlfriend():
    girl_list = itchat.search_friends(name=u'name')  # name替换为对象微信名即可
    girl_name = girl_list[0]['UserName']
    return girl_name


def send_text(todo):
    name = get_girlfriend()
    itchat.send_msg(todo,toUserName=name)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)    # 登录
    list = ['小可爱早安','要记得乖乖吃饭哦~~','快去午睡休息啦❤️','乖乖睡觉哦，别熬夜啦，晚安~']
    schedule.every().day.at('08:30').do(send_text, list[0])    # 早安语
    schedule.every().day.at('12:00').do(send_text, list[1])    # 提醒吃饭
    schedule.every().day.at('13:00').do(send_text, list[2])    # 提醒午睡
    schedule.every().day.at('22:30').do(send_text, list[3])    # 晚安告别

    while True:
        schedule.run_pending()

