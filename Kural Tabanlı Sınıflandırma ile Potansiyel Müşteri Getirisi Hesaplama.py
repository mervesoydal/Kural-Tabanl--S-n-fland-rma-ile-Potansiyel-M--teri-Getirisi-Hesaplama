#PART1:
# Soru 1: persona.csvdosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
df = pd.read_csv("datasets/persona.csv")
df.info()
df.head()
df.shape
df.index
df.describe().T
df.isnull().values.any()

#Soru 2: Kaç uniqueSOURCE vardır? Frekansları nedir?
df.nunique()
#TV: 190
#radio:167
#newspaper:172
#sales:121

#
#Soru 3:Kaç uniquePRICE vardır
df["PRICE"].nunique()

#Soru 4:Hangi PRICE'dankaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts().head()

#Soru 5:Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts().head()

#Soru 6:Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df["COUNTRY"].value_counts().sum()

#Soru 7:SOURCE türlerine göre satış sayıları nedir?
df["SOURCE"].value_counts().head()

#Soru 8:Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()

#Soru 9:SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE")["PRICE"].mean()

#Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":["mean"]})

#Görev 2:COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE": "mean"})

#Görev 3:Çıktıyı PRICE’a göre sıralayınız.

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE": "mean"})
agg_df.sort_values("PRICE",ascending=False).head()

#Görev 4: Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler indexisimleridir. Bu isimleri değişken isimlerine çeviriniz.

agg_df = agg_df.reset_index()
agg_df.head()
#Görev5:

newlabels = ['0_18','19_23','24_30','31_40','41_70']

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"],[0, 18, 23, 30, 40, 70] , labels=newlabels)

#Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız

agg_df["customers_level_based"] =[row[0].upper() + '_' + row[1].upper() + '_' + row[2].upper()+'_'+row[5] for row in agg_df.values]
agg_df.head()

agg_df.groupby(["customers_level_based"]).agg({"PRICE": ["mean"]})
agg_df.head(10)

agg_df.value_counts()
#Görev 7:  Yeni müşterileri (personaları) segmentlereayırınız.

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby(["SEGMENT"]).agg({"PRICE": ["mean","max","sum"]})
agg_df.head(30)
#Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user2]