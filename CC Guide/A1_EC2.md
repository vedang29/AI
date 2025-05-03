# Assignment A1: EC2 Instance

[Amazon AWS Console](https://aws.amazon.com/console/)

### Steps:

1. Login to Amazon AWS.
2. Click on **EC2** or search for EC2.
3. Select region: **Asia Pacific (Mumbai)**.
4. Go to **Instances**.
5. Click on **Launch Instances**.
6. Name the instance: `My_Web_Server`.
7. Choose **Amazon Linux 2023 AMI** (selected by default).
8. Architecture: **64-bit (x86)** (selected by default).
9. Instance type: **t2.micro** (selected by default) — *questions can be asked*.
10. Key pair (login): Create a new key pair and download the `.pem` file.
11. Click **Launch Instance**.
12. Select the instance and click **Connect**.
13. Go to **SSH Client** and copy the example command.

### In Terminal:

```bash
cd Downloads  # Navigate to the folder containing the .pem file
chmod 400 "vedang_2.pem"
ssh -i "vedang_2.pem" ec2-user@ec2-04-112-78-12.ap-south-1.compute.amazonaws.com
```
