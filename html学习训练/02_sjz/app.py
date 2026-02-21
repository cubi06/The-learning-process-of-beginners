from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

jifeng_data = [
    {
        "skill_img": "/static/images/tuji.png",
        "skill_name": "突击",
        "skill_info": "突击兵有更强的战斗能力，在举镜瞄准状态下拥有更快的移动速度。",
        "back": "/static/images/background.jpg",
        "nickname": "疾风",
        "name": "[姓名：克莱尔·安·拜尔斯]",
        "info": "疾风是集高机动移动、缴械突入为一体的突击型干员。她可以在交战中提升自己的移动与翻滚速度，并使用钻墙电钻缴械掩体后的敌人，在战斗时还可以在原地布置锚点，进行闪回和自救，让敌人难以捕捉。"
    },
    {
        "skill_img": "/static/images/skill1.png",
        "skill_name": "爆发型辅助脊椎",
        "skill_info": "被子弹击中或有子弹从身边飞过时增加移动速度，常驻加速游泳效果。"
    },
    {
        "skill_img": "/static/images/skill2.png",
        "skill_name": "战术翻滚",
        "skill_info": "借助背部的辅助脊椎可以进行8个方向的快速翻滚，翻滚时会激活辅助脊椎，增加移动速度。"
    },
    {
        "skill_img": "/static/images/skill3.png",
        "skill_name": "钻墙电刺",
        "skill_info": "投掷电钻，可穿透掩体发射导电粉末并释放电击，电击可以麻痹敌人并击飞敌人手中的武器。"
    },
    {
        "skill_img": "/static/images/skill4.png",
        "skill_name": "紧急回避装置",
        "skill_info": "原地发射锚点，并通过安全绳连结身体，再次激活可通过安全绳将自己拉回锚点。技能激活期间若受到致命伤害，返回锚点可进行自救。"
    }
]

wuming_data = [
    {
        "skill_img": "/static/images/tuji.png",
        "skill_name": "突击",
        "skill_info": "突击兵有更强的战斗能力，在举镜瞄准状态下拥有更快的移动速度。",
        "back": "/static/images/background2.jpg",
        "nickname": "无名",
        "name": "[姓名：埃利·德·蒙贝尔]",
        "info": "无名曾接受过来自哈夫克的军事训练，也有丰富的佣兵经验，擅长信息干扰，精通多种战斗技巧。他是集单兵绕后、追踪伤害、闪光突破为一体的干员，对隐蔽突袭作战造诣极深，能在战场上出其不意地刺入敌方防御空缺。"
    },
    {
        "skill_img": "/static/images/skill5.png",
        "skill_name": "重伤延滞",
        "skill_info": "被无名击伤的敌人需要花更长时间使用药品，被击倒的敌人也需要更长的时间才能被救起。"
    },
    {
        "skill_img": "/static/images/skill6.png",
        "skill_name": "旋刃飞行器",
        "skill_info": "旋刃飞行器会锁定前方的敌人，锁定后丢出即可自动追踪敌人并爆开，释放内部的刀片，伤害并减速敌人，同时附加流血状态。"
    },
    {
        "skill_img": "/static/images/skill7.png",
        "skill_name": "突破型闪光弹",
        "skill_info": "向前投掷一颗特制的突破型闪光弹，该闪光弹会在接触到墙体后短时间内爆炸，对所有面朝闪光的附近敌人进行闪光震撼。"
    },
    {
        "skill_img": "/static/images/skill8.png",
        "skill_name": "静默潜袭",
        "skill_info": "启动声波干扰器与信号干扰器，缩小自身移动时的声音传播范围，同时使敌方的侦察道具无法侦察到无名的具体位置。"
    }
]

@app.route('/api/jifeng', methods=['GET'])
def get_jifeng():
    return jsonify(jifeng_data)


@app.route('/api/wuming', methods=['GET'])
def get_wuming():
    return jsonify(wuming_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)