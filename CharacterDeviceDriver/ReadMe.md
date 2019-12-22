# CHARACTER Device Driver

This project contains functionality of character device driver.

With This we increment all the functions which are executed by the driver routine of the kernel.

Instead of targeting the real device we use sudo Devide to perform the operation.

## Insert the Device Driver

the steps to insert the device driver in the kernal are:
> make

> sudo insmod ./CharacterDeviceDriver.ko

To see the information about the device driver:
> modinfo CharacterDeviceDriver.ko

To Check whether device driver is properly loaded:
> cat /proc/modules

To Check The System Log:
> cat /var/log/syslog

## To run the demo program

> gcc test.c 
> ./a.out


