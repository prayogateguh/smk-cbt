from django.contrib import admin

from .models import SoalUlangan, Ulangan, Nilai


class SoalUlanganInline(admin.StackedInline):
    fieldsets = (
        ('+', {
            'classes': ('collapse',),
            'fields': (
                'pertanyaan', 'gambar', 'a', 'b', 'c', 'd', 'e', 'jawaban',)
        }),
    )
    model = SoalUlangan
    extra = 0


@admin.register(Ulangan)
class MapelAdmin(admin.ModelAdmin):
    list_display = ('mata_pelajaran', 'id', 'guru', 'kelas', 'semester', 'tanggal',)

    fieldsets = (
        ('+', {
            'classes': ('collapse',),
            'fields': (
                'mata_pelajaran', 'guru', 'kelas',
                'semester', 'kkm', 'duration', 'kisi_kisi')
        }),
    )

    inlines = [SoalUlanganInline,]


@admin.register(Nilai)
class NilaiAdmin(admin.ModelAdmin):
    list_display = ('siswa', 'mapel', 'nilai', 'tanggal',)

    fields = ('siswa', 'mapel', 'nilai')
