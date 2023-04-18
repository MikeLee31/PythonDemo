#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

from email.utils import formataddr


class MyMail(object):
	def __init__(self, receiver,name,subject,context):
		self.message = MIMEMultipart()
		self.mail_host = 'smtp.qq.com'
		self.mail_user = "253514942@qq.com"  # 用户名
		self.mail_pass = "lpasbuiwwunbbhgj"  # 口令
		self.sender = '253514942@qq.com'
		self.receiver = receiver
		self.subject = subject
		self.text = context
		self.name=name

	# 发送
	def send(self):
		ret = True
		try:
			self.message = MIMEText(self.text, 'plain', 'utf-8')
			self.message['From'] = formataddr(['MikeLee', self.sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
			self.message['To'] = formataddr([self.name, self.receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
			self.message['Subject'] = self.subject  # 邮件的主题，也可以说是标题

			server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
			server.login(self.mail_user, self.mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
			server.sendmail(self.sender, [self.receiver, ], self.message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
			server.quit()  # 关闭连接
		except smtplib.SMTPException:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
			ret = False
			print(smtplib.SMTPException.strerror)

		if ret:
			print("邮件发送成功")
		else:
			print("邮件发送失败")
		return ret


# if __name__ == "__main__":
# 	#             发送对象             发件人   标题     正文
# 	mail = MyMail('441053808@qq.com','李涵','这是标题','这是正文')
# 	mail.send()
