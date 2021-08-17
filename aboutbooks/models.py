from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(verbose_name='거주지역', max_length=100)
    phone = models.IntegerField(verbose_name='전화번호')
    address = models.TextField(verbose_name='주소', blank=True, null=True)
    unsubscribe = models.TextField(
        verbose_name='구독 해제 사유', blank=True, null=True)


class Interest(models.Model):
    topic = models.CharField(verbose_name='관심 주제', max_length=100)


class Child(models.Model):
    GENDER_CHOICES = {
        ('male', 'Male'),  # 오른쪽에 있는 것이 화면에 보인다.
        ('female', 'Female'),
    }
    parents = models.ForeignKey(
        Profile, related_name='parents', on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='아이 이름', max_length=100)
    age = models.IntegerField(verbose_name='아이 나이')
    sex = models.CharField(max_length=80, choices=GENDER_CHOICES)
    book_level = models.IntegerField(
        verbose_name='책읽기 레벨', blank=True, null=True)
    interest1 = models.ManyToManyField(
        Interest, related_name='interest1', blank=True)
    interest2 = models.ManyToManyField(
        Interest, related_name='interest2', blank=True)
    interest3 = models.ManyToManyField(
        Interest, related_name='interest3', blank=True)


class Book(models.Model):
    title = models.TextField(verbose_name='책 제목')
    status = models.IntegerField(verbose_name='책 상태')
    page = models.IntegerField(verbose_name='페이지 수')
    level = models.IntegerField(verbose_name='책 레벨')
    category = models.CharField(verbose_name='책 종류', max_length=100)
    published = models.DateField(verbose_name='출간일')
    publisher = models.CharField(verbose_name='출판사', max_length=100)
    writer = models.CharField(
        verbose_name='글쓴이', max_length=100, blank=True, null=True)
    painter = models.CharField(
        verbose_name='그린이', max_length=100, blank=True, null=True)
    subject1 = models.ManyToManyField(
        Interest, related_name='subject1', blank=True)
    subject2 = models.ManyToManyField(
        Interest, related_name='subject2', blank=True)
    subject3 = models.ManyToManyField(
        Interest, related_name='subject3', blank=True)
    subject4 = models.ManyToManyField(
        Interest, related_name='subject4', blank=True)
    subject5 = models.ManyToManyField(
        Interest, related_name='subject5', blank=True)
    possession = models.ForeignKey(
        Child, related_name='possession', on_delete=models.DO_NOTHING, blank=True, null=True)
    borrowed = models.DateField(verbose_name='대여일', blank=True, null=True)
    returned = models.DateField(verbose_name='반납일')


class Read(models.Model):
    child = models.ForeignKey(
        Child, related_name='child', on_delete=models.DO_NOTHING)
    reading = models.IntegerField(verbose_name='회차')
    address = models.TextField(verbose_name='주소', blank=True, null=True)
    book1 = models.ForeignKey(
        Book, related_name='book1', on_delete=models.DO_NOTHING)
    rate1 = models.FloatField(verbose_name='책1 별점', blank=True, null=True)
    report1 = models.TextField(verbose_name='신고사유', blank=True, null=True)
    book2 = models.ForeignKey(
        Book, related_name='book2', on_delete=models.DO_NOTHING)
    rate2 = models.FloatField(verbose_name='책2 별점', blank=True, null=True)
    report2 = models.TextField(verbose_name='신고사유', blank=True, null=True)
    book3 = models.ForeignKey(
        Book, related_name='book3', on_delete=models.DO_NOTHING)
    rate3 = models.FloatField(verbose_name='책3 별점', blank=True, null=True)
    report3 = models.TextField(verbose_name='신고사유', blank=True, null=True)
    book4 = models.ForeignKey(
        Book, related_name='book4', on_delete=models.DO_NOTHING)
    rate4 = models.FloatField(verbose_name='책4 별점', blank=True, null=True)
    report4 = models.TextField(verbose_name='신고사유', blank=True, null=True)
    book5 = models.ForeignKey(
        Book, related_name='book5', on_delete=models.DO_NOTHING)
    rate5 = models.FloatField(verbose_name='책5 별점', blank=True, null=True)
    report5 = models.TextField(verbose_name='신고사유', blank=True, null=True)
    borrowed = models.DateField(verbose_name='대여일', blank=True, null=True)
    returned = models.DateField(verbose_name='예상 반납일')


class Question(models.Model):
    question = models.TextField(verbose_name='문의사항')
    profile = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)
    answered = models.BooleanField(
        verbose_name='질문에 답을 했으면 true, 아직 안했으면 false', default=False)


class Review(models.Model):
    review = models.TextField(verbose_name='서비스 리뷰')
    profile = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)
