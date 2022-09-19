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
from datetime import datetime, timedelta, timezone
import discord

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
DEBUG_HIDE_ID = 1021028778983571456                     #裏チャンネル

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

#要塞通知文
yosai_title = "要塞だよ！全員集合！！"
yosai_color = 0x884898
yosai_png ='https://lh3.googleusercontent.com/hhJItqq38dI1mVqmeDvsxd3jKh5fN8KSyS8i_i8ufl9TuYQBrOOT-KSh47art2XgeuLMN4EjK1wvbxu903tTzeQLEIIdmTyEAvyPWa6klWvt=rw'
yosai_contents = "@everyone "

#建設物通知文
building_title = "建設物アップデートお済みですか？"
building_color = 0xffffff
building_png ='data:image/jpeg;base64,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'
building_contents = "@everyone "

#建設物シャレニアン通知文
syarenian_title = "シャレニアン＆建設物アップデートお済みですか？"
syarenian_color = 0xffffff
syarenian_png ='https://lh3.googleusercontent.com/4CgX8xm_BUM5UNRi2UbVfAX9dBX28kQwqSUb1H3-M-CSv7cy7ICajAOSmsJyQ14N5AP15zQsgoqnAqo1t6Rw1zzl8VrFloXCeOk-TTmhMlv7=rw'
syarenian_contents = "@everyone "

#アカイラム募集文
redram_title = "アカイラム募集"
redram_color = 0xED1C24
redram_png = "https://lh3.googleusercontent.com/erYTDwgrj6fKqOWI9MR8j4zzS9Lbeocq_UjsdY7ltKKDju4mX1yxLwG-AvKyJHjvnIGWOp-tPkjx7K_wwq1Kk3ihyGGtsuNGk-DOJy3x6zA=rw"
redram_contents = "🙆‍♀ ハード(22:00頃)\r\n"\
        "🙅‍♂️ ノーマル(21:20頃)\r\n"\

#カオスアビス募集文
chaosAbyss_title = "22:00頃のカオスアビス募集"
chaosAbyss_color = 0xEDE51C
chaosAbyss_png = "https://lh3.googleusercontent.com/yOWzbPyDW5he5IKvDx6gGlK6kEoKFPmt-96FD-JTMvgCTK-LcSPCRP4uxkXhxI_AFH1CJ9eZT1MW59P11l3kiTWqzWxIY9px0rKz20cVwFI=rw"
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
        debug_log(f'[send_message]:チャンネルIDの取得に失敗しました({channel_id})')
        return
    await channel.send(message)

async def send_embed(channel_id, _embed):
    """
    メッセージ送信
    Parameters:
    ----------
    channel_id : int
        チャンネルID
    _embed : discord.Embed
        Embed内容
    """
    debug_log(f'[send_embed]:{channel_id}, {_embed}')
    #メッセージ送信
    channel = client.get_channel(channel_id)
    if channel is None:
        debug_log(f'[send_embed]:チャンネルIDの取得に失敗しました({channel_id})')
        return
    await channel.send(embed=_embed)

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
            debug_log('[on_message_for_setupkun]:アカイラム募集リアクション')
            await message.add_reaction("🙆‍♀️")
            await message.add_reaction("🙅‍♂️")
        elif message.embeds[0].title == chaosAbyss_title:
            debug_log('[on_message_for_setupkun]:カオスアビス募集リアクション')
            await message.add_reaction("🙆‍♀️")
        elif message.embeds[0].title == chaosMagnus_title:
            debug_log('[on_message_for_setupkun]:カオスマグナス募集リアクション')
            await message.add_reaction("🙆‍♀️")

async def on_message_for_another_bot(message):
    """
    メッセージ受信(他Bot)
    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    global trade_ngword_list
    if message.author.id == DYNO_ID_1:
        #デバックに画像削除メッセージ通知
        debug_log('[on_message_for_another_bot]:デバックに画像削除メッセージ通知')
        await send_embed(DEBUG_ACTIONCHANNEL1_ID, message.embeds[0].copy())
        return

    elif message.author.id == DYNO_ID_2:
        #デバッグに削除メッセージ通知
        debug_log('[on_message_for_another_bot]:デバッグに削除メッセージ通知')
        await send_embed(DEBUG_ACTIONCHANNEL2_ID, message.embeds[0].copy())
        return

    elif message.author.id == DYNO_ID_3:
        #デバッグにVC接続メッセージ通知
        debug_log('[on_message_for_another_bot]:デバッグにVC接続メッセージ通知')
        await send_embed(DEBUG_ACTIONCHANNEL3_ID, message.embeds[0].copy())
        return
    
    if message.channel.id == MEE6_CHANNEL_ID:
        #mee6での発言
        debug_log('[on_message_for_another_bot]:mee6での発言')
        if message.content.startswith('!LevelUp'):
            debug_log('[on_message_for_another_bot]:Mee6レベルアップ処理')
            mentions = message.mentions
            if not mentions:
                debug_log('[on_message_for_another_bot]:メンション取得失敗')
                return
            member = message.guild.get_member(mentions[0].id)
            tmp = message.content.split(',')
            #配列が3つないと区切り失敗
            if len(tmp) < 3:
                debug_log('[on_message_for_another_bot]:区切りに失敗')
                return

            level = tmp[2]
            if level == 'Level5':
                debug_log('[on_message_for_another_bot]:Level5ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV5))
                await send_message(message.channel.id, 'ロールを追加しました！！「Level5」')
            elif level == 'Level15':
                debug_log('[on_message_for_another_bot]:Level15ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV15))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV5))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level5」→「Level15」')
            elif level == 'Level25':
                debug_log('[on_message_for_another_bot]:Level25ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV25))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV15))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level15」→「Level25」')
            elif level == 'Level35':
                debug_log('[on_message_for_another_bot]:Level35ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV35))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV25))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level25」→「Level35」')
            elif level == 'Level45':
                debug_log('[on_message_for_another_bot]:Level45ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV45))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV35))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level35」→「Level45」')
            elif level == 'Level55':
                debug_log('[on_message_for_another_bot]:Level55ロール付与')
                await member.add_roles(message.guild.get_role(ID_ROLE_LV55))
                await member.remove_roles(message.guild.get_role(ID_ROLE_LV45))
                await send_message(message.channel.id, 'ロールを変更しました！！「Level45」→「Level55」')
            else:
                debug_log('[on_message_for_another_bot]:ロール変更なし')
            return
    
    elif message.channel.id == OFFICIAL_TWEET_CHANNEL_ID:
        #公式ツイートチャンネルでの発言
        debug_log('[on_message_for_another_bot]:公式ツイートチャンネルでの発言')
        if '瞬断' in message.content or 'パッチの適用' in message.content:
            debug_log('[on_message_for_another_bot]:瞬断通知')
            await send_message(ZATUDAN_CHANNEL_ID, "@everyone 瞬断をお知らせします。\r\n\r\n───以下内容───\r\n" + message.content)
            return

    elif message.channel.id == INSIDE_CHANNEL_ID:
        #裏チャンネルでの発言
        debug_log('[on_message_for_another_bot]:裏チャンネルでの発言')
        #メル販売切り分け処理
        tmp = message.content.split('!-!-!-!-!-!-!')
        #配列が2つないと区切り失敗
        if len(tmp) < 2:
            debug_log('[on_message_for_another_bot]:区切りに失敗')
            return

        for word in trade_ngword_list:
            if word in tmp[0]:
                debug_log('[on_message_for_another_bot]:メル売りなので通知しない')
                await send_message(INSIDE_CHANNEL_ID, 'ひゃっはああ！てめぇはダメだ！地獄に堕ちな')
                return

        debug_log('[on_message_for_another_bot]:メル売り以外なので通知')
        await send_message(BUSINESS_TWEET_CHANNEL_ID, tmp[1])
        return
    
    elif message.channel.id == DEBUG_INFORMATION_ID:
        #infomationlogでの発言
        if '!要塞通知' in message.content:
            embed = discord.Embed(title=yosai_title,description=yosai_contents,color=yosai_color)
            #embed.add_field(name=yosai_contents,inline=False)
            embed.set_thumbnail(url=yosai_png)
            await send_embed(DEBUG_HIDE_ID, embed)
        
        if '!建設物' in message.content:
            embed = discord.Embed(title=building_title,description=building_contents,color=building_color)
            #embed.add_field(name=building_contents,inline=False)
            embed.set_thumbnail(url=building_png)
            await send_embed(DEBUG_HIDE_ID, embed)

        if '!シャレニアン' in message.content:
            embed = discord.Embed(title=syarenian_title,description=syarenian_contents,color=syarenian_color)
            #embed.add_field(name=syarenian_contents,inline=False)
            embed.set_thumbnail(url=syarenian_png)
            await send_embed(DEBUG_HIDE_ID, embed)

        if '!カオスアビス' in message.content:
            debug_log('[on_message_for_another_bot]:カオスアビス討伐通知')
            embed = discord.Embed(title=chaosAbyss_title,description="",color=chaosAbyss_color)
            embed.add_field(name=f"以下のリアクションをポチッと",value=chaosAbyss_contents,inline=False)
            embed.set_thumbnail(url=chaosAbyss_png)
            await send_embed(DEBUG_HIDE_ID, embed)

        if '!アカイラム' in message.content:
            debug_log('[on_message_for_another_bot]:アカイラム討伐通知')
            embed = discord.Embed(title=redram_title,description="",color=redram_color)
            embed.add_field(name=f"以下のリアクションをポチッと",value=redram_contents,inline=False)
            embed.set_thumbnail(url=redram_png)
            await send_embed(DEBUG_HIDE_ID, embed)

        if '!カオスマグナス' in message.content:
            debug_log('[on_message_for_another_bot]:カオスマグナス討伐通知')
            embed = discord.Embed(title=chaosMagnus_title,description="",color=chaosMagnus_color)
            embed.add_field(name=f"以下のリアクションをポチッと",value=chaosMagnus_contents,inline=False)
            embed.set_thumbnail(url=chaosMagnus_png)
            await send_embed(DEBUG_HIDE_ID, embed)
        return

async def on_message_for_user(message):
    """
    メッセージ受信(ユーザー)
    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    global embed_help
    global embed_test
    await send_message(DEBUG_CHANNEL_ID, f"[{message.channel.name}],[{message.author.name}]:{message.content}")

    if message.content.startswith('/せとうぽ'):
        tmp = message.content.split()
        if '/せとうぽ' != tmp[0]:
            #トリガーコマンドが間違えている
            debug_log('[on_message_for_user]:/せとうぽのコマンドミス(/せとうぽの後にスペースが入っていない)')
            await send_message(message.channel.id, 'コマンドの入力に失敗しました。今一度ご確認ください。')
            await send_embed(message.channel.id, embed_help)
            return

        if len(tmp) == 1:
            #コマンドがせとうぽのみ
            debug_log('[on_message_for_user]:ヘルプ表示処理')
            await send_embed(message.channel.id, embed_help)
            return

        elif len(tmp) == 2:
            #コマンドに引数が1つある
            if 'おみくじ' == tmp[1]:
                #おみくじ
                debug_log('[on_message_for_user]:おみくじ')
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
                    debug_log('[on_message_for_user]:公式 ロール剥奪')
                    await member.remove_roles(change_role)
                    await send_message(message.channel.id, 'あなたの「公式ツイート監視」ロールを剥奪しました')
                else:
                    debug_log('[on_message_for_user]:公式 ロール付与')
                    await member.add_roles(change_role)
                    await send_message(message.channel.id, 'あなたに「公式ツイート監視」ロールを付与しました')
                return
            
            elif '取引所' == tmp[1]:
                #取引所ロール付与/剥奪
                change_role = message.guild.get_role(ID_ROLE_MONITOR_BUSINESS)
                member = message.guild.get_member(message.author.id)
                if change_role in member.roles:
                    debug_log('[on_message_for_user]:取引所 ロール剥奪')
                    await member.remove_roles(change_role)
                    await send_message(message.channel.id, 'あなたの「取引所ツイート監視」ロールを剥奪しました')
                else:
                    debug_log('[on_message_for_user]:取引所 ロール付与')
                    await member.add_roles(change_role)
                    await send_message(message.channel.id, 'あなたに「取引所ツイート監視」ロールを付与しました')
                return
            
            elif 'テスト' == tmp[1]:
                #テスト コマンド
                debug_log('[on_message_for_user]:テストコマンド実行')
                await send_embed(message.channel.id, embed_test)
                return

            else:
                #該当コマンドなし 第一引数指定ミス
                debug_log('[on_message_for_user]:該当コマンドなし 第一引数指定ミス')
                await send_message(message.channel.id, 'コマンドの入力に失敗しました。今一度ご確認ください。')
                await send_embed(message.channel.id, embed_help)
                return

        elif len(tmp) == 4:
            #せとうぽくんで発言
            debug_log('[on_message_for_user]:せとうぽくんで発言')
            if '発言' == tmp[1]:
                id = int(tmp[2])
                msg = tmp[3]
                await send_message(id, msg)
                return
        
        else:
            #/せとうぽだったが該当コマンドではなかった
            debug_log('[on_message_for_user]:該当コマンドなし 引数の数ミス')
            await send_message(message.channel.id, 'コマンドの入力に失敗しました。今一度ご確認ください。')
            await send_embed(message.channel.id, embed_help)
            return

############################################################
#client.event
############################################################
@client.event
async def on_ready():
    """
    Discode Bot 起動
    """
    #プレイ中を更新
    presence = discord.Game(random.choice(play_word_list))
    await client.change_presence(activity=presence)
    #せとうぽくん起動メッセージ
    await send_message(DEBUG_CHANNEL_ID, 'せとうぽくん起動しました')

@client.event
async def on_member_join(member):
    """
    Discode Bot メンバー参加
    
    Parameters:
    ----------
    member : discord.Member
        メンバー情報
    """
    global welcomemsg_title
    global welcomemsg_color
    global welcomemsg_img
    global welcomemsg_contents

    if member.guild.id != STUP_SERVER_ID:
        debug_log(f'[on_member_join]:せとうぽサーバー以外のためスキップ({member.guild.id})')
        return

    #ようこそ文送信
    embed_join = discord.Embed(title=welcomemsg_title,description="",color=welcomemsg_color)
    embed_join.add_field(name=f":sparkles:{member.name}さん:sparkles:\r\nご参加ありがとうございます",value=welcomemsg_contents,inline=False)
    embed_join.set_thumbnail(url=welcomemsg_img)
    await send_embed(ZATUDAN_CHANNEL_ID, embed_join)

@client.event
async def on_message(message):
    """
    Discode Bot メッセージ受信
    
    Parameters:
    ----------
    message : discord.Message
        メッセージ情報
    """
    if message.author.bot:
        #Botの発言
        if message.author.id == SETUPKUN_ID:
            await on_message_for_setupkun(message)
        else:
            await on_message_for_another_bot(message)

    else:
        #ユーザーの発言
        await on_message_for_user(message)

#実行
client.run(token)
