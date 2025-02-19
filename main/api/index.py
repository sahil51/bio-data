from wsgi import application  # आपके Django प्रोजेक्ट का WSGI ऐप इम्पोर्ट करें

# Vercel को यह बताने के लिए कि Django एप्लिकेशन रन करना है
app = application
