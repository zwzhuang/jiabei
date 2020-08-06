import unittest
import requests
import json
import os  # 增加了一个os，需要用来组装路径
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from method.read_excel import *  # 从项目路径下导入
from method.case_log import log_case_info  # 从项目路径下导入

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),"TestUserLogin")  # 增加data路径


    def test_user_login_normal(self):
      case_data = get_test_data(self.data_list,'test_user_login_normal') # 从数据列表中查找到该用例数据
      if not case_data:
        logging.error("用例数据不存在")
      url = case_data.get('url') # 从字典中取数据，excel中的标题也必须是小写url
      data = case_data.get('data') # 注意字符串格式，需要用json.loads()转化为字典格式
      expect_res = case_data.get('expect_res') # 期望数据
      res = requests.post(url=url, data=json.loads(data)) # 表单请求，数据转为字典格式
      res_text = res.text
      log_case_info('test_user_login_normal', url, data, expect_res, res_text)  # 输出用例log信息
      self.assertIn(expect_res,res.text)  # 断言

    def test_user_password_wrong(self):
      case_data = get_test_data(self.data_list, 'test_user_password_wrong')  # 从数据列表中查找到该用例数据
      if not case_data:
        print("用例数据不存在")
      url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
      data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
      expect_res = case_data.get('expect_res')  # 期望数据
      res = requests.post(url=url, data=json.loads(data))  # 表单请求，数据转为字典格式
      res_text = res.text
      log_case_info('test_user_login_normal', url, data, expect_res, res_text)  # 输出用例log信息
      self.assertIn(expect_res,res.text)  # 断言

    def test_user_not(self):
      case_data = get_test_data(self.data_list, 'test_user_not')  # 从数据列表中查找到该用例数据
      if not case_data:
        print("用例数据不存在")
      url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
      data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
      expect_res = case_data.get('expect_res')  # 期望数据
      res = requests.post(url=url, data=json.loads(data))  # 表单请求，数据转为字典格式
      res_text = res.text
      log_case_info('test_user_login_normal', url, data, expect_res, res_text)  # 输出用例log信息
      self.assertIn(expect_res,res.text)  # 断言


if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
    unittest.main(verbosity=2)    # 运行本测试类所有用例,verbosity为结果显示级别
