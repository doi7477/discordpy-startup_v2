from ast import Not
import os
import random
import traceback
import asyncio
from datetime import datetime, timedelta, timezone

import discord
from discord.ext import tasks

#Discord設定
token = os.environ['DISCORD_BOT_TOKEN']
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#せとうぽサーバー
STUP_SERVER_ID = 578209286639976448                     #せとうぽ サーバID
ZATUDAN_CHANNEL_ID = 578209286639976452                 #せとうぽ-雑談
YOUSAI_CHANNEL_ID = 713535093469347955                  #せとうぽ-要塞攻略室
BOSS_CHANNEL_ID = 716168222075912192                    #せとうぽ-ボス討伐
KANBU_CHANNEL_ID = 605428683364106288                   #せとうぽ-幹部用
MEE6_CHANNEL_ID = 680065406878482473                    #せとうぽ-Mee6用
OFFICIAL_TWEET_CHANNEL_ID = 585415444790509568          #せとうぽ-公式ツイート
BUSINESS_TWEET_CHANNEL_ID = 890230400272715796          #せとうぽ-取引所ツイート
CHATDEL_CHANNEL_ID = 890168012232073306                 #せとうぽ-チャット削除
CONNECT_CHANNEL_ID = 890173732201570304                 #せとうぽ-接続通知
INSIDE_CHANNEL_ID = 895617944078393364                  #せとうぽ-裏チャンネル

#せとうぽロール
ID_ROLE_LV5 = 712327375479898194                        #ノーマルレベル
ID_ROLE_LV15 = 712328701605576744                       #レアレベル
ID_ROLE_LV25 = 712328832379650069                       #エピックレベル
ID_ROLE_LV35 = 712329159615053845                       #ユニークレベル
ID_ROLE_LV45 = 712329511978401808                       #レジェンドレベル
ID_ROLE_LV55= 890950275257495612                        #ミスティックレベル
ID_ROLE_MONITOR_OFFICIAL = 890901918971494451           #公式ツイート監視
ID_ROLE_MONITOR_BUSINESS = 890902056502702081           #取引所ツイート監視

#デバッグサーバー
DEBUG_SERVER_ID = 751149121284603935                    #どい動物園 サーバーID
DEBUG_CHANNEL_ID = 751149121876000851                   #どい動物園 debuglog
DEBUG_ACTIONCHANNEL1_ID = 905595698794356776            #どい動物園 actionlog-画像
DEBUG_ACTIONCHANNEL2_ID = 905675136563294219            #どい動物園 actionlog-テキスト
DEBUG_ACTIONCHANNEL3_ID = 905675346198798358            #どい動物園 actionlog-VC

#ユーザーID
DYNO_ID_1 = 905665627736383528                          #Dyno-通知オフにしてね
DYNO_ID_2 = 905614211424591912                          #Dyno-TC削除
DYNO_ID_3 = 905614058387017809                          #Dyno-VC接続
SETUPKUN_ID = 751252316187000885                        #せとうぽくんID

#メンションID
CHINO_MENTION = "<@567583369257287690>"
RIRI_MENTION = "<@586424949703442444>"
MIMO_MENTION = "<@568447476953251861>"

#ヘルプ文
embed_help = discord.Embed(title="**コマンドリスト一覧**",description="",color=0x4169E1)
embed_help.add_field(name="**/せとうぽ**",value="--> ヘルプを呼び出します",inline=False)
embed_help.add_field(name="**/せとうぽ おみくじ**",value="--> おみくじを引きます",inline=False)
embed_help.add_field(name="**/せとうぽ 公式**",value="--> 公式ツイート監視CHをON/OFFします",inline=False)
embed_help.add_field(name="**/せとうぽ 取引所**",value="--> 取引所ツイート監視CHをON/OFFします",inline=False)

#ようこそ文
welcomemsg_title = "ようこそ せとうぽへ"
welcomemsg_color = 0x4169E1
welcomemsg_png = "https://img.altema.jp/altema/uploads/2019/03/2019y03m07d_1405336875.png"
welcomemsg_contents = "以下で自己紹介をお願いします\r\n"\
        " <#771510773549629480> \r\n"\
        "\r\n"\
        ":large_blue_diamond: 基本ルール :large_blue_diamond: \r\n"\
        "以下リンクをご確認ください\r\n"\
        "https://discord.com/channels/578209286639976448/581850951682359296/773011836970205204\r\n"\
        "\r\n"\
        ":large_blue_diamond: 要塞の立ち回り方 :large_blue_diamond: \r\n"\
        "以下リンクをご確認ください\r\n"\
        "https://discord.com/channels/578209286639976448/713535093469347955/849246973202923531\r\n"\
        "\r\n"\
        ":large_blue_diamond: せとうぽくんについて :large_blue_diamond: \r\n"\
        "以下コマンドでご確認ください\r\n"\
        "/せとうぽ\r\n\r\n"\
        "↓↓↓おすすめコマンド↓↓↓\r\n"\
        "/せとうぽ 取引所\r\n"\
        "※Twitterの[#メイプルmTwitter取引所]を監視します\r\n"\
        "\r\n"\
        "不明点は気軽に連絡ください\r\n"

#アカイラム募集文
redram_title = "今日22時のアカイラム募集"
redram_color = 0xED1C24
redram_png = "https://lh3.googleusercontent.com/erYTDwgrj6fKqOWI9MR8j4zzS9Lbeocq_UjsdY7ltKKDju4mX1yxLwG-AvKyJHjvnIGWOp-tPkjx7K_wwq1Kk3ihyGGtsuNGk-DOJy3x6zA=rw"
redram_contents = "🙆‍♀ ハード\r\n"\
        "🙅‍♂️ ノーマル\r\n"\

#カオスアビス募集文 
chaosAbyss_title = "今日22時のカオスアビス募集"
chaosAbyss_color = 0xEDE51C
chaosAbyss_png = "https://lh3.googleusercontent.com/uO2fjlRg4QQQRzBzE8ZG4D-z2XZCnPHohcwNV-4oZ8PRTDlMjMVvQ0wzwFuv7Dp3x_TKYaJ0krGpynXQ8HLxgu_454KfFplO8Ibuo943eGw=rw"
chaosAbyss_contents = "🙆‍♀️ 参加\r\n"\

#テスト用
embed_test = discord.Embed(title=welcomemsg_title,description="",color=welcomemsg_color)
embed_test.add_field(name=":sparkles:テストさん:sparkles:\r\nご参加ありがとうございます",value=welcomemsg_contents,inline=False)
embed_test.set_thumbnail(url=welcomemsg_png)

#取引所NGワード
trade_ngword_list = ['メル売り','メル販売','メル買い手募集','1G=','1G＝','1g=','1g＝']

#プレイ中のワード
play_word_list = ['ヒーロー','ダークナイト','パラディン','ボウマスター','クロスボウマスター','ナイトロード','シャドー','ビショップ',\
                  'アークメイジ(火/毒)','アークメイジ(氷/雷)','キャプテン','バイパー','ソウルマスター','ウィンドシューター','ナイトウォーカー','フレイムウィザード',\
                  'ストライカー','デーモンスレイヤー','バトルメイジ','ワイルドハンター','カンナ','アラン','メルセデス','ファントム','エヴァン','ルミナス','隠月','ゼノン',\
                  'メカニック','ハヤト','カイザー','パスファインダー','エンジェリックバスター','キャノンシューター','デュアルブレイド','人生','オフ会']

####################
#タイマー処理
####################
@tasks.loop(seconds=60)
async def loops():
    channel_ready = client.get_channel(DEBUG_CHANNEL_ID)
    if channel_ready is None:
        print('デバックチャンネルIDの取得に失敗した')
        return
    await channel_ready.send('Loop')
    
    #現在時刻取得
    JST = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(JST).strftime('%H:%M')
    #要塞通知処理
    if now == '21:00': 
        print('21:00の要塞通知処理')
        channel = client.get_channel(YOUSAI_CHANNEL_ID)
        if channel is None:
            print('要塞チャンネルIDの取得に失敗した')
            return
        await channel.send('@everyone 要塞だよ！全員集合！！')
    elif now == '11:30': 
        print('11:30の通知処理')
        nowday = datetime.now(JST).weekday()
        print(f'{nowday}の日です')
        # 3は木曜日
        if nowday == 3:
            channel = client.get_channel(BOSS_CHANNEL_ID)
            if channel is None:
                print('ボス討伐チャンネルIDの取得に失敗した')
                return
            embed_join = discord.Embed(title=chaosAbyss_title,description="",color=chaosAbyss_color)
            embed_join.add_field(name=f"以下のリアクションをポチッと",value=chaosAbyss_contents,inline=False)
            embed_join.set_thumbnail(url=chaosAbyss_png)
            print('カオスアビス討伐通知')
            await channel.send(embed=embed_join)
    elif now == '18:00': 
        print('18:00の通知処理')
        channel = client.get_channel(BOSS_CHANNEL_ID)
        if channel is None:
            print('ボス討伐チャンネルIDの取得に失敗した')
            return
        embed_join = discord.Embed(title=redram_title,description="",color=redram_color)
        embed_join.add_field(name=f"以下のリアクションをポチッと",value=redram_contents,inline=False)
        embed_join.set_thumbnail(url=redram_png)
        print('アカイラム討伐通知')
        await channel.send(embed=embed_join)
    elif now == '23:00':
        print('23:00の要塞通知処理')
        channel = client.get_channel(ZATUDAN_CHANNEL_ID)
        if channel is None:
            print('雑談討伐チャンネルIDの取得に失敗した')
            return
        nowday = datetime.now(JST).weekday()
        print(f'{nowday}の日です')
        # 6は日曜日
        if nowday == 6:
            await channel.send('@everyone \r\n「シャレニアンの地下水路」と本日の「ギルド活動 施設物アップデート」はお済みですか？\r\nついでに、「戦え！伝説の帰還」もあと1時間でリセットです')
        else:
            await channel.send('@everyone \r\n本日の「ギルド活動 施設物アップデート」はお済みですか？')
    return

@loops.before_loop
async def loops_task_before_loop():
    print('waiting...')
    await client.wait_until_ready()

####################
#起動時の処理
####################
@client.event
async def on_ready():
    print('起動処理')
    #プレイ中更新
    presence = discord.Game(random.choice(play_word_list))
    await client.change_presence(activity=presence)

    channel_ready = client.get_channel(DEBUG_CHANNEL_ID)
    if channel_ready is None:
        print('デバックチャンネルIDの取得に失敗した')
        return
    await channel_ready.send('せとうぽくん起動しました')
    return

####################
#新規メンバー参加処理
####################
@client.event
async def on_member_join(member):
    print(f'新規メンバー参加処理 参加したサーバーID:[{member.guild.id}]')
    global welcomemsg_title
    global welcomemsg_color
    global welcomemsg_png
    global welcomemsg_contents

    channel_join = client.get_channel(ZATUDAN_CHANNEL_ID)
    if channel_join is None:
        print('雑談チャンネルIDの取得に失敗した')
        return

    if member.guild.id != STUP_SERVER_ID:
        print('別サーバーに入っているのでスキップ')
        return

    #ようこそ文発行
    embed_join = discord.Embed(title=welcomemsg_title,description="",color=welcomemsg_color)
    embed_join.add_field(name=f":sparkles:{member.name}さん:sparkles:\r\nご参加ありがとうございます",value=welcomemsg_contents,inline=False)
    embed_join.set_thumbnail(url=welcomemsg_png)
    await channel_join.send(embed=embed_join)
    return

####################
#メッセージ受信処理
####################
@client.event
async def on_message(message):
    global embed_help
    global embed_test
    global trade_ngword_list

    if message.author.id == SETUPKUN_ID:
        if len(message.embeds)!=0:
            if message.embeds[0].title == redram_title:
                await message.add_reaction("🙆‍♀️")
                await message.add_reaction("🙅‍♂️")
            elif message.embeds[0].title == chaosAbyss_title:
                await message.add_reaction("🙆‍♀️")
        return

    #BOT処理
    if message.author.bot:
        print(message.author.id)
        #デバッグに削除画像通知
        if message.author.id == DYNO_ID_1:
            channel_send = client.get_channel(DEBUG_ACTIONCHANNEL1_ID)
            if channel_send is None:
                print('チャンネルIDの取得に失敗した')
                return
            await channel_send.send(embed=message.embeds[0].copy())
            await message.delete()
            return

        #デバッグに削除メッセージ通知
        elif message.author.id == DYNO_ID_2:
            channel_send = client.get_channel(DEBUG_ACTIONCHANNEL2_ID)
            if channel_send is None:
                print('チャンネルIDの取得に失敗した')
                return
            await channel_send.send(embed=message.embeds[0].copy())
            return

        #デバッグにVC接続通知
        elif message.author.id == DYNO_ID_3:
            channel_send = client.get_channel(DEBUG_ACTIONCHANNEL3_ID)
            if channel_send is None:
                print('チャンネルIDの取得に失敗した')
                return
            await channel_send.send(embed=message.embeds[0].copy())
            return

        #Mee6チャンネルでの発言
        if message.channel.id == MEE6_CHANNEL_ID:
            if message.content.startswith('!LevelUp'):
                print('レベルアップ処理')
                mentions = message.mentions
                if not mentions:
                    print('メンション取得失敗')
                    return
                member = message.guild.get_member(mentions[0].id)
                tmp = message.content.split(',')
                #配列が3つないと区切り失敗
                if len(tmp) < 3:
                    print('区切りに失敗')
                    return

                level = tmp[2]
                if level == 'Level5':
                    print('Level5ロール付与')
                    addrole = message.guild.get_role(ID_ROLE_LV5)
                    await member.add_roles(addrole)
                    await message.channel.send('ロールを追加しました！！「Level5」')
                elif level == 'Level15':
                    print('Level15ロール付与')
                    addrole = message.guild.get_role(ID_ROLE_LV15)
                    remrole = message.guild.get_role(ID_ROLE_LV5)
                    await member.add_roles(addrole)
                    await member.remove_roles(remrole)
                    await message.channel.send('ロールを変更しました！！「Level5」→「Level15」')
                elif level == 'Level25':
                    print('Level25ロール付与')
                    addrole = message.guild.get_role(ID_ROLE_LV25)
                    remrole = message.guild.get_role(ID_ROLE_LV15)
                    await member.add_roles(addrole)
                    await member.remove_roles(remrole)
                    await message.channel.send('ロールを変更しました！！「Level15」→「Level25」')
                elif level == 'Level35':
                    print('Level35ロール付与')
                    addrole = message.guild.get_role(ID_ROLE_LV35)
                    remrole = message.guild.get_role(ID_ROLE_LV25)
                    await member.add_roles(addrole)
                    await member.remove_roles(remrole)
                    await message.channel.send('ロールを変更しました！！「Level25」→「Level35」')
                elif level == 'Level45':
                    print('Level45ロール付与')
                    addrole = message.guild.get_role(ID_ROLE_LV45)
                    remrole = message.guild.get_role(ID_ROLE_LV35)
                    await member.add_roles(addrole)
                    await member.remove_roles(remrole)
                    await message.channel.send('ロールを変更しました！！「Level35」→「Level45」')
                elif level == 'Level55':
                    print('Level55ロール付与')
                    addrole = message.guild.get_role(ID_ROLE_LV55)
                    remrole = message.guild.get_role(ID_ROLE_LV45)
                    await member.add_roles(addrole)
                    await member.remove_roles(remrole)
                    await message.channel.send('ロールを変更しました！！「Level45」→「Level55」')
                else:
                    print('ロール変更なし')
            return

        #公式ツイートチャンネルでの発言
        elif message.channel.id == OFFICIAL_TWEET_CHANNEL_ID:
            if '瞬断' in message.content or 'パッチの適用' in message.content:
                channel = client.get_channel(ZATUDAN_CHANNEL_ID)
                if channel is None:
                    print('雑談チャンネルIDの取得に失敗した')
                    return
                await channel.send("@everyone 瞬断をお知らせします。\r\n\r\n───以下内容───\r\n" + message.content)
            return

        #裏チャンネルでの発言
        elif message.channel.id == INSIDE_CHANNEL_ID:
            #メル販売切り分け処理
            tmp = message.content.split('!-!-!-!-!-!-!')
            #配列が2つないと区切り失敗
            if len(tmp) < 2:
                print('区切りに失敗')
                return

            for word in trade_ngword_list:
                if word in tmp[0]:
                    #メル売りなので通知しません
                    inside_channel = client.get_channel(INSIDE_CHANNEL_ID)
                    if inside_channel is None:
                        print('裏チャンネルIDの取得に失敗した')
                        return     
                    await inside_channel.send('ひゃっはああ！てめぇはダメだ！地獄に堕ちな')
                    return

            #メル売り以外なので通知します
            tweet_cannel = client.get_channel(BUSINESS_TWEET_CHANNEL_ID)
            if tweet_cannel is None:
                print('取引所ツイートチャンネルIDの取得に失敗した')
                return
            await tweet_cannel.send(tmp[1])
            return
        else:
            #特に連携しないBOTの発言のため何もせずに終了
            return

    #ユーザー処理
    else:
        channel_debugss = client.get_channel(DEBUG_CHANNEL_ID)
        if channel_debugss is None:
            print('デバックチャンネルIDの取得に失敗した')
            return
        await channel_debugss.send("[" + message.channel.name + "],[" + message.author.name + "]:" + message.content)

        if message.content.startswith('/せとうぽ'):
            tmp = message.content.split()
            if '/せとうぽ'  != tmp[0]:
                #トリガーコマンドが間違えている
                print('/せとうぽのコマンドミス')
                await message.channel.send('コマンドの入力に失敗しました。今一度ご確認ください。')
                await message.channel.send(embed=embed_help)
                return

            #コマンドがせとうぽのみ
            if len(tmp) == 1:
                print('ヘルプ表示処理')
                await message.channel.send(embed=embed_help)
                return

            #コマンドに引数が1つある
            elif len(tmp) == 2:
                #おみくじ処理
                if 'おみくじ' == tmp[1]:
                    print('おみくじ処理')
                    rand_result = random.randint(1,100)
                    if rand_result < 20:
                        await message.channel.send('大吉 です')
                    elif rand_result < 30:
                        await message.channel.send('中吉 です')
                    elif rand_result < 40:
                        await message.channel.send('吉 です')
                    elif rand_result < 50:
                        await message.channel.send('末吉 です')
                    elif rand_result < 60:
                        await message.channel.send('大区 です')
                    elif rand_result < 70:
                        await message.channel.send('大古 です')
                    elif rand_result < 80:
                        await message.channel.send('凶 です')
                    elif rand_result < 99:
                        await message.channel.send('大凶 です')
                    else:
                        await message.channel.send('占えませんでした')
                    return
                #公式ロール付与処理
                elif '公式' == tmp[1]:
                    change_role = message.guild.get_role(ID_ROLE_MONITOR_OFFICIAL)
                    member = message.guild.get_member(message.author.id)
                    if change_role in member.roles:
                        print('公式 ロール剥奪')
                        await member.remove_roles(change_role)
                        await message.channel.send('あなたの「公式ツイート監視」ロールを剥奪しました')
                    else:
                        print('公式 ロール付与')
                        await member.add_roles(change_role)
                        await message.channel.send('あなたに「公式ツイート監視」ロールを付与しました')
                    return
                #取引所ロール付与処理
                elif '取引所' == tmp[1]:
                    change_role = message.guild.get_role(ID_ROLE_MONITOR_BUSINESS)
                    member = message.guild.get_member(message.author.id)
                    if change_role in member.roles:
                        print('取引所 ロール剥奪')
                        await member.remove_roles(change_role)
                        await message.channel.send('あなたの「取引所ツイート監視」ロールを剥奪しました')
                    else:
                        print('取引所 ロール付与')
                        await member.add_roles(change_role)
                        await message.channel.send('あなたに「取引所ツイート監視」ロールを付与しました')
                    return
                #テストコマンド
                elif 'テスト' == tmp[1]:
                    print('テストコマンド実行処理')
                    await message.channel.send(embed=embed_test)
                    return
                else:
                    print('該当コマンドなし 第一引数指定ミス')
                    await message.channel.send('コマンドの入力に失敗しました。今一度ご確認ください。')
                    await message.channel.send(embed=embed_help)
                    return
            elif len(tmp) == 4:
                if '発言' == tmp[1]:
                    send_id = int(tmp[2])
                    send_message = tmp[3]
                    send_channel = client.get_channel(send_id)
                    if send_channel is None:
                        await message.channel.send('IDの入力に失敗してます')
                        return
                    await send_channel.send(send_message)
                    return
            #/せとうぽだったが該当コマンドではなかった
            else:
                print('該当コマンドなし 引数の数ミス')
                await message.channel.send('コマンドの入力に失敗しました。今一度ご確認ください。')
                await message.channel.send(embed=embed_help)
                return

#実行
#loops.start()
#loops.start()
#client.loop.create_task(loops())
async def fn():
    print('fn() start')
    await loops.start()
    print('fn() end')

client.run(token)
loop_ = asyncio.get_event_loop()
loop_.run_until_complete(fn())

#async def main():
#    task1 = asyncio.create_task(fn())
#    task2 = asyncio.create_task(client.run(token))
#    await task1
#    await task2
#asyncio.run(main())


