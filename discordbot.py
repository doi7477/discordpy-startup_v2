#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Discode bot SetupKun Version.2.0.0

Todo:
    * 
    * 
"""
from ast import Not
import os
import random
from re import A
import traceback
from datetime import datetime, timedelta, timezone
import asyncio
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
DEBUG_INFORMATION_ID = 1020902066639614053              #通知用チャンネル

#Bot ID
DYNO_ID_1 = 905665627736383528                          #Dyno-通知オフにしてね
DYNO_ID_2 = 905614211424591912                          #Dyno-TC削除
DYNO_ID_3 = 905614058387017809                          #Dyno-VC接続
MEE6_ID = 159985870458322944                            #Mee6ID
SETUPKUN_ID = 1018078962167066685                       #せとうぽくんID

#ユーザーメンションID
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
welcomemsg_img = "https://img.altema.jp/altema/uploads/2019/03/2019y03m07d_1405336875.png"
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
redram_title = "22:00頃のアカイラム募集"
redram_color = 0xED1C24
redram_png = "https://lh3.googleusercontent.com/erYTDwgrj6fKqOWI9MR8j4zzS9Lbeocq_UjsdY7ltKKDju4mX1yxLwG-AvKyJHjvnIGWOp-tPkjx7K_wwq1Kk3ihyGGtsuNGk-DOJy3x6zA=rw"
redram_contents = "🙆‍♀ ハード\r\n"\
        "🙅‍♂️ ノーマル\r\n"\

#カオスアビス募集文
chaosAbyss_title = "22:00頃のカオスアビス募集"
chaosAbyss_color = 0xEDE51C
chaosAbyss_png = "https://lh3.googleusercontent.com/uO2fjlRg4QQQRzBzE8ZG4D-z2XZCnPHohcwNV-4oZ8PRTDlMjMVvQ0wzwFuv7Dp3x_TKYaJ0krGpynXQ8HLxgu_454KfFplO8Ibuo943eGw=rw"
chaosAbyss_contents = "🙆‍♀️ 参加\r\n"\

#カオスマグナス募集文
chaosMagnus_title = "22:20頃のカオスマグナス募集"
chaosMagnus_color = 0x4c6cb3
chaosMagnus_png = "https://lh3.googleusercontent.com/vo5KF13NSLJo_OS7JC5H1u5LzO1M16SJqb5tDz08eDJSWYAHnK60HaNM0MiTfx2wJLtfJYUresODRXPNURUYwZlQTFqIr2cHqQVFDYza5wQ=rw"
chaosMagnus_contents = "🙆‍♀️ 参加\r\n"\

#テスト用
embed_test = discord.Embed(title=welcomemsg_title,description="",color=welcomemsg_color)
embed_test.add_field(name=":sparkles:テストさん:sparkles:\r\nご参加ありがとうございます",value=welcomemsg_contents,inline=False)
embed_test.set_thumbnail(url=welcomemsg_img)

#取引所NGワード
trade_ngword_list = ['メル売り','メル販売','メル買い手募集','1G=','1G＝','1g=','1g＝']

#プレイ中のワード
play_word_list = ['ヒーロー','ダークナイト','パラディン','ボウマスター','クロスボウマスター','ナイトロード','シャドー','ビショップ',\
                  'アークメイジ(火/毒)','アークメイジ(氷/雷)','キャプテン','バイパー','ソウルマスター','ウィンドシューター','ナイトウォーカー','フレイムウィザード',\
                  'ストライカー','デーモンスレイヤー','バトルメイジ','ワイルドハンター','カンナ','アラン','メルセデス','ファントム','エヴァン','ルミナス','隠月','ゼノン',\
                  'メカニック','ハヤト','カイザー','パスファインダー','エンジェリックバスター','キャノンシューター','デュアルブレイド']

############################################################
# Proprietary method
############################################################
def debug_log(text):
    """
    ログ出力

    Parameters:
    ----------
    text : String
        出力するテキスト
    """
    #時刻取得
    JST = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(JST).strftime('%Y-%m-%dT%H:%M:%S.%f')
    #時刻含めたログ出力
    print(f'[{now}]{text}')

async def send_message(channel_id, message):
    """
    メッセージ送信

    Parameters:
    ----------
    channel_id : int
        チャンネルID
    message : String
        メッセージ内容
    """
    debug_log(f'[send_message]:{channel_id}, {message}')
    #メッセージ送信
    channel = client.get_channel(channel_id)
    if channel is None:
        debug_log(f'チャンネルIDの取得に失敗しました({channel_id})')
        return
    await channel.send(message)

async def on_message_for_setupkun(message):
    """
    メッセージ受信(せとうぽくん)

    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    #せとうぽくんのメッセージがボス募集通知の場合リアクションを付ける
    
    if len(message.embeds)!=0:
        if message.embeds[0].title == redram_title:
            debug_log('アカイラム募集リアクション')
            await message.add_reaction("🙆‍♀️")
            await message.add_reaction("🙅‍♂️")
        elif message.embeds[0].title == chaosAbyss_title:
            debug_log('カオスアビス募集リアクション')
            await message.add_reaction("🙆‍♀️")
        elif message.embeds[0].title == chaosMagnus_title:
            debug_log('カオスマグナス募集リアクション')
            await message.add_reaction("🙆‍♀️")
        else:
            debug_log('メッセージ受信(せとうぽくん) 何もしない')
    else:
        debug_log('メッセージ受信(せとうぽくん) 何もしない')

async def on_message_for_another_bot(message):
    """
    メッセージ受信(他Bot)

    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    if message.author.id == DYNO_ID_1:
        #デバックに画像削除メッセージ通知
        debug_log('デバックに画像削除メッセージ通知')
        await send_message(DEBUG_ACTIONCHANNEL1_ID, embed=message.embeds[0].copy())
        return

    elif message.author.id == DYNO_ID_2:
        #デバッグに削除メッセージ通知
        debug_log('デバッグに削除メッセージ通知')
        await send_message(DEBUG_ACTIONCHANNEL2_ID, embed=message.embeds[0].copy())
        return

    elif message.author.id == DYNO_ID_3:
        #デバッグにVC接続メッセージ通知
        debug_log('デバッグにVC接続メッセージ通知')
        await send_message(DEBUG_ACTIONCHANNEL3_ID, embed=message.embeds[0].copy())
        return
    
    if message.channel.id == MEE6_CHANNEL_ID:
        #mee6での発言
        debug_log('mee6での発言')
        if message.content.startswith('!LevelUp'):
            debug_log('Mee6レベルアップ処理')
            mentions = message.mentions
            if not mentions:
                debug_log('メンション取得失敗')
                return
            member = message.guild.get_member(mentions[0].id)
            tmp = message.content.split(',')
            #配列が3つないと区切り失敗
            if len(tmp) < 3:
                debug_log('区切りに失敗')
                return

            level = tmp[2]
            if level == 'Level5':
                debug_log('Level5ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV5))
                await send_message(message.channel.id, 'ロールを追加しました！！「Level5」')
            elif level == 'Level15':
                debug_log('Level15ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV15))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV5))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level5」→「Level15」')
            elif level == 'Level25':
                debug_log('Level25ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV25))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV15))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level15」→「Level25」')
            elif level == 'Level35':
                debug_log('Level35ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV35))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV25))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level25」→「Level35」')
            elif level == 'Level45':
                debug_log('Level45ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV45))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV35))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level35」→「Level45」')
            elif level == 'Level55':
                debug_log('Level55ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV55))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV45))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level45」→「Level55」')
            else:
                debug_log('ロール変更なし')
            return
    
    elif message.channel.id == OFFICIAL_TWEET_CHANNEL_ID:
        #公式ツイートチャンネルでの発言
        debug_log('公式ツイートチャンネルでの発言')
        if '瞬断' in message.content or 'パッチの適用' in message.content:
            debug_log('瞬断通知')
            await send_message(ZATUDAN_CHANNEL_ID, "@everyone 瞬断をお知らせします。\r\n\r\n───以下内容───\r\n" + message.content)
            return

    elif message.channel.id == INSIDE_CHANNEL_ID:
        #裏チャンネルでの発言
        debug_log('#裏チャンネルでの発言')
        #メル販売切り分け処理
        tmp = message.content.split('!-!-!-!-!-!-!')
        #配列が2つないと区切り失敗
        if len(tmp) < 2:
            debug_log('区切りに失敗')
            return

        for word in trade_ngword_list:
            if word in tmp[0]:
                debug_log('メル売りなので通知しない')
                await send_message(INSIDE_CHANNEL_ID, 'ひゃっはああ！てめぇはダメだ！地獄に堕ちな')
                return

        debug_log('メル売り以外なので通知')
        await send_message(BUSINESS_TWEET_CHANNEL_ID, tmp[1])
        return

async def on_message_for_user(message):
    """
    メッセージ受信(ユーザー)

    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    await send_message(DEBUG_CHANNEL_ID, "[" + message.channel.name + "],[" + message.author.name + "]:" + message.content)

    if message.content.startswith('/せとうぽ'):
        tmp = message.content.split()
        if '/せとうぽ' != tmp[0]:
            #トリガーコマンドが間違えている
            debug_log('/せとうぽのコマンドミス(/せとうぽの後にスペースが入っていない)')
            await send_message(message.channel.id, 'コマンドの入力に失敗しました。今一度ご確認ください。')
            await send_message(message.channel.id, embed=embed_help)
            return

        if len(tmp) == 1:
            #コマンドがせとうぽのみ
            debug_log('ヘルプ表示処理')
            await send_message(message.channel.id, embed=embed_help)
            return

        elif len(tmp) == 2:
            #コマンドに引数が1つある
            if 'おみくじ' == tmp[1]:
                #おみくじ
                debug_log('おみくじ')
                rand_result = random.randint(1,100)
                if rand_result < 20:
                    await send_message(message.channel.id, '大吉 です')
                elif rand_result < 30:
                    await send_message(message.channel.id, '中吉 です')
                elif rand_result < 40:
                    await send_message(message.channel.id, '吉 です')
                elif rand_result < 50:
                    await send_message(message.channel.id, '末吉 です')
                elif rand_result < 60:
                    await send_message(message.channel.id, '大区 です')
                elif rand_result < 70:
                    await send_message(message.channel.id, '大古 です')
                elif rand_result < 80:
                    await send_message(message.channel.id,'凶 です')
                elif rand_result < 99:
                    await send_message(message.channel.id,'大凶 です')
                else:
                    await send_message(message.channel.id,'占えませんでした')
                return
            
            elif '公式' == tmp[1]:
                #公式ロール付与/剥奪
                change_role = message.guild.get_role(ID_ROLE_MONITOR_OFFICIAL)
                member = message.guild.get_member(message.author.id)
                if change_role in member.roles:
                    debug_log('公式 ロール剥奪')
                    await member.remove_roles(change_role)
                    await send_message(message.channel.id, 'あなたの「公式ツイート監視」ロールを剥奪しました')
                else:
                    debug_log('公式 ロール付与')
                    await member.add_roles(change_role)
                    await send_message(message.channel.id, 'あなたに「公式ツイート監視」ロールを付与しました')
                return
            
            elif '取引所' == tmp[1]:
                #取引所ロール付与/剥奪
                change_role = message.guild.get_role(ID_ROLE_MONITOR_BUSINESS)
                member = message.guild.get_member(message.author.id)
                if change_role in member.roles:
                    debug_log('取引所 ロール剥奪')
                    await member.remove_roles(change_role)
                    await send_message(message.channel.id, 'あなたの「取引所ツイート監視」ロールを剥奪しました')
                else:
                    debug_log('取引所 ロール付与')
                    await member.add_roles(change_role)
                    await send_message(message.channel.id, 'あなたに「取引所ツイート監視」ロールを付与しました')
                return
            
            elif 'テスト' == tmp[1]:
                #テストコマンド
                debug_log('テストコマンド実行')
                await message.channel.send(embed=embed_test)
                return

            else:
                #該当コマンドなし 第一引数指定ミス
                debug_log('該当コマンドなし 第一引数指定ミス')
                await send_message(message.channel.id, 'コマンドの入力に失敗しました。今一度ご確認ください。')
                await send_message(message.channel.id, embed=embed_help)
                return

        elif len(tmp) == 4:
            #せとうぽくんで発言
            debug_log('せとうぽくんで発言')
            if '発言' == tmp[1]:
                send_id = int(tmp[2])
                send_message = tmp[3]
                await send_message(send_id, send_message)
                return
        
        else:
            #/せとうぽだったが該当コマンドではなかった
            debug_log('該当コマンドなし 引数の数ミス')
            await send_message(message.channel.id, 'コマンドの入力に失敗しました。今一度ご確認ください。')
            await send_message(message.channel.id, embed=embed_help)
            return

############################################################
#client.event
############################################################
@client.event
async def on_ready():
    """
    Discode Bot 起動

    """
    debug_log('on_ready() Start')
    #プレイ中を更新
    presence = discord.Game(random.choice(play_word_list))
    await client.change_presence(activity=presence)
    #せとうぽくん起動メッセージ
    await send_message(DEBUG_CHANNEL_ID, 'せとうぽくん起動しました')
    debug_log('on_ready() End')

@client.event
async def on_member_join(member):
    """
    Discode Bot メンバー参加
    
    Parameters:
    ----------
    member : discord.Member
        メンバー情報
    """
    debug_log('on_member_join(member) Start')
    global welcomemsg_title
    global welcomemsg_color
    global welcomemsg_img
    global welcomemsg_contents

    if member.guild.id != STUP_SERVER_ID:
        debug_log(f'せとうぽサーバー以外のためスキップ({member.guild.id})')
        debug_log('on_member_join(member) End')
        return

    #ようこそ文送信
    embed_join = discord.Embed(title=welcomemsg_title,description="",color=welcomemsg_color)
    embed_join.add_field(name=f":sparkles:{member.name}さん:sparkles:\r\nご参加ありがとうございます",value=welcomemsg_contents,inline=False)
    embed_join.set_thumbnail(url=welcomemsg_img)
    await send_message(ZATUDAN_CHANNEL_ID, embed=embed_join)
    debug_log('on_member_join(member) End')

@client.event
async def on_message(message):
    """
    Discode Bot メッセージ受信
    
    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    global embed_help
    global embed_test
    global trade_ngword_list
    debug_log('on_message(message) Start')
    
    if message.author.bot:
        #Botの発言
        if message.author.id == SETUPKUN_ID:
            await on_message_for_setupkun(message)
        else:
            await on_message_for_another_bot(message)

    else:
        #ユーザーの発言
        await on_message_for_user(message)
    
    debug_log('on_message(message) End')

####################
#タイマー処理
####################
@tasks.loop(seconds=60)
async def loop():

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
#    elif now == '21:30': 
#        print('21:30の通知処理')
#        nowday = datetime.now(JST).weekday()
#        print(f'{nowday}の日です')
#        # 3は木曜日
#        if nowday == 3:
#            channel = client.get_channel(BOSS_CHANNEL_ID)
#            if channel is None:
#                print('ボス討伐チャンネルIDの取得に失敗した')
#                return
#            print('カオスアビスPT作ったか？通知')
#            await channel.send(f'{CHINO_MENTION} {RIRI_MENTION} {MIMO_MENTION}  \r\nもうアビスのPT作ったかい？')
    elif now == '11:30': 
        print('11:30の通知処理')
        nowday = datetime.now(JST).weekday()
        print(f'{nowday}の日です')
        # 3は木曜日
        if nowday == 3:
            # カオスアビス
            channel = client.get_channel(BOSS_CHANNEL_ID)
            if channel is None:
                print('ボス討伐チャンネルIDの取得に失敗した')
                return
            embed_join = discord.Embed(title=chaosAbyss_title,description="",color=chaosAbyss_color)
            embed_join.add_field(name=f"以下のリアクションをポチッと",value=chaosAbyss_contents,inline=False)
            embed_join.set_thumbnail(url=chaosAbyss_png)
            print('カオスアビス討伐通知')
            await channel.send(embed=embed_join)
            # カオスマグナス
            embed_join2 = discord.Embed(title=chaosMagnus_title,description="",color=chaosMagnus_color)
            embed_join2.add_field(name=f"以下のリアクションをポチッと",value=chaosMagnus_contents,inline=False)
            embed_join2.set_thumbnail(url=chaosMagnus_png)
            print('ハードマグナス討伐通知')
            await channel.send(embed=embed_join2)
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

#実行
client.run(token)
