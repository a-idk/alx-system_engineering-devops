# Command line for the win

CMD CHALLENGE is a pretty cool game challenging you on Bash skills

## Project Description
- Everything is done via the command line and the questions are becoming increasingly complicated
- It’s a good training to improve your command line skills!
- Secure file transfer Protocol is also a major concept in this project

### Steps/Procedures

1. Complete the tasks or challenges accordingly
  - First 9 challenges and save the screenshot files as "0-first_9_tasks.jpg" and "0-first_9_tasks.png"
  - Next 9 challenges and save the screenshot files as "1-next_9_tasks.jpg" and "1-next_9_tasks.png"
  - Next 9 challenges and save the screenshot files as "2-next_9_tasks.jpg" and "2-next_9_tasks.png"
  - Complete all the challenges and save the screenshot files as "All_tasks.jpg" and "All_tasks.png"
2. Save all these screenshots in a folder. 
    NOTE: In my case, I saved them in this directory (C:\Users\Family\Pictures\Screenshots)
3. Open command prompt on windows systems
  - press "win key + R" 
  - type "cmd" in the run prompt window
  - then hit Enter or return key on the keyboard
4. Establish a Secure File Transfer Protocol (SFTP) by typing the following into the command prompt
    "sftp username@sandbox_hostname" without the quotes
    NOTE: username, hostname, and password can be gotten from the Credentials column view in your intranet
    (https://intranet.alxswe.com/user_containers/current)
5. Navigate to the directory of interest (cd /alx-system_engineering-devops/command_line_for_the_win)
    NOTE: the "command_line_for_the_win" directory had been previously created. If it has not been
    created, then create it in the sandbox (webterm), then navigate to it as said/shown earlier
6. Uploading the Screenshots by using the "put" command. Below is the complete command
    "put C:/Users/Family/Pictures/Screenshots/*.jpg"
                        and
    "put C:/Users/Family/Pictures/Screenshots/*.png"
7. Confirm successful Transfer by using the "ls" command
8. Exit the sftp interface in command prompt by typing "exit" and hit enter
9. Login into the sandbox webterm and navigate to the directory of interest
10. Push all the files to GitHub
    " git add . && git commit -m 'cmd challenge task' && git push "
