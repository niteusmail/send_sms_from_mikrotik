import paramiko

def send_sms(phone_number, message):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('YOUR_MIKROTIK_IP', port=YOUR_SSH_PORT, username='Your UserName', password='Password')

    command = f"/tool/sms/send lte1 type=class-1 phone-number={phone_number} message={message}"
    ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command(command)

    ssh_client.close()
