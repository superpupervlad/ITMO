#!/bin/bash

set -exuo

apt-get -y install cifs-utils
cd ~ || exit
# 1
(
echo n # New partition
echo p # Primary
echo # Default partition number (first available)
echo # Default first sector (first available)
echo +300M # Partiotion size
echo w # Write changes
) | fdisk /dev/sda

selected_disk=$(blkid | tail -1 | awk '{split($0,a,":"); print a[1]}')
blkid "$selected_disk" > ~/selected_disk_part_uuid

mkfs.ext4 -F -b 4096 "$selected_disk"

dumpe2fs "$selected_disk"
# 5
tune2fs "$selected_disk" -i 2m -c 2

mkdir -p /mnt/newdisk 
mount "$selected_disk" /mnt/newdisk

ln -s /mnt/newdisk mount

mkdir mount/task_8

echo "$selected_disk    /mnt/newdisk    ext4    noexec,noatime    0    2" >> /etc/fstab

# 10
umount /mnt/newdisk
(
echo d # Delete
echo # Last partition
echo n # New partition
echo p # Primary
echo # Default partition number (first available)
echo # Default first sector (first available)
echo +350M # Partiotion size
#echo N # >Partition #2 contains a ext4 signature. Do you want to remove the signature?
echo w # Write changes
) | fdisk /dev/sda
sudo resize2fs -f "$selected_disk"

e2fsck -fvn "$selected_disk"
# mount "$selected_disk" /mnt/newdisk -o ro,noload

(
echo n # New partition
echo p # Primary
echo # Default partition number (first available)
echo # Default first sector (first available)
echo +12M # Partiotion size
echo w # Write changes
) | fdisk /dev/sda

journal_device=$(blkid | tail -1 | awk '{split($0,a,":"); print a[1]}')
tune2fs -O "^has_journal" /dev/sda2
mke2fs -O journal_dev -b 4096 "$journal_device"
tune2fs -J device="$journal_device" "$selected_disk"

(
echo n # New partition
echo e # Extended
echo # Default partition number (first available)
echo # Default first sector (first available)
echo # All left free space

echo n # New partition
echo # Default first sector (first available)
echo +100M # Partiotion size

echo n # New partition
echo # Default first sector (first available)
echo +100M # Partiotion size

echo w # Write changes
) | fdisk /dev/sda

mkdir /mnt/supernewdisk
vgcreate task_14 /dev/sda5 /dev/sda6
lvcreate -l 100%FREE task_14
mkfs.ext4 /dev/task_14/lvol0
mount /dev/task_14/lvol0 /mnt/supernewdisk

# 15
mkdir /mnt/share
mount -t cifs -o password="" //192.168.1.139/smb /mnt/share

echo "//192.168.1.139/smb    /mnt/share    cifs    ro    0    2" >> /etc/fstab

#umount /mnt/share
