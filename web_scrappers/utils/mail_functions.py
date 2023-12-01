import smtplib

def send_mail(host, port, login, app_password, from_addr, to_addrs, message):

    smtpObj=smtplib.SMTP_SSL(host, port)
    code, msg = smtpObj.ehlo()

    if code == 250:
        code_auth, msg_auth = smtpObj.login(login, app_password)
        if code_auth == 235:
            smtpObj.sendmail(from_addr, to_addrs, message)
            smtpObj.quit()
        else:
            print(code_auth, msg_auth)
    else:
        print(code, msg)
    return