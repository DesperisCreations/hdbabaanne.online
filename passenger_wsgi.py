import sys
import os

# Django projenizin yolunu belirleyin
sys.path.insert(0, '/home/username/hdbabaan/hdbabaanne')  # 'username' yerine CPanel kullanıcı adınızı ve projenizin doğru yolunu yazın.

# Django ayarlarını yükleyin
os.environ['DJANGO_SETTINGS_MODULE'] = 'hdbabaanne.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()