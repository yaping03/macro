from django.db import models

# Create your models here.
class Ns1_detail(models.Model):
    Accession_id = models.CharField(primary_key=True,max_length=32)
    Sequence_name = models.CharField(max_length=32)
    Scientific_name = models.CharField(max_length=255)
    Taxonomic_identifier = models.CharField(max_length=32)
    Subtype = models.CharField(max_length=32)
    Host = models.CharField(max_length=32)
    Collection_year = models.CharField(max_length=32)
    Country = models.CharField(max_length=255)
    Protein_attributes = models.CharField(max_length=255)
    Sequence = models.CharField(max_length=1999)

class R16srna(models.Model):
    NO = models.CharField(primary_key=True,max_length=36)
    Genus = models.CharField(max_length=64)
    Species = models.CharField(max_length=36)
    Subspecies = models.CharField(max_length=36)
    Typestrain = models.CharField(max_length=36)
    NCBI = models.CharField(max_length=36)
    Sequence = models.CharField(max_length=9999)

class Cell_detail(models.Model):
    保藏号 = models.CharField(primary_key=True,max_length=255)
    细胞名称 = models.CharField(max_length=255)
    种属 = models.CharField(max_length=255)
    组织来源 = models.CharField(max_length=255)
    生长特性 = models.CharField(max_length=255)
    细胞形态 = models.CharField(max_length=255)
    背景描述 = models.CharField(max_length=255)
    生长培养基 = models.CharField(max_length=255)
    培养条件 = models.CharField(max_length=255)
    备注 = models.CharField(max_length=255)

class Fungus_detail(models.Model):
    pre_no = models.CharField(primary_key=True,max_length=255)
    名称 = models.CharField(max_length=255)
    别名 = models.CharField(max_length=255)
    属 = models.CharField(max_length=255)
    种 = models.CharField(max_length=255)
    亚种 = models.CharField(max_length=255)
    来源 = models.CharField(max_length=255)
    s_rna = models.CharField(max_length=255)
    特性 = models.CharField(max_length=255)
    是否测序 = models.CharField(max_length=255)
    是否模式 = models.CharField(max_length=255)
    培养基 = models.CharField(max_length=255)
    保存条件 = models.CharField(max_length=255)
    安全等级 = models.CharField(max_length=255)
    参考文献 = models.CharField(max_length=255)
    数量 = models.CharField(max_length=255)
    其他库 = models.CharField(max_length=255)
    保存形式 = models.CharField(max_length=255)
    描述 = models.CharField(max_length=255)
    发表论文 = models.CharField(max_length=255)
    保存时间 = models.CharField(max_length=255)

class Ns1_3d_detail(models.Model):
    PDB_ID = models.CharField(primary_key=True,max_length=32)
    Title = models.CharField(max_length=255)
    Method = models.CharField(max_length=255)
    Resolution = models.FloatField(max_length=32)
    Reference = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Journal = models.CharField(max_length=255)
    Mole_Chains = models.CharField(max_length=64)
    Mole_Molecule = models.CharField(max_length=255)
    Mole_Details = models.CharField(max_length=255)
    Mole_Organism = models.CharField(max_length=255)
    Mole_Sequence = models.CharField(max_length=32)
    Mole_Chains1 = models.CharField(max_length=255)
    Mole_Molecule1 = models.CharField(max_length=255)
    Mole_Details1 = models.CharField(max_length=255)
    Mole_Organism1 = models.CharField(max_length=255)
    Mole_Sequence1 = models.CharField(max_length=255)

class Plasmid_detail(models.Model):
    保藏号 = models.CharField(primary_key=True,max_length=255)
    质粒名称 = models.CharField(max_length=255)
    质粒类型 = models.CharField(max_length=255)
    载体大小 = models.CharField(max_length=255)
    载体标签 = models.CharField(max_length=255)
    载体抗性 = models.CharField(max_length=255)
    保存菌株 = models.CharField(max_length=255)
    质粒图谱 = models.CharField(max_length=255)
    来源 = models.CharField(max_length=255)
    保存时间 = models.CharField(max_length=255)
    载体描述 = models.CharField(max_length=255)
    备注 = models.CharField(max_length=255)
    图片 = models.CharField(max_length=255)
    描述 = models.CharField(max_length=255)
    上传时间 = models.CharField(max_length=255)
