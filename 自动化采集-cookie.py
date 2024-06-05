from selenium import webdriver
import time
import pickle
from selenium.webdriver.edge.options import Options

target_url='https://www.express.com/clothing/women/striped-one-button-blazer/pro/06747392/color/Black%20and%20White%20Stripe/'

edge_options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
edge_options.add_argument(f'user-agent={user_agent}')
# 创建Edge浏览器实例
edge = webdriver.Edge(options=edge_options)

# 最大化浏览器窗口
edge.maximize_window()

# 设置最大等待时长为10秒
edge.implicitly_wait(10)

# 打开抖音网站
edge.get(target_url)

# 等待一段时间，以便手动登录
time.sleep(1)
input("登入抖音账号后，请输入任意键继续...")
time.sleep(0.3)

# 保存Cookie到文件
with open("douyin_cookie.pickle", 'wb') as file:
    pickle.dump(edge.get_cookies(), file)

# 删除浏览器中的所有Cookie
edge.delete_all_cookies()

# 关闭浏览器
edge.quit()