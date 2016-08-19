# Fast-file-transfer
This project is developed as part of Operating system course.This project majorly consist of two parts :<br>
**1. Android application** <i>(written in java)</i><br>
**2. FTP server** <i>(written in python)</i><br><br>
##Android Application<br>
Android application is based upon the concept of file splitter and joiner.As user upload file to application, it breaks into several parts.For example if we have file of 1000mb then our app will split it into 10 parts of 100mb each(user can chose in what size it actually wants to break the files).The idea behind it was that, it is easier to download a 100mb files into
10 parts than directly downloading 1000mb, specially on the low network connectivity.

##Ftp Server
Once application break media files into several part the role of ftp server comes.We have used ftp server to upload all the parts individually so that user can download files remotely.After files being uploaded on the server, user can now download the individual part into the their device and our app will join all the individual parts to one single item.

P.S- We have used an application named AndFTP to upload and download individual parts of file to and from ftp server.

**Important Note** : Instructions to do all the setup has been given in the setip_instructions.pdf file.

**Developers** :

**Android Application** : Developed by **[Vishwajeet Srivastava](https://github.com/vjs3) <br>
**Ftp Server** : Developed by **Palansh Agarwal**
