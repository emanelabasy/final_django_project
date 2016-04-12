from django.db.models import signals
from django.dispatch import dispatcher


def count_changes(sender, instance, signal, *args, **kwargs):
	from articles.models import Article
	for Comment_art_id in Article.objects.all():
		Comment_art_id.count_changes()