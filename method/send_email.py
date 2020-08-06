import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config.config import *
import os

#获取测试报告
def get_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print("最新测试报告: "+lists[-1])
    #找到最新生成的测试报告
    report_file = os.path.join(report_path,lists[-1])
    return report_file

#发送报告
def send_email(report_file):
    msg = MIMEMultipart()
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))

    msg['From'] = '1062301500@qq.com'
    msg['To'] = 'zengweizhuang@win-sky.com.cn'
    msg['Subject'] = Header(subject, 'utf-8')  # 从配置文件中读取


    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 从配置文件中读取
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # 参数化一下report_file
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)  # 从配置文件中读取
        smtp.login(smtp_user, smtp_password)  # 从配置文件中读取
        smtp.sendmail(sender, receiver, msg.as_string())
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()