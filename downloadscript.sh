telegram-cli --json -W --exec "history @chtwrsreports 600" | tail -n 3 | head  > chtwrsreports.json
telegram-cli --json -W --exec "history @CWMiniReports 600" | tail -n 3 | head  > CWMiniReports.json