import tgtg
from tgtg import TgtgClient
import schedule
import time
import pandas as pd
import PySimpleGUI as sg
import schedule
import time
from datetime import datetime
import pytz

# client = TgtgClient(email="<ridgley.knapp@gmail.com>")
# credentials = client.get_credentials()


client = TgtgClient(access_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzgyMDg0MzksImlhdCI6MTczODAzNTYzOSwiaXNzIjoidGd0Z19zb3RlcmlhIiwidCI6ImlKX3lyVGQ2UmJHdzlGbVdWe\
lJxTHc6MToxIiwic3ViIjoiMTAyNzU1MTAyMjc2OTE1NzQ1In0.e7LEEidsEbSW5o-zaAlN2deL2TEHHuyZhSln59XTM_I", refresh_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Njk1NzE2MzksImlhdCI\
6MTczODAzNTYzOSwiaXNzIjoidGd0Z19zb3RlcmlhIiwidCI6IkZfbVI5UmdCUjJxaVNhWC1BU1N3Mmc6MTowIiwic3ViIjoiMTAyNzU1MTAyMjc2OTE1NzQ1In0.MBXtaWKjVIJyfHJRGi0H1z9a5fgp076UEHIQk_3mMSI", cookie="d\
atadome=PVQvNUkt0rWu2Ew_6wpqF7LkrxtLEYCifQS7Jkhaksedqko4DGC5wq_4YS6M01MxnLdnO1HFFOA~fmoxPPQf~rlzK41rn9Pg3Qnsrc46LLqgGjXb4CWNl7b3NCImB01Q;")

def tgtg_job():
    global items
    items = client.get_items(
        favorites_only=False,
        latitude=41.948401,
        longitude=-87.650231,
        radius=10,
    )
    global df
    df = pd.DataFrame(items)

    # global filtered_list
    # filtered_list = list(filter(lambda x: 'Whole Foods' in x, df['display_name'].values.tolist()))

    # print(filtered_list)

    df2 = df[df['display_name'].str.contains('Whole Foods')][['display_name','item_tags','sold_out_at']]
    df2['sold_out_at'] = pd.to_datetime(df2['sold_out_at'])
    df2['sold_out_at'] = df2['sold_out_at'].dt.tz_convert('US/Central')
    df2['sold_out_at'] = df2['sold_out_at'].dt.strftime('%A, %I:%M %p')

    # print(df2)

    if df2['item_tags'].str.contains('SOLD_OUT').all():
        text_to_show = 'Too slow :/     Sold out at: '
        sell_out_time_string = " & ".join([str(element) for element in (df2['sold_out_at']).to_list()])
    else:
        text_to_show = 'get your ass to whole foods ! ! ! '
        sell_out_time_string = ''


    if text_to_show:
        print(text_to_show)
        print(sell_out_time_string)

        layout = [  [sg.Text(text_to_show, font = ("Calibri", 24))], [sg.Text(sell_out_time_string, font = ("Calibri", 14))]]

        window = sg.Window('TGTG Whole Foods Tracker',layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            print('You entered ',values[0])

        window.close()

    # print(items) #print all items 

# tgtg_job()

schedule.every().day.at("10:30").do(tgtg_job)
schedule.every().day.at("15:15").do(tgtg_job)
schedule.every().day.at("15:51").do(tgtg_job)
schedule.every().day.at("16:12").do(tgtg_job)
schedule.every().day.at("21:02").do(tgtg_job)
schedule.every().day.at("21:12").do(tgtg_job)
schedule.every().day.at("21:25").do(tgtg_job)
schedule.every().day.at("21:33").do(tgtg_job)

while True:
    schedule.run_pending()
    time.sleep(1)