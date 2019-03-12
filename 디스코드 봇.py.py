import urllib
import urllib.request
import bs4
import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
from urllib.request import urlopen, Request
from selenium import webdriver
import time
import datetime
import image
import sys
import os
import json
import datetime





client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-----------------")
    await client.change_presence(game=discord.Game(name="악구리봇이 현재 온라인 상태입니다. ", type=1))


def request(url, headers):
    pass


@client.event
async def on_message(message):



    if message.content.startswith("!흑우"):
        await client.send_message(message.channel, '**"악구리봇" 으로 변경된 이름을 불러주세요.**')

    if message.content.startswith("!악구리"):
        await client.send_message(message.channel, '기타치는 중 이에요.')

    if message.content.startswith("!하이"):
        await client.send_message(message.channel, '안녕하세요 ㅎㅅㅎ')

    if message.content.startswith("!안녕"):
        await client.send_message(message.channel, '할루할루~')

    if message.content.startswith("!섹시"):
        await client.send_message(message.channel, '내 각선미가 쫌 ^^')

    if message.content.startswith("!귀엽"):
         await client.send_message(message.channel, '어머~ 나도안다구~')

    if message.content.startswith("!ㅎㅇ"):
        await client.send_message(message.channel, 'ㅎㅇㅎㅇ')

    if message.content.startswith("!보겸"):
        await client.send_message(message.channel, '400만 가즈아!')

    if message.content.startswith("!마"):
        await client.send_message(message.channel, '마! 니자신있나??')

    if message.content.startswith("!어린"):
        await client.send_message(message.channel, '멋쟁이 토마토같은 여자')

    if message.content.startswith("!나연"):
        await client.send_message(message.channel, '흑우방 존예보스☆')

    if message.content.startswith("!존예") or message.content.startswith("!조녜"):
        await client.send_message(message.channel, '__** 규리, 나연 양대산맥 아인교 ? **__')

    if message.content.startswith("!돼지"):
        await client.send_message(message.channel, '혹시 @어린 << 이분을 찾으셨나요? 제가 도와드리겠습니다.')

    if message.content.startswith("!흑돼지"):
        await client.send_message(message.channel, '혹시 @어린 << 이분을 찾으셨나요? 제가 도와드리겠습니다.')

    if message.content.startswith("!회장"):
        await client.send_message(message.channel, '아 도사님 저 죽어요 도사님 ..')

    if message.content.startswith("!해삼"):
        await client.send_message(message.channel, '이히히히히힣 히히힣힣힣히히힣')

    if message.content.startswith("!여니"):
        await client.send_message(message.channel, '이게↘아주그냥↗세상이↗미쳐↗돌아가는구만↗그래↘')

    if message.content.startswith("!서린"):
        await client.send_message(message.channel, '그는 한국의 No.1 손절킹이다.')

    if message.content.startswith("!갱"):
        await client.send_message(message.channel, '저거닦고옴백업ㄴㄴ = 상자 ')

    if message.content.startswith("!한아"):
        await client.send_message(message.channel, '도라이새기 머갈통 빨래판에 빨아뿔라')

    if message.content.startswith("!제딘") or message.content.startswith("!도토리"):
        await client.send_message(message.channel, '그의 웃음소리...= 베이가 (= 해삼웃는소리?)')

    if message.content.startswith("!도사"):
        await client.send_message(message.channel, '하늘은 푸르고 강물은 맑다 , 무슨 설명이 더 필요하단 말인가 ? ')

    if message.content.startswith("!혁잉") or message.content.startswith("!동혁"):
        await client.send_message(message.channel, '**5252!! \n어린ㅡ쿤!**')

    if message.content.startswith("!수기") or message.content.startswith("!미소"):
        await client.send_message(message.channel, '= 지갑전사 ( He is 와규... )')

    if message.content.startswith("!잘도"):
       await client.send_message(message.channel, '아직 업데이트 되지 않았습니다. 의견을 제시해주세요!')

    if message.content.startswith("!포비"):
        await client.send_message(message.channel, '아직 업데이트 되지 않았습니다. 의견을 제시해주세요!')

    if message.content.startswith("!은서"):
        await client.send_message(message.channel, '아직 업데이트 되지 않았습니다. 의견을 제시해주세요!')

    if message.content.startswith("!대장"):
        await client.send_message(message.channel, '아직 업데이트 되지 않았습니다. 의견을 제시해주세요!')

    if message.content.startswith("!이수") or message.content.startswith("!수콩"):
        await client.send_message(message.channel, '아직 업데이트 되지 않았습니다. 의견을 제시해주세요!')

    if message.content.startswith("!규리") or message.content.startswith("!귤"):
        await client.send_message(message.channel, '**특: 맨날 뭐먹음**')

    if message.content.startswith("!다람쥐") or message.content.startswith("!람쥐") or message.content.startswith("!규리"):
        await client.send_message(message.channel, '**특: 조금 귀여움**')

    if message.content.startswith("!환준")  or message.content.startswith("!핀치"):
        await client.send_message(message.channel, '도사님의 스승')

    if message.content.startswith("!기온"):
        await client.send_message(message.channel, '!날씨 <지역> 명령어를 통해 확인해주세요.')

    if message.content.startswith("!시간"):
        await client.send_message(message.channel, '지원하지 않는 기능입니다.')

    if message.content.startswith("!습도"):
        await client.send_message(message.channel, '지원하지 않는 기능입니다.')

    if message.content.startswith("!전기의자"):
        await client.send_message(message.channel, '지이이이이이이이이잉잉 웅앵우우웅앵엥엥엥엥웅')

    if message.content.startswith("!정길"):
        await client.send_message(message.channel, '제 아버지의 이름이네요. 아주 멋진 분이시죠.')

    if message.content.startswith("!전갈"):
        await client.send_message(message.channel, '위대하신 분의 이름을 감히..!!')

    if message.content.startswith("!뉴찡"):
        await client.send_message(message.channel, '예전 커플닉입니다. 즉, 그 단어는 현재 옳바르지 않은 표현입니다.')

    if message.content.startswith("!길이"):
        await client.send_message(message.channel, '그분을 호출하실 땐 "@길이" 로 호출해 주세요.')

    if message.content.startswith("!해장"):
        await client.send_message(message.channel, '**판사님 드랍더비트!**')

    if message.content.startswith("!해장"):
        await client.send_message(message.channel, '**+메모장 소환!**')

    if message.content.startswith("!메모장"):
        await client.send_message(message.channel, "작성되었습니다.")

    if message.content.startswith("!메모장"):
        await client.send_message(message.channel, 'ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

    if message.content.startswith("!메모장"):
        await client.send_message(message.channel, '이 기능은 지원되지 않습니다.')

    if message.content.startswith("!메모보기"):
        await client.send_message(message.channel, '이 기능은 지원되지 않습니다.')



    if message.content.startswith('!롤ㄱ'):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="롤 ㄱㄱ", color=discord.Color.blue()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="때리치워~!", color=discord.Color.red()))


    if message.content.startswith('!배그ㄱ'):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="배그 ㄱㄱ", color=discord.Color.blue()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="때리치워~!", color=discord.Color.red()))



    if message.content.startswith("!골라"):
        await client.send_message(message.channel, '제 생각에는')

    if message.content.startswith('!골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)


    if message.content.startswith('!뭐먹지'):
        food = "치킨 피자 족발 보쌈 까나리액젓 라면 비빔냉면 만둣국 간장게장 양념게장 떡볶이 갈비찜 스테이크 " \
               " 된장찌개 김치찌개 부대찌개 제육덮밥 카레라이스 육개장 김치볶음밥 미역국 떡국 콘치즈 쏘야 파스타 " \
               "짜장면+탕슉 짬뽕+탕슉 우동 토스트 또띠아 찜닭 캘리포니아롤 오니기리 치킨마요덮밥 샐러드 수육 " \
               "수프 주먹밥 감동란 그라탕 김치전 감자전 돈까스 치킨까스 멘보샤 꿔바로우 찹쌀탕수육 깐풍기 유산슬 " \
               "닭꼬치 리조또 크레이프케이크 치즈케이크 초코케이크 블루베리케이크 에그타르트3개 고등어조림 " \
               "따끈따끈하고보슬보슬한쌀밥한그릇 코다리조림 명태조림 "


        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)

    if message.content.startswith("!뭐먹지"):
        await client.send_message(message.channel, '제가골랐지만 너무 맛있겠는걸요?')




    if message.content.startswith('!치킨'):
        food = "보드람치킨 교촌치킨 깐부치킨 굽네치킨 또레오레 60계치킨 BHC 치킨 페리카나 멕시카나 네네치킨 " \
               "코리엔탈깻잎두마리치킨 티바두마리치킨 또봉이통닭 디디치킨"


        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)


    if message.content.startswith("!치킨"):
        await client.send_message(message.channel, '치킨은 바삭바삭한게 진리!')




    if message.content.startswith('!피자'):
        food = "미스터피자 피자헛 파파존스 피자알볼로 피자에땅 빨간모자피자 피자랑치킨이랑 리츠델리피자 7번가피자 " \
               "피자헤븐  뽕드락피자 "


        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)


    if message.content.startswith("!피자"):
        await client.send_message(message.channel, '혼자먹으면 살찐다')



    if message.content.startswith('!라면'):
        food = " 신라면 신라면(블랙) 안성탕면 삼양라면 너구리(매운맛) 너구리(순한맜) 진라면(매운맛) 진라면(순한맛) 참깨라면 " \
               "볶음너구리 김치라면 열라면 수타면 팔~도비빔면♪ 공화춘 짜왕 짜빠게티 진짬뽕 진짜장 무파마 " \
               "맛있는라면 육개장 나가사키짬뽕 꼬꼬면 불닭볶음면 까르보불닭볶음면 오모리김치찌개라면 김치시발면 " \
               "굴짬뽕 홍석천의매운치즈볶음면 새우탕면 틈새라면 스낵면 콕!콕!콕!스파게티 콕!콕1콕!라면볶이 콕!콕!콕! 치즈볶이 " \
               "왕뚜껑 왕뚜껑(김치) 뽀글이 튀김우동 오징어짬뽕 설렁탕면  生生야끼우동 사리곰탕 드레싱누들(오리엔탈) 드레싱누들(참깨) "


        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)




    if message.content.startswith("!꺼져"):
        await client.send_message(message.channel, 'ㅅㄹ')

    if message.content.startswith("!닥쳐"):
        await client.send_message(message.channel, 'ㅗ^오^ㅗ')

    if message.content.startswith("!닭쳐"):
        await client.send_message(message.channel, '꼬우면 닭을 주시든가~')

    if message.content.startswith("!조용"):
        await client.send_message(message.channel, '응~~~시러')

    if message.content.startswith("!죽어"):
        await client.send_message(message.channel, ' 시른뒙? ⎛⎝⎛° ͜ʖ°⎞⎠⎞ ')

    if message.content.startswith("!사랑해"):
        await client.send_message(message.channel, "ʕ㋛'͡༼~~'♥ ")

    if message.content.startswith("!밥먹"):
        await client.send_message(message.channel, '내입에 소스코드를 부어줘.. ⍜⍙⍜ ')

    if message.content.startswith("!시공"):
        await client.send_message(message.channel, '옾눞|ᓀ운lY')

    if message.content.startswith("!일어나") or message.content.startswith("!일나"):
        embed = discord.Embed(
            title='시스템 가동',
            description="I AM READY !",
            color=discord.Colour.green()
        )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith("!잘자") or message.content.startswith("!자라"):
        embed = discord.Embed(
            title='성공적으로 종료 요청되었습니다.',
            description="But, 관리자 이외의 요청일 경우 취소됩니다.",
            color=discord.Colour.purple()
        )
        await client.send_message(message.channel, embed=embed)



    if message.content.startswith('!도움말') or message.content.startswith('!명령어') or message.content.startswith('!help'):
        embed = discord.Embed(
            title='악구리봇 명령어',
            description='\n \n인사하기 ---- !하이, 안녕, ㅎㅇ '
                      '\n흑우상태 ---- !뭐해 (추가예정) \n사진검색 ---- !사진 <사진검색어>  \n날씨검색 ---- !날씨 <지역> ' \
                      '\n기온검색 ---- !기온 <지역> \n맴버검색 ---- !<별명> ' \
                      '\n영화순위 ---- !영화순위' \
                      '\n메모하기 ---- !메모장 \n메모보기 ---- !메모장보기 \n실검보기 ---- !"실검" or "실시간검색어"' \
                      '\n음식추천 ---- !뭐먹지 \n항목선택 ---- !골라 <항목1> <항목2> ... \n복권뽑기 ---- !복권'
                      '\n제비뽑기 ---- !제비뽑기 <숫자>'
                      '\n주사위 ---- !주사위 1~6의 숫자중 한가지를 고름 \n타이머 ---- !타이머<숫자> or !Time <숫자> '
                      '\n\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ전적검색 명령어ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ  '
                      '\n\n배틀그라운드 - !배그솔로 <닉> !배그듀오 <닉> !배그스쿼드 <닉> \n\n리그오브레전드 - !롤 <닉네임> 곧 추가예정 '
                      '\n\n\n 종료하기 ---- !잘자',
            colour=discord.Colour.blue()
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("!업데이트"):
        embed = discord.Embed(
            title='업데이트 사항 Ver 1.5.1',
            description="\n\n주사위 기능이 추가되었습니다.  \n\n제비뽑기 기능이 추가되었습니다. \n\n복권뽑기 기능이 추가되었습니다."
                        "\n\n날씨 기능이 추가되었습니다. \n\n타이머 기능이 추가되었습니다. \n\n사진검색 기능이 추가되었습니다."
                        "\n\n이제 배틀그라운드의 전적을 확인할 수 있습니다! "
                        "\n\n고양이와 강아지 사진을 업데이트 하였습니다!"
                        "\n\n영화순위 기능을 추가하였습니다."
                        "\n\n이모리콘 기능을 추가하였습니다."
                        "\n\n[ 명령어는 !도움말로 확인할 수 있습니다 ] ",
            color=discord.Colour.orange()
        )
        await client.send_message(message.channel, embed=embed)





    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')

        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0, 10):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i + 1) + '위', value='\n' + '[%s](<%s>)' % (realTimeSerach, realURL),
                            inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await client.send_message(message.channel, embed=embed)



    if message.content.startswith('!주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))


    if message.content.startswith("!복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]  # 배열크기 선언해줌
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자  - 8,145,060의 확률!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await client.send_message(message.channel, embed=embed)


    if message.content.startswith('!제비뽑기'):
        channel = message.channel
        embed = discord.Embed(
            title='제비뽑기',
            description='각 번호별로 번호를 지정합니다.',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='뽑기 완료!')


        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip()) #입력한 명령어

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List:  # 중복일때만
                num = random.randrange(0, number)  # 다시 랜덤수 생성

            List.append(num)  # 중복 아닐때만 리스트에 추가
            embed.add_field(name=str(i) + '번째', value=str(num), inline=True)

        print(List)
        await client.send_message(channel, embed=embed)





        #embed.set_footer(text = 'End')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")

        embed.add_field(name='!롤', value='!롤 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그솔로', value='!배그솔로 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그듀오', value='!배그듀오 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그스쿼드', value='!배그스쿼드 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
    if message.content.startswith("!배그솔로"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/"+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        solo1 = bsObj.find("div", {"class": "overview"})
        solo2 = solo1.text
        solo3 = solo2.strip()
        channel = message.channel
        embed = discord.Embed(
            title='배그솔로 정보',
            description='배그솔로 정보입니다.',
            colour=discord.Colour.green())
        if solo3 == "No record":
            print("솔로 경기가 없습니다.")
            embed.add_field(name='솔로경기를 한판이상 해주세요', value='솔로 경기 전적이 없습니다.', inline=False)
            await client.send_message(channel, embed=embed)

        else:
            solo4 = solo1.find("span", {"class": "value"})
            soloratting = solo4.text  # -------솔로레이팅---------
            solorank0_1 = solo1.find("div", {"class": "grade-info"})
            solorank0_2 = solorank0_1.text
            solorank = solorank0_2.strip()  # -------랭크(그마,브론즈)---------

            print("레이팅 : " + soloratting)
            print("등급 : " + solorank)
            print("")
            embed.add_field(name='레이팅', value=soloratting, inline=False)
            embed.add_field(name='등급', value=solorank, inline=False)

            soloKD1 = bsObj.find("div", {"class": "kd stats-item stats-top-graph"})
            soloKD2 = soloKD1.find("p", {"class": "value"})
            soloKD3 = soloKD2.text
            soloKD = soloKD3.strip()  # -------킬뎃(2.0---------
            soloSky1 = soloKD1.find("span", {"class": "top"})
            soloSky2 = soloSky1.text  # -------상위10.24%---------

            print("킬뎃 : " + soloKD)
            print("킬뎃상위 : " + soloSky2)
            print("")
            embed.add_field(name='킬뎃,킬뎃상위', value=soloKD+" "+soloSky2, inline=False)
            #embed.add_field(name='킬뎃상위', value=soloSky2, inline=False)

            soloWinRat1 = bsObj.find("div", {"class": "stats"})  # 박스
            soloWinRat2 = soloWinRat1.find("div", {"class": "winratio stats-item stats-top-graph"})
            soloWinRat3 = soloWinRat2.find("p", {"class": "value"})
            soloWinRat = soloWinRat3.text.strip()  # -------승률---------
            soloWinRatSky1 = soloWinRat2.find("span", {"class": "top"})
            soloWinRatSky = soloWinRatSky1.text.strip()  # -------상위?%---------

            print("승률 : " + soloWinRat)
            print("승률상위 : " + soloWinRatSky)
            print("")
            embed.add_field(name='승률,승률상위', value=soloWinRat+" "+soloWinRatSky, inline=False)
            #embed.add_field(name='승률상위', value=soloWinRatSky, inline=False)

            soloHead1 = soloWinRat1.find("div", {"class": "headshots stats-item stats-top-graph"})
            soloHead2 = soloHead1.find("p", {"class": "value"})
            soloHead = soloHead2.text.strip()  # -------헤드샷---------
            soloHeadSky1 = soloHead1.find("span", {"class": "top"})
            soloHeadSky = soloHeadSky1.text.strip()  # # -------상위?%---------

            print("헤드샷 : " + soloHead)
            print("헤드샷상위 : " + soloHeadSky)
            print("")
            embed.add_field(name='헤드샷,헤드샷상위', value=soloHead+" "+soloHeadSky, inline=False)
            #embed.add_field(name='헤드샷상위', value=soloHeadSky, inline=False)
            await client.send_message(channel, embed=embed)



    if message.content.startswith("!배그듀오"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "duo modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----
        print(duoRecord)
        channel = message.channel
        embed = discord.Embed(
            title='배그듀오 정보',
            description='배그듀오 정보입니다.',
            colour=discord.Colour.green())
        if duoRecord == 'No record':
            print('듀오 경기가 없습니다.')
            embed.add_field(name='듀오경기를 한판이상 해주세요', value='듀오 경기 전적이 없습니다.', inline=False)
            await client.send_message(channel, embed=embed)

        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----레이팅----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----등급----
            print(duoRank)
            embed.add_field(name='레이팅', value=duoRat, inline=False)
            embed.add_field(name='등급', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----킬뎃----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----
            print(duoKD)
            print(duoKdSky)
            embed.add_field(name='킬뎃,킬뎃상위', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----승률----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----
            print(duoWinRat)
            print(duoWinRatSky)
            embed.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----헤드샷----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----
            print(duoHead)
            print(duoHeadSky)
            embed.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)
            await client.send_message(channel, embed=embed)



    if message.content.startswith("!배그스쿼드"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "squad modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----
        print(duoRecord)
        channel = message.channel
        embed = discord.Embed(
            title='배그스쿼드 정보',
            description='배그스쿼드 정보입니다.',
            colour=discord.Colour.green())
        if duoRecord == 'No record':
            print('스쿼드 경기가 없습니다.')
            embed.add_field(name='스쿼드경기를 한판이라도 해주세요', value='스쿼드 경기 전적이 없습니다.', inline=False)
            await client.send_message(channel, embed=embed)

        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----레이팅----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----등급----
            print(duoRank)
            embed.add_field(name='레이팅', value=duoRat, inline=False)
            embed.add_field(name='등급', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----킬뎃----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----
            print(duoKD)
            print(duoKdSky)
            embed.add_field(name='킬뎃,킬뎃상위', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----승률----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----
            print(duoWinRat)
            print(duoWinRatSky)
            embed.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----헤드샷----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----
            print(duoHead)
            print(duoHeadSky)
            embed.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)
            await client.send_message(channel, embed=embed)


    if message.content.startswith('!고양이'):
        embed = discord.Embed(
            title='',
            description='',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!강아지'):
        embed = discord.Embed(
            title='',
            description='',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await client.send_message(message.channel, embed=embed)




    if message.content.startswith('!영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
        i1 = 0 # 랭킹 string값
        embed = discord.Embed(
            title = "영화순위",
            description = "현재 흥행순위 정보",
            colour= discord.Color.dark_orange()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 10):
            i1 = i1+1
            stri1 = str(i1) # i1은 영화랭킹을 나타내는데 사용됩니다
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
            print()
            embed.add_field(name='---------------랭킹'+stri1+'위---------------', value='\n영화제목 : '+moviechartLi1MovieName+'\n영화평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) # 영화랭킹


        await client.send_message(message.channel, embed=embed)



    if message.content.startswith("!날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            colour=discord.Colour.green()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태



        await client.send_message(message.channel,embed=embed)



    if message.content.startswith('!타이머') or message.content.startswith('!Time') or message.content.startswith('!time'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        sec = int(Text) #!타이머 5 라고입력하면 sec값은 5가됩니다.

        for i in range(sec, 0, -1):
            print(i)
            await client.send_message(message.channel, embed=discord.Embed(description='남은시간 : '+str(i)+'초'))
            time.sleep(1)
        else:
            print("땡")
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))

    if message.content.startswith('!사진'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 40) # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location) # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        # 크롤링 하는데 있어서 가끔씩 안되는 사이트가 있습니다.
        # 그 이유는 사이트가 접속하는 상대를 봇으로 인식하였기 때문인데
        # 이 코드는 자신이 봇이 아닌것을 증명하여 사이트에 접속이 가능해집니다!
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img') # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source') # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.set_image(url=imgsrc) # 이미지의 링크를 지정해 이미지를 설정합니다.
        await client.send_message(message.channel, embed=embed) # 메시지를 보냅니다.






client.run('NTM5ODY0ODA3MDUwODM4MDM4.D1yzkg.E-8m_D76LykeF8-zgB6NZzFbOvE')