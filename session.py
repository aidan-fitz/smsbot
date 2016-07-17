class SMSSession:
    def __init__(self, post_data):
        # post_data describes an SMS message
        # see API description here: https://www.twilio.com/docs/api/twiml/sms/twilio_request#synchronous
        msg_id = post_data['MessageSid']
        from_phone = post_data['From']
        to_phone = post_data['To']
        text = post_data['Body']
