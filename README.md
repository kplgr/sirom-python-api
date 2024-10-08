## SIROM Python api
Send individual commands to SIROM devices, through python & SocketCAN (Linux).

## Dependencies

- Python 3
- SocketCAN Linux kernel module
- python-can PyPi module

The kernel module should already be loaded on any recent distro.

For the python-can module, beware of the name. There also exists a "can" module available through PyPi/pip, which is *not* the right one. 

```$ pip install python-can```


## TL;DR

1) Set up CAN bus interface (e.g. can0). The interface appears only when a USB-CAN adapter is connected on the computer.
   ```
     $ ip link set can0 down                      # In case it's already up
     $ ip link set can0 type can bitrate 1000000  # That's 1Mbps, 6 zeros.
     $ ip link set can0 up
   ```

   Or, succinctly, ``ip link set can0 up type can bitrate 1000000``
   
   You can verify the status of the connection by checking on the LED(s) on the USB-CAN adapter.
   When the interface is configured properly, a LED will turn on.
   
2) Send commands with ``python sendcommand.py [options] <COMMAND>``
   ```
     $ python sendcommand.py --device 2 POWER_ON     # ENABLE SIROM
     $ python sendcommand.py --device 2 GOTO_OPER    # GO TO OPERATIONAL MODE
     $ python sendcommand.py --device 2 GOTO_LAT     # CLOSE (LATCH)
     $ python sendcommand.py --device 2 GOTO_RTC     # OPEN (READY-TO-CAPTURE)
   ```

After each power up of the device, ``POWER_ON`` and ``GOTO_OPER`` need to be sent only once (each).

See ``python sendcommand.py -h`` for more information on commands, and possible options.

Default values for options (especially SIROM Device ID) might have to be changed.
   
