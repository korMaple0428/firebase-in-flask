import os, sys, json
import math, string, random, datetime

from app.util       import MapleException

def check_item(item, name) :
    if ( name in item ) and (item[name] != None) :
        return True
    return False

## Util Function
def get_distance_from_coordinates(x0, y0, x1, y1):
    x_ = float(x0)
    y_ = float(y0)
    _x = float(x1)
    _y = float(y1)

    p = 0.017453292519943295
    a = 0.5 - math.cos((_y - y_) * p)/2 + math.cos(y_ * p) * math.cos(_y * p) * (1 - math.cos((_x - x_) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))


__ascii__ = string.ascii_uppercase + string.ascii_lowercase + string.digits
def rand_str(length) :
    result = ""
    for i in range(length) :
        result += random.choice(__ascii__)
    return result

def detect_unicode(query) :
    # korean
    if re.search("[\uac00-\ud7a3]", texts):
        return "ko"
    # japanese
    if re.search("[\u3040-\u30ff]", texts):
        return "ja"
    # chinese
    if re.search("[\u4e00-\u9FFF]", texts):
        return "zh"
    return "en"

def query_analyze(query) :
    lang = detect_unicode(query)
    
    if lang == 'en' :
        query_analyze_eng(query)
    elif lang == 'ja' : 
        query_analyze_jap(query)
    else :
        print("[ERROR] CommonUtil.query_analyze() : not supported lang [%s]", lang)
        return

def query_analyze_eng(query) :
    lang = detect_unicode(query)

    if 'delivery' in query.lower() : 
        return True
    else :
        return False


imgs = [
          "http://farm8.staticflickr.com/7300/10114363345_e83f300c6b_b.jpg"
        , "http://25.media.tumblr.com/e95bcf39059d10214ab98bcbc34e6c2f/tumblr_mmbo2xW6dw1rmyhabo1_500.gif"
        , "https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile1.uf.tistory.com%2Fimage%2F2113B13E5880D2FE09B8D8"
        , "http://mblogthumb1.phinf.naver.net/MjAxNzAxMzBfMTU3/MDAxNDg1NzE1ODk1MzI2.KUCDFFkpI7Jrmdu-dnlbAFcDhjfpjDoxaNdCL_iIU5Eg.RB9NTv_0rQDetKSjhEca4r-bnjq7iirs74K_sU766j0g.GIF.ahsjdk0807/1.gif?type=w800"
        , "https://img.fmnation.net/files/attach/images/60017/007/235/005/9f42aeaf24580c0a07932d606f6b0fd3.gif"
        , "http://mblogthumb3.phinf.naver.net/MjAxNzA4MTdfNzMg/MDAxNTAyOTc2ODkyNzEw.IYr2exDN7UVFOwbaUjZVYxrJ40xDe-TOFvRI8WeF298g.AbnzknQxGxWxYOcVlMPiA684dYdGpy-cpUPoFT83YWQg.GIF.sinnam88/%EC%84%BC%EA%B3%BC_%EC%B9%98%ED%9E%88%EB%A1%9C%EC%9D%98_%ED%96%89%EB%B0%A9%EB%B6%88%EB%AA%85_%EC%9B%80%EC%A7%A4_%2824%29.gif?type=w800"
        , "http://file.instiz.net/data/cached_img/upload/5/e/a/5ea599cc9a1f193f1d19dcc5b5fbaf43.gif"
        , "https://t1.daumcdn.net/cfile/tistory/25501E3E56C731B50A"
        , "http://mblogthumb2.phinf.naver.net/MjAxNzAzMjNfMjQ5/MDAxNDkwMjQ5NzI4NTkz.wcFMy0YC2rxksNwZJ5p8dKUpEeXgJFBGe8gDPDyord8g.cyBQk_4OBwEK0o5MPfeAvFq9iPDh8SvKB3HncA4LWQIg.GIF.pjhboy9/1.gif?type=w2"
        , "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FQP77b%2FbtqtZO45Io7%2FTdbmXw8j9AkPIQiAqrKprk%2Fimg.gif"
        , "https://2.bp.blogspot.com/-7qZgwC7YmeQ/XYLNVgxMeoI/AAAAAAAMsDw/Z0rPLqqMdX08Oe7jzYMwiCXHhdXwM-8PACLcBGAsYHQ/s1600/AS0005789_00.gif"
        , "http://appdata.hungryapp.co.kr/data_file/data_img/201909/09/W15679603420645818.gif"
        , "https://t1.daumcdn.net/cfile/tistory/240CCF3B57F5EB5A24"
        , "https://67.media.tumblr.com/8f4aa0e7872fb1300a4798f42a8e30ef/tumblr_o8bzmm73no1v6xsm2o1_540.gif"
        , "https://t1.daumcdn.net/liveboard/wngproject/16e8b717245a4275963cae8b24088bdb.png"
        ]

def get_rand_img() :
    return random.choice(imgs)

def get_zoom(boundary, z=15) :
    #139.680915^35.671386^139.744056^35.730056

    coords = boundary.split("^")

    r = get_distance_from_coordinates(coords[0], coords[1], coords[2], coords[3])

    if r < 2 :
        z = 18
    elif r < 50 :
        z = 15
    elif r < 100 :
        z = 14
    elif r < 1000 :
        z = 7
    else :
        z = 5

    print("r[%d] z[%d]"%(r, z));

    return z


