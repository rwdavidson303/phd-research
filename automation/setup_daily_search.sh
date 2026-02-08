#!/bin/bash
# Setup daily article search automation using macOS launchd
# Run this script once to install the daily job

PLIST_NAME="com.phd-research.daily-article-search"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"
SCRIPT_PATH="$HOME/phd-research/automation/daily_article_search.py"
LOG_PATH="$HOME/phd-research/automation/logs"
PYTHON_PATH=$(which python3)

# Create log directory
mkdir -p "$LOG_PATH"

# Create the launchd plist
cat > "$PLIST_PATH" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>${PYTHON_PATH}</string>
        <string>${SCRIPT_PATH}</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>${LOG_PATH}/daily_search.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_PATH}/daily_search_error.log</string>
    <key>WorkingDirectory</key>
    <string>${HOME}/phd-research</string>
</dict>
</plist>
EOF

echo "Created launchd plist: $PLIST_PATH"

# Load the job
launchctl load "$PLIST_PATH"
echo "Daily search scheduled for 7:00 AM every day"
echo ""
echo "Commands:"
echo "  Run now:     python3 $SCRIPT_PATH"
echo "  View report: python3 $SCRIPT_PATH --report"
echo "  Export CSV:   python3 $SCRIPT_PATH --export"
echo "  Stop job:    launchctl unload $PLIST_PATH"
echo "  View logs:   tail -f $LOG_PATH/daily_search.log"
