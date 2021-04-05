# from django.apps import AppConfig
# from django.db.models.signals import post_save
#
# from csv_generator import signals
#
#
# class CsvGeneratorConfig(AppConfig):
#     name = 'csv_generator'
#
#     def connect_model_signals(self):
#         from csv_generator.models import GeneratedFile
#         post_save.connect(signals.generated_file_status_changed, GeneratedFile)
#
#     def ready(self):
#         self.connect_model_signals()