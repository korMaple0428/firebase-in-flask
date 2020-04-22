import json
import random, string
import Geohash
from app.util import Sample

def pin_lst(_x, _y) :

    lst = list()

    try :
        for i in range(0, 10) :
            x = float(_x) + ( random.choice([-1, 1]) * random.randrange(0,9) / 1000 ) + ( random.choice([-1, 1]) * random.randrange(0,9) / 10000 )
            y = float(_y) + ( random.choice([-1, 1]) * random.randrange(0,9) / 1000 ) + ( random.choice([-1, 1]) * random.randrange(0,9) / 10000 )

            user = random.choice(Sample.users)
            print("x[%f] y[%f]"%(x, y))

            category = random.choice(Sample.category)
            lst.append({ 
                  'id'          : ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                , 'owner'       : user
                , 'title'       : 'title_' + ''.join(random.choices(string.digits, k=5))
                , 'category'    : category
                , 'tags'        : random.choices(Sample.tags[category], k=3)
                , 'img'         : random.choice(Sample.sample_imgs)
                , 'x'           : x
                , 'y'           : y
                , 'geohash'     : Geohash.encode(y, x, precision=4)
            })

    except Exception as e :
        print(e)

    return lst
