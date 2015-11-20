tweetcount=$(echo "USE junk; select count(*) from trump;" | /home/centos/dse-4.8.1/bin/cqlsh 128.138.202.117 | tail -n 3 | head -n 1 | cut -d ' ' -f 2)

password=$(python hash.py)
sudo sh -c "echo $tweetcount > tweetCount.md"
git add tweetCount.md
git commit -m "updated tweet count"
git push
expect "Username for 'https://github.com':"
send "commandoscorch16"
expect "Password for 'https://commandoscorch16@github.com':"
send "$password"
