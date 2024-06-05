import requests
from bs4 import BeautifulSoup

# url_test='https://www.express.com/clothing/women/collared-cropped-jacket/pro/06747053/color/neutral/'
# url='https://www.ralphlauren.co.uk/en/relaxed-fit-striped-cotton-shirt-648859.html?webcat=women%2Fclothing%2Fwomen%20clothing%20shop%20all%20rd'
url='https://www.express.com/graphql'

header={
  # 'Accept-Encoding':'gzip, deflate, br, zstd',
  # 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  # 'Cache-Control':'no-cache',
  # 'Content-Length':'1200',
  # 'Content-Type':'application/json',
  # 'Cookie':'BAGID=632f3ca8-fdf4-4875-b6a4-6206ab62f9a9; crl8.fpcuid=7413edb5-0344-4b31-897b-ff0d201299d9; _bamls_usid=baf04075-75bf-46d5-818d-3f8337667009; s_ecid=MCMID%7C53297444565386037682892420100918268292; _tt_enable_cookie=1; _ttp=e0V1573lLHrltAt_cvcxyZCEJry; _ga=GA1.2.2071369550.1716802474; _gid=GA1.2.2003216255.1716802474; unbxd.userId=uid-1716802473607-79884; IR_PI=0b0707fe-1c0c-11ef-83d2-81b510efe492%7C1716802473801; cjevent=null; QuantumMetricUserID=aa593330f17d045daeb412b3f07140ea; _gcl_au=1.1.1523939094.1716802490; _scid=cd370290-7bb2-4995-8ce0-b973b6e15891; _fbp=fb.1.1716802490129.922869204; _pin_unauth=dWlkPU5HSmtZVE5rWXpNdFpEUXdOeTAwTkRreExUZ3pNMkl0WTJFeE16WTNZbVpoWkdSaw; _sctr=1%7C1716739200000; BVBRANDID=3da55fa9-12cb-4869-952b-7bf5026878e7; isMobile=false; isTablet=false; AKA_A2=A; at_check=true; accessToken=j%3A%7B%22accessToken%22%3A%22eyJhbGciOiJSUzI1NiIsImtpZCI6IjNjOTNjMWEyNGNhZjgyN2I4ZGRlOWY4MmQyMzE1MzY1MDg4YWU2MTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZWNvbW0tcmVzb3VyY2VzLXByb2QiLCJhdWQiOiJlY29tbS1yZXNvdXJjZXMtcHJvZCIsImF1dGhfdGltZSI6MTcxNjg1NjgwNCwidXNlcl9pZCI6IldaM2FsdlF1OXRaSzU1QjUwemxJZmlTSDZqRDIiLCJzdWIiOiJXWjNhbHZRdTl0Wks1NUI1MHpsSWZpU0g2akQyIiwiaWF0IjoxNzE2ODU2ODA0LCJleHAiOjE3MTY4NjA0MDQsImVtYWlsIjoiZ3Vlc3RAZXhwcmVzcy5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsiZ3Vlc3RAZXhwcmVzcy5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.cekRdrBFHi6mQK743JpxejzfAWh8M7EjAooayYyHfk0TrkUkItNzRCAVpoXTnh2U4iL7cguH0yYLDRAqcYl-e08I2pAMZoCEE1zTK5Wa-1Xjr2sqoPPGCXwFxwcvJ4sfmqCVosWo5kyw4tn4UwurBH4v-uUSMnjHisTAeG55XONSRGH_AS_vKHGuHLZ_MWzFTRbhNegyOesPeY7apJzyHBjQRl2Ilj-2NtDeduRXB1qJnLqXXUDp-EIq1-tIyvoLq0rmj43nZ0G0A_J5hPiZcesC5TfqAF_-5U_-fMTuH1gfMH56L0k9wJWCKjQkr0N4IzT4LsG1OhfF-04vavqNwQ%22%2C%22expireTime%22%3A1716860404%7D; JSESSIONID=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJndWVzdCIsInNlc3Npb25TdGF0ZSI6IkdVRVNUIiwic2Vzc2lvbklkIjoib2MwZ2loOWJueWVlMXB4cHE4eDN0cDEzdi50ZXN0IiwidGltZXN0YW1wIjoxNzE2ODU3NDYzMjM5fQ.oBxfCrosNZ3TvGA8l5F8ReFfOVQqAzSkEs_GhJIPcb0lDRUoUmydY5GsuDe0_MBBNtvCYXSb-6FltysdlaEqSQ; exp_hbeat=1; bm_mi=622280100C57266FFF850BAEFC56AEA0~YAAQXDArF8Jc0KSPAQAAvuStvBd8y2lqwCZqBiUVDKN47pHXt5GUb6VyQoq8+pqRyfBrLUYRux/XwxS1mvKNw1xQji2HnKSvmqVVHkaaq6IuvMQwd9ikIdBMxGpuW9dAtaxvT2yRCc30+8qJ09H+hMV3V530UHLc0iwTPngKu6vgO2OovTDKBBavucG5H5WJGWiS6cDePPHfIfTRX8At2P0lQu/vnVNPvCTnreDQbdNjm8z5zCE9IQ1BpfS7J5tKImHsJKI76R5a14ltVnfEAr2/tFrf0OIpP0Qg8Uy8NA9N/wCm8W1ZSnvuC2Rq+1w5F4IMMGFStVhZedfOvpTeZpU+GNYz5S/t1wm5rdiFONA=~1; ak_bmsc=2FE8276AA66B455212163E3333BB011D~000000000000000000000000000000~YAAQXDArF9Vc0KSPAQAAWuutvBcysD10isLqI+OLm98ANN3nshbsU+DBxyNPPpez3PkdwwrtxTpWbnW1WElwT3SagTNKIGtpkY2kUrWOHD87Y2SVBCzH7JihiYrE2njR26s56UkXJhTiIN5prBw/hSLsI9Gj30JOtUJ0E7z4BWQD+jZLFCvDrf8YlR8QPCdJrNbLUPm9gwzn6GzAXG/l76wy7OjoW5L1dMnj2eVUOXgyHbrz2+K3EPlbGQCezCUyxCFzCBeJemvVVpT0uF+fj1InPdFX51v72p5LwWkZ58IghpB4h9pMBpi0JEesrRHbr4+POKI7I8MzfasplBhpT5iYDlntjSwVOKqoSDIYR5Ctd4Ut7lOmqHaHUHp0z6gbOLQjYBuc/W4j2SLn87EEvwc3L1X9z0Ncgl1MgBpaPED52Y8l16NSIR0GO5IVD4vm55T/VGZ3VSOuYbBN2iXQMCa+uTGlg29Q3V5oyNMtUL6854t/DtCACmc4sq7oXATxhdnDtk8=; QuantumMetricSessionID=2ea19e1488e8b2a976b9f903cd4c44d6; AMCVS_5F17123F5245B46D0A490D45%40AdobeOrg=1; AMCV_5F17123F5245B46D0A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19871%7CMCMID%7C53297444565386037682892420100918268292%7CMCAID%7CNONE%7CMCOPTOUT-1716864690s%7CNONE%7CMCAAMLH-1717462290%7C11%7CMCAAMB-1717462290%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19878%7CvVersion%7C5.5.0; expCustId=4dae528a117e4bb38639801a0706eddf; unbxd.visit=repeat; unbxd.visitId=visitId-1716857496559-21519; s_sess=%20s_cc%3Dtrue%3B; IR_gbd=express.com; bluecoreNV=false; BVBRANDSID=6d4bf77d-0bf9-48e1-8ff3-2b05992ad34d; styliticsWidgetSession=undefined; OptanonAlertBoxClosed=2024-05-28T01:16:33.427Z; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+28+2024+09%3A16%3A34+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=f75d7d30-e71b-4e74-b7d4-05e541147015&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=HK%3B&AwaitingReconsent=false; granify.uuid=a5c0311d-3860-4dd5-918f-1db14932644d; IR_22046=1716858996594%7C4940227%7C1716858996594%7C%7C; mp_express_mixpanel=%7B%22distinct_id%22%3A%20%2218fb9670e0a116d-0081543d1484e6-4c657b58-1fa400-18fb9670e0b1210%22%2C%22bc_persist_updated%22%3A%201716802489869%7D; _scid_r=cd370290-7bb2-4995-8ce0-b973b6e15891; bc_invalidateUrlCache_targeting=1716858997037; granify.new_user.1447=false; _gat=1; cto_bundle=n_5xt19tJTJCNFJLQU1Hc1AlMkZmUyUyRjdCOUxpSHh5M2R3UlVndzF0TEdYenBLT0hWU2xjM2tnck50UWJOV1lRdHQxNHJRYTNKZExVbHAyc2NMY2wyZ2tiek44eWtOMmhWdWwxU2hwMmUlMkJsbllNWmNtSSUyRkZkM2hhT3ZjTzIxSDBFOXNUSHl0em5FcHVHS3V4cHlMSDU0b25iN3BSZExRJTNEJTNE; _ga_RFQTHME9SL=GS1.2.1716857515.2.1.1716858997.60.0.0; inside-us2=784642310-c60b0ca2adaca80bb835150771461ec5bf501da66eabaabd53ed0f2db6d10507-0-0; s_pers=%20s_vnum%3D1719394472925%2526vn%253D2%7C1719394472925%3B%20pn%3D6%7C1719450014032%3B%20c19%3D1716859006411%7C1811467006411%3B%20c19_s%3DLess%2520than%25201%2520day%7C1716860806411%3B%20s_invisit%3Dtrue%7C1716860806412%3B%20c5%3DWomens%2520%253A%2520Product%2520Detail%2520%253A%2520Collared%2520Cropped%2520Jacket%7C1716860806413%3B; s_sq=expfashioncom%3D%2526c.%2526a.%2526activitymap.%2526page%253DWomens%252520%25253A%252520Product%252520Detail%252520%25253A%252520Collared%252520Cropped%252520Jacket%2526link%253DClose%252520Modal%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DWomens%252520%25253A%252520Product%252520Detail%252520%25253A%252520Collared%252520Cropped%252520Jacket%2526pidt%253D1%2526oid%253Dfunction%252528%252529%25257B%25255Bnativecode%25255D%25257D%2526oidt%253D2%2526ot%253DBUTTON; _gali=closeModal; granify.session.1447=-1; _4c_=%7B%22_4c_s_%22%3A%22jVTZbtNAFP2VyhJ9quPZl0gVShchEKEUihBPke0ZxyZOxhqbuqXKv3PHWZouIPziuWfuOb6rH6K%2BtKtojCUWimuEEcXoJFrY%2BzYaP0S%2BMuF1G42jLEtVJpGNjbZ5zPJCx1kqVFwUjBBluBBERSfRXdAijEvFJGKErk%2BivNlqPES5Mxa0sB5hNsI4LlqgdL8BYgrBsfHO%2FMq7WXffBL%2FeZketWcCFsbdVbmd9ZbpyECDoES1tNS%2B7AKNBxTQ%2BGHDqq5Vx%2FQENk0d0T2OaA5p517c2MM9L75b2CJMAOyhE9H1ghGC9Laz3gxtYbdWFOO1d423bjnK33IJQwEd8tsGbUEYcwqpdntYDcQXW1fTmy%2BzscnJ%2B9Qmgsuuadpwk7dJ2vsrb0YF4kiVtmwBQpG1ZuVWAcPLha0xGhI5Q%2FPHiepq0VCNBCOGcUELfTq7PTvHxsjKnnBItGWNccKoEolIoojRhBLqONFYEbE2OJ9eXp3gX1vT8%2FQUE9X9UIL2bzL4NDIIkpkJzjkbDbCHCJAOHX74%2BSLLv%2Byf55bXrymo1T3powCrJXV2n3po4965p4P0zzRe2S2BMEgTikmIdnJxPPkNB3xD0w9a16%2BE7dhWq3XgD5xtfzefWT21XOphnsFNTdVC%2FtA7TAuMPbTW2reahHSaMBFiLzjV7eL2dbCw040hzhRUMbge5KMFQeNabBg%2BDjvGBO8OYwVq9dN8MXGxX%2F%2BKxl7zbareTRMgMyxTHUmkBO6lxrGQq48JoQXmhMspRtJeE%2FeYEE0G2kljtFI0tdpI2FRI22sSo0GnMKJWxQlLGFmWGZzYjTKvoWZT0texCWTeSB7Xd%2Fh0EyAaaAr%2Bq6XbZDzFKibmm9KlvQILvTjKNXr33%2FV5qcxHSfSo1IKFX%2FtlX%2F%2Ba6Xv8B%22%7D; bm_sz=A6859EA540289F83FA5F074C53BF9B7C~YAAQXDArF+Xz0KSPAQAAwX3FvBfGgINM8kFCmYW3XAKCbNbmpCAOHsCMbIMQh1QIvaLWpwx9TC3UdzNwSehGtkW1uWKRVe+E1XLGN15DothuI4HY//F3PlAGXNnRb92bhNePJRwdZqm3oTqeFWH9aixMxpQUd7Cd7ZgBHgeSX/ABcqvxRPP8fJKgM/wO2BYodIPTr5Jgshew6r+fvja6AQHn36cGBje0xQZFkFMerK4uOLIJKyvnz0zixQShGfSrB3X4IHrSZhdgS1bg626ZTeZPE/+maf1pPxfJ4oUiITpepHS+pNY0f4et1zk8k6+pc+hPkQIq4xxBboUQoBVbArwUQRGaZIs9+RTusDCWN5yHWjPUuFdqUhAy1njYEqbv2/DEMvRAfv7KzoIpuMCMsfNOrXPjdmnKmndsm57r0YueoMyYMSducSiY91fsB5TFU7UMNinlWTXzS44kzOKfRKCGesFl6ghPo7ldvQARIEp1vVCsvP7aaCP5UTI1LRzmgn0MUiAvpmxGI2UrpvS6CM8PWPhjU1b01NLmWAXGeZTKH2I=~3555896~3552306; RT="z=1&dm=www.express.com&si=e16f877c-f590-46cb-b081-3fce442cb3b7&ss=lwpolrq3&sl=8&tt=gjn&bcn=%2F%2F684d0d47.akstat.io%2F&obo=4&rl=1"; mbox=PC#df14acb4783146acb8142aca5108fa03.32_0#1780103813|session#fe0eb2e351fb4640b9e68b62244f9158#1716860873; akavpau_wwwexpcom=1716859313~id=38887637b2d43fee2f287b68623d0bb8; _abck=EAC4C6BD4EDB64351BCF2FF0B1960054~-1~YAAQXDArF/bz0KSPAQAAqofFvAslzMYPp3xNm1p2VXy+rbPACBsFXnS96miDsbgxY3L+80t14FosBP2t3S+7JK+MIzKR1DKfcjUirrMPVC/WHJI27Z6p1Rh4I0FdURMe5727Jb4jkuuRSwUze7m2V/Q+78Xc2j8d9wR+pSH2tGMBHZ/OYSLA7qdxSE1xa65uIyYGVasBsqZQ0hrsTiXGqLvE616BLGp5gQUMITjtVh7NrxaOtPMF6ja4YBLkS6EqZ9gmNJNqVn5znXn+ILChL/3nYYfxBsRozsse0PhEP7OMlVhcbT5oxswLmR28dZQGVBCTSydA5x/uY2UvbuVq6rEKRwABNkRwHCJTBNOjbWI/lPkvGNJ60GdDzC0cU4q/mv4I10Hn1Y/3FhQu+ZNWqkK9EHCseKH3D/BmOJaql6MuumINqyB7~-1~-1~-1; bm_sv=29241DD84EAE78F342B69DAD2235F998~YAAQXDArF/fz0KSPAQAAB4jFvBdA0PTSzdDP++aGfFok/U3TnXGxfPu46sGsKiD2bgQI2TVUH5N7CQjri03xbkeCB5Vr4RBAKMY0B3dkWmyXDCdtsLO7BGfbdef1DnSbGVrN4sSQenr+fzZ8bxeY0kAzt4GiZ5MYZN1vjw/Ju9hIkG/ETENnMe5P6QASV78riYoo91bdHDthc7uT5ysSqeywUyFGfDjCeMomdMprhsveZRmhsacKLnB/PotpGc3hkVuB~1',
  # 'Origin':'https://www.express.com',
  # 'Pragma':'no-cache',
  # 'Priority':'u=1, i',
  # 'Referer':'https://www.express.com/clothing/women/editor-one-button-boyfriend-blazer/pro/06957319/color/Pale%20Yellow/',
  'Referer': 'https://www.express.com/clothing/women/collared-cropped-jacket/pro/06747289/color/PINK%20BLOOM/',
  # 'Sec-Ch-Ua':"'Microsoft Edge';v='125', 'Chromium';v='125', 'Not.A/Brand';v='24'",
  # 'Sec-Ch-Ua-Mobile':'?0',
  # 'Sec-Ch-Ua-Platform':"Windows",
  # 'Sec-Fetch-Dest':'empty',
  # 'Sec-Fetch-Mode':'cors',
  # 'Sec-Fetch-Site':'same-origin',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
  'X-Exp-Request-Id':'12cbb28f-2ab1-4714-8858-804ba608be82',
  'X-Exp-Rvn-Cache-Key':'28926937b330041c776e0ea8fb70e90229a2bf834dccec64ab8420cb20dd1800',
  'X-Exp-Rvn-Cacheable':'false',
  'X-Exp-Rvn-Query-Classification':'getGcpPredictions',
  'Classification':'',
  'X-Exp-Rvn-Source':'app_express.com'
}


my_parm={
    "operationName": "getGcpPredictions",
    "variables": {
        "payload": {
            "servingConfig": "recently_viewed_default",
            "options": {
                "attributionToken": "",
                "eventType": "detailPageView",
                "experimentIds": [],
                "filter": "",
                "filterMode": "override",
                "pageCategories": [],
                "pageSize": 20,
                "pageViewId": "",
                "productsList": [
                    {
                        #06747289
                        #06957319
                        "productId": "06747289"
                    }
                ],
                "purchaseTransaction": None,
                "returnProduct": True,
                "sessionId": "c6e1ccc5-1c8c-11ef-8d45-163d2d9bb601::YiyMMNMcdhtAln47omWW",
                "userId": "",
                "visitorId": "53297444565386037682892420100918268292",
                "validateOnly": False
            }
        }
    },
    "query": "query getGcpPredictions($payload: GCPPrectionInput!) {\n  getGcpPredictions(payload: $payload) {\n    attributionToken\n    filter\n    pageSize\n    products {\n      cartPromoMessage\n      clearancePromoMessage\n      colorCount\n      finalSalePromoMessage\n      imageSet\n      key\n      listPrice\n      name\n      newProduct\n      onlineExclusive\n      productColorSwatches\n      productDescription\n      productId\n      productImage\n      productRating\n      productURL\n      salePrice\n      totalReviewCount\n      __typename\n    }\n    productDataSource\n    servingConfig\n    source\n    successful\n    validateOnly\n    __typename\n  }\n}\n"
}

# res=requests.get(url=url_test,headers=header).text
res=requests.post(url=url,headers=header,json=my_parm).text
print(res)
