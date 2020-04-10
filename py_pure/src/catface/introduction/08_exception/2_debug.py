# -调试
## 方案一、各种print


## 方案二、各种assert[可在启动python解释器时 python -0 err.py 来关闭assert]


## 方案三、logging
import logging

logging.basicConfig(level=logging.INFO)

s = 1 / 0
logging.info('n = %s' % s)

## 方案四、python调试器pdb


## 方案五、使用IDE
