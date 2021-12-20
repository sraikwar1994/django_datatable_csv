from django.views.generic import TemplateView
import pandas as pd
import json


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        df = pd.read_csv('data/data.csv')
        parsed = df.to_json(orient="split")
        data['content'] = parsed
        return data
