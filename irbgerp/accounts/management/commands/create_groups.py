from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from orders.models import Order

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # 관리자 그룹 생성
        manager_group, created = Group.objects.get_or_create(name='Managers')
        if created:
            self.stdout.write(self.style.SUCCESS('Managers group created'))
        
        # 모든 Order 모델 권한 부여
        content_type = ContentType.objects.get_for_model(Order)
        permissions = Permission.objects.filter(content_type=content_type)
        manager_group.permissions.set(permissions)
        manager_group.save()

        # 작가 그룹 생성
        author_group, created = Group.objects.get_or_create(name='Authors')
        if created:
            self.stdout.write(self.style.SUCCESS('Authors group created'))
        
        # 작가는 자신의 Order만 읽기/쓰기 가능 (권한은 코드에서 처리)
        # 추가적인 권한 설정이 필요하다면 여기에 추가

        self.stdout.write(self.style.SUCCESS('Permissions assigned to groups'))
