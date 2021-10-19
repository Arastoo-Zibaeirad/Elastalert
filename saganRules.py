f = open("[CISCO-IOS] SNMP Authentication Failure [0/5].yaml", "w")
f.write('''
ANPdata: 
- creation_date = "2021/09/11"
- maturity = "production"
- updated_date = "2021/09/11" 

ANPrule:

- author: ["Sagan"]

- description: |
    """
    [CISCO-IOS] SNMP Authentication Failure [0/5]
    """

- language : "sagan"

- license : "Quadrant Information Security"

- references : []

- rule_id : ""

- tags : ["Sagan", "Elastic"]

- type = "kql"

name: ""

index: packetbeat-*, auditbeat-*, winlogbeat-*

type: any

kql:
  "query": ""

alert:
- "slack"

slack:
slack_webhook_url: "https://hooks.slack.com/services/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"

''')