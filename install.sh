#!/bin/bash

echo "Updating system"
sudo yum update -y

# influxdb
echo "Installing influxdb"
wget https://dl.influxdata.com/influxdb/releases/influxdb-1.7.10.x86_64.rpm
sudo yum localinstall -y influxdb-1.7.10.x86_64.rpm
sudo systemctl daemon-reload
sudo systemctl start influxdb
echo "influxdb started"

# trades recorder
echo "Installing trades recorder"
sudo yum install -y python3 python3-pip
sudo -H pip3 install -U pip
pip3 install -U --no-cache-dir -r requirements.txt
sudo cp trades_recorder.service /etc/systemd/system
sudo chown -R root:root /etc/systemd/system/trades_recorder.service
sudo chmod -R 644 /etc/systemd/system/trades_recorder.service
sudo systemctl daemon-reload
sudo systemctl enable trades_recorder.service
sudo systemctl start trades_recorder.service
echo "Trades recorder started"

# account recorder
echo "Installing account recorder"
sudo cp account_recorder.service /etc/systemd/system
sudo chown -R root:root /etc/systemd/system/account_recorder.service
sudo chmod -R 644 /etc/systemd/system/account_recorder.service
sudo systemctl daemon-reload
sudo systemctl enable account_recorder.service
sudo systemctl start account_recorder.service
echo "Account recorder started"
