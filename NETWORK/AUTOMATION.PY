event manager applet Backup_Config_On_Change
 event cli pattern "copy running-config startup-config" sync yes
 action 1.0 cli command "enable"
 action 2.0 cli command "copy running-config tftp://192.168.1.100/backup.cfg"
 action 2.1 puts "Configuration backed up to TFTP server."


Explanation:
Event Trigger:

The event cli statement sets the trigger for this applet. In this example, the applet activates whenever the command copy running-config startup-config is executed.
The sync yes ensures the applet runs synchronously.
Actions:

Action 1.0: Switches to privileged EXEC mode (enable).
Action 2.0: Executes the command to copy the running configuration to a TFTP server.
Action 2.1: Prints a message confirming the backup.
Output: Whenever the copy running-config startup-config command is run, the applet automatically backs up the configuration to the specified TFTP server.

Other Use Cases for EEM Applets:
Automated Troubleshooting: Collect interface statistics when an interface goes down.

bash
Copy code
event manager applet Interface_Troubleshooting
 event interface name GigabitEthernet0/1 lineprotocol down
 action 1.0 cli command "enable"
 action 2.0 cli command "show interface GigabitEthernet0/1 > flash:interface_status.txt"
 action 3.0 puts "Interface statistics saved to flash."
Automated Log Collection: Collect logs when a specific log message appears.

bash
Copy code
event manager applet Log_Collector
 event syslog pattern ".*error.*"
 action 1.0 cli command "enable"
 action 2.0 cli command "show log | include error > flash:errors.txt"
 action 3.0 puts "Relevant error logs saved to flash."
Resource Monitoring: Restart a process if CPU utilization exceeds 90%.

bash
Copy code
event manager applet CPU_Monitor
 event resource policy cpu usage rising threshold 90
 action 1.0 cli command "enable"
 action 2.0 cli command "reload"
 action 3.0 puts "CPU usage exceeded threshold. Device reloaded."


Benefits of EEM Applets:
Automation: Reduce manual intervention for repetitive tasks.
Event-Driven: Trigger actions based on system events or conditions.
Customization: Tailor applets for specific operational needs.
Let me know if you'd like help creating an EEM applet for a specific use case!
