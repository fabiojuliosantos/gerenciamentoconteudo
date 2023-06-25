from django.test import TestCase
from articles.models import Article, Category, Tag


class ArticleModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(
            name='python'
        )

        cls.category = Category.objects.create(
            name='Programação'
        )

          
    def test_tag_name_empty_field(self):
        tag = Tag.objects.get(name='python')
        self.assertEqual(tag.name, 'python')
      
    
    def test_category_name_empty_field(self):
        category = Category.objects.get(name='Programação')
        self.assertEqual(category.name, 'Programação')
    
   