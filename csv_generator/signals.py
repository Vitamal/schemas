from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save)
def generated_file_status_changed(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created and instance.is_generated:
        import channels.layers
        channel_layer = channels.layers.get_channel_layer()
        data = {
            'generated_file_id': instance.id
        }
        from asgiref.sync import async_to_sync
        async_to_sync(channel_layer.group_send)('generator', data)
