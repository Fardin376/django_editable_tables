from django.db import models
import pandas as pd


# Create your models here.
class DataTable(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    trade_code = models.CharField(max_length=10)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    


class Meta:
    ordering = [ 'date', ]
    db_table = "tblDATA"

def importFromCSV():
    csv_file = "static/csv/stock_market_data.csv"
    df = pd.read_csv(csv_file)
    df["volume"] = df["volume"].str.replace(",", "").astype(int)
    df["high"] = df["high"].str.replace(",", "").astype(float)
    df["low"] = df["low"].str.replace(",", "").astype(float)
    df["open"] = df["open"].str.replace(",", "").astype(float)
    df["close"] = df["close"].str.replace(",", "").astype(float)
    data_to_insert = df.to_dict(orient="records")
    DataTable.objects.bulk_create([DataTable(**data) for data in data_to_insert])