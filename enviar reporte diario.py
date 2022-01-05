# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 12:35:27 2021

@author: chris
"""

import smtplib, ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# pedir datos para iniciar sesion

username = "christianmorales270@gmail.com"
# password = "qqwetiqe21"
# password = getpass.getpass("ingrese su password: ")


while True:
    
    password = getpass.getpass("ingrese su password: ")
    
    if password == "qqwetiqe21":
        
        destinatario = "maliagam@vivienda.gob.pe"
        # maliagam@vivienda.gob.pe
        asunto = "actividades diaria de christian morales" 
        
        # crear el mensaje
        
        
        mensaje = MIMEMultipart("alternative")
        mensaje["Subject"] = asunto
        mensaje["From"] = username
        mensaje["To"] = destinatario
        
        print("Estimado Ing. Mario:")
        print("El dia de hoy se avanso con lo siguiente:")
        
        mense = input()
        html = f"""
        <html>
        <body>
        Estimado Ing. Mario:<br><br>
        El dia de hoy se avanso con lo siguiente:<br><br>
        {mense}<br><br>
        Atte.<br>
        Ernesto Christian Morales P.
        <body>
        <html>
        """
        
        # el contenido del mensaje como html
        
        parte_html = MIMEText(html, "html")
        
        # agregar ese contenido al mensaje
        
        mensaje.attach(parte_html)
        
        mensaje_texto = mensaje.as_string()
        
        context = ssl.create_default_context()
    
    
        # print("Estimado Ing. Mario:")
        # print("El dia de hoy se avanso con lo siguiente:")
        
        # mense = input()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username, password)
               
            print("sesion iniciada")
            
            server.sendmail(username, destinatario, mensaje_texto)
            print("mensaje enviado")
            
        break
            
    else:
        
        print("contraseña errada")
    
        
