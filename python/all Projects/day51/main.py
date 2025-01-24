# import math
# import speedtest
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def bytes_to_mb(sizebytes):
#     i = int(math.floor(math.log(sizebytes, 1204)))
#     power = math.pow(1024, i)
#     size = round(sizebytes / power, 2)
#     return f"{size} Mbps"

# def send_email(subject, body):
#     sender_email = "koiryrishan1@gmail.com"
#     receiver_email = "koiryrishan1@gmail.com"
#     password =  "pplp lrem kdjg fumg"  

#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = subject

#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, password)
#         text = msg.as_string()
#         server.sendmail(sender_email, receiver_email, text)
#         server.quit()
#         print("Email is Sending....")
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email: {e}")

# wifi = speedtest.Speedtest()
# print("Getting download speed....")
# download_speed = wifi.download()
# print("Getting upload speed...")
# upload_speed = wifi.upload()

# download_speed_mb = bytes_to_mb(download_speed)
# upload_speed_mb = bytes_to_mb(upload_speed)

# print("download:", download_speed_mb)
# print("upload:", upload_speed_mb)

# # Email the speed details every time the program runs
# subject = "Internet Speed Details"
# body = f"Your current download speed is {download_speed_mb} and upload speed is {upload_speed_mb}."

# send_email(subject, body)

# # Send email if speeds are below the threshold
# if download_speed < 25 * 1024 * 1024 and upload_speed < 75 * 1024 * 1024:
#     alert_subject = "Low Internet Speed Alert"
#     alert_body = f"Your current download speed is {download_speed_mb} and upload speed is {upload_speed_mb}, which are below the acceptable thresholds."
#     send_email(alert_subject, alert_body)
