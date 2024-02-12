
class ReadonlyFieldMixin:
    readonly_fields = '__all__'

    def _apply_readonly_on_fields(self):
        for field in self.get_fields:
            self.fields[field].widget.attrs['readonly'] = True

    @property
    def get_fields(self):
        if self.readonly_fields == '__all__':
            return self.fields.keys()

        return self.readonly_fields
