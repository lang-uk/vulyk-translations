# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from vulyk.models.task_types import AbstractTaskType

from vulyk_translations.models.tasks import TranslationAnswer, TranslationTask


class TranslationTaskType(AbstractTaskType):
    """
    Translation QE Task to work with Vulyk.
    """

    answer_model = TranslationAnswer
    task_model = TranslationTask

    name = "Оцінка якості перекладу речень"
    description = "Визначення якості перекладу речень за шкалою від 1 до 5"

    template = "base.html"
    helptext_template = "help.html"
    type_name = "translations_qe_task"

    redundancy = 3

    JS_ASSETS = [
        "static/scripts/keymaster.js",
        "static/scripts/handlebars.js",
        "static/scripts/bootstrap-select.js",
        # "static/scripts/typeahead.js",
        # "static/scripts/bootstrap-tagsinput.js",
        "static/scripts/base.js",
    ]

    CSS_ASSETS = [
        "static/styles/bootstrap-select.css",
        # "static/styles/bootstrap-tagsinput.css",
        "static/styles/base.css",
        # "static/styles/autocomplete.css",
    ]
