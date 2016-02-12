#Using a newly attached volume
---
##1. Make sure that you can see the new volume by using the command 'sudo fdisk
-l'
##2. When it is visible, you need to make a partition table. To do this, use the command 'sudo fdisk /dev/<name_of_volume>'. If you are using OpenStack, and this is your first volume, it will probably be name vdb.
##3. At the prompt, type 'w' and hit enter. It should say that the partition table has been altered.
##4. Now you need to make a filesystem. Make sure this new file system matches the one of the instance you are attaching it to. If you do not know which file system your instance is using, you can use the command ' df -T | awk '{print $1,$2,$NF}' | grep "^/dev" '
##5. Once you know the right filesystem, use the command 'sudo mkfs -t <name_of_filesystem> /dev/vdb1'
##6. Nice, you have made a filesystem! Now all you need to do is make a directory using 'sudo mkdir <path_to_directory>' and then mount the new volume using 'sudo mount /dev/vdb1 <path_to_directory>'
##7. Now all you need to do is modify /etc/fstab so that the volume is automatically mounted on boot
