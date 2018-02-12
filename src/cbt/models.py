from django.db import models


class Ulangan(models.Model):
    tanggal = models.DateTimeField(auto_now=False, auto_now_add=True)
    mata_pelajaran = models.CharField(max_length=100)
    guru = models.CharField(max_length=75)
    kelas = models.CharField(max_length=20)
    PILIHAN_SEMESTER = (
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
    )
    semester = models.CharField(max_length=1, choices=PILIHAN_SEMESTER)
    kkm = models.IntegerField('KKM')
    duration = models.IntegerField()
    kisi_kisi = models.TextField()

    def __str__(self):
        return self.mata_pelajaran

    class Meta:
        verbose_name_plural = 'Ulangan'


class SoalUlangan(models.Model):
    soal = models.ForeignKey(Ulangan, related_name='soal_ulangan')
    pertanyaan = models.TextField()
    gambar = models.ImageField(upload_to='soal', blank=True)
    a = models.CharField(max_length=500)
    b = models.CharField(max_length=500)
    c = models.CharField(max_length=500)
    d = models.CharField(max_length=500)
    e = models.CharField(max_length=500)
    PILIHAN_JAWABAN = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
        ('e', 'E'),
    )
    jawaban = models.CharField(max_length=1, choices=PILIHAN_JAWABAN)

    def __str__(self):
        return '#{} - {}'.format(str(self.pk), self.pertanyaan)
