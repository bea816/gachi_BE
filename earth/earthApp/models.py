from django.db import models

# 구매 아이템
class Item(models.Model):
    # ('db저장값', '사용자에게보이는값')
    ITEM_TYPE_CHOICES = [
        ('sticker', '스티커'),
        ('theme', '테마'),
        ('frame', '프레임'),
    ]

    item_name = models.CharField(max_length=50)         # 아이템 이름
    description = models.TextField(max_length=100)      # 아이템 설명
    price = models.IntegerField()                       # 아이템 가격
    item_image = models.ImageField(upload_to='items/')  # 아이템 이미지
    item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES)  # 아이템 타입
    note = models.TextField(max_length=200, blank=True)             # 참고 사항

    def __str__(self):
        return self.item_name
    
# 광고 배너
class Advertisement(models.Model):
    ad_title = models.CharField(max_length=100)                    # 광고 제목
    ad_image = models.ImageField(upload_to='advertisements/')      # 광고 이미지
    ad_link = models.URLField(max_length=200)                      # 광고 링크
    #display_order = models.IntegerField(default=0)                 # 표시 순서

    def __str__(self):
        return self.ad_title