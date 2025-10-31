# Hi!
# This message is a Quine.
# A Quine is a computer program that outputs its own source code when it is run.
# This does the same thing, only the "output" is a imessage to a phone number or contact saved in the phone_number variable
# If you save the entirety of this message as a python .py file and run it on a MacOS computer it will send this exact text to "phone_number"

import subprocess

phone_number = 'XXXXXXXXX'#[Remember to change this in both locations!]

code = '# Hi!\n# This message is a Quine.\n# A Quine is a computer program that outputs its own source code when it is run.\n# This does the same thing, only the "output" is a imessage to a phone number or contact saved in the phone_number variable\n# If you save the entirety of this message as a python .py file and run it on a MacOS computer it will send this exact text to "phone_number"\n\nimport subprocess\n\nphone_number = \'XXXXXXXXX\'#[Remember to change this in both locations!]\n\ncode = %r\n\n# Create the complete message by formatting the code into itself\nmessage = code %% code\n\n# Escape the message for AppleScript\nescaped_message = message.replace(\'\\\\\', \'\\\\\\\\\')\nescaped_message = escaped_message.replace(\'"\', \'\\\\"\')\nescaped_message = escaped_message.replace(\'\\n\', \'\\\\n\')\nescaped_message = escaped_message.replace(\'\\r\', \'\\\\r\')\n\n# Build the AppleScript command\napplescript_command  = \'tell application "Messages"\\n\'\napplescript_command += \'set targetService to 1st service whose service type = iMessage\\n\'\napplescript_command += \'set targetBuddy to buddy "\' + phone_number + \'" of targetService\\n\'\napplescript_command += \'send "\' + escaped_message + \'" to targetBuddy\\n\'\napplescript_command += \'end tell\'\n\n# Execute the AppleScript\nsubprocess.run([\'osascript\', \'-e\', applescript_command])'

# Create the complete message by formatting the code into itself
message = code % code

# Escape the message for AppleScript
escaped_message = message.replace('\\', '\\\\')
escaped_message = escaped_message.replace('"', '\\"')
escaped_message = escaped_message.replace('\n', '\\n')
escaped_message = escaped_message.replace('\r', '\\r')

# Build the AppleScript command
applescript_command  = 'tell application "Messages"\n'
applescript_command += 'set targetService to 1st service whose service type = iMessage\n'
applescript_command += 'set targetBuddy to buddy "' + phone_number + '" of targetService\n'
applescript_command += 'send "' + escaped_message + '" to targetBuddy\n'
applescript_command += 'end tell'

# Execute the AppleScript
subprocess.run(['osascript', '-e', applescript_command])
