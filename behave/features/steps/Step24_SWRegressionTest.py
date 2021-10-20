import re
import time

import paramiko


# Edit Line 169 if code is not running, just call the accessAWS() function on this line inside the definition.
# Functions for Step-24


def accessAWS():
    ssh = paramiko.SSHClient()
    # Allow connections to hosts that are not in the know? Hosts file
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Establish a connection to superman
    ssh.connect("superman", username="hri", port=22, password="hriSummer2020!")

    # Use this connection to execute commands
    scanner = 'HG21020002/'  # change to appropriate scanner name and add a /
    # day = '20210417_+'

    awsImage = 'aws s3 ls s3://admiral-storage-staging/image/'
    awsbaseband = 'aws s3 ls s3://admiral-storage-staging/basebanded/'

    login = ['su andrei', 'peanutbutter']  # sudo command

    # running these twice will provide all the dates the scanner has been used to upload to aws
    awslist = [awsImage + scanner, awsImage + scanner]
    # print(awsImage + scanner + day)

    channel = ssh.invoke_shell()
    # go.send("su andrei")

    # ping to terminal
    time.sleep(1)
    channel.recv(9999)
    channel.send("\n")
    time.sleep(1)

    yuh = []

    # logs in via su
    for command in login:
        channel.send(command + "\n")
        while not channel.recv_ready():  # Wait for the server to read and respond
            time.sleep(0.5)
        time.sleep(2)  # wait enough for writing to (hopefully) be finished
        output = channel.recv(9999)  # read in
        print(output.decode('utf-8'))
        time.sleep(1)

    # checks aws for the list of scans and dates
    for i in awslist:
        channel.send(i + "\n")
        while not channel.recv_ready():  # Wait for the server to read and respond
            time.sleep(0.5)
        a = 0
        time.sleep(2)
        output = channel.recv(9999)
        lit = (output.decode('utf-8'))
        # print(lit)
        yuh.append(lit)
        a = a + 1
        # print("next")

    yuh[0:1] = [''.join(yuh[1:2])]
    # yuh[2:3] = [''.join(yuh[2:3])]

    y = "20210917/"  # change date number here and put a /

    b = re.findall("20210917_[0-9]{6}", yuh[1])  # change date number here as well
    # print(b)
    # print(b[-1])
    c = b[-1] + '/'

    awsBasebanded = 'aws s3 ls s3://admiral-storage-staging/basebanded/' + scanner + c
    awscalibs = 'aws s3 ls s3://admiral-storage-staging/DeviceCalibs/' + scanner + y
    awsconfigs = 'aws s3 ls s3://admiral-storage-staging/DeviceConfigs/' + scanner + y
    awsLogs = 'aws s3 ls s3://admiral-storage-staging/DeviceLogs/' + scanner + y + "hf/"
    awsDiags = 'aws s3 ls s3://admiral-storage-staging/DeviceDiags/' + scanner + y
    awsImage1 = awsImage + scanner + c

    commands1 = [awsbaseband, awsBasebanded, awsImage1, awscalibs, awsconfigs, awsLogs, awsDiags]

    print(commands1)
    word = []
    for i in commands1:
        channel.send(i + "\n")
        while not channel.recv_ready():  # Wait for the server to read and respond
            time.sleep(0.5)
        a = 0
        time.sleep(1)
        outputt = channel.recv(9999)
        q = (outputt.decode('utf-8'))
        word.append(q)
        # print(q)
    # print("next")

    # word[1:2] = [''.join(word[1:2])]
    # word[2:3] = [''.join(word[2:3])]

    baseband = word[1]
    image = word[2]
    calibs = word[3]
    configs = word[4]
    logs = word[5]
    diags = word[6]
    awstextfile = open("awstext.txt", "w")

    if '.h5' in baseband:
        print('baseband has files in aws')
    else:
        print('ERROR: Baseband does not have files in aws')
    time.sleep(1)
    awstextfile.write(baseband)

    if '.h5' in image:
        print('image has files in aws')
    else:
        print('ERROR image does not have files in aws')
    time.sleep(1)
    awstextfile.write(image)

    if '.h5' in calibs:
        print('device calibs has files in aws')
    else:
        print('ERROR device calibs does not have files in aws')
    time.sleep(1)
    awstextfile.write(calibs)

    if '.json' in configs:
        print('device configs has files in aws')
    else:
        print('ERROR device configs does not have files in aws')
    time.sleep(1)
    awstextfile.write(configs)

    if '.log' in logs:
        print('device logs has files in aws')
    else:
        print('ERROR device logs does not have files in aws')
    time.sleep(1)
    awstextfile.write(logs)

    if '.h5' in diags and '.pdf' in diags:
        print('device diagnostics has files in aws')
    else:
        print('ERROR device diagnostics does not have files in aws')
    time.sleep(1)
    awstextfile.write(diags)
    print("step completed")
    channel.close()

    accessAWS()
