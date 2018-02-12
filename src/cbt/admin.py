from django.contrib import admin

from .models import SoalUlangan, Ulangan


class SoalUlanganInline(admin.StackedInline):
    fieldsets = (
        ('+', {
            'classes': ('collapse wide',),
            'fields': (
                'pertanyaan', 'gambar', 'a', 'b', 'c', 'd', 'e', 'jawaban')
        }),
    )
    model = SoalUlangan
    extra = 0


@admin.register(Ulangan)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('mata_pelajaran', 'guru', 'kelas', 'semester', 'tanggal',)

    fieldsets = (
        ('+', {
            'classes': ('collapse wide',),
            'fields': (
                'mata_pelajaran',
                'guru', 'kelas', 'semester', 'kkm', 'duration', 'kisi_kisi')
        }),
    )

    inlines = [SoalUlanganInline, ]
