from twilio.rest import Client

account_sid = 'ACa4fe6fb7c47847a1d34d53f7d18a76db'
auth_token = '0a510259a16b6b8f44e6c6a0fd7ac0e7'
client = Client(account_sid, auth_token)
message = client.messages.create(
                from_='+12058929610',
                body='From Satya: Hello, GB! Happy BIRTHDAY BOTH OF YOU. HAVE A CHEERFULL DAY WITH ARMU!',
                to='+917846950020'
            )
print(message.sid)