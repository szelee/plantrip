from processemail import googleapi
from allauth.socialaccount.models import GoogleCredential
from django.contrib.auth.models import User
from oauth2client.django_orm import Storage
from django.utils import timezone

def main():
    all_credentials = GoogleCredential.objects.all()

    for item in all_credentials:
        print "user: ", item.user_id
        storage = Storage(GoogleCredential, 'user_id', item.user_id, 'credential')
        credential = storage.get()
        print credential
        service = googleapi.build_service(credential)
        messages = googleapi.ListMessages(service, 'me', 'reservation confirmation')
    
        #with open('emails/' + item.user_id + '/gmail-data.json', 'w') as
        #outfile:
        #    json.dump(messages, outfile)
        #outfile.close()
        for message in messages:
            #print message
            try:
                email = googleapi.GetMimeMessage(service, 'me', message['id'])
                with open('processemail\emails\email' + message['id'] + '.txt', 'wb') as outfile:
                    outfile.write(str(email))   
                    outfile.close()  
            except Exception as e:
                error_file = open('processemail\error.txt', 'a')
                error_file.writelines("%s %s: Error for file %s with error %s \n" %(timezone.now(), threadId, file, str(e)))
                error_file.close()               

main()