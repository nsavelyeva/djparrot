import re
import json
from abc import ABCMeta, abstractmethod


LANGUAGES = ['en', 'ru', 'nl', 'de', 'fr', 'es', 'pl', 'lt', 'el', 'hi']


class FormValidators(object):
    """Abstract class to handle Validators."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate(self, request):
        """A method to perform form validation."""
        pass

    @staticmethod
    def collect_field_errors(value, exp_type=int, preset=None, regexp=None):
        errors = []
        value = json.loads(str(value)) if isinstance(value, str) else value
        if not isinstance(value, exp_type):
            errors.append('Value "%s" should be of type "%s"' % (value, exp_type))
        if preset and exp_type==list and not (set(value)<=set(preset)):
            errors.append('Value "%s" is not a member of a predefined preset %s' % (value, preset))
        if regexp and not re.match(regexp, value):
            errors.append('Value "%s" does not match the pattern %s' % (value, regexp))
        return errors


class TranslateForm(FormValidators):

    def validate(self, request):
        errors = []
        entry = request.forms.get('entry').strip()
        if not entry:
            errors.append('Search entry is empty. Nothing to search for.')
        elif entry.replace('\'', '') != entry:
            errors.append('Search entry has been rejected because it contains an apostrophe.')
        src_language = request.forms.getall("src_language")
        errors.extend(self.collect_field_errors(src_language, list, LANGUAGES))
        flashes = [('danger', error) for error in errors]
        return flashes


class SearchForm(FormValidators):

    def validate(self, request):
        errors = []
        search = request.forms.get('search').strip()
        lang_checkbox = request.forms.getall('lang_checkbox')
        if not search:
            errors.append('Search entry is empty. Nothing to search for.')
        elif search.replace('\'', '') != search:
            errors.append('Search entry has been rejected because it contains an apostrophe.')
        errors.extend(self.collect_field_errors(lang_checkbox, list, LANGUAGES))
        flashes = [('danger', error) for error in errors]
        if len(lang_checkbox) > 5:
            errors.append('Max 5 languages allowed.')
        if not lang_checkbox:
            flashes.append(('warning', 'No languages selected, so defaulted to "en".'))
        return flashes


class WordsForm(FormValidators):

    def validate(self, request):
        errors = []
        category = request.forms.get('category').strip()
        subcategory = request.forms.get('subcategory').strip()
        lang_checkbox = request.forms.getall('lang_checkbox')
        errors.extend(self.collect_field_errors(category, int))
        errors.extend(self.collect_field_errors(subcategory, int))
        errors.extend(self.collect_field_errors(lang_checkbox, list, LANGUAGES))
        if len(lang_checkbox) > 5:
            errors.append('Max 5 languages allowed.')
        flashes = [('danger', error) for error in errors]
        if not lang_checkbox:
            flashes.append(('warning', 'No languages selected, so defaulted to "en".'))
        return flashes
